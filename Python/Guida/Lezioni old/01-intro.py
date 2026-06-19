nome = input("Come ti chiami? ") 
# input salva sempre delle stringhe
# print(nome) # controllo che ha salvato la cosa giusta
cognome = input("Qual è il tuo cognome? ")

# print("Ti chiami " + nome + " " + cognome)
#c'è un modo più smart di unire le stringhe
print(f"Ti chiami {nome} {cognome}")
# quando chiedo un numero devo mettere int davanti
eta = int(input("Quanti anni hai? "))
# non posso unire un numero con una stringa
# usare f e le parentesi graffe permette di non preoccuparsi
# di convertire le stringhe in numeri
print(f"Ti chiami {nome} e hai {eta} anni")
