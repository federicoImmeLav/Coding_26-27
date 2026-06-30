# ============================================================
# LEZIONE 19 — Ripasso: cicli, liste, dizionari
# Unità 1 · Settimana 2
# ============================================================
# Prerequisiti: L18 (ripasso base), contenuti Anno 1 (L4–L9)
# Obiettivo: lo studente sa combinare cicli, liste e dizionari
# in programmi che raccolgono, filtrano e riassumono dati.
# ============================================================


# ------------------------------------------------------------
# 1. FOR SU LISTA — filtrare e accumulare
# ------------------------------------------------------------

# il for su una lista scorre ogni elemento; l'if decide cosa fare
# questo pattern — scorra + filtra + accumula — si usa continuamente

voti = [6, 9, 4, 7, 5, 8, 6, 3]

somma        = 0
insufficienti = 0

for voto in voti:
    somma += voto
    if voto < 6:
        insufficienti += 1

media = somma / len(voti)
print(f"Media: {media:.1f}  —  Insufficienti: {insufficienti}")

# per trovare il massimo (o minimo), parti dal primo elemento della lista,
# non da zero — altrimenti con tutti negativi il risultato sarebbe sbagliato
massimo = voti[0]
for voto in voti:
    if voto > massimo:
        massimo = voto
print(f"Voto più alto: {massimo}")


# ------------------------------------------------------------
# 2. WHILE CON INPUT — validare quello che scrive l'utente
# ------------------------------------------------------------

# il while è lo strumento giusto quando non sai quante volte
# l'utente sbaglierà: continui a chiedere finché il dato è valido

# schema: chiedi FUORI, ripeti DENTRO
eta = int(input("Inserisci la tua età (0-120): "))
while eta < 0 or eta > 120:
    print("Valore non valido.")
    eta = int(input("Riprova (0-120): "))
print(f"Età accettata: {eta}")

# lo stesso schema funziona per parole chiave di uscita
scelta = input("Vuoi continuare? (si/no) ")
while scelta != "si" and scelta != "no":
    print("Scrivi 'si' oppure 'no'.")
    scelta = input("Vuoi continuare? (si/no) ")


# ------------------------------------------------------------
# 3. COSTRUIRE UNA LISTA DA ZERO — append dentro al ciclo
# ------------------------------------------------------------

# pattern da ricordare:
# 1. crea lista vuota FUORI
# 2. ciclo (for o while)
# 3. costruisci il dato
# 4. append lo aggiunge DENTRO al ciclo
# 5. usa la lista completa FUORI, dopo il ciclo

n = int(input("Quanti voti vuoi inserire? "))
registro = []

for i in range(n):
    voto = int(input(f"  Voto {i + 1}: "))
    registro.append(voto)

registro.sort()
print(f"Voti in ordine: {registro}")
print(f"Minimo: {registro[0]}  —  Massimo: {registro[-1]}")


# ------------------------------------------------------------
# 4. DIZIONARI — accedere, modificare, scorrere
# ------------------------------------------------------------

# un dizionario è come una lista, ma le posizioni hanno un nome
# accesso con la chiave tra parentesi quadre: dizionario["chiave"]

studente = {"nome": "Luca", "classe": "3A", "media": 7.2, "promosso": True}

# leggere
print(studente["nome"])         # Luca

# modificare un valore esistente
studente["media"] = 7.8
print(studente["media"])        # 7.8

# aggiungere una chiave nuova
studente["sport"] = "nuoto"

# scorrere tutte le coppie chiave–valore con .items()
for chiave, valore in studente.items():
    print(f"  {chiave}: {valore}")

# controllare se una chiave esiste prima di accederla
if "sport" in studente:
    print(f"Lo sport di Luca è {studente['sport']}")


# ------------------------------------------------------------
# 5. LISTA DI DIZIONARI — il pattern che useremo spesso
# ------------------------------------------------------------

# una lista di dizionari è come una tabella:
# ogni dizionario è una riga, ogni chiave è una colonna
# questo schema tornerà quando faremo le classi nell'Unità 3

inventario = [
    {"prodotto": "penna",     "prezzo": 0.80, "scorte": 120},
    {"prodotto": "quaderno",  "prezzo": 2.50, "scorte": 45},
    {"prodotto": "zaino",     "prezzo": 35.0, "scorte": 8},
    {"prodotto": "righello",  "prezzo": 1.20, "scorte": 0},
]

# scorrere la lista e leggere i campi di ogni dizionario
print("\n--- Inventario ---")
for articolo in inventario:
    disponibile = "disponibile" if articolo["scorte"] > 0 else "ESAURITO"
    print(f"  {articolo['prodotto']:12}  {articolo['prezzo']:.2f} €  [{disponibile}]")

