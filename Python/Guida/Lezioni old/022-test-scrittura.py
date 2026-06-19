# Creo un gioco che misura quanto tempo ci metto a scrivere
# una frase e mi dice poi quanto tempo effettivamente ci
# ho messo. La frase deve essere casuale ogni volta

import time
import random

# creo elenco di frasi per scelta random
frasi = [
    "La pioggia battente cadde sul vecchio tetto di paglia.",
    "Ogni mattina porto il cane al parco vicino al fiume.",
    "La biblioteca era piena di libri rari e manoscritti antichi."
]

# creo la funzione di gioco
def gioco():
    print("Benvenuto nel gioco di test di scrittura")
    print("Il tuo obiettivo è scrivere la prossima frase nel minor tempo possibile")
    pronto = input("Sei pronto per giocare? y/n ")
    # se rispondo di si, parte il gioco
    if pronto == "y":
        print("La frase che devi scrivere è:")
        frase = random.choice(frasi)
        print(frase)
        # input per far si che il giocatore scrive
        tempo_inizio = time.time()
        risposta = input("Scrivi:")
        # controllo che ho risposto giusto
        if risposta == frase:
            tempo_fine = time.time()
            tempo = tempo_fine - tempo_inizio
            print(f"Ci hai messo {tempo: .2f} secondi")
        else:
            print("Sbagliato")
            gioco()
    else:
        print("okey, ciao")
        gioco()
gioco()