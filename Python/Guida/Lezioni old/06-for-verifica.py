# comando per ripetere quanto vogliamo noi: for
# for i in range(0,5):
#     print("ciao")

# se voglio scrivere dei numeri che aumentano 
# for i in range(5):
#     print(i)

# se aggiungo un terzo numero gli dico quanti deve saltarne
# for i in range(0,10,3):
#     print(i)

# esercizio 1: 
# calcola la somma dei primi 10 numeri e stampala con un print
# somma = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

# a = 1
# for i in range(10): # range 10 perchè primi 10 numeri
#     a = a + i
# print(a)

# a = 1
# for i in range(10):
#     a = a + i
# print(a)

# fai un for che prima chiede il numero e poi ti stampa la sua tabellina
numero = int(input("Dimmi un numero da 1 a 9 "))
for i in range(10):
    risultato = numero * i
    print(risultato)
