# ============================================================
# LEZIONE 2 — Operatori e condizioni if / elif / else
# Unità 1 · Settimane 3-4
# ============================================================
# Prerequisiti: lezione 1 (variabili, input, f-string)
# Obiettivo: lo studente sa fare calcoli e far prendere
# decisioni al programma in base ai dati.
# ============================================================


# ------------------------------------------------------------
# 1. OPERATORI ARITMETICI — i calcoli di base
# ------------------------------------------------------------

a = 10
b = 3

print(a + b)    # addizione      → 13
print(a - b)    # sottrazione    → 7
print(a * b)    # moltiplicazione → 30
print(a / b)    # divisione      → 3.333... (restituisce float)
print(a // b)   # divisione intera → 3 (solo la parte intera)
print(a % b)    # modulo = resto → 1  (quanto avanza dividendo per b)
print(a ** b)   # potenza        → 1000 (a elevato a b)

# il % (modulo) è molto utile: se il resto è 0, il numero è divisibile
print(10 % 2)   # → 0, quindi 10 è divisibile per 2 (è pari)
print(7 % 2)    # → 1, quindi 7 NON è divisibile per 2 (è dispari)


# ------------------------------------------------------------
# 2. OPERATORI DI CONFRONTO — confrontare due valori
# ------------------------------------------------------------

# restituiscono sempre True o False
x = 5

print(x == 5)   # uguale a        → True
print(x != 3)   # diverso da      → True
print(x > 3)    # maggiore di     → True
print(x < 3)    # minore di       → False
print(x >= 5)   # maggiore o uguale → True
print(x <= 4)   # minore o uguale   → False

# attenzione: = assegna, == confronta
# y = 5   → metto 5 nella variabile y
# y == 5  → controllo se y vale 5


# ------------------------------------------------------------
# 3. IF — fare una cosa solo se una condizione è vera
# ------------------------------------------------------------

# la struttura è:
# if condizione:
#     cosa fare se è vera
# (l'indentazione — lo spazio prima — è obbligatoria!)

numero = int(input("Dimmi un numero: "))

if numero > 0:
    print("Il numero è positivo")

# se la condizione è falsa, il blocco viene saltato completamente


# ------------------------------------------------------------
# 4. IF / ELSE — una cosa se vera, un'altra se falsa
# ------------------------------------------------------------

voto = int(input("Qual è il tuo voto? "))

if voto >= 6:
    print("Sei promosso!")
else:
    print("Sei bocciato.")


# ------------------------------------------------------------
# 5. IF / ELIF / ELSE — gestire più casi
# ------------------------------------------------------------

# elif = "altrimenti se" — si usa quando i casi sono più di due
# python controlla dall'alto verso il basso e si ferma al primo True

temperatura = float(input("Che temperatura fa fuori? "))

if temperatura >= 30:
    print("Caldo!")
elif temperatura >= 20:
    print("Bello")
elif temperatura >= 10:
    print("Fresco")
else:
    print("Freddo!")

# esempio completo: calcolo voto con giudizio
print("---")
voto2 = int(input("Inserisci un voto da 1 a 10: "))
media = voto2  # qui è solo un voto, ma potrebbe essere una media

if media < 6:
    print("Insufficiente")
elif media == 6:
    print("Sufficiente")
elif media == 7:
    print("Discreto")
elif media == 8:
    print("Buono")
elif media == 9:
    print("Ottimo")
else:
    print("Eccellente!")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Chiedi un numero. Se è pari stampa "pari", altrimenti "dispari".
#    (suggerimento: usa %)
#
# 2. Chiedi l'anno di nascita. Calcola l'età.
#    Se l'età è >= 18 stampa "maggiorenne", altrimenti "minorenne".
#
# 3. Chiedi il prezzo di un biglietto (intero) e l'età della persona.
#    - meno di 6 anni: gratis
#    - da 6 a 17 anni: metà prezzo
#    - 18 anni o più: prezzo intero
#    Stampa quanto deve pagare.
# ============================================================
