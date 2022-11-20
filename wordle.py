import math
import random
import multiprocessing as mp
from itertools import product

# VARIABLE DECLARATION

lWords = []
lAllUserInputs = []
lPermutations = list(product('012', repeat=5))

# FILE PARSING

with open("cuvinte_wordle.txt", "r") as wordleList:
    text = wordleList.read()
    lWords = [str(x) for x in text.split()]

# POST FILE PARSING VARIABLE DECLARATION

lRemainingList = lWords.copy()

# FUNCTIONS

def truncate_list(strargQueryWord, largPermutation, largWords):

    sReturn = set(largWords)

    for i in range(5):
        if int(largPermutation[i]) == 2:
            #verde
            for strWord in largWords:
                if strWord[i] != strargQueryWord[i]:
                    sReturn.discard(strWord)
        if int(largPermutation[i]) == 0:
            for strWord in largWords:
                if strargQueryWord[i] in strWord:
                    sReturn.discard(strWord)
        if int(largPermutation[i]) == 1:
            for strWord in largWords:
                if strargQueryWord[i] not in strWord or strargQueryWord[i] == strWord[i]:
                    sReturn.discard(strWord)
    
    lReturn = list(sReturn)
    lReturn.sort()

    return lReturn


def word_entropy(lArgWords):


    maxEntropy = -1.0
    for strargWord in lArgWords:
        finalEntropy = 0.0
        word_prob = 0.0
        
        for tPerm in lPermutations:
            sPossibleQueries = set(lArgWords)
            var_word_information = 0.0
            
            #ALGORITM 2 
            
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
        
            
            if (len(sPossibleQueries) != 0):
                word_prob = len(sPossibleQueries) / len(lArgWords) 
                var_word_information = -(word_prob)*math.log2(word_prob)
            finalEntropy += var_word_information
        
        if (finalEntropy > maxEntropy):
            maxEntropy = finalEntropy
            strNextQuery = strargWord

    return strNextQuery

# WORDLE SOLVER

# Primul query va fi TAREI, deoarece are cea mai mare entropie
# din lista initiala de cuvinte. 
#  
# Pentru a consulta lista cu entropiile
# pentru primul query, vedeti fisierul entropii_toata_lista.txt

strUserInput = "TAREI"
lUserInput = list(strUserInput)
lQueryPermutation = [0,0,0,0,0]

print("Bine ati venit in jocul Wordle!")

strGuessWord = random.choice(lWords)
lGuessWord = list(strGuessWord)
print(f"Pentru aceasta runda, cuvantul ales de jocul wordle este {strGuessWord}!")

cnt = 0
maxEntropy = 0

while lUserInput != lGuessWord:

    lUserInput = list(strUserInput)
    print(f"Query-ul cu numarul {cnt + 1} este {strUserInput}!")
    print("In urma aplicarii, vom obtine:")
    print(*lUserInput)
    lAllUserInputs.append(strUserInput)
    
    cnt += 1
    # litera pe aceeasi pozitie 🟩 -> \U0001F7E9
    # litera nu e in pozitia corecta 🟨 -> \U0001F7E8
    # litera nu exista ⬜ -> \U00002B1C

    #array cu cifre bazat pe ce intoarce query-ul
    # 2 -> aceeasi pozitie
    # 1 -> undeva in cuvant
    # 0 -> nu este
    
    for i in range(5):
        if lUserInput[i] == lGuessWord[i]:
            lQueryPermutation[i] = 2
            print('\U0001F7E9', end='')
        elif lUserInput[i] in lGuessWord:
            lQueryPermutation[i] = 1
            print('\U0001F7E8', end='')
        else:
            lQueryPermutation[i] = 0
            print('\U00002B1C', end='')
    print()

    lRemainingList = truncate_list(strUserInput, lQueryPermutation, lRemainingList).copy()
    strUserInput = word_entropy(lRemainingList)
    lUserInput = list(strUserInput)
else: 
    print(f"Ai gasit {strGuessWord}") 
    cnt += 1
    lAllUserInputs.append(strGuessWord)

print(f"Felicitari, dragule! Ai luat sfantul 5 la A$C, din {cnt} incercari.")
print(f"Istoricul query-urilor tale este: {lAllUserInputs}")