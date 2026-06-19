# voglio fare un programma che calcola l'eta partendo 
# dall'anno di nascita e se il calcolo è più di 18 anni
# mi dice che sono maggiorenne, altrimenti mi dice 
# che sono minorenne 

nome = input("Come ti chiami? ")
#int si usa per i numeri interi
anno = int(input("In che anno sei nato? "))

#float si usa per salvare i numeri decimali
altezza = float(input("Quanto sei alto?" ))
#la virgola nei decimali in python non si usa, si usa il .

eta = 2025 - anno # calcolo eta sapendo l'anno
#stampo la frase "[nome] ha [eta] anni"
print(f"{nome} ha {eta} anni ed è alto {altezza}")
#per mettere una condizione devo usare if
if eta >= 18:
    print("ed è maggiorenne!") #lo spazio prima è fondamentale
else: #considero tutti gli altri casi
    print("ed è minorenne!")