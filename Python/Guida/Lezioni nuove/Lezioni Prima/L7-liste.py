# ============================================================
# LEZIONE 7 — Le liste
# Unità 3 · Settimane 13-14
# ============================================================
# Prerequisiti: L4 (for, iterazione su liste), L6 (cicli misti)
# Obiettivo: lo studente sa creare e modificare una lista,
# aggiungere e rimuovere elementi, ordinarla e scorrerla.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA — perché le variabili singole non bastano
# ------------------------------------------------------------

# immagina di voler memorizzare i voti di 5 studenti
# con le variabili che conosci, dovresti fare così:

voto_1 = 7
voto_2 = 8
voto_3 = 6
voto_4 = 9
voto_5 = 5

# ora vuoi calcolare la media: devi scrivere tutti i nomi a mano
media = (voto_1 + voto_2 + voto_3 + voto_4 + voto_5) / 5
print(f"Media: {media}")

# questo funziona con 5 voti — ma con 30 studenti?
# dovresti scrivere 30 variabili e ricordare tutti i nomi
# una lista risolve il problema: è un'unica variabile
# che contiene più valori, tutti accessibili con un indice


# ------------------------------------------------------------
# 2. CREARE UNA LISTA — e accedere agli elementi
# ------------------------------------------------------------

# una lista si crea con le parentesi quadre, valori separati da virgole
voti = [7, 8, 6, 9, 5]

# ogni elemento ha una posizione: si chiama INDICE
# gli indici partono da 0, non da 1

#  voti =  [ 7,  8,  6,  9,  5 ]
# indice:    0   1   2   3   4

print(voti[0])    # stampa 7  ← primo elemento
print(voti[1])    # stampa 8  ← secondo elemento
print(voti[4])    # stampa 5  ← quinto (e ultimo) elemento

# trucco: -1 prende l'ultimo elemento, -2 il penultimo, ecc.
print(voti[-1])   # stampa 5  ← ultimo
print(voti[-2])   # stampa 9  ← penultimo

# len() dà il numero di elementi nella lista
print(len(voti))  # stampa 5

# funziona anche con stringhe
materie = ["italiano", "matematica", "storia", "inglese"]
print(materie[0])    # italiano
print(materie[-1])   # inglese
print(len(materie))  # 4


# ------------------------------------------------------------
# 3. APPEND — aggiungere un elemento alla fine
# ------------------------------------------------------------

# finora abbiamo creato liste con tutti i valori già noti
# ma spesso vogliamo costruire una lista raccogliendo dati dall'utente
# append() aggiunge un elemento in fondo alla lista

# esempio: costruire una lista partendo vuota
spesa = []       # lista vuota

spesa.append("pane")
spesa.append("latte")
spesa.append("uova")

print(spesa)     # ['pane', 'latte', 'uova']
print(len(spesa))  # 3

# pattern: raccogliere dati dall'utente con append
# passo 1: crea una lista vuota FUORI dal ciclo
# passo 2: for ... in range(quante volte):
# passo 3:     chiedi il dato all'utente
# passo 4:     append lo aggiunge alla lista
# passo 5: dopo il ciclo, usa la lista completa

n = int(input("Quanti voti vuoi inserire? "))
registro = []

for i in range(n):
    voto = int(input(f"Voto {i + 1}: "))
    registro.append(voto)

print(f"Voti inseriti: {registro}")
print(f"Numero di voti: {len(registro)}")


# ------------------------------------------------------------
# 4. MODIFICARE UN ELEMENTO — cambiare un valore per indice
# ------------------------------------------------------------

# puoi cambiare il valore di un elemento assegnandogli un nuovo valore
# si usa la stessa sintassi dell'accesso, ma con l'uguale

voti = [7, 8, 6, 9, 5]
print(voti)          # [7, 8, 6, 9, 5]

voti[2] = 10         # sostituisce il voto in posizione 2 (era 6)
print(voti)          # [7, 8, 10, 9, 5]

# attenzione: se usi un indice che non esiste, Python dà errore
# voti[10] = 8  ← IndexError: list index out of range


