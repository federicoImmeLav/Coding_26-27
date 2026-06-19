# # # lista
# # spesa = ["acqua", "farina", "zucchero"]

# # # esempio di dizionario
# # ingrediente = {"cosa": "mele", "quanto": 5}

# # persona = {"nome": "Yassine", "cognome": "Ahrar", "eta": 14}

# # codice che mi chiede informazioni e le mette in un dizionario
# # nome = input("Qual è il tuo nome? ")
# # cognome = input("Qual è il tuo cognome? ")
# # eta = int(input("Quanti anni hai? "))

# # prendi le info che ha chiesto e mettile in un dizionario
# # persona = {"nome": nome, "cognome": cognome, "eta": eta}

# # print(persona)

# ######################################################################

# # programma che mi chiede gli ingredienti per una ricetta, va avanti 
# # a chiedermeli fino a quando non dico stop e mi crea una lista 
# # con gli ingredienti (while)

# # creo lista vuota
# # spesa = []

# # chiedo il primo ingrediente
# # ingrediente = input("Che ingrediente ti serve? ")

# # while
# # while ingrediente != "stop":
# #     spesa.append(ingrediente) # aggiungo alla lista l'ingrediente
# #     ingrediente = input("Dimmi un altro ingrediente (stop per fermare) ")

# # metto il comando che mi stampa la lista quando finisce
# # per stampare ciascun elemento singolo di una lista si usa for
# # for i in spesa: 
# #     print(i)

# ##############################################################################
# # programma che mi chiede oltre all'ingrediente, anche la quantità, 
# # con queste informazioni costruisce una lista di dizionari 
# # creo lista vuota
# spesa = []
# # chiedo il primo ingrediente
# ingrediente = input("Che ingrediente di serve? ")
# # while
# while ingrediente != "stop":
#     quanto = int(input("Quanto te ne serve? "))
#     # creo il dizionario per il singolo elemento che ho chiesto
#     elemento = {"nome": ingrediente, "quantità": quanto}
#     # aggiungo l'elemento alla lista della spesa
#     spesa.append(elemento)
#     # richiedo l'ingrediente così riparte il ciclo
#     ingrediente = input("Dimmene un altro (stop per finire) ")

# # metto il comando che mi stampa la lista quando finisce
# # per stampare ciascun elemento singolo di una lista si usa for
# for i in spesa: 
#     print(i)


print("Ciao! Rispondi alle domande qui sotto.")

nome = input("Come ti chiami? ")
anno_nascita = int(input("In che anno sei nato? "))

print(f"Ciao, {nome}! Sei nato nel {anno_nascita}")