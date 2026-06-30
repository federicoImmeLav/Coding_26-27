# ============================================================
# LEZIONE 10 — Ripasso Unità 3 e progetto intermedio
# Unità 3 · Settimane 19-20
# ============================================================
# Prerequisiti: L7 (liste), L8 (funzioni), L9 (dizionari)
# Obiettivo: lo studente sa combinare liste, dizionari e
# funzioni per costruire un programma completo da zero.
# ============================================================


# ------------------------------------------------------------
# 1. RIPASSO — i tre strumenti dell'unità 3
# ------------------------------------------------------------

# LISTA — una sequenza di valori dello stesso tipo
voti = [7, 8, 6, 9, 5]

# DIZIONARIO — le proprietà di una singola cosa
studente = {"nome": "Marco", "eta": 16, "media": 7.5}

# LISTA DI DIZIONARI — una raccolta di cose, ognuna con le sue proprietà
classe = [
    {"nome": "Marco",  "media": 7.5},
    {"nome": "Giulia", "media": 8.9},
    {"nome": "Andrea", "media": 6.2},
]

# regola pratica:
# - valori semplici in sequenza?                   -> lista
# - una cosa con più proprietà?                    -> dizionario
# - una raccolta di cose con più proprietà?        -> lista di dizionari

# FUNZIONE — un blocco di codice con un nome, da richiamare quando serve
def media(numeri):
    somma = 0
    for n in numeri:
        somma = somma + n
    return somma / len(numeri)

print(f"Media voti: {media(voti):.1f}")


# ------------------------------------------------------------
# 2. PROGETTO — struttura dei dati
# ------------------------------------------------------------

# costruiamo un gestore della lista della spesa
# ogni prodotto ha un nome e una quantità: usiamo una lista di dizionari

# spesa = [
#     {"nome": "pane",  "quantita": 2},
#     {"nome": "latte", "quantita": 1},
#     ...
# ]

# partiamo con una lista vuota: l'utente la riempie usando il menu
spesa = []


# ------------------------------------------------------------
# 3. PROGETTO — le funzioni di gestione
# ------------------------------------------------------------

# scriviamo una funzione per ogni operazione
# così il menu (blocco 4) resta corto e leggibile

def stampa_spesa(spesa):
    if len(spesa) == 0:
        print("  La lista e' vuota.")
        return
    for prodotto in spesa:
        print(f"  - {prodotto['nome']} (x{prodotto['quantita']})")
    print(f"  Totale: {len(spesa)} prodotti")

def aggiungi_prodotto(spesa, nome, quantita):
    spesa.append({"nome": nome, "quantita": quantita})
    print(f"  '{nome}' aggiunto.")

def rimuovi_prodotto(spesa, nome):
    for prodotto in spesa:
        if prodotto["nome"] == nome:
            spesa.remove(prodotto)
            print(f"  '{nome}' rimosso.")
            return
    print(f"  '{nome}' non trovato nella lista.")


# ------------------------------------------------------------
# 4. PROGETTO — il menu principale
# ------------------------------------------------------------

# un ciclo while mostra il menu e chiama le funzioni giuste
# il programma va avanti finché l'utente non scrive "q"

print("=== LISTA DELLA SPESA ===")

scelta = ""
while scelta != "q":
    print("\nCosa vuoi fare?")
    print("  a -> aggiungi un prodotto")
    print("  r -> rimuovi un prodotto")
    print("  v -> visualizza la lista")
    print("  q -> esci")
    scelta = input("Scelta: ")

    if scelta == "a":
        nome = input("  Nome prodotto: ")
        quantita = int(input("  Quantita': "))
        aggiungi_prodotto(spesa, nome, quantita)

    elif scelta == "r":
        nome = input("  Prodotto da rimuovere: ")
        rimuovi_prodotto(spesa, nome)

    elif scelta == "v":
        stampa_spesa(spesa)

    elif scelta != "q":
        print("  Scelta non valida.")

print("\nLista finale:")
stampa_spesa(spesa)
print("A presto!")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Aggiungi al progetto una funzione cerca_prodotto(spesa, nome)
#    che stampa le informazioni di un prodotto se esiste,
#    oppure "Prodotto non trovato." se non c'è.
#    Aggiungila al menu con l'opzione "c".
#
# 2. Aggiungi al dizionario di ogni prodotto un campo "prezzo"
#    (float). Modifica aggiungi_prodotto() per chiederlo,
#    e scrivi una funzione totale_spesa(spesa) che restituisce
#    la somma di prezzo x quantita' per tutti i prodotti.
#    Mostra il totale alla fine di ogni visualizzazione.
#
# 3. Mini-progetto libero: scegli un tema e costruisci un
#    programma simile al gestore della spesa:
#    a) Rubrica telefonica (nome, numero, email)
#    b) Registro voti (materia, voto, data)
#    c) Inventario magazzino (prodotto, quantita', prezzo)
#    Il programma deve avere: struttura dati, almeno 3 funzioni,
#    un menu while con almeno 4 opzioni.
# ============================================================
