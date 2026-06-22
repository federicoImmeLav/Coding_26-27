# ============================================================
# LEZIONE 6 — Ripasso cicli e mini-progetto
# Unità 2 · Settimane 11-12
# ============================================================
# Prerequisiti: L4 (for, range, liste), L5 (while, contatori)
# Obiettivo: lo studente sa scegliere tra for e while,
# combinarli con if e accumulatori, e costruire un programma
# completo da zero seguendo passi logici.
# ============================================================


# ------------------------------------------------------------
# 1. COME SCEGLIERE — for o while?
# ------------------------------------------------------------

# prima di scrivere un ciclo, fatti questa domanda:
# "so già quante volte devo ripetere?"

# SE SÌ → usa il for
# SE NO → usa il while

# esempi:

# "stampa i numeri da 1 a 10"
# → sai già quante volte: 10 → usa il for
for n in range(1, 11):
    print(n)

# "chiedi un numero all'utente finché non scrive qualcosa di valido"
# → non sai quante volte l'utente sbaglierà → usa il while
numero = int(input("Scrivi un numero positivo: "))
while numero <= 0:
    print("Deve essere positivo.")
    numero = int(input("Riprova: "))

# "stampa tutta la tabellina del 7"
# → sai già quante volte: 10 → usa il for
for i in range(1, 11):
    print(f"7 × {i} = {7 * i}")

# "chiedi numeri e sommali finché l'utente scrive stop"
# → non sai quante voci inserirà → usa il while


# ------------------------------------------------------------
# 2. IL FOR CON ACCUMULATORE — schema da ricordare
# ------------------------------------------------------------

# l'accumulatore è una variabile che tieni fuori dal for
# e aggiorni ad ogni giro

# schema:
# variabile = valore_iniziale    ← FUORI dal for
# for ...:
#     variabile = variabile + qualcosa   ← DENTRO il for
# usa variabile   ← FUORI dal for, dopo

# esempio: somma dei voti
voti = [6, 7, 5, 8, 6, 9]
somma = 0                       # ← FUORI: parto da zero

for voto in voti:
    somma = somma + voto        # ← DENTRO: aggiungo ogni voto

media = somma / len(voti)       # ← FUORI: uso il risultato
print(f"Media: {media:.1f}")    # :.1f stampa un solo decimale

# lo stesso schema funziona per trovare il massimo:
massimo = voti[0]               # parto dal primo elemento, non da zero

for voto in voti:
    if voto > massimo:
        massimo = voto          # aggiorno solo quando trovo uno più grande

print(f"Voto più alto: {massimo}")


# ------------------------------------------------------------
# 3. IL WHILE CON CONTATORE — schema da ricordare
# ------------------------------------------------------------

# il contatore tiene traccia di quante volte è successa una cosa

# schema:
# contatore = 0                 ← FUORI: inizializzo
# while condizione:
#     if condizione_specifica:
#         contatore += 1        ← DENTRO: aumento solo quando serve
# usa contatore   ← FUORI: dopo il ciclo

# esempio: quanti tentativi per indovinare una parola
parola_segreta = "balena"
tentativi = 0

tentativo = input("Indovina la parola segreta: ")
tentativi += 1

while tentativo != parola_segreta:
    print("Sbagliato!")
    tentativo = input("Riprova: ")
    tentativi += 1

print(f"Bravo! Hai impiegato {tentativi} tentativi.")


# ------------------------------------------------------------
# 4. LO STESSO PROBLEMA IN DUE MODI — tabellina
# ------------------------------------------------------------

# a volte si può usare sia il for che il while per risolvere lo stesso problema
# è utile vederli entrambi per capire davvero la differenza

# VERSIONE CON FOR — più naturale quando sai quante righe stampare
n = int(input("Di quale numero vuoi la tabellina? "))

print(f"\nTabellina del {n} — versione for:")
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")