# trovare il prodotto più costoso
# (stesso schema del massimo su lista di numeri, ma il confronto è su un campo)
piu_caro = inventario[0]
for articolo in inventario:
    if articolo["prezzo"] > piu_caro["prezzo"]:
        piu_caro = articolo
print(f"\nArticolo più caro: {piu_caro['prodotto']} ({piu_caro['prezzo']} €)")


# ------------------------------------------------------------
# 6. ESERCIZIO RIEPILOGATIVO — registro di una classe
# ------------------------------------------------------------

# questo esercizio si costruisce in due fasi separate:
# FASE 1 — raccogliere i dati (costruire la lista)
# FASE 2 — elaborare i dati (scorrere la lista)
# tenerle separate rende il codice più chiaro

# --- come funziona un singolo studente ---
# uno studente è un dizionario: una scatola con etichette
#
#   nome  = "Luca"
#   voto  = 7
#   s     = {"nome": nome, "voto": voto}
#   # s vale ora: {"nome": "Luca", "voto": 7}
#
# puoi leggere i suoi campi con s["nome"] e s["voto"]

# --- come aggiungere quel dizionario alla lista ---
# classe è una lista vuota; append ci infila dentro il dizionario
#
#   classe = []
#   classe.append(s)
#   # classe vale ora: [{"nome": "Luca", "voto": 7}]
#
# al secondo giro, append aggiunge il secondo dizionario in fondo:
#   # classe vale: [{"nome": "Luca", "voto": 7}, {"nome": "Sara", "voto": 9}]

# --- come farlo N volte con il for ---
# invece di scrivere studente1, studente2, studente3... a mano,
# il for ripete la stessa operazione quanti volte serve:
#
# passo 1: lista vuota FUORI dal for
# passo 2: for i in range(quanti):
# passo 3:     chiedi nome e voto
# passo 4:     append({"nome": nome, "voto": voto})  ← dizionario creato al volo
# passo 5: usa la lista completa FUORI, dopo il for

quanti = int(input("\nQuanti studenti vuoi registrare? "))
classe = []                                    # passo 1: lista vuota

for i in range(quanti):                        # passo 2: ripeti quanti volte
    print(f"\nStudente {i + 1}:")
    nome = input("  Nome: ")                   # passo 3: chiedi i dati
    voto = int(input("  Voto (0-10): "))
    while voto < 0 or voto > 10:
        print("  Voto non valido.")
        voto = int(input("  Voto (0-10): "))
    classe.append({"nome": nome, "voto": voto})  # passo 4: aggiungi il dizionario

# --- FASE 2: elaborare ---
# for s in classe: fa sì che s assuma a turno il valore di ogni dizionario
#   giro 1: s è {"nome": "Luca", "voto": 7}
#   giro 2: s è {"nome": "Sara", "voto": 9}
# quindi s["voto"] dà il voto di quello studente in quel giro specifico

somma_voti = 0
promossi   = 0

for s in classe:                               # passo 5: scorri la lista completa
    somma_voti += s["voto"]
    if s["voto"] >= 6:
        promossi += 1

media_classe = somma_voti / len(classe)

print(f"\n--- Risultati ---")
print(f"Media classe:  {media_classe:.1f}")
print(f"Promossi:      {promossi} su {len(classe)}")
print(f"\nStudenti con voto sopra la media:")
for s in classe:
    if s["voto"] > media_classe:
        print(f"  {s['nome']}: {s['voto']}")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Hai questa lista di temperature settimanali (°C):
#    [18, 22, 15, 25, 20, 13, 24]
#    Con un solo ciclo for calcola e stampa:
#    - la media
#    - quanti giorni hanno superato i 20°C
#    - la temperatura massima e quella minima
#
# 2. Costruisci un programma che chiede all'utente numeri interi
#    finché non scrive 0 (usa while). Accumula i numeri in una lista.
#    Alla fine stampa: quanti numeri ha inserito, la somma,
#    e la lista ordinata dal più grande al più piccolo.
#    Non contare lo 0 nella lista.
#
# 3. Hai questa lista di dizionari:
#    catalogo = [
#        {"titolo": "Il Piccolo Principe", "anno": 1943, "pagine": 96},
#        {"titolo": "1984",                "anno": 1949, "pagine": 328},
#        {"titolo": "Harry Potter 1",      "anno": 1997, "pagine": 309},
#        {"titolo": "Il nome della rosa",  "anno": 1980, "pagine": 502},
#        {"titolo": "Dune",                "anno": 1965, "pagine": 604},
#    ]
#    Scrivere un programma che chiede all'utente un anno minimo.
#    Stampa solo i libri pubblicati da quell'anno in poi,
#    in ordine di lunghezza (dal più corto al più lungo).
#    Suggerimento: prima filtra in una nuova lista con append,
#    poi ordina con sort() — ma sort() non sa ordinare dizionari
#    da solo. Usa invece: lista.sort(key=lambda x: x["pagine"])
# ============================================================
