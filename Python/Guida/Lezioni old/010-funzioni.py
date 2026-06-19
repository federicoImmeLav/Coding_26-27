# FUNZIONI
# definisco la funzione che saluta con print
# def saluta():
    # print("ciao")
# per farla funzionare devo chiamarla 
# saluta()

############################################################
# funzione con parametro nome
# def saluta(nome):
    # print(f"ciao {nome}")
# quando chiamo la funzione devo anche dirgli il parametro
# saluta("Cristian")

# faccio esempio in cui il nome lo dico io al programma
# usando input 
# risposta = input("Chi devo salutare? ")
# chiamo la funzione mettendo il parametro del nome 
# saluta(risposta)

############################################################
# funzione che calcola l'area del rettangolo come
# base per altezza, il mio programma deve quindi chiedermi
# quanto valgono la base e l'altezza e poi stampare
# il risultato 
# 1. creo la funzione con due parametri
# def area(base, altezza):
    # return base * altezza # risultato che viene sputato fuori dalla funzione

# 2. chiedo con input quanto valgono base e altezza
# base = int(input("Quanto vale la base? "))
# altezza = int(input("Quanto vale l'altezza? "))

# print(f"L'area del rettangolo vale: {area(base,altezza)}")

############################################################
# Creo programma con una funzione che mi dice quanto 
# costerà un prodotto se io gli dico quanto costava prima 
# e di quanti euro è scontato 

# Creo la funzione che prende il prezzo originale e lo sconto 
# e li sottrae 
def prezzo_scontato(prezzo_iniziale, sconto):
    return prezzo_iniziale - sconto

# chiedo all'utente i due valori 
prezzo_iniziale = float(input("Quanto costa il prodotto? "))
sconto = float(input("Di quanti euro è lo sconto? "))

print(f"Il prezzo scontato è di: {prezzo_scontato(prezzo_iniziale, sconto)}")
