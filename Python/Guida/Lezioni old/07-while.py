# for i in range(5):
#     print("ciao")

# for ripete le cose il numero che vogliamo noi, while invece ripete
# finchè non succede qualcosa

# i = 0
# while i < 5:
#     print("ciao")
#     i = i + 1 # condizione di stop

#################################################################################

# programma che mi chiede come mi chiamo e fino a quando non rispondo
# giusto continua a chiedermelo

# definisco quale è il nome giusto
# nomegiusto = "Federico"

# # chiedo la prima volta il nome
# nome = input("Come ti chiami? ") 

#  # fino a quando il nome è diverso dal nome 
#  # giusto fai quello che c'è scritto qui dentro
# while nome != nomegiusto:
#     print("hai sbagliato")
#     # richiedo il nome
#     nome = input("Riprova, come ti chiami? ")

# # solo quando il nome è corretto, scrivi questo
# print("Bravo, hai indovinato!")

#################################################################################

# programma che chiede un numero e somma i numeri 
# che scrivo fino a quando non scrivo stop 

# punto di partenza della mia somma
# num = 0

# # chiedo un numero a caso
# numero_chiesto = input("Dimmi un numero a caso ")

# # fino a quando dico numeri e non stop, lui somma, quando dico stop si ferma
# while numero_chiesto != "stop":
#     num = num + int(numero_chiesto) # somma il numero precedente
#     print(f"la somma è: {num}") # mi scrive a quanto è arrivata la somma
#     # mi chiede un altro numero, oppure stop per fermare
#     numero_chiesto = input("dimmi un altro numero, se vuoi fermare dimmi stop ")

# #  finisce tutto, mi dice a quanto sono arrivato
# print(f"ti sei fermato a {num}")

#################################################################################
# scrivo un programma che mi fa indovinare un numero

# punto di partenza, definisco il numero da indovinare
numero_segreto = 17

# chiedo alla persona di dirmi un numero per indovinare
numero = int(input("Indovina il numero segreto (è minore di 20) "))

# finchè la risposta è diversa dal numero_segreto continua a chiedermi numeri
while numero != numero_segreto:
    # prima di fare tutto controllo se il numero è minore di 20
    if numero < 20:
        print("hai sbagliato!")
        numero = int(input("dimmi un altro numero "))
    # se non è minore di 20 dico questo:
    else:
        print("avevo detto minore di 20!")
        numero = int(input("dimmi un altro numero "))

print("Corretto! Bravo!")
