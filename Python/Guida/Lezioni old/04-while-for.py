# 04-while-for.py 
# for e while sono 
# due comandi per fare delle azioni ripetute
# for i in range(5):
#    print("ciao")

# for i in range(10):
#    print(i)

# i = 0
# while i < 10:
#     print("ciao")
#     # con while ricordiamoci di mettere la condizione
#     # di stop 
#     i = i + 1


# la password è "Yassine"
# voglio fare un programma che mi chiede la password
# se la password è giusta, mi dice bravo
# se la passoword è sbagliata me la richiede
# password = "Yassine"
# parola = input("Scrivi la password: ")

# #!= vuole dire diverso
# while parola != password:
#     parola = input("Hai sbagliato, Scrivi la password: ")
# #qui scrivo cosa deve fare quando indovina
# print("Hai azzeccato la password!")

# creo un programma che da un numero definito mi 
# scrive i 10 successivi
A = int(input("dimmi un numero"))
a = A + 10
while A < a:
    print(A)
    A = A + 1