from operator import countOf
import random
from re import U

with open("cuvinte_wordle.txt", "r") as wordle_list:
    text = wordle_list.read()
    cuvinte = list(map(str, text.split()))
    #TODO de ce am folosit asta
  
    guess_word = random.choice(cuvinte)

guess_word = list(guess_word)
#guess_word = ['S', 'I', 'U', 'U', 'U']
user_input = []

cnt = 0

while user_input != guess_word:
    user_input = list(input("baga cuv: ").upper())
    s_user_input = "".join(user_input)
    s_guess_word = "".join(guess_word)
    if s_user_input not in cuvinte:
        print("nu e query valid")
        continue
    cnt += 1
    # litera pe aceeasi pozitie 🟩
    # litera nu e in pozitia corecta 🟨
    # litera nu exista ⬜

    print(" ".join(user_input))
    ok = 0
    
    for i in range(5):
        if user_input[i] == guess_word[i]:
            print('🟩', end='')
        elif user_input[i] in guess_word and countOf(user_input, user_input[i]) <= countOf(guess_word, user_input[i]):
            print('🟨', end='')
        elif user_input[i] in guess_word and countOf(user_input, user_input[i]) > countOf(guess_word, user_input[i]):
            if ok != countOf(user_input, user_input[i]) - countOf(guess_word, user_input[i]):
               print('🟨', end='')
               ok += 1
            else:
                print('⬜', end='')
        else:
            print('⬜', end='')
    print()
        
else: 
    print("Ai gasit") 

print(f"Felicitari, dragule! Ai luat sfantul 5 la A$C, din {cnt} incercari.")
