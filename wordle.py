import multiprocessing
import time
from functools import partial

with open("cuvinte_wordle.txt", "r") as wordleList:
    text = wordleList.read()
    lWords = [str(x) for x in text.split()]
  

def write_permutation_file():
    with open("rez_query.txt", "w") as rezQuery:
        rezQuery.write(sUserInput + " ")
        for x in lQueryPermutation:
            rezQuery.write(str(x) + ' ')

sUserInput = ""

def read_query_word():
    while True:
        with open("cuvan_query.txt", "r") as cuvantQuery:
            sUserInput = cuvantQuery.read()

lUserInput = []
sGuessWord = "DRACU"
lAllUserInputs = []
lQueryPermutation = [0,0,0,0,0]

cntFinal = 0


lGuessWord = list(sGuessWord)
cnt = 0
def wordle_game():
        while lUserInput != lGuessWord:
            
            lUserInput = list(input("baga cuv: ").upper())
            sUserInput = "".join(lUserInput)
            if sUserInput not in lWords:
                print("nu e query valid")
                continue
            lAllUserInputs.append(sUserInput)
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
            write_permutation_file()
            #entropie_gen.word_information()
        else: 
            print("Ai gasit") 

        print(f"Felicitari, dragule! Ai luat sfantul 5 la A$C, din {cnt} incercari.")
        print(f"Istoricul query-urilor tale este: {lAllUserInputs}")

        with open("rezultate.txt", "w") as rezultate:
            rezultate.write(sGuessWord + " ")
            for x in lAllUserInputs:
                rezultate.write(str(x) + " ")
            #rezultate.write(str(x) for x in lAllUserInputs)

        cntFinal += cnt

medieRezolvari = cntFinal / len(lWords)

print(f"Programul nostru ghiceste cuvantul in {medieRezolvari} incercari!")

if __name__=="__main__":
    tStart = time.perf_counter()

    p1 = multiprocessing.Process(read_query_word, )
    p2 = multiprocessing.Process(wordle_game, )
    p1.start()
    p2.start()

    p1.join()
    p2.join()