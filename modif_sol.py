fin = open("solutii.txt", "r")
fout = open("solutii2.txt", "w")

x = fin.readlines()
#print(x)
for words in x:
    lwords = words.split()
    print(lwords)
    for i in range(len(lwords)):
        word = lwords[i]
        fout.write(word.lower())
        if i != len(lwords) - 1:
            fout.write(", ")
    fout.write('\n')
