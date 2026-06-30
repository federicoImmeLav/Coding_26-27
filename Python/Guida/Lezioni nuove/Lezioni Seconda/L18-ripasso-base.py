# ============================================================
# LEZIONE 18 — Ripasso: variabili, tipi, condizioni, logici
# Unità 1 · Settimana 1
# ============================================================
# Prerequisiti: contenuti Anno 1 (L1–L3)
# Obiettivo: lo studente recupera la padronanza di variabili,
# tipi e condizioni — fondamenta su cui costruiamo tutto l'anno.
# ============================================================


# ------------------------------------------------------------
# 1. VARIABILI E TIPI — il ripasso rapido
# ------------------------------------------------------------

# una variabile è una scatola con un'etichetta
# Python capisce il tipo dal valore che ci metti dentro

nome     = "Sara"    # str   — testo tra virgolette
eta      = 17        # int   — numero intero
media    = 7.4       # float — numero decimale (punto, non virgola)
promossa = True      # bool  — solo True o False, mai "true" minuscolo

# type() ti dice di che tipo è una variabile — utile per debug
print(type(nome))       # <class 'str'>
print(type(eta))        # <class 'int'>
print(type(media))      # <class 'float'>
print(type(promossa))   # <class 'bool'>

# le f-string permettono di inserire variabili nel testo senza conversioni
print(f"{nome} ha {eta} anni e una media di {media}")


# ------------------------------------------------------------
# 2. CONVERSIONI — perché input() è sempre una stringa
# ------------------------------------------------------------

# input() restituisce SEMPRE una stringa, anche se l'utente scrive un numero
# se provi a fare calcoli senza convertire, Python dà TypeError

# SBAGLIATO — TypeError: can only concatenate str (not "int") to str
# anni = input("Età: ")
# tra_dieci_anni = anni + 10

# GIUSTO — converti subito con int() o float()
anni = int(input("Quanti anni hai? "))
tra_dieci_anni = anni + 10
print(f"Tra dieci anni ne avrai {tra_dieci_anni}.")

# usa float() se ti aspetti un numero con la virgola
altezza = float(input("Quanto sei alto in metri? (es. 1.72) "))
print(f"Sei alto {altezza} m")

# int() su "3.7" dà errore — se l'utente può scrivere decimali, usa float()


# ------------------------------------------------------------
# 3. OPERATORI DI CONFRONTO — producono sempre True o False
# ------------------------------------------------------------

# questi operatori sono la base di ogni condizione

punteggio = 85

print(punteggio == 100)    # False — uguale?
print(punteggio != 100)    # True  — diverso?
print(punteggio > 60)      # True  — maggiore?
print(punteggio < 60)      # False — minore?
print(punteggio >= 85)     # True  — maggiore o uguale?
print(punteggio <= 85)     # True  — minore o uguale?

# errore classico: confondere = (assegnazione) con == (confronto)
#   punteggio = 85    → salva 85 in punteggio
#   punteggio == 85   → controlla se punteggio vale 85, dà True o False


# ------------------------------------------------------------
# 4. IF / ELIF / ELSE — eseguire codice solo in certi casi
# ------------------------------------------------------------

# Python controlla le condizioni dall'alto verso il basso:
# appena ne trova una vera, entra in quel blocco e salta tutto il resto

voto = int(input("Inserisci un voto (0-10): "))

if voto >= 9:
    giudizio = "ottimo"
elif voto >= 7:
    giudizio = "buono"
elif voto >= 6:
    giudizio = "sufficiente"
else:
    giudizio = "insufficiente"

print(f"Voto {voto}: {giudizio}")

# l'ordine conta: se mettessi "voto >= 6" per primo, ci entrano anche
# 7, 8 e 9 — e gli elif successivi non verrebbero mai raggiunti


# ------------------------------------------------------------
# 5. OPERATORI LOGICI — and, or, not
# ------------------------------------------------------------

# and → entrambe le condizioni devono essere True
# or  → basta che almeno una sia True
# not → inverte: True diventa False, False diventa True

eta_utente = int(input("Quanti anni hai? "))
documento  = input("Hai un documento? (si/no) ")
abbonato   = False

# and: tutte e due devono valere
if eta_utente >= 18 and documento == "si":
    print("Accesso consentito.")

# or: basta una
if eta_utente < 14 or eta_utente > 65:
    print("Hai diritto allo sconto.")

# not: utile quando è più semplice scrivere la condizione "negativa"
if not abbonato:
    print("Devi registrarti prima di continuare.")

# tabella riassuntiva:
# True  and True  → True    |    True  or True  → True
# True  and False → False   |    True  or False → True
# False and True  → False   |    False or True  → True
# False and False → False   |    False or False → False


# ------------------------------------------------------------
# 6. ESERCIZIO RIEPILOGATIVO — tutto insieme
# ------------------------------------------------------------

# programma: calcolo prezzo biglietto cinema
# regole:
#   - under 14 oppure over 65: 5 €
#   - studente con tessera fedeltà: 7 €
#   - tutti gli altri: 10 €

eta_cinema = int(input("\nEtà: "))
studente   = input("Sei studente? (si/no) ")
tessera    = input("Hai la tessera del cinema? (si/no) ")

if eta_cinema < 14 or eta_cinema > 65:
    prezzo = 5
elif studente == "si" and tessera == "si":
    prezzo = 7
else:
    prezzo = 10

print(f"Il tuo biglietto costa {prezzo} €.")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Chiedi i voti di italiano, matematica e inglese.
#    Calcola la media e stampa:
#    - "promosso"  se la media è >= 6
#    - "rimandato" se la media è tra 5.0 e 5.9
#    - "bocciato"  se la media è < 5
#
# 2. Chiedi un anno di nascita. Calcola l'età (anno corrente: 2026).
#    Stampa l'età e poi rispondi a queste domande con si/no:
#    - può avere la patente AM? (si prende a 14 anni)
#    - può votare? (maggiorenne a 18)
#    - ha diritto al biglietto ridotto under 26?
#    Usa tre if separati, non un unico if/elif/else.
#
# 3. Scrivi un convertitore da voto numerico a lettera (sistema USA):
#    10 → A+  |  9 → A  |  8 → B  |  7 → C  |  6 → D  |  <6 → F
#    Chiedi anche se il voto è "con lode" (si/no).
#    Se il voto è 10 e c'è la lode, stampa "A+ con lode".
#    Se il voto non è nell'intervallo 0-10, avvisa l'utente
#    e non assegnare nessuna lettera.
# ============================================================
