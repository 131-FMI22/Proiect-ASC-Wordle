from itertools import product
import math
import multiprocessing
from functools import partial
import os
import time

# VARIABLE DECLARATION

#lPossibleQueries = lQueryWords
lPermutations = list(product('012', repeat=5))
lEntropy = []
lWords = []

# FILE PARSING

def read_permutation_file():
    with open("rez_query.txt", "r") as rezQuery:
        strAux = rezQuery.read()
        lPermutation = [x for x in strAux.split()]
        strWord = lPermutation[0]
        lPermutation = lPermutation[1:]
    rezQuery.close()

    return strWord, lPermutation

with open("cuvinte_wordle.txt", "r") as wordleList:
    text = wordleList.read()
    lWords = [str(x) for x in text.split()]

# POST FILE PARSING VARIABLE DECLARATION

lQueryWords = lWords.copy()

#primul query va fi TAREI, deoarece are cea mai mare entropie
#din lista initiala de cuvinte. 
# 
# Pentru a consulta lista cu entropiile
# pentru primul query, vedeti fisierul TODO

strUserInput = "TAREI"
lUserInput = list(strUserInput)

strGuessWord = "DRACU" #TODO remove after debugging
lGuessWord = list(strGuessWord)


lAllUserInputs = []
lQueryPermutation = [0,0,0,0,0]

cnt = 0
cntFinal = 0




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

#strWord, L = read_permutation_file()
#print(L)
#print(strWord)
#print(lPermutations[209])
#print(L)

def word_entropy(lArgWords, argInc):
    finalEntropy = 0.0
    strargWord = lArgWords[argInc]
    word_prob = 0.0
        
    for tPerm in lPermutations:
        sPossibleQueries = set(lArgWords)
        var_word_information = 0.0
        
        #ALGORITM 2 

        
        for i in range(5):
            if int(tPerm[i]) == 2:
                #verde
                for strWord in lArgWords:
                    if strWord[i] != strargWord[i]:
                        sPossibleQueries.discard(strWord)
            if int(tPerm[i]) == 0:
                for strWord in lArgWords:
                    if strargWord[i] in strWord:
                        sPossibleQueries.discard(strWord)
            if int(tPerm[i]) == 1:
                for strWord in lArgWords:
                    if strargWord[i] not in strWord or strargWord[i] == strWord[i]:
                        sPossibleQueries.discard(strWord)
    
        
        #print(len(sPossibleQueries))
        #print([str(x) for x in sPossibleQueries])
        #print(str(len(sPossibleQueries)) + ' ' + str(len(lQueryWords)))
        if (len(sPossibleQueries) != 0):
            word_prob = len(sPossibleQueries) / len(lQueryWords) 
            #print(tPerm)    
            #print(word_prob)
            var_word_information = -(word_prob)*math.log2(word_prob)
            #print(*tPerm, end="    ")
            #print(var_word_information, end= "    ")
            #print(len(sPossibleQueries))
        #print(var_word_information)
        #print(tPerm)
        #print()
        finalEntropy += var_word_information



    #print(finalEntropy)
    return finalEntropy


# DOMNULE RUSU SUNTEM INTELIGENTI :))))))
# (va rugam sa ne strangeti mana)
"""
def calc_entropie(strargQueryWord, largQueryPermutation, largQueryWords):

    cpuCount = multiprocessing.cpu_count() 

    #tStart = time.perf_counter()
    
    pool = multiprocessing.Pool(cpuCount)
    lRemainingList = truncate_list(strargQueryWord, largQueryPermutation, largQueryWords)
    #print(*lTruncatedList)
    #while(read_permutation_file[1].count(2) != 5):
    lEntropy = pool.map(partial(word_entropy, lTruncatedList), range(len(lTruncatedList)))
    pool.close()
    pool.terminate()
    pool.join()
    maxEntropy = 0
    for i in range(len(lEntropy)):
        if lEntropy[i] > maxEntropy:
            maxEntropy = lEntropy[i]
            strNextQuery = lTruncatedList[i]
    #with open("cuvan_query.txt", "w") as cuv_query:
    #   cuv_query.write(strNextQuery)


    

    #print("Done!")
    

    #tStop = time.perf_counter()
    #print(tStop - tStart) 
    
    
    with open("entropie_cuvinte.txt", "w") as entropyDictionary:
        for i in range(0, 100):
            entropyDictionary.write(lQueryWords[i] + ' ' + str(lEntropy[i]) + '\n')
    

    return strNextQuery, lTruncatedList
"""



