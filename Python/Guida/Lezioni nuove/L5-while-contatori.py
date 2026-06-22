# ============================================================
# LEZIONE 5 — Il ciclo while, contatori e input in loop
# Unità 2 · Settimane 9-10
# ============================================================
# Prerequisiti: L4 (for, range, iterazione su liste)
# Obiettivo: lo studente sa usare il while per ripetere azioni
# finché una condizione è vera, costruire contatori e chiedere
# input all'utente finché la risposta è valida.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA DEL FOR — quando non sai quante volte ripetere
# ------------------------------------------------------------

# con il for, devi sempre sapere PRIMA quante volte vuoi ripetere:

for i in range(5):
    print("ciao")   # questo stampa "ciao" esattamente 5 volte

# ma cosa succede se non sai in anticipo quante volte ripetere?
# esempio: "chiedi all'utente un numero finché non inserisce qualcosa di valido"
# l'utente potrebbe sbagliare 1 volta, 5 volte, 100 volte — non puoi saperlo

# per questo esiste il while


# ------------------------------------------------------------
# 2. IL WHILE — la struttura base
# ------------------------------------------------------------

# il while funziona così:
# "finché questa condizione è vera, esegui il blocco"

# STRUTTURA:
# while condizione:
#     istruzione
#     istruzione

# esempio minimo:
numero = 0
while numero < 3:
    print(numero)
    numero = numero + 1

# cosa succede passo per passo:
# - Python guarda: numero < 3 ?  →  0 < 3 → True  → entra nel blocco → stampa 0 → numero diventa 1
# - Python guarda: numero < 3 ?  →  1 < 3 → True  → entra nel blocco → stampa 1 → numero diventa 2
# - Python guarda: numero < 3 ?  →  2 < 3 → True  → entra nel blocco → stampa 2 → numero diventa 3
# - Python guarda: numero < 3 ?  →  3 < 3 → False → ESCE dal ciclo
# risultato: stampa 0, 1, 2


# ------------------------------------------------------------
# 3. IL LOOP INFINITO — il pericolo del while
# ------------------------------------------------------------

# il while va avanti FINCHÉ la condizione è vera
# se la condizione non diventa mai False, il programma non si ferma mai

# esempio di loop infinito (NON eseguire questo):
# numero = 0
# while numero < 3:
#     print(numero)
#     # abbiamo dimenticato: numero = numero + 1
#     # numero resta sempre 0, la condizione resta sempre True → loop infinito

# se ti capita per sbaglio: usa Ctrl+C per fermare il programma

# regola da ricordare:
# dentro il while ci deve essere SEMPRE qualcosa che prima o poi
# fa diventare la condizione False


# ------------------------------------------------------------
# 4. WHILE vs FOR — quando usare quale
# ------------------------------------------------------------

# FOR → quando sai già quante volte ripetere
for i in range(5):
    print("questo lo faccio esattamente 5 volte")

# WHILE → quando non sai quante volte, e vai avanti finché vale una condizione
tentativo = 0
while tentativo < 5:
    print(f"tentativo numero {tentativo}")
    tentativo = tentativo + 1

# questi due esempi fanno la stessa cosa, ma il while è più flessibile:
# puoi cambiare la condizione di uscita come vuoi


# ------------------------------------------------------------
# 5. CONTATORE — tenere il conto dentro al while
# ------------------------------------------------------------

# un contatore è una variabile intera che parte da 0
# e viene aumentata di 1 ogni volta che accade qualcosa

# costruiamo un contatore passo per passo:

# passo 1: creo il contatore e lo metto a zero
contatore = 0

# passo 2: scrivo il while con la condizione che mi serve
while contatore < 5:

    # passo 3: dentro al while faccio quello che mi serve
    print(f"il contatore vale {contatore}")

    # passo 4: aumento il contatore di 1 — altrimenti loop infinito!
    contatore = contatore + 1

print(f"finito! il contatore è arrivato a {contatore}")

# nota: contatore = contatore + 1  si può scrivere anche  contatore += 1
# le due forme fanno la stessa cosa


# ------------------------------------------------------------
# 6. CONTARE QUANTE VOLTE SUCCEDE QUALCOSA
# ------------------------------------------------------------

# il contatore non deve per forza aumentare ad ogni giro:
# può aumentare solo quando si verifica una certa condizione

# esempio: quante volte l'utente dice "sì"
risposte = ["sì", "no", "sì", "sì", "no", "sì"]
i = 0       # serve per scorrere la lista
sì_count = 0   # conta le risposte positive

