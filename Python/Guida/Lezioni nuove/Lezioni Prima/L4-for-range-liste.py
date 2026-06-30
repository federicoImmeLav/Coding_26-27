# ============================================================
# LEZIONE 4 — Il ciclo for, range e iterazione
# Unità 2 · Settimane 7-8
# ============================================================
# Prerequisiti: L3 (operatori logici, messaggi di errore)
# Obiettivo: lo studente sa usare il for per ripetere azioni,
# controllare il range e scorrere stringhe e liste semplici.
# ============================================================


# ------------------------------------------------------------
# 1. IL CICLO FOR — ripetere un'azione un numero preciso di volte
# ------------------------------------------------------------

# il for serve quando SAI già quante volte vuoi ripetere qualcosa
# è come dire "fai questa cosa 5 volte"

for i in range(5):
    print("Buongiorno!")

# la variabile i cambia ad ogni giro: 0, 1, 2, 3, 4
# il nome i è una convenzione — puoi usare qualsiasi nome

for numero in range(5):
    print(numero)   # stampa: 0, 1, 2, 3, 4


# ------------------------------------------------------------
# 2. RANGE — controllare inizio, fine e passo
# ------------------------------------------------------------

# range(fine)           → parte da 0, si ferma prima di "fine"
# range(inizio, fine)   → parte da inizio, si ferma prima di fine
# range(inizio, fine, passo) → salta di "passo" in "passo"

# numeri da 1 a 10 incluso
for n in range(1, 11):
    print(n)

# solo i numeri pari tra 0 e 10
for n in range(0, 11, 2):
    print(n)   # stampa: 0, 2, 4, 6, 8, 10

# conto alla rovescia
for n in range(5, 0, -1):
    print(n)   # stampa: 5, 4, 3, 2, 1
print("Via!")


# ------------------------------------------------------------
# 3. ACCUMULATORE — calcolare dentro al ciclo
# ------------------------------------------------------------

# per sommare (o contare) dentro un for,
# inizializzi una variabile FUORI e la aggiorni DENTRO

# somma dei numeri da 1 a 100
somma = 0
for n in range(1, 101):
    somma = somma + n
print(f"La somma da 1 a 100 è {somma}")

# tabellina di un numero scelto dall'utente
numero = int(input("Di quale numero vuoi la tabellina? "))
for i in range(1, 11):
    print(f"{numero} × {i} = {numero * i}")


# ------------------------------------------------------------
# 4. ITERARE SU UNA STRINGA — lettera per lettera
# ------------------------------------------------------------

# il for non funziona solo con i numeri:
# puoi usarlo su una stringa per scorrere le lettere una alla volta

nome = input("Scrivi il tuo nome: ")
for lettera in nome:
    print(lettera)

# esempio pratico: conta quante lettere "a" ci sono nel nome
contatore = 0
for lettera in nome:
    if lettera == "a" or lettera == "A":
        contatore = contatore + 1
print(f"Il tuo nome contiene {contatore} lettere A")


# ------------------------------------------------------------
# 5. ITERARE SU UNA LISTA — elemento per elemento
# ------------------------------------------------------------

# una lista è un gruppo di valori scritti tra parentesi quadre
# il for ci permette di accedere a ogni elemento uno alla volta

voti = [7, 8, 6, 9, 5]
for voto in voti:
    print(f"Voto: {voto}")

# calcoliamo la media dei voti
totale = 0
for voto in voti:
    totale = totale + voto
media = totale / len(voti)   # len() dà il numero di elementi
print(f"Media: {media}")

# funziona anche con stringhe nella lista
materie = ["italiano", "matematica", "storia", "inglese"]
for materia in materie:
    print(f"Hai una lezione di {materia}")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Chiedi un numero all'utente e stampa la sua tabellina
#    da 1 a 10, nel formato: "7 × 3 = 21".
#
# 2. Chiedi il nome all'utente e conta quante vocali contiene.
#    Stampa: "Il tuo nome ha 3 vocali."
#    Suggerimento: controlla se ogni lettera è in "aeiouAEIOU".
#
# 3. Hai questa lista di prezzi: [3.50, 1.20, 8.00, 2.75, 5.40]
#    Calcola e stampa il totale e il prezzo più alto.
#    Suggerimento: usa due accumulatori, uno per il totale
#    e uno che tieni aggiornato con il massimo trovato finora.
# ============================================================
