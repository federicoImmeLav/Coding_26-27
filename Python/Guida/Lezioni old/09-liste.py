# 1. Creo una lista di esempio
# spesa = ["mele", "pesche", "acqua"]

# stampo tutta la lista completa
# print(spesa) 

# stampo un elemento singolo della lista,
# quello al posto 1, che è il secondo
# print(spesa[1])

# 2. Aggiungere e rimuovere cose alla lista 
# nomi = ["Federico", "Alessio", "Amir"]
# print(nomi)

# aggiungo un nome alla lista
# nomi.append("Raf")
# print(nomi)

# rimuovo Federico dalla lista
# nomi.remove("Federico")
# print(nomi)

# 3. Ordino o cambio ordine alla lista
# num = [1, 5, 2, 7, 4] # lista di numeri
# print(num)

# ordine inverso della lista
# num.reverse()
# print(num)

# metto in ordine crescente la lista
# num.sort()
# print(num)

# metto in ordine decrescente
# num.sort()
# num.reverse()
# print(num)

########################################################
# 4. Esempi

# - Creo un programma che costruisce la lista della spesa
# chiedendo all'utente quali sono gli ingredienti.
# La lista deve essere di tre elementi

# creo la lista vuota 
# spesa = []

# programma mi chiede un elemento
# elemento = input("Dimmi il primo ingrediente ")
# metto l'elemento dentro a spesa
# spesa.append(elemento)

# ripeto due volte la richiesta
# elemento = input("Dimmi un altro ingrediente: ")
# spesa.append(elemento)

# elemento = input("Dimmi un altro ingrediente: ")
# spesa.append(elemento)

# print(spesa)

# faccio lo stesso esercizio con for
# spesa = []

# for i in range(3):
#     elemento = input("Dimmi un ingrediente: ")
#     spesa.append(elemento)

# print(spesa)

############################################################
# - Creo un programma che mi fa fare una lista della spesa
# va avanti a crearla fino a quando non dico stop
# quando dico stop, mette la lista in ordine alfabetico
# dopo mi stampa la lista
# spesa = []
# elemento = ""

# # finchè elemento non è uguale a stop, continua ad aggiungere
# # elemento alla lista e continua a chiedermene un altro 
# while elemento != "stop":
#     elemento = input("dimmi un ingrediente, se vuoi fermarti dimmi stop: ")
#     spesa.append(elemento)

# # quando il while finisce, ordino la lista e la stampo
# spesa.sort()
# spesa.remove("stop") # tolgo stop dalla lista
# for i in spesa:
#     print(i)