while i < len(risposte):
    if risposte[i] == "sì":
        sì_count = sì_count + 1   # aumenta SOLO se la risposta è "sì"
    i = i + 1   # questo aumenta sempre, ad ogni giro

print(f"Hai detto sì {sì_count} volte su {len(risposte)}")


# ------------------------------------------------------------
# 7. INPUT IN LOOP — chiedere finché la risposta è valida
# ------------------------------------------------------------

# uno dei casi più utili del while:
# continuare a chiedere all'utente finché inserisce qualcosa di valido

# versione SENZA while (fragile: se l'utente sbaglia, il programma va avanti lo stesso):
# età = int(input("Quanti anni hai? "))

# versione CON while (robusta: richiede finché il dato è corretto):

# passo 1: faccio la prima domanda FUORI dal while
età = int(input("Quanti anni hai? "))

# passo 2: controllo se la risposta è sbagliata
# nota: la condizione è quella dell'ERRORE, non quella giusta
while età < 0 or età > 120:

    # passo 3: dentro al while dico che c'è un problema
    print("Età non valida. Inserisci un numero tra 0 e 120.")

    # passo 4: chiedo di nuovo — DENTRO al while
    età = int(input("Quanti anni hai? "))

# qui arriviamo solo quando età è valida
print(f"Hai {età} anni.")

# schema da ricordare:
# 1. chiedi FUORI dal while
# 2. while la risposta è sbagliata:
# 3.     avvisa l'utente
# 4.     chiedi di nuovo DENTRO al while


# ------------------------------------------------------------
# 8. INPUT IN LOOP — uscire con una parola speciale
# ------------------------------------------------------------

# a volte non si sa quanti dati arriveranno:
# si continua finché l'utente scrive una parola di stop

# esempio: somma numeri finché l'utente scrive "fine"

# passo 1: chiedo il primo dato FUORI dal while
inserito = input("Scrivi un numero (o 'fine' per fermarti): ")

totale = 0   # qui accumulerò la somma

# passo 2: vado avanti finché NON ha scritto "fine"
while inserito != "fine":

    # passo 3: uso il dato inserito
    totale = totale + int(inserito)
    print(f"Totale parziale: {totale}")

    # passo 4: chiedo il prossimo dato
    inserito = input("Scrivi un numero (o 'fine' per fermarti): ")

# qui l'utente ha scritto "fine"
print(f"Hai finito. La somma totale è {totale}")


# ------------------------------------------------------------
# 9. METTERE TUTTO INSIEME — indovina il numero
# ------------------------------------------------------------

# costruiamo un gioco completo usando while + contatore + input in loop

# il numero da indovinare (scelto da noi nel codice)
numero_segreto = 13

# contatore dei tentativi — parte da 0
tentativi = 0

# prima domanda FUORI dal while
risposta = int(input("Indovina il numero segreto (tra 1 e 20): "))
tentativi = tentativi + 1   # il primo tentativo conta

# continuo finché la risposta è sbagliata
while risposta != numero_segreto:

    # do un indizio
    if risposta < numero_segreto:
        print("Troppo basso! Prova con un numero più grande.")
    else:
        print("Troppo alto! Prova con un numero più piccolo.")

    # chiedo di nuovo
    risposta = int(input("Riprova: "))
    tentativi = tentativi + 1   # conto questo tentativo

# quando arrivo qui, la risposta è corretta
print(f"Esatto! Hai indovinato {numero_segreto} in {tentativi} tentativi.")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Chiedi all'utente un voto da 1 a 10.
#    Se il voto è fuori da questo intervallo, mostra
#    "Voto non valido" e chiedi di nuovo.
#    Quando il voto è corretto, stampa "Promosso" (>= 6)
#    oppure "Bocciato" (< 6).
#    Suggerimento: usa lo schema del blocco 7.
#
# 2. Chiedi all'utente di indovinare una parola segreta
#    (sceglila tu nel codice, es. "python").
#    Ogni volta che sbaglia, stampa "Sbagliato, riprova."
#    Quando indovina, stampa quanti tentativi ha usato.
#    Suggerimento: inizia con il contatore a 0 e aumentalo
#    di 1 ad ogni risposta, anche alla prima.
#
# 3. Chiedi all'utente numeri uno alla volta.
#    Finisce quando scrive "fine".
#    Alla fine stampa: quanti numeri ha inserito,
#    la loro somma e la media.
#    Suggerimento: tieni tre variabili separate — contatore,
#    somma — e calcola la media alla fine dividendo i due.
#    Attenzione: se l'utente scrive "fine" subito (0 numeri),
#    non dividere per zero.
# ============================================================
