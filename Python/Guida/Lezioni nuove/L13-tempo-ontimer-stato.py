# ============================================================
# LEZIONE 13 — Tempo, ontimer e booleani come stato
# Unità 5 · Settimane 25-26
# ============================================================
# Prerequisiti: L12 (turtle con tasti, onkey, mainloop)
# Obiettivo: lo studente sa misurare il tempo con time.time(),
# usare ontimer per aggiornare la schermata a intervalli regolari,
# usare global per modificare variabili esterne alle funzioni,
# e usare True/False per rappresentare lo stato di un programma.
# ============================================================


# ------------------------------------------------------------
# 1. MISURARE IL TEMPO — time.time()
# ------------------------------------------------------------

# la libreria time permette di lavorare con il tempo
# time.time() restituisce i secondi passati dal 1° gennaio 1970
# di per sé quel numero è enorme e poco utile —
# ma la differenza tra due misure è esattamente il tempo trascorso

import time

inizio = time.time()
print("Misurazione avviata...")

nome = input("Come ti chiami? ")

fine = time.time()
trascorso = fine - inizio

print(f"Hai impiegato {int(trascorso)} secondi a scrivere il tuo nome")

# schema da ricordare:
# 1. salva time.time() PRIMA dell'azione
# 2. esegui l'azione
# 3. salva time.time() DOPO l'azione
# 4. sottrai: fine - inizio = secondi trascorsi


# ------------------------------------------------------------
# 2. SCRIVERE SULLA SCHERMATA — write() e clear()
# ------------------------------------------------------------

# in turtle si può usare una tartaruga "invisibile" come etichetta
# write() scrive del testo nella posizione della tartaruga
# clear() cancella quello che ha scritto — per aggiornarlo

import turtle

s = turtle.Screen()

etichetta = turtle.Turtle()
etichetta.hideturtle()   # nasconde la freccia
etichetta.penup()
etichetta.goto(0, 100)   # posiziona l'etichetta in alto al centro

etichetta.write("Ciao!", font=("Arial", 24), align="center")

# per aggiornare il testo: prima clear(), poi write() di nuovo
# (non si può "sovrascrivere" — il vecchio testo rimane sotto)
etichetta.clear()
etichetta.write("Testo aggiornato!", font=("Arial", 24), align="center")

s.mainloop()


# ------------------------------------------------------------
# 3. ONTIMER — eseguire una funzione dopo X millisecondi
# ------------------------------------------------------------

# s.ontimer(funzione, millisecondi) esegue una funzione
# una volta sola, dopo il ritardo indicato

# ma se dentro la funzione richiamiamo s.ontimer() su se stessa,
# otteniamo un aggiornamento continuo — come un orologio

import turtle
import time

s = turtle.Screen()

contatore = turtle.Turtle()
contatore.hideturtle()
contatore.penup()

n = 0   # variabile che conta i secondi

def aggiorna():
    global n          # dice a Python di usare la n esterna (vedi blocco 4)
    n = n + 1
    contatore.clear()
    contatore.write(f"Secondi: {n}", font=("Arial", 30), align="center")
    s.ontimer(aggiorna, 1000)   # si richiama dopo 1000ms = 1 secondo

aggiorna()   # prima chiamata — poi si richiama da sola
s.mainloop()

# cosa succede:
# - aggiorna() viene chiamata
# - aggiorna n, cancella e riscrive
# - programma ontimer per richiamarsi tra 1 secondo
# - 1 secondo dopo, aggiorna() viene chiamata di nuovo
# - e così via, all'infinito


# ------------------------------------------------------------
# 4. GLOBAL — usare variabili esterne dentro le funzioni
# ------------------------------------------------------------

# le funzioni in Python hanno la loro "zona" di variabili
# se vuoi leggere o modificare una variabile esterna,
# devi dichiararlo con global

# esempio senza global (non funziona come ci aspettiamo):
punteggio = 0

def aggiungi_punto():
    punteggio = punteggio + 1   # ERRORE: Python pensa che punteggio sia locale

