# ============================================================
# LEZIONE 9 — I dizionari
# Unità 3 · Settimane 17-18
# ============================================================
# Prerequisiti: L7 (liste), L8 (funzioni)
# Obiettivo: lo studente sa creare dizionari, accedere e
# aggiornare i valori, e gestire liste di dizionari.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA — quando la lista non basta
# ------------------------------------------------------------

# immagina di voler memorizzare le informazioni di uno studente
# con una lista puoi fare così:

studente = ["Marco", "Rossi", 16, "3A"]

# ma come accedi al cognome? devi sapere che è in posizione 1
print(studente[1])   # Rossi

# questo codice è fragile: se sposti un elemento, tutto si rompe
# e tra un mese non ricordi più cosa c'è in posizione 2 o 3

# un dizionario risolve il problema:
# invece di un numero, ogni valore ha un'etichetta (la chiave)
studente = {"nome": "Marco", "cognome": "Rossi", "eta": 16, "classe": "3A"}

# ora l'accesso è immediato e leggibile
print(studente["cognome"])   # Rossi
print(studente["classe"])    # 3A


# ------------------------------------------------------------
# 2. CREARE UN DIZIONARIO — chiavi e valori
# ------------------------------------------------------------

# un dizionario si crea con le parentesi graffe { }
# ogni voce è una coppia   chiave: valore
# le coppie sono separate da virgole

prodotto = {"nome": "pasta", "prezzo": 1.20, "scorte": 50}

# la chiave è di solito una stringa
# il valore può essere qualsiasi tipo: stringa, int, float, bool...

# accedere a un valore: dizionario["chiave"]
print(prodotto["nome"])      # pasta
print(prodotto["prezzo"])    # 1.2
print(prodotto["scorte"])    # 50

# se la chiave non esiste, Python dà un KeyError
# prodotto["scadenza"]   ← KeyError: 'scadenza'

# per sapere se una chiave esiste, si usa l'operatore in
if "prezzo" in prodotto:
    print(f"Il prezzo è {prodotto['prezzo']} €")


# ------------------------------------------------------------
# 3. AGGIORNARE E AGGIUNGERE — modificare il dizionario
# ------------------------------------------------------------

# modificare un valore esistente: assegni un nuovo valore alla chiave
prodotto["prezzo"] = 1.35
print(prodotto["prezzo"])    # 1.35

# aggiungere una nuova coppia chiave-valore: stessa sintassi
prodotto["categoria"] = "pasta e riso"
print(prodotto)

# esempio: costruire un dizionario dai dati inseriti dall'utente
nome = input("Nome studente: ")
voto = int(input("Voto: "))

scheda = {"nome": nome, "voto": voto, "promosso": voto >= 6}
print(scheda)

# il valore "promosso" è un booleano calcolato direttamente


# ------------------------------------------------------------
# 4. SCORRERE UN DIZIONARIO — accedere a chiavi e valori
# ------------------------------------------------------------

# .keys() restituisce tutte le chiavi
# .values() restituisce tutti i valori
# .items() restituisce coppie (chiave, valore) — la più utile

persona = {"nome": "Giulia", "eta": 17, "classe": "4B", "media": 7.8}

# scorrere le chiavi
for chiave in persona.keys():
    print(chiave)

# scorrere i valori
for valore in persona.values():
    print(valore)

# scorrere chiavi e valori insieme — il modo più completo
for chiave, valore in persona.items():
    print(f"{chiave}: {valore}")

# utile per stampare una scheda formattata
print("\n--- Scheda studente ---")
for chiave, valore in persona.items():
    print(f"  {chiave.capitalize()}: {valore}")


# ------------------------------------------------------------
# 5. LISTA DI DIZIONARI — una raccolta di schede
# ------------------------------------------------------------

# la combinazione più potente: una lista dove ogni elemento
# è un dizionario — come una tabella con righe e colonne

# passo 1: crea la lista vuota
# passo 2: chiedi i dati di ogni voce
# passo 3: crea il dizionario e aggiungilo con append
# passo 4: dopo il ciclo, usa la lista per elaborare i dati

classe = []

n = int(input("Quanti studenti vuoi inserire? "))
for i in range(n):
    print(f"\nStudente {i + 1}:")
    nome = input("  Nome: ")
    voto = int(input("  Voto: "))
    classe.append({"nome": nome, "voto": voto})

# ora classe è una lista di dizionari, esempio:
# [{"nome": "Marco", "voto": 7}, {"nome": "Giulia", "voto": 9}, ...]

# scorrere e stampare ogni scheda
print("\n--- Registro ---")
for studente in classe:
    stato = "promosso" if studente["voto"] >= 6 else "rimandato"
    print(f"  {studente['nome']}: {studente['voto']} ({stato})")

# calcolare la media della classe
somma = 0
for studente in classe:
    somma = somma + studente["voto"]
media_classe = somma / len(classe)
print(f"\nMedia classe: {media_classe:.1f}")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Crea un dizionario che rappresenta il tuo film preferito
#    con le chiavi: "titolo", "anno", "regista", "voto" (da 1 a 10).
#    Poi stampa ogni informazione in una riga separata,
#    usando un for su .items().
#
# 2. Scrivi un programma che chiede all'utente di inserire
#    3 prodotti con nome e prezzo (usa append per costruire
#    la lista di dizionari). Alla fine stampa tutti i prodotti
#    e indica quale ha il prezzo più alto.
#    Suggerimento: tieni traccia del massimo con una variabile,
#    come hai fatto con le liste di numeri.
#
# 3. Registro presenze.
#    Crea una lista di dizionari con almeno 5 studenti,
#    ognuno con "nome" e "presente" (True o False).
#    Scrivi una funzione conta_presenti(classe) che restituisce
#    quanti studenti sono presenti.
#    Stampa l'elenco dei presenti e il totale.
# ============================================================
