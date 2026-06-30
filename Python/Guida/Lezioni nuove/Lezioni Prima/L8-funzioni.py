# ============================================================
# LEZIONE 8 — Le funzioni
# Unità 3 · Settimane 15-16
# ============================================================
# Prerequisiti: L7 (liste), L4-L6 (cicli)
# Obiettivo: lo studente sa definire funzioni con parametri
# e return, e capisce perché separare il codice in funzioni.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA — codice che si ripete
# ------------------------------------------------------------

# immagina di dover salutare tre studenti all'inizio del programma:

nome1 = "Marco"
print(f"Ciao {nome1}! Benvenuto a scuola.")
print(f"Oggi è una bella giornata, {nome1}.")
print("---")

nome2 = "Giulia"
print(f"Ciao {nome2}! Benvenuta a scuola.")
print(f"Oggi è una bella giornata, {nome2}.")
print("---")

nome3 = "Andrea"
print(f"Ciao {nome3}! Benvenuto a scuola.")
print(f"Oggi è una bella giornata, {nome3}.")
print("---")

# il codice è quasi identico tre volte
# se vuoi cambiare il messaggio, devi modificarlo in tre posti
# con 30 studenti, dovresti copiare il blocco 30 volte
# una funzione risolve questo: scrivi il codice una volta sola
# e lo "chiami" ogni volta che ti serve


# ------------------------------------------------------------
# 2. DEF — definire e chiamare una funzione
# ------------------------------------------------------------

# la parola chiave def dice a Python che stiamo definendo una funzione
# il nome deve descrivere cosa fa
# le parentesi e i due punti sono obbligatori
# tutto il codice indentato sotto è il corpo della funzione

# passo 1: DEFINIRE la funzione (scrivi la ricetta una volta)
def saluta_base():
    print("Ciao! Benvenuto a scuola.")
    print("Oggi è una bella giornata.")
    print("---")

# passo 2: CHIAMARE la funzione (esegui la ricetta quando serve)
saluta_base()
saluta_base()
saluta_base()

# ATTENZIONE: la funzione non parte da sola
# def dice solo "questa funzione esiste e si chiama così"
# solo quando scrivi saluta_base() con le parentesi la esegui


# ------------------------------------------------------------
# 3. PARAMETRI — rendere la funzione flessibile
# ------------------------------------------------------------

# la funzione qui sopra fa sempre la stessa cosa per tutti
# con un parametro possiamo passarle un'informazione diversa ogni volta
# il parametro è una variabile che esiste solo dentro la funzione

def saluta(nome):
    print(f"Ciao {nome}! Benvenuto a scuola.")
    print(f"Oggi è una bella giornata, {nome}.")
    print("---")

# ora posso personalizzare ogni saluto con un valore diverso
saluta("Marco")
saluta("Giulia")
saluta("Andrea")

# posso anche passare una variabile come parametro
studente = input("Come ti chiami? ")
saluta(studente)


# ------------------------------------------------------------
# 4. RETURN — ottenere un risultato dalla funzione
# ------------------------------------------------------------

# finora le funzioni hanno solo FATTO cose (stampato testo)
# ma spesso ci serve una funzione che CALCOLI qualcosa
# e ci restituisca il risultato — per questo esiste return

def doppio(numero):
    return numero * 2

# il valore restituito da return si può salvare in una variabile
risultato = doppio(5)
print(risultato)         # stampa 10

# oppure usarlo direttamente
print(doppio(7))         # stampa 14
print(doppio(3) + 1)     # stampa 7

# --- la trappola di print dentro una funzione ---
#
# è tentante scrivere print dentro la funzione invece di return:

def doppio_con_print(numero):
    print(numero * 2)    # mostra il risultato, ma NON lo restituisce

valore = doppio_con_print(5)   # esegue la funzione: stampa 10
print(valore)                  # stampa None — il risultato è andato perso!

# None è il "niente" di Python: significa che la funzione non ha dato nulla
# se hai bisogno di usare il risultato (salvarlo, confrontarlo, sommarlo),
# devi usare return, non print


# ------------------------------------------------------------
# 5. PIÙ PARAMETRI — passare più informazioni alla funzione
# ------------------------------------------------------------

# una funzione può avere quanti parametri servono
# si scrivono separati da virgola, nell'ordine in cui li passi

def area_rettangolo(base, altezza):
    return base * altezza

# l'ordine conta: primo valore → primo parametro, ecc.
# area_rettangolo(5, 3) → base = 5, altezza = 3
print(area_rettangolo(5, 3))     # 15
print(area_rettangolo(10, 4))    # 40

# esempio con input: calcolare il prezzo dopo uno sconto percentuale
def prezzo_scontato(prezzo, sconto_percentuale):
    risparmio = prezzo * sconto_percentuale / 100
    return prezzo - risparmio

p = float(input("Prezzo originale (€): "))
s = float(input("Sconto in percentuale: "))
finale = prezzo_scontato(p, s)
print(f"Prezzo scontato: {finale:.2f} €")


# ------------------------------------------------------------
# 6. FUNZIONI + LISTE — la combinazione più utile
# ------------------------------------------------------------

# una funzione che riceve una lista può elaborarla tutta
# e restituire un risultato riassuntivo

def media(numeri):
    somma = 0
    for n in numeri:
        somma = somma + n
    return somma / len(numeri)

# come funziona la chiamata media([7, 8, 6, 9, 5]):
# giro 1: somma = 0 + 7 = 7
# giro 2: somma = 7 + 8 = 15
# giro 3: somma = 15 + 6 = 21
# giro 4: somma = 21 + 9 = 30
# giro 5: somma = 30 + 5 = 35
# return 35 / 5 = 7.0

voti = [7, 8, 6, 9, 5]
print(f"Media voti: {media(voti):.1f}")

# la stessa funzione funziona su qualsiasi lista di numeri
temperature = [12, 18, 22, 15, 9, 20, 17]
print(f"Temperatura media: {media(temperature):.1f}")

# funzione con lista e un secondo parametro di confronto
def conta_sopra(numeri, soglia):
    contatore = 0
    for n in numeri:
        if n > soglia:
            contatore = contatore + 1
    return contatore

print(f"Voti superiori al 6: {conta_sopra(voti, 6)}")
print(f"Giorni sopra 15°C: {conta_sopra(temperature, 15)}")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Scrivi una funzione saluta_formale(nome, titolo) che
#    stampa: "Buongiorno, Prof. Rossi!" (usa i parametri per
#    nome e titolo). Chiamala almeno tre volte con valori diversi.
#
# 2. Scrivi una funzione area_triangolo(base, altezza) che
#    restituisce l'area (base * altezza / 2).
#    Poi chiedi all'utente base e altezza di tre triangoli,
#    calcola e stampa l'area di ciascuno usando la funzione.
#
# 3. Hai questa lista di voti: [5, 7, 8, 4, 6, 9, 5, 7, 6, 8]
#    Scrivi due funzioni:
#    - media(voti): restituisce la media dei voti
#    - promossi(voti): restituisce quanti voti sono >= 6
#    Usale entrambe sulla lista e stampa i risultati.
# ============================================================
