import random

with open("cuvinte_wordle.txt", "r") as wordleList:
    text = wordleList.read()
    lWords = [str(x) for x in text.split()]
wordleList.close()
  
sGuessWord = random.choice(lWords)

def write_permutation_file():
    with open("rez_query.txt", "w") as rezQuery:
        for x in lQueryPermutation:
            rezQuery.write(str(x) + ' ')
    rezQuery.close()


lGuessWord = list(sGuessWord)
print(lGuessWord)
lUserInput = []
lAllUserInputs = []
lQueryPermutation = [2, 2, 2, 2, 2]

cnt = 0

while lUserInput != lGuessWord:
    lUserInput = list(input("baga cuv: ").upper())
    sUserInput = "".join(lUserInput)
    if sUserInput not in lWords:
        print("nu e query valid")
        continue
    lAllUserInputs.append(sUserInput)
    cnt += 1
    # litera pe aceeasi pozitie 🟩
    # litera nu e in pozitia corecta 🟨
    # litera nu exista ⬜

    #array cu cifre bazat pe ce intoarce query-ul
    # 0 -> aceeasi pozitie
    # 1 -> undeva in cuvant
    # 2 -> nu este
    

    print(" ".join(lUserInput))
    
    for i in range(5):
        if lUserInput[i] == lGuessWord[i]:
            lQueryPermutation[i] = 0
            print('🟩', end='')
        elif lUserInput[i] in lGuessWord:
            lQueryPermutation[i] = 1
            print('🟨', end='')
        else:
            lQueryPermutation[i] = 2
            print('⬜', end='')
    print()
    write_permutation_file()
else: 
    print("Ai gasit") 

print(f"Felicitari, dragule! Ai luat sfantul 5 la A$C, din {cnt} incercari.")
print(f"Istoricul query-urilor tale este: {lAllUserInputs}")

with open("rezultate.txt", "w") as rezultate:
    rezultate.write(sGuessWord + " ")
    for x in lAllUserInputs:
        rezultate.write(str(x) + " ")
    #rezultate.write(str(x) for x in lAllUserInputs)


