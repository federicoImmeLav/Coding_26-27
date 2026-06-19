# # 1. Ripasso if
# # Creo un programma che mi chiede un numero
# # se il numero è maggiore di 15 mi dice "maggiore"
# # se il numero è minore di 15 mi dice "minore"

# # per chiedere si mette input e se è un numero si mette int
# numero = int(input("Dimmi un numero casuale: "))

# # # dopo if metto la condizione che mi serve
# if numero >= 15:
#     print("maggiore")
# # per aggiungere un altro if nella stessa condizione 
# # metto elif
# elif numero < 15:
#     print("minore")
########################################################################
# 2. Esercizio con for
# Creo un programma che mi scrive tutti i numeri
# da 27 a 56

# per cambiare i numeri dobbiamo cambiare 
# il range in cui si muove la i 
# for i in range(27,57):
#     print(i)
# il range può essere sia numero ma anche stringa
# for i in "ciao":
#     print(i)
########################################################################
# 3. Esercizio for
# Creo un programma che stampa i numeri
# pari da 0 a 10 
# i numeri pari sono quelli che se divisi
# per 2 danno resto 0 
# in python per calcolare il resto in una divisione
# si usa % 

# per la i nel range 0,10
# se faccio i diviso 2 e ottengo come resto 0
# stampa i
# for i in range(0,10):
#     # stampa solo i numeri pari, 
#     # non stampa quelli che hanno un resto
#     if i % 2 != 0:
#         print(i)
########################################################################
# # 4. Esercizio con while
# # Creo un programma che mi chiede di indovinare
# # un numero minore di 45
# # fino a quando non lo indovino, continua a chiedermelo
# # quando lo indovino mi dice "bravo"

# # scrivo il punto di partenza
# numero = 36

# # scrivo la prima domanda
# tentativo = int(input("Indovina il numero, è minore di 45: "))

# # faccio il while
# while tentativo != numero:
#     if tentativo > 45:
#         print("avevo detto meno di 45!")
#         tentativo = int(input("riprova: "))
#     print("hai sbagliato")
#     tentativo = int(input("riprova: "))

# # scrivo cosa succede quando indovino
# print("hai indovinato!")
