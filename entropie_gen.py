from itertools import combinations_with_replacement, product
from operator import countOf
import random
from re import U

with open("cuvinte_wordle.txt", "r") as wordle_list:
    text = wordle_list.read()
    cuvinte = list(map(list, text.split()))

permutari = []

permutari = list(product('⬜🟨🟩', repeat=3))
#for x in cuvinte:
   # for i in range (243):
    #    for j in range (5):
     #        aux = i
     #        permutari=aux%3
     #        aux=aux//3   
print(permutari)
#def temp1():