# ------------------------------------------------------------
# 5. REMOVE — rimuovere un elemento per valore
# ------------------------------------------------------------

# remove() rimuove la prima occorrenza del valore che gli passi

spesa = ["pane", "latte", "uova", "pane"]
print(spesa)               # ['pane', 'latte', 'uova', 'pane']

spesa.remove("latte")
print(spesa)               # ['pane', 'uova', 'pane']

# se il valore appare più volte, remove toglie solo la prima
spesa.remove("pane")
print(spesa)               # ['uova', 'pane']

# ATTENZIONE: se provi a rimuovere un valore che non c'è,
# Python dà un ValueError — vale la pena sapere che esiste
# spesa.remove("succo")  ← ValueError: list.remove(x): x not in list

# per evitare l'errore, puoi controllare prima con l'operatore in
prodotto = input("Cosa vuoi togliere dalla spesa? ")
if prodotto in spesa:
    spesa.remove(prodotto)
    print(f"'{prodotto}' rimosso. Lista aggiornata: {spesa}")
else:
    print(f"'{prodotto}' non è nella lista.")


# ------------------------------------------------------------
# 6. SORT E REVERSE — ordinare e invertire
# ------------------------------------------------------------

# sort() ordina la lista in ordine crescente (dal più piccolo al più grande)
# reverse() inverte l'ordine degli elementi

numeri = [3, 1, 4, 1, 5, 9, 2, 6]
print(numeri)         # [3, 1, 4, 1, 5, 9, 2, 6]

numeri.sort()
print(numeri)         # [1, 1, 2, 3, 4, 5, 6, 9]

numeri.reverse()
print(numeri)         # [9, 6, 5, 4, 3, 2, 1, 1]

# funziona anche con stringhe: sort() ordina alfabeticamente
nomi = ["Giulia", "Andrea", "Marco", "Beatrice"]
nomi.sort()
print(nomi)           # ['Andrea', 'Beatrice', 'Giulia', 'Marco']

# IMPORTANTE: sort() e reverse() modificano la lista originale
# non restituiscono una nuova lista — la cambiano direttamente

# esempio pratico: raccogliere voti e mostrarli in ordine
punteggi = [62, 85, 71, 90, 58, 77]
punteggi.sort()
print(f"Dal più basso al più alto: {punteggi}")

punteggi.reverse()
print(f"Dal più alto al più basso: {punteggi}")


# ------------------------------------------------------------
# 7. SCORRERE UNA LISTA — for su una lista modificata
# ------------------------------------------------------------

# il for su una lista funziona sempre allo stesso modo
# anche dopo append, remove, sort, reverse

voti = [6, 8, 7, 9, 5, 6]
voti.sort()

somma = 0
insufficienti = 0

for voto in voti:
    somma = somma + voto
    if voto < 6:
        insufficienti = insufficienti + 1

media = somma / len(voti)

print(f"Voti in ordine:   {voti}")
print(f"Media:            {media:.1f}")
print(f"Insufficienti:    {insufficienti}")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Crea una lista con i nomi di 4 tuoi compagni di classe.
#    Stampa il primo e l'ultimo elemento usando gli indici.
#    Poi ordina la lista alfabeticamente con sort() e stampala.
#
# 2. Scrivi un programma che chiede all'utente di inserire
#    5 numeri interi uno alla volta (usa append per costruire
#    la lista). Alla fine stampa:
#    - la lista originale
#    - la lista ordinata dal più grande al più piccolo
#    - il valore massimo (che dopo il sort è il primo elemento)
#
# 3. Gestione lista della spesa.
#    Il programma parte con questa lista:
#    spesa = ["pane", "latte", "pasta", "uova", "succo"]
#    Poi fa un ciclo in cui chiede all'utente cosa vuole fare:
#      "a" → aggiunge un prodotto (chiede quale)
#      "r" → rimuove un prodotto (chiede quale, gestisci
#             il caso in cui non esiste)
#      "s" → stampa la lista ordinata
#      "q" → esce dal programma
#    Suggerimento: usa un while con una variabile booleana
#    o controlla che la scelta non sia "q".
# ============================================================
