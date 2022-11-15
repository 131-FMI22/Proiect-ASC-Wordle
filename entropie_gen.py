from itertools import product
import math
import multiprocessing
import time
from functools import partial

with open("cuvinte_wordle.txt", "r") as wordleList:
    sAux = wordleList.read()
    lQueryWords = [str(x) for x in sAux.split()]
wordleList.close()

#lPossibleQueries = lQueryWords
lEntropy = []

def read_permutation_file():
    with open("rez_query.txt", "r") as rezQuery:
        strAux = rezQuery.read()
        lPermutation = [x for x in strAux.split()]
        strWord = lPermutation[0]
        lPermutation = lPermutation[1:]

    return strWord, lPermutation

def truncate_list(strQueryWord, largPermutation, largWords):

    sReturn = set(largWords)

    for i in range(5):
        if int(largPermutation[i]) == 2:
            #verde
            for strWord in lQueryWords:
                if strWord[i] != strQueryWord[i]:
                    sReturn.discard(strWord)
        if int(largPermutation[i]) == 0:
            for strWord in lQueryWords:
                if strQueryWord[i] in strWord:
                    sReturn.discard(strWord)
        if int(largPermutation[i]) == 1:
            for strWord in lQueryWords:
                if strQueryWord[i] not in strWord or strQueryWord[i] == strWord[i]:
                    sReturn.discard(strWord)
    
    return list(sReturn)

#strWord, L = read_permutation_file()
#print(L)
#print(strWord)
lPermutations = list(product('012', repeat=5))
#print(lPermutations[209])
#print(L)

def word_entropy(lArgWords, argInc):
    finalEntropy = 0.0
    strargWord = lArgWords[argInc]
    word_prob = 0.0
        
    for tPerm in lPermutations:
        sPossibleQueries = set(lArgWords)
        var_word_information = 0.0
        
        """

        #ALGORITM 1
        for strWord in lQueryWords:

            for i in range(5):
                if int(tPerm[i]) == 2:
                    if strargWord[i] != strWord[i]:
                        break
                if int(tPerm[i]) == 0:
                    if strargWord[i] in strWord:
                        break
                if int(tPerm[i]) == 1:
                    if (strargWord[i] not in strWord) or (strargWord[i] == strWord[i]):
                        break
            else:
                #break
                sPossibleQueries.add(strWord)

        """   
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
if __name__=="__main__":

    cpuCount = multiprocessing.cpu_count() 

    tStart = time.perf_counter()
    
    pool = multiprocessing.Pool(cpuCount - 4)
    strWord, lPermutation = read_permutation_file()
    lTruncatedList = truncate_list(strWord, lPermutation, lQueryWords)
    print(*lTruncatedList)
    #while(read_permutation_file[1].count(2) != 5):
    lEntropy = pool.map(partial(word_entropy, lTruncatedList), range(len(lTruncatedList)))
    pool.close()
    pool.join()
    maxEntropy = 0
    for i in range(len(lEntropy)):
        if lEntropy[i] > maxEntropy:
            maxEntropy = lEntropy[i]
            strNextQuery = lTruncatedList[i]
    with open("cuvan_query.txt", "w") as cuv_query:
        cuv_query.write(strNextQuery)


    

    print("Done!")
    

    tStop = time.perf_counter()
    print(tStop - tStart) 
    
    """
    with open("entropie_cuvinte.txt", "w") as entropyDictionary:
        for i in range(0, 100):
            entropyDictionary.write(lQueryWords[i] + ' ' + str(lEntropy[i]) + '\n')
    """