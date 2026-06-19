# 012-funz+while.py
# FUNZIONI
# insieme di comandi che fanno qualcosa
# e ci restituiscono un risultato 

# funzione che calcola area del triangolo
# base x altezza / 2
# def areaTri(base,altezza):
    # return base * altezza / 2

# print(areaTri(4,7)) # base 4 altezza 7
# print(areaTri(10,4)) # base 10 altezza 4

#################################################
# funzione usata insieme a un for
# Data una lista di numeri [2,5,7,9]
# creare una funzione che calcola 
# il triplo di un numero
# stampare la lista con tutti i valori triplicati

# lista = [2,5,7,9]

# # creo la funzione
# def triplo(num):
#     return num * 3

# # prendo ciascun elemento della lista (i) 
# # e lo triplico usando la funzione 
# for i in lista:
#     print(triplo(i))
#################################################
# data la lista [2,5,6,8,9,11,14,15,17,18]
# usando for e %, stampare solo i numeri pari

# lista = [2,5,6,8,9,11,14,15,17,18]

# for i in lista:
#     if i % 2 == 0: # se è pari
#         print(i)

##################################################
# crea una funzione che moltiplica gli elementi 
# di una lista e ritorna il risultato

# def moltiplica(lista):
#     risultato = 1
#     for i in lista:
#         risultato = risultato * i
#     return risultato

# lista = [2,3,4]
# print(moltiplica(lista))

##################################################
# ripeto ciao usando while 50 volte
# punto di partenza
# a = 0
# # while
# while a < 50:
#     print("ciao")
#     a = a + 1 # metere la condizione che lo fermare

##################################################
# while che mi chiede un animale fino a quando 
# non lo indovino (l'animale da indovinare è cane)

soluzione = "cane"

animale = input("Indovina l'animale che sto pensando ")

while animale != soluzione:
    animale = input("Riprova: ")

print("Bravo hai indovinato!") # qui scrivo quando vinco
