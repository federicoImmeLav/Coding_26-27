# ============================================================
# LEZIONE 3 — Operatori logici e messaggi di errore
# Unità 1 · Settimane 5-6
# ============================================================
# Prerequisiti: lezione 1 e 2
# Obiettivo: lo studente sa combinare più condizioni con
# and/or/not e sa leggere i messaggi di errore più comuni.
# ============================================================


# ------------------------------------------------------------
# 1. AND — entrambe le condizioni devono essere vere
# ------------------------------------------------------------

# and è come dire "sia... che..."
# è True solo se la condizione di SINISTRA e quella di DESTRA
# sono entrambe True

eta = int(input("Quanti anni hai? "))
patente = input("Hai la patente? (si/no) ")

if eta >= 18 and patente == "si":
    print("Puoi guidare!")
else:
    print("Non puoi guidare.")

# tabella della verità di and:
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False


# ------------------------------------------------------------
# 2. OR — basta che una delle due condizioni sia vera
# ------------------------------------------------------------

# or è come dire "oppure"
# è True se ALMENO UNA delle due condizioni è True

giorno = input("Che giorno è oggi? (lunedi/martedi/.../sabato/domenica) ")

if giorno == "sabato" or giorno == "domenica":
    print("È weekend!")
else:
    print("È un giorno di scuola.")

# tabella della verità di or:
# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False


# ------------------------------------------------------------
# 3. NOT — inverte il risultato
# ------------------------------------------------------------

# not trasforma True in False e viceversa
# si usa per rendere più leggibili certe condizioni

connesso = False

if not connesso:
    print("Non sei connesso a internet.")

# è equivalente a scrivere:
# if connesso == False:
#     print(...)
# ma "if not connesso" si legge più naturalmente


# ------------------------------------------------------------
# 4. COMBINARE AND, OR, NOT insieme
# ------------------------------------------------------------

# si possono usare le parentesi per raggruppare le condizioni
# come in matematica

voto_ita = int(input("Voto italiano: "))
voto_mat = int(input("Voto matematica: "))
assenze = int(input("Quante assenze hai? "))

# promosso se: tutti e due i voti >= 6 E meno di 30 assenze
if voto_ita >= 6 and voto_mat >= 6 and assenze < 30:
    print("Promosso!")
elif voto_ita < 6 or voto_mat < 6:
    print("Bocciato per voto insufficiente.")
else:
    print("Bocciato per troppe assenze.")


# ------------------------------------------------------------
# 5. MESSAGGI DI ERRORE — cosa significano
# ------------------------------------------------------------

# Python, quando trova un problema, si ferma e scrive un messaggio.
# Imparare a leggere questi messaggi è fondamentale.

# --- SyntaxError: hai scritto male la sintassi ---
# Python non riesce nemmeno a leggere il codice.
# Esempi comuni:
#   if x = 5:         → hai usato = invece di ==
#   print("ciao"      → hai dimenticato la parentesi di chiusura
#   if x > 5          → manca i due punti finali

# --- NameError: usi una variabile che non esiste ---
# Python non trova la variabile perché non l'hai mai creata
# oppure hai fatto un errore di battitura nel nome.
# Esempio:
#   print(Nome)       → hai scritto Nome con la N maiuscola,
#                        ma la variabile si chiama nome

# --- TypeError: stai mischiando tipi incompatibili ---
# Il caso più comune: cerchi di fare operazioni
# tra una stringa e un numero senza convertire.
# Esempio:
#   eta = input("Età: ")
#   eta_tra_10_anni = eta + 10   → ERRORE: non puoi sommare
#                                    una stringa e un int
# Soluzione:
#   eta = int(input("Età: "))    → converti subito con int()

# --- come leggere il messaggio di errore ---
# Python ti dice:
#   1. il file e il numero di riga dove è successo il problema
#   2. il tipo di errore (SyntaxError, NameError, TypeError...)
#   3. una breve spiegazione
# Inizia SEMPRE dalla riga indicata — lì c'è il problema.


# ------------------------------------------------------------
# 6. ESERCIZIO RIEPILOGATIVO
# ------------------------------------------------------------

# programma: calcolatore biglietto cinema
# chiedi eta e se ha la tessera fedeltà
# regole:
#   - meno di 10 anni: gratis
#   - da 10 a 17 anni: 6 euro
#   - 18 anni o più con tessera: 8 euro
#   - 18 anni o più senza tessera: 10 euro

eta_cinema = int(input("Quanti anni hai? "))
tessera = input("Hai la tessera fedeltà? (si/no) ")

if eta_cinema < 10:
    print("Ingresso gratuito!")
elif eta_cinema < 18:
    print("Paghi 6 euro.")
elif eta_cinema >= 18 and tessera == "si":
    print("Paghi 8 euro.")
else:
    print("Paghi 10 euro.")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Chiedi un numero. Stampa "nel range" se è tra 10 e 20
#    (estremi inclusi), altrimenti "fuori range".
#    Usa and.
#
# 2. Chiedi il mese (in numero). Stampa "estate" se è luglio
#    o agosto, "inverno" se è dicembre, gennaio o febbraio,
#    altrimenti "altra stagione". Usa or.
#
# 3. Chiedi username e password.
#    L'accesso è consentito solo se username è "admin"
#    E password è "1234". In tutti gli altri casi stampa
#    "accesso negato".
# ============================================================