# VERSIONE CON WHILE — equivalente, ma più verbosa
print(f"\nTabellina del {n} — versione while:")
i = 1
while i <= 10:
    print(f"{n} × {i} = {n * i}")
    i += 1

# entrambe producono lo stesso risultato
# il for è più leggibile quando il numero di ripetizioni è fisso
# il while è più utile quando la condizione di uscita è variabile


# ------------------------------------------------------------
# 5. FOR E IF INSIEME — filtrare i dati
# ------------------------------------------------------------

# il for e l'if si usano spesso insieme:
# il for scorre tutti gli elementi, l'if decide cosa fare con ciascuno

# esempio: dato un listino prezzi, stampa solo i prodotti in offerta
prodotti = ["pasta", "latte", "biscotti", "caffè", "succo"]
prezzi   = [0.80,    1.20,    2.50,       3.90,    1.60]

print("\nProdotti sotto i 2 euro:")
for i in range(len(prodotti)):
    if prezzi[i] < 2.00:
        print(f"  {prodotti[i]}: {prezzi[i]:.2f} €")

# nota: range(len(prodotti)) genera gli indici 0, 1, 2, 3, 4
# così possiamo usare lo stesso indice su entrambe le liste


# ------------------------------------------------------------
# 6. MINI-PROGETTO — calcolatrice a somma continua
# ------------------------------------------------------------

# costruiamo un programma completo, un pezzo alla volta
# il programma chiede numeri all'utente e li somma,
# finché l'utente scrive "fine"
# alla fine mostra: quanti numeri, la somma, la media

# --- passo 1: le variabili di partenza ---
contatore = 0   # quanti numeri ha inserito
somma_tot = 0   # somma totale

# --- passo 2: chiedere il primo numero (fuori dal while) ---
inserito = input("\nCalcolatrice — scrivi un numero (o 'fine' per finire): ")

# --- passo 3: il ciclo principale ---
while inserito != "fine":

    # passo 3a: convertiamo il testo in numero e aggiorniamo i dati
    numero = int(inserito)
    somma_tot = somma_tot + numero
    contatore = contatore + 1

    # passo 3b: mostriamo il totale parziale
    print(f"  Totale finora: {somma_tot}  (inseriti: {contatore} numeri)")

    # passo 3c: chiediamo il prossimo numero
    inserito = input("Prossimo numero (o 'fine'): ")

# --- passo 4: i risultati finali ---
# arriviamo qui solo dopo che l'utente ha scritto "fine"

if contatore == 0:
    # caso speciale: l'utente non ha inserito nessun numero
    print("Non hai inserito nessun numero.")
else:
    media = somma_tot / contatore
    print(f"\nRisultati:")
    print(f"  Numeri inseriti: {contatore}")
    print(f"  Somma:           {somma_tot}")
    print(f"  Media:           {media:.1f}")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Hai questa lista di temperature giornaliere (in °C):
#    [12, 18, 9, 22, 15, 7, 20, 11, 25, 14]
#    Usa un for per calcolare e stampare:
#    - la temperatura media
#    - quante giornate hanno superato i 15°C
#    - la temperatura più alta
#
# 2. Scrivi un programma che chiede all'utente un numero
#    intero maggiore di 0. Se il numero inserito non è
#    valido, chiedi di nuovo (usa il while).
#    Poi stampa tutti i divisori del numero
#    (i numeri per cui il resto della divisione è 0).
#    Esempio: divisori di 12 → 1, 2, 3, 4, 6, 12
#    Suggerimento: usa un for con range(1, numero+1)
#    e controlla con numero % i == 0.
#
# 3. Mini-progetto: registro voti.
#    Il programma chiede voti (da 1 a 10) uno alla volta.
#    Finisce quando l'utente scrive "fine".
#    Valida ogni voto: se non è tra 1 e 10, avvisa e
#    non aggiungerlo al registro.
#    Alla fine stampa: quanti voti validi, la media,
#    e quante volte è stato preso un voto >= 6.
# ============================================================
