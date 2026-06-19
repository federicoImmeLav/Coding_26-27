# ============================================================
# LEZIONE 1 — Output, variabili, tipi, input
# Unità 1 · Settimane 1-2
# ============================================================
# Obiettivo: lo studente sa stampare testo, salvare dati
# in variabili e chiedere informazioni all'utente.
# ============================================================


# ------------------------------------------------------------
# 1. PRINT — come far scrivere qualcosa al programma
# ------------------------------------------------------------

print("Ciao, mondo!")          # testo tra virgolette
print("Python è figo")
print(42)                      # i numeri non vogliono le virgolette


# ------------------------------------------------------------
# 2. VARIABILI — come salvare un dato in memoria
# ------------------------------------------------------------

# una variabile è come una scatola con un'etichetta
nome = "Luca"          # dentro c'è una parola (stringa)
eta = 16               # dentro c'è un numero intero
altezza = 1.75         # dentro c'è un numero con la virgola

print(nome)
print(eta)
print(altezza)


# ------------------------------------------------------------
# 3. TIPI — ogni dato ha un tipo
# ------------------------------------------------------------

# str  → stringa, cioè testo tra virgolette
# int  → numero intero  (es. 5, -3, 100)
# float → numero decimale (es. 1.75, 3.14)
# la virgola in Python si scrive con il PUNTO: 1.75 non 1,75

tipo_nome    = "Giulia"     # str
tipo_intero  = 20           # int
tipo_decimale = 9.5         # float


# ------------------------------------------------------------
# 4. F-STRING — il modo smart per costruire frasi con le variabili
# ------------------------------------------------------------

# metto la f prima delle virgolette e uso le {} per inserire variabili
print(f"Mi chiamo {nome} e ho {eta} anni")
print(f"Sono alto {altezza} metri")

# senza f-string sarebbe complicato: devo convertire tutto in stringa
# print("Ho " + str(eta) + " anni")   # funziona ma è brutto
# con la f-string non devo preoccuparmi dei tipi


# ------------------------------------------------------------
# 5. INPUT — come chiedere qualcosa all'utente
# ------------------------------------------------------------

# input() mette in pausa il programma e aspetta che l'utente scriva
# quello che scrive viene SEMPRE salvato come stringa

nome_utente = input("Come ti chiami? ")
print(f"Ciao, {nome_utente}!")

# se voglio un numero devo convertire con int() o float()
anno = int(input("In che anno sei nato? "))
eta_calcolata = 2026 - anno
print(f"Hai circa {eta_calcolata} anni")

peso = float(input("Quanto pesi in kg? "))
print(f"Il tuo peso è {peso} kg")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Chiedi nome, cognome e città dell'utente.
#    Stampa: "Ciao [nome] [cognome], sei di [città]!"
#
# 2. Chiedi l'anno di nascita e calcola quanti anni mancano
#    al 2050. Stampa il risultato.
#
# 3. Chiedi il prezzo di un prodotto (con decimali).
#    Calcola il prezzo con l'IVA al 22% e stampalo.
# ============================================================
