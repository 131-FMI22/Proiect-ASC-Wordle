# Proiect-ASC-Wordle


## Tabela de Continut

- [Cum functioneaza](#cum-functioneaza)
- [Creatori](#creatori)
- [Referinte](#referinte)
- [Feedback](#feedback)


## Cum functioneaza

Programul nostru este o copie a jocului Wordle, asupra caruia putem initializa un proces separat care ne ofera hinturi.

Hinturile sunt calculate folosind entropia lui Shannon pe o lista de cuvinte triata, in functie de ce ne returneaza ultimul query.

Procesele comunica intre ele prin intermediul unui JoinableQueue, componenta a librariei multiprocessing.

Media de guess-uri din care programul nostru gaseste un cuvant este 4.373581.

Programul nostru a fost conceput in jurul versiunii Python 3.11.

Mai multe detalii pot fi gasite in fisierul wordle.py


## Creatori

**Tudor Chitu**
- <https://github.com/tedi11>
- <tudor.chitu@s.unibuc.ro>

**Alexandru-Cristian Ingeaua**
- <https://github.com/ingeaua>
- <alexandru-cristian.ingeaua@s.unibuc.ro>

**Alexandru Miclea**
- <https://github.com/AlexandruMiclea>
- <alexandru.miclea@s.unibuc.ro>

**Andrei Popa**
- <https://github.com/HaiduculRo>
- <andrei.popa1@s.unibuc.ro>

## Referinte

* https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/

* https://docs.python.org/3/library/itertools.html

* https://docs.python.org/3.7/library/multiprocessing.html

* cursurile domului profesor Radu Boriga, real life-savers :))

## Feedback

Daca ati dori sa ne oferiti feedback asupra proiectului, o puteti face [aici](https://github.com/131-FMI22/Proiect-ASC-Wordle/discussions/categories/feedback). Multumim!
