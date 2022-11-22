import math
import random
import multiprocessing as mp
from itertools import product
import time

# VARIABLE DECLARATION

lWords = []
lAllUserInputs = []
lPermutations = list(product('012', repeat=5))
cnt = 0

# FILE PARSING

with open("cuvinte_wordle.txt", "r") as wordleList:
    text = wordleList.read()
    lWords = [str(x) for x in text.split()]

# ENTROPY FUNCTION

def word_entropy(q):

    # Aceasta este functia care ne ofera sugestii de query-uri.
    # In cadrul unui loop infinit verificam daca avem request-uri in queue.
    # Pentru fiecare request, triem lista de cuvintele care nu pot fi folosite,
    # iar pe acea lista calculam entropia fiecarui cuvant. Cuvantul cu cea mai
    # mare entropie este printat drept hint.

    lArgWords = lWords.copy()
    bLoop = True
    
    while bLoop:
        if not q.empty():

            # Folosim set deoarece stergerea este mai rapida
            sReturn = set(lArgWords)

            # Preluam request-ul din queue
            largPermutation, strargQueryWord = q.get() 

            if largPermutation == [2,2,2,2,2]:
                # Inseamna ca am gasit cuvantul, deci putem inchide procesul
                bLoop = False
                mp.current_process().close()
                continue
            
            # Verificam fiecare cuvant din lista, si pe baza valorilor din permutare determinam
            # daca mai putem lucra cu el sau nu
            for i in range(5):
                if int(largPermutation[i]) == 2:
                    #verde
                    for strWord in lArgWords:
                        if strWord[i] != strargQueryWord[i]:
                            sReturn.discard(strWord)
                if int(largPermutation[i]) == 0:
                    for strWord in lArgWords:
                        if strargQueryWord[i] in strWord:
                            sReturn.discard(strWord)
                if int(largPermutation[i]) == 1:
                    for strWord in lArgWords:
                        if strargQueryWord[i] not in strWord or strargQueryWord[i] == strWord[i]:
                            sReturn.discard(strWord)
            
            # conversie inapoi la lista + sortare (valorile din set nu sunt sortate)
            lReturn = list(sReturn)
            lReturn.sort()
            lArgWords = lReturn.copy()

            strNextQuery = ""

            # initializez cu valoare negativa deoarece pot avea un cuvant
            # cu entropie 0 (este singurul ramas in lista)
            maxEntropy = -1.0

            # Pentru fiecare cuvant din lista triata verific entropia cuvantului
            for strargWord in lArgWords:
                finalEntropy = 0.0
                word_prob = 0.0
                
                # un cuvant folosit drept query ne poate incoarce 3 ** 5 permutari de raspuns
                # pentru fiecare astfel de permutare vedem ce cuvinte raman in lista
                for tPerm in lPermutations:
                    sPossibleQueries = set(lArgWords)
                    var_word_information = 0.0
                    
                    for i in range(5):
                        if int(tPerm[i]) == 2:
                            for strWord in lArgWords:
                                if strWord[i] != strargWord[i]:
                                    sPossibleQueries.discard(strWord)
                        if int(tPerm[i]) == 0:
                            for strWord in lArgWords:
                                if strargWord[i] in strWord:
                                    sPossibleQueries.discard(strWord)
                        if int(tPerm[i]) == 1:
                            for strWord in lArgWords:
                                if strargWord[i] not in strWord or strWord[i] == strargWord[i]:
                                    sPossibleQueries.discard(strWord)
                
                    # Aici avem grija sa nu avem lista goala
                    # deoarece log2(0) = -inf
                    if (len(sPossibleQueries) != 0):

                        # numarul de cuvinte ramase / numarul de cuvinte cu care am plecat este probabilitatea
                        # de aici, aplicam formula entropiei lui Shannon:
                        word_prob = len(sPossibleQueries) / len(lArgWords) 
                        var_word_information = -(word_prob)*math.log2(word_prob)
                    finalEntropy += var_word_information
                
                if (finalEntropy > maxEntropy):
                    maxEntropy = finalEntropy
                    strNextQuery = strargWord
            print()
            print(f"O sugestie din partea noastra este cuvantul {strNextQuery}!")
    


# WORDLE SOLVER

# pun aceasta conditie aici ca sa nu intre procesul lui word_entropy peste codul de aici
if __name__ == "__main__":

    strUserInput = ""

    strGuessWord = random.choice(lWords)

    # q este un queue initializat in memoria comuna a proceselor
    q = mp.JoinableQueue()

    # lista care imi memoreaza permutarea unui cuvant
    lQueryPermutation = [0,0,0,0,0]

    print("Bine ati venit in jocul Wordle!")
    strAns = input("Doriti sa jucati cu modul hint? (y/n) ").lower()
    varHelper = True if strAns == "y" else False
    if varHelper == True:
        print(f"Pentru aceasta runda, cuvantul ales de jocul wordle este {strGuessWord}!")

        # Primul query va fi TAREI, deoarece are cea mai mare entropie
        # din lista initiala de cuvinte. 
        #  
        # Pentru a consulta lista cu entropiile
        # pentru primul query, vedeti fisierul entropii_toata_lista.txt

        print(f"De asemenea, pentru a minimiza numarul de incercari, recomandam TAREI drept prim query!")

        # initializam procesul pentru calculat cuvantul cu cea mai mare entropie
        entropy_process = mp.Process(target=word_entropy, args=(q,))
        entropy_process.start()

    while strUserInput != strGuessWord:

        strUserInput = input("Introduceti cuvantul: ").upper()
        if strUserInput not in lWords:
            print("Query-ul nu este valid!")
            continue
        
        print("In urma aplicarii, vom obtine:")
        print(" ".join([x for x in strUserInput]))
        lAllUserInputs.append(strUserInput)
        
        # litera pe aceeasi pozitie (verde) -> \U0001F7E9
        # litera nu e in pozitia corecta (galben) -> \U0001F7E8
        # litera nu exista (alb) -> \U00002B1C

        # lista cu cifre bazat pe ce intoarce query-ul
        # 2 -> aceeasi pozitie
        # 1 -> undeva in cuvant
        # 0 -> nu este
        
        for i in range(5):
            if strUserInput[i] == strGuessWord[i]:
                lQueryPermutation[i] = 2
                print('\U0001F7E9', end='')
            elif strUserInput[i] in strGuessWord:
                lQueryPermutation[i] = 1
                print('\U0001F7E8', end='')
            else:
                lQueryPermutation[i] = 0
                print('\U00002B1C', end='')
        print()

        # pasam request-ul pe queue procesului de calculat entropii
        q.put((lQueryPermutation, strUserInput))

    else:
        print(f"Ai gasit {strGuessWord}") 
        lAllUserInputs.append(strGuessWord)

    print(f"Felicitari, dragule! Ai luat sfantul 5 la A$C, din {len(lAllUserInputs)} incercari.")
    print(f"Istoricul query-urilor tale este: {lAllUserInputs}")