# esempio con global (funziona):
punteggio = 0

def aggiungi_punto():
    global punteggio            # dice a Python: usa quella esterna
    punteggio = punteggio + 1

aggiungi_punto()
aggiungi_punto()
print(punteggio)   # stampa 2

# regola pratica: usa global solo quando hai bisogno di MODIFICARE
# una variabile definita fuori dalla funzione


# ------------------------------------------------------------
# 5. BOOLEANI COME STATO — True/False per "cosa sta succedendo"
# ------------------------------------------------------------

# un booleano può rappresentare lo stato di qualcosa:
# True = acceso / attivo / in corso
# False = spento / fermo / non iniziato

# esempio concreto: una luce
luce_accesa = False

def accendi():
    global luce_accesa
    luce_accesa = True
    print("Luce accesa")

def spegni():
    global luce_accesa
    luce_accesa = False
    print("Luce spenta")

# il booleano non fa niente da solo — serve per prendere decisioni:
if luce_accesa:
    print("Puoi leggere")
else:
    print("È buio")

# nei giochi si usa lo stesso schema:
# gioco_avviato = False → il gioco è fermo
# gioco_avviato = True  → il gioco è in corso

# questo permette di controllare nelle funzioni se il gioco
# è ancora attivo prima di aggiornare schermata o punteggio


# ------------------------------------------------------------
# 6. METTERE TUTTO INSIEME — cronometro con start e stop
# ------------------------------------------------------------

# costruiamo un cronometro interattivo:
# spazio → avvia il cronometro
# s → ferma il cronometro e mostra il tempo totale

import turtle
import time

s = turtle.Screen()
s.listen()

# etichetta delle istruzioni
istruzioni = turtle.Turtle()
istruzioni.hideturtle()
istruzioni.penup()
istruzioni.goto(0, -150)
istruzioni.write("SPAZIO = avvia  |  S = ferma", font=("Arial", 16), align="center")

# etichetta del tempo
display = turtle.Turtle()
display.hideturtle()
display.penup()
display.write("0.00", font=("Arial", 48), align="center")

# variabili di stato
in_corso = False    # True quando il cronometro sta girando
tempo_inizio = 0    # quando è partito

def aggiorna_display():
    global in_corso
    if in_corso:
        trascorso = time.time() - tempo_inizio
        display.clear()
        display.write(f"{trascorso:.2f}", font=("Arial", 48), align="center")
        s.ontimer(aggiorna_display, 50)   # aggiorna ogni 50ms = 20 volte al secondo

def avvia():
    global in_corso, tempo_inizio
    if not in_corso:              # avvia solo se non è già in corso
        in_corso = True
        tempo_inizio = time.time()
        aggiorna_display()

def ferma():
    global in_corso
    in_corso = False              # ferma gli aggiornamenti

s.onkey(avvia, "space")
s.onkey(ferma, "s")

s.mainloop()


# ============================================================
# ESERCIZI
# ============================================================
# 1. Crea un programma che misura quanto tempo impiega l'utente
#    a rispondere a tre domande di cultura generale (sceglile tu).
#    Alla fine stampa il tempo totale e se ha risposto correttamente
#    a tutte e tre.
#    Suggerimento: usa lo schema del blocco 1 — salva time.time()
#    prima e dopo le domande, poi sottrai.
#
# 2. Crea un conto alla rovescia in turtle: parte da 10 e scala
#    di 1 ogni secondo. Quando arriva a 0 scrive "TEMPO SCADUTO!"
#    Suggerimento: usa ontimer con intervallo 1000 e un if
#    per fermarsi quando n == 0 invece di richiamare ontimer.
#
# 3. Partendo dal cronometro del blocco 6, aggiungi un tasto "r"
#    che resetta il cronometro a zero (ferma il conteggio e
#    riporta il display a "0.00").
#    Suggerimento: nella funzione reset() metti in_corso = False,
#    poi aggiorna tempo_inizio e riscrivi il display.
# ============================================================
