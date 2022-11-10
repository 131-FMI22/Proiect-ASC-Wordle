from itertools import product
import math
import multiprocessing
import time

with open("cuvinte_wordle.txt", "r") as wordleList:
    sAux = wordleList.read()
    lQueryWords = [str(x) for x in sAux.split()]
wordleList.close()


#lPossibleQueries = lQueryWords
dEntropy = {}

def read_permutation_file():
    """
    Reads the rez_query.txt file, in which 5 digits are written,
    describing the wordle game's response to the last given query

    The feedback is returned by the function as a list
    """
    with open("rez_query.txt", "r") as rezQuery:
        strAux = rezQuery.read()
        lPermutation = [int(x) for x in strAux.split()]

    return lPermutation


lPermutations = []



L = read_permutation_file()
lPermutations = list(product('012', repeat=5))
#print(lPermutations[209])
#print(L)

def word_entropy(strargWord):
    finalEntropy = 0.0
    word_prob = 0.0
    
    
    """
        

        for strWord in lQueryWords:
            for i in range(5):
                if int(tPerm[i]) == 2:
                    if strargWord[i] != strWord[i]:
                        break
                if int(tPerm[i]) == 0:
                    if strargWord[i] in strWord:
                        break
                if int(tPerm[i]) == 1:
                    if strargWord[i] not in strWord:
                        break
            else:
                #break
                sPossibleQueries.add(strWord)

    """
    for tPerm in lPermutations:
        sPossibleQueries = set(lQueryWords)
        #print(tPerm)
        var_word_entropy = 0.0

        for i in range(5):
            if int(tPerm[i]) == 2:
                #verde
                for strWord in lQueryWords:
                    if strWord[i] != strargWord[i]:
                        sPossibleQueries.discard(strWord)
            if int(tPerm[i]) == 0:
                for strWord in lQueryWords:
                    if strargWord[i] in strWord:
                        sPossibleQueries.discard(strWord)
            if int(tPerm[i]) == 1:
                for strWord in lQueryWords:
                    if strargWord[i] not in strWord:
                        sPossibleQueries.discard(strWord)
        
        
        #print(len(sPossibleQueries))
        #print([str(x) for x in sPossibleQueries])
        #print(str(len(sPossibleQueries)) + ' ' + str(len(lQueryWords)))
        word_prob = round(len(sPossibleQueries) / len(lQueryWords),4)
        #print(word_prob)
        try:
            var_word_entropy -= word_prob*math.log(word_prob,2)
        except ValueError:
            pass
        finalEntropy += var_word_entropy
    
    #print(finalEntropy)
    return finalEntropy

def dictionary_entropy(arg):
    
    sWord = lQueryWords[arg]
    #dEntropy[sWord] = 
    return word_entropy(sWord)

    #print(dic_entropty.items())


# DOMNULE RUSU SUNTEM INTELIGENTI :))))))
# (va rugam sa ne strangeti mana)
if __name__=="__main__":

    cpuCount = multiprocessing.cpu_count()

    tStart = time.perf_counter()
    
    pool = multiprocessing.Pool(cpuCount)
    
    dEntropy = pool.map(dictionary_entropy, range(0,500))
    pool.close()
    pool.join()

    print("Done!")
    

    tStop = time.perf_counter()
    print(tStop - tStart)

    """
    with open("entropie_cuvinte.txt", "w") as entropyDictionary:
        for i in range(0, 500):
            entropyDictionary.write(lQueryWords[i] + ' ' + str(dEntropy[i]) + '\n')
    """

#print(word_entropy("TAREI"))

#print(lPermutations)