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
        
    for tPerm in lPermutations:
        sPossibleQueries = set(lQueryWords)
        var_word_information = 0.0
        ok = 1
        
        #TODO check if permutation is valid before applying it
        #i.e. if a word has 2 of 'A' and the query has an 'A', both are
        #collored yellow
        
        """

        #ALGORITM 1
        for strWord in lQueryWords:

            for i in range(5):
                for j in range(5):
                    if (strargWord[i] == strargWord[j]):
                        if (tPerm[i] == 1 or tPerm[i] == 2) and tPerm[j] == 0:
                            ok = 0
                            break
            if ok:
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
                for j in range(5):
                    if (strargWord[i] == strargWord[j]):
                        if (tPerm[i] == 1 or tPerm[i] == 2) and tPerm[j] == 0:
                            ok = 0
                            break

        if ok:
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
                        if strargWord[i] not in strWord or strargWord[i] == strWord[i]:
                            sPossibleQueries.discard(strWord)
        
        
        #print(len(sPossibleQueries))
        #print([str(x) for x in sPossibleQueries])
        #print(str(len(sPossibleQueries)) + ' ' + str(len(lQueryWords)))
        if (len(sPossibleQueries) != 0):
            word_prob = len(sPossibleQueries) / len(lQueryWords) 
            #print(tPerm)    
            #print(word_prob)
            var_word_information = -round((word_prob)*math.log2(word_prob),7)
            #print(*tPerm, end="    ")
            #print(var_word_information, end= "    ")
            #print(len(sPossibleQueries))
        #print(var_word_information)
        #print(tPerm)
        #print()
        finalEntropy += var_word_information

    #print(finalEntropy)
    return finalEntropy

def dictionary_entropy(arg):

    #print(f"{arg} done!")
    sWord = lQueryWords[arg]
    return word_entropy(sWord)

    #print(dic_entropty.items())


# DOMNULE RUSU SUNTEM INTELIGENTI :))))))
# (va rugam sa ne strangeti mana)
if __name__=="__main__":

    cpuCount = multiprocessing.cpu_count()

    tStart = time.perf_counter()
    pool = multiprocessing.Pool(cpuCount)
    
    dEntropy = pool.map(dictionary_entropy, range(0,len(lQueryWords)))
    pool.close()
    pool.join()

    print("Done!")
    

    tStop = time.perf_counter()
    print(tStop - tStart)
    
    with open("entropie_cuvinte.txt", "w") as entropyDictionary:
        for i in range(0, len(lQueryWords)):
            entropyDictionary.write(lQueryWords[i] + ' ' + str(dEntropy[i]) + '\n')
#print(word_entropy("HOBBY"))

#print(lPermutations)
