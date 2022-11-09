import random

with open("cuvinte_wordle.txt", "r") as wordle_list_file:
    text = wordle_list_file.read()
    cuvinte = [str(x) for x in text.split()]
wordle_list_file.close()
  
guess_word = random.choice(cuvinte)

def writePermutationFile():
    with open("rez_query.txt", "w") as rez_query:
        for x in permutare_query:
            rez_query.write(str(x) + ' ')
    rez_query.close()


guess_word = list(guess_word)
print(guess_word)
user_input = []
L_user_inputs = []
permutare_query = [2, 2, 2, 2, 2]

cnt = 0

while user_input != guess_word:
    user_input = list(input("baga cuv: ").upper())
    s_user_input = "".join(user_input)
    s_guess_word = "".join(guess_word)
    if s_user_input not in cuvinte:
        print("nu e query valid")
        continue
    L_user_inputs.append(s_user_input)
    cnt += 1
    # litera pe aceeasi pozitie 🟩
    # litera nu e in pozitia corecta 🟨
    # litera nu exista ⬜

    #array cu cifre bazat pe ce intoarce query-ul
    # 0 -> aceeasi pozitie
    # 1 -> undeva in cuvant
    # 2 -> nu este
    

    print(" ".join(user_input))
    
    for i in range(5):
        if user_input[i] == guess_word[i]:
            permutare_query[i] = 0
            print('🟩', end='')
        elif user_input[i] in guess_word:
            permutare_query[i] = 1
            print('🟨', end='')
        else:
            permutare_query[i] = 2
            print('⬜', end='')
    print()
    writePermutationToFile()
else: 
    print("Ai gasit") 

print(f"Felicitari, dragule! Ai luat sfantul 5 la A$C, din {cnt} incercari.")
print(f"Istoricul query-urilor tale este: {L_user_inputs}")

with open("rezultate.txt", "w") as rezultate:
    rezultate.write(s_guess_word + " ")
    for x in L_user_inputs:
        rezultate.write(str(x) + " ")
    #rezultate.write(str(x) for x in L_user_inputs)