# def write_permutation_file():
#     with open("rez_query.txt", "w") as rezQuery:
#         rezQuery.write(strUserInput + " ")
#         for x in lQueryPermutation:
#             rezQuery.write(str(x) + ' ')





ok = 1

# WORDLE SOLVER
tStart = time.time()
for strWord in lWords[:100]:
    
    # urmatoarele doua linii de cod sunt improvizate maxim
    # nu intelegem de ce __mp_main__ are treaba cu zona asta
    # cand pool-ul nostru ar trebui doar sa calculeze entropii

    if __name__ == "__mp_main__":
        continue

    strGuessWord = strWord
    lGuessWord = list(strGuessWord)
    strUserInput = "TAREI"
    lUserInput = list(strUserInput)
    lRemainingList = lWords.copy()
    lAllUserInputs = []
    cnt = 0

    while lUserInput != lGuessWord and ok == 1:

        strNextQuery = ""
        lUserInput = list(strUserInput)
        lAllUserInputs.append(strUserInput)
        cnt += 1
        # litera pe aceeasi pozitie 🟩 -> \U0001F7E9
        # litera nu e in pozitia corecta 🟨 -> \U0001F7E8
        # litera nu exista ⬜ -> \U00002B1C

        #array cu cifre bazat pe ce intoarce query-ul
        # 2 -> aceeasi pozitie
        # 1 -> undeva in cuvant
        # 0 -> nu este
        

        print(" ".join(lUserInput))
        
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

        # single processing
        #print(os.getpid())
        #print(os.getppid())

        #lRemainingList = truncate_list(strUserInput, lQueryPermutation, lRemainingList).copy()
        #lEntropy = [word_entropy(lRemainingList, i) for i in range(len(lRemainingList))]
        
        # multi processing
        
        lRemainingList = truncate_list(strUserInput, lQueryPermutation, lRemainingList).copy()

        #print (__name__)
        if __name__ == "__main__":
            #strUserInput, lRemainingList = calc_entropie(strUserInput, lQueryPermutation, lRemainingList)

            cpuCount = os.cpu_count()
            #print(len(os.sched_getaffinity(0)))

            #tStart = time.perf_counter()
            
            
            #print(*lTruncatedList)
            #while(read_permutation_file[1].count(2) != 5):
            pool = multiprocessing.Pool(cpuCount)
            lEntropy = pool.map(partial(word_entropy, lRemainingList), range(len(lRemainingList)))
            pool.close()
            pool.join()
        
        maxEntropy = 0
        for i in range(len(lEntropy)):
            if lEntropy[i] > maxEntropy:
                maxEntropy = lEntropy[i]
                strNextQuery = lRemainingList[i]

        
        strUserInput = strNextQuery

        #ok = 0
        
        #write_permutation_file()
        #entropie_gen.word_information()
    else: 
        print("Ai gasit") 

    #print(f"Felicitari, dragule! Ai luat sfantul 5 la A$C, din {cnt} incercari.")
    #print(f"Istoricul query-urilor tale este: {lAllUserInputs}")

    with open("rezultate.txt", "a") as rezultate:
        rezultate.write(strGuessWord + " ")
        for strAux in lAllUserInputs:
            rezultate.write(strAux + " ")
        rezultate.write("\n")
    rezultate.close()

    cntFinal += cnt


if __name__ == "__main__":
    print(time.time() - tStart)
    medieRezolvari = cntFinal / 100

    print(f"Programul nostru ghiceste cuvantul in {medieRezolvari} incercari!")