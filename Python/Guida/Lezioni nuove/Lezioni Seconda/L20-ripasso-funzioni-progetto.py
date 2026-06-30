# ============================================================
# LEZIONE 20 — Ripasso: funzioni + mini-progetto a menu
# Unità 1 · Settimana 3
# ============================================================
# Prerequisiti: L18 (base), L19 (cicli e strutture), L8 (funzioni)
# Obiettivo: lo studente riattiva le funzioni e costruisce un
# programma completo con menu testuale usando solo gli strumenti
# dell'Anno 1.
# ============================================================


# ------------------------------------------------------------
# 1. FUNZIONI — il ripasso rapido
# ------------------------------------------------------------

# una funzione è un blocco di codice con un nome
# def la definisce, le parentesi () la chiamano

# senza parametri: fa sempre la stessa cosa
def stampa_separatore():
    print("-" * 40)

stampa_separatore()

# con parametri: si comporta diversamente in base ai dati che riceve
def saluta(nome):
    print(f"Ciao, {nome}!")

saluta("Marco")
saluta("Giulia")

# con return: calcola qualcosa e restituisce il risultato
# senza return la funzione "finisce nel vuoto" e non puoi usare il valore
def calcola_media(lista):
    return sum(lista) / len(lista)

voti = [7, 8, 6, 9]
print(f"Media: {calcola_media(voti):.1f}")

# errore frequente: confondere print con return
# print dentro la funzione MOSTRA il valore ma non lo restituisce
# return lo restituisce così puoi salvarlo, confrontarlo, passarlo ad altri


# ------------------------------------------------------------
# 2. FUNZIONI CHE OPERANO SU LISTE DI DIZIONARI
# ------------------------------------------------------------

# le funzioni diventano molto più utili quando lavorano
# su strutture dati — ricevono una lista, la elaborano, restituiscono un dato

def conta_promossi(registro):
    contatore = 0
    for s in registro:
        if s["voto"] >= 6:
            contatore += 1
    return contatore

def media_classe(registro):
    somma = 0
    for s in registro:
        somma += s["voto"]
    return somma / len(registro)

def cerca_studente(registro, nome):
    for s in registro:
        if s["nome"] == nome:
            return s        # restituisce il dizionario trovato
    return None             # None = "non trovato"

# esempio d'uso
classe = [
    {"nome": "Marco",  "voto": 7},
    {"nome": "Giulia", "voto": 5},
    {"nome": "Andrea", "voto": 8},
]

print(f"Promossi: {conta_promossi(classe)}")
print(f"Media:    {media_classe(classe):.1f}")

trovato = cerca_studente(classe, "Giulia")
if trovato:
    print(f"Trovato: {trovato['nome']} — voto {trovato['voto']}")
else:
    print("Studente non trovato.")


# ------------------------------------------------------------
# 3. IL PATTERN DEL MENU TESTUALE
# ------------------------------------------------------------

# un programma a menu ripete sempre la stessa struttura:
# mostra le opzioni → aspetta la scelta → esegue l'azione → ricomincia
# si ferma solo quando l'utente sceglie "esci"

# --- come funziona il ciclo del menu ---
# while True crea un ciclo infinito: non si ferma da solo
# break è l'unico modo per uscire — lo mettiamo nell'opzione "esci"
#
# passo 1: while True:
# passo 2:     stampa le opzioni disponibili
# passo 3:     chiedi la scelta all'utente
# passo 4:     if scelta == "1": esegui azione 1
#              elif scelta == "2": esegui azione 2
#              elif scelta == "0": break   ← esce dal while
#              else: avvisa che la scelta non è valida

# --- esempio minimo: menu a tre voci ---
# (commentato per non eseguire durante la lezione — sarà nel progetto sotto)
#
# while True:
#     print("\n1 - Saluta")
#     print("2 - Conta")
#     print("0 - Esci")
#     scelta = input("Scelta: ")
#
#     if scelta == "1":
#         print("Ciao!")
#     elif scelta == "2":
#         print("1, 2, 3!")
#     elif scelta == "0":
#         print("Arrivederci.")
#         break
#     else:
#         print("Scelta non valida.")

# nota: la scelta è sempre una stringa (viene da input)
# per questo si confronta con "1", "2", "0" — non con 1, 2, 0


# ------------------------------------------------------------
# 4. MINI-PROGETTO — gestore voti con menu
# ------------------------------------------------------------

# costruiamo un programma completo che usa tutto quello che sappiamo:
# liste di dizionari, funzioni, cicli, condizioni, menu testuale

# le funzioni sono definite prima del menu così il codice è ordinato:
# prima le "azioni", poi il "cervello" che le coordina

def mostra_registro(registro):
    if not registro:
        print("  Il registro è vuoto.")
        return
    print(f"\n  {'Nome':<12} Voto  Esito")
    print(f"  {'-'*26}")
    for s in registro:
        esito = "promosso" if s["voto"] >= 6 else "rimandato"
        print(f"  {s['nome']:<12} {s['voto']}     {esito}")

def aggiungi_studente(registro):
    nome = input("  Nome studente: ")
    voto = int(input("  Voto (0-10): "))
    while voto < 0 or voto > 10:
        print("  Voto non valido.")
        voto = int(input("  Voto (0-10): "))
    registro.append({"nome": nome, "voto": voto})
    print(f"  {nome} aggiunto.")

def mostra_statistiche(registro):
    if not registro:
        print("  Nessun dato disponibile.")
        return
    print(f"  Studenti:  {len(registro)}")
    print(f"  Media:     {media_classe(registro):.1f}")
    print(f"  Promossi:  {conta_promossi(registro)} su {len(registro)}")

# --- il menu ---
# registro è la lista condivisa: tutte le funzioni ci lavorano sopra
registro = []

print("=== Gestore Voti ===")

while True:
    print("\n1 - Aggiungi studente")
    print("2 - Mostra registro")
    print("3 - Statistiche")
    print("0 - Esci")
    scelta = input("\nScelta: ")

    if scelta == "1":
        aggiungi_studente(registro)
    elif scelta == "2":
        mostra_registro(registro)
    elif scelta == "3":
        mostra_statistiche(registro)
    elif scelta == "0":
        print("Arrivederci.")
        break
    else:
        print("Scelta non valida. Scegli 0, 1, 2 o 3.")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Aggiungi al programma sopra una quarta voce nel menu:
#    "4 - Cerca studente"
#    Chiede un nome e usa la funzione cerca_studente() già definita.
#    Se lo trova, stampa nome e voto. Se non lo trova, avvisa.
#
# 2. Scrivi un programma a menu per gestire una lista della spesa.
#    Il menu ha tre voci:
#    1 - Aggiungi prodotto (chiede nome e prezzo)
#    2 - Mostra lista (nome e prezzo di ogni prodotto, totale in fondo)
#    0 - Esci
#    Ogni prodotto è un dizionario {"nome": ..., "prezzo": ...}.
#    Metti le azioni in funzioni separate prima del menu.
#
# 3. Estendi il programma dell'esercizio 2 con due voci extra:
#    3 - Rimuovi prodotto (chiede il nome, rimuove se esiste)
#    4 - Prodotto più caro (stampa il nome e il prezzo del più costoso)
#    Anche queste devono essere funzioni separate.
# ============================================================
