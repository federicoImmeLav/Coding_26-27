# ============================================================
# LEZIONE 14 — Collisioni, punteggio e primo gioco completo
# Unità 5 · Settimane 27-28
# ============================================================
# Prerequisiti: L13 (time, ontimer, global, booleani come stato)
# Obiettivo: lo studente sa generare posizioni casuali con random,
# rilevare collisioni con distance(), aggiornare un punteggio
# sullo schermo e costruire un gioco completo con fine partita.
# ============================================================


# ------------------------------------------------------------
# 1. NUMERI CASUALI — random.randint()
# ------------------------------------------------------------

# la libreria random permette di generare numeri "a caso"
# random.randint(a, b) restituisce un numero intero tra a e b inclusi
# ogni volta che lo chiami, il numero è diverso

import random

dado = random.randint(1, 6)
print(f"Hai tirato il dado: {dado}")

# si usa molto nei giochi per:
# - posizionare oggetti in punti casuali dello schermo
# - decidere eventi casuali (un ostacolo che appare, una mela che si sposta)

# esempio: cinque posizioni x casuali per una schermata 600×600
for i in range(5):
    x = random.randint(-300, 300)
    print(f"Posizione x: {x}")


# ------------------------------------------------------------
# 2. GOTO — posizionare una tartaruga su coordinate precise
# ------------------------------------------------------------

# t.goto(x, y) sposta la tartaruga alle coordinate indicate
# il centro della schermata è (0, 0)
# x cresce verso destra, y cresce verso l'alto

import turtle

s = turtle.Screen()

oggetto = turtle.Turtle()
oggetto.shape("circle")
oggetto.color("red")
oggetto.penup()        # penup prima di goto, altrimenti disegna una linea

oggetto.goto(100, 50)   # va a x=100, y=50
oggetto.goto(-200, 0)   # torna a sinistra
oggetto.goto(0, 0)      # torna al centro

# combinato con random: sposta l'oggetto in un posto casuale
import random
x = random.randint(-250, 250)
y = random.randint(-250, 250)
oggetto.goto(x, y)

s.mainloop()


# ------------------------------------------------------------
# 3. DISTANZA TRA DUE OGGETTI — distance()
# ------------------------------------------------------------

# t1.distance(t2) restituisce la distanza in pixel tra t1 e t2
# si usa per capire se due oggetti si sono "toccati"
# se la distanza è minore di una soglia → collisione!

import turtle

s = turtle.Screen()

giocatore = turtle.Turtle()
giocatore.shape("square")
giocatore.color("blue")
giocatore.penup()

bersaglio = turtle.Turtle()
bersaglio.shape("circle")
bersaglio.color("red")
bersaglio.penup()
bersaglio.goto(80, 0)

# controllo: sono vicini?
distanza = giocatore.distance(bersaglio)
print(f"Distanza: {distanza} pixel")

if distanza < 20:
    print("Collisione!")
else:
    print("Ancora lontani")

# la soglia (20 pixel) dipende dalla dimensione degli oggetti:
# oggetti piccoli → soglia piccola (10-15px)
# oggetti grandi → soglia grande (30-40px)

s.mainloop()


# ------------------------------------------------------------
# 4. PUNTEGGIO SULLO SCHERMO — scrivere e aggiornare
# ------------------------------------------------------------

# per mostrare il punteggio in una finestra turtle
# si usa una tartaruga nascosta come etichetta (come in L13)
# ogni volta che il punteggio cambia: clear() poi write()

import turtle

s = turtle.Screen()

punteggio = 0

display_punti = turtle.Turtle()
display_punti.hideturtle()
display_punti.penup()
display_punti.goto(0, 260)
display_punti.write(f"Punteggio: {punteggio}", font=("Arial", 20), align="center")

def aggiorna_punteggio():
    global punteggio
    punteggio += 1
    display_punti.clear()
    display_punti.write(f"Punteggio: {punteggio}", font=("Arial", 20), align="center")

# esempio: aumenta il punteggio ogni volta che si preme spazio
s.listen()
s.onkey(aggiorna_punteggio, "space")

s.mainloop()


# ------------------------------------------------------------
# 5. GAME LOOP CON ONTIMER — aggiornare il gioco ogni frame
# ------------------------------------------------------------

# nei giochi la logica (movimento, collisioni, punteggio)
# viene controllata molte volte al secondo — ogni "frame"
# ontimer ci permette di costruire questo loop:

# def aggiorna():
#     # tutto quello che succede ogni frame va qui
#     muovi_personaggio()
#     controlla_collisioni()
#     aggiorna_schermata()
#     s.ontimer(aggiorna, 16)   # 16ms ≈ 60 frame al secondo

# turtle.tracer(0) e turtle.update() servono a disegnare
# tutto in una volta sola — senza, ogni movimento fa lampeggiare la schermata

import turtle
turtle.tracer(0)   # disattiva il disegno automatico

# ... (muovi le tartarughe) ...

turtle.update()    # ridisegna tutto in una volta sola


# ------------------------------------------------------------
# 6. GIOCO COMPLETO — raccogli le mele
# ------------------------------------------------------------

# costruiamo un gioco completo passo per passo:
# - un quadrato verde controllato con wasd
# - una mela rossa in posizione casuale
# - ogni volta che il quadrato tocca la mela, punteggio +1
# - la mela si sposta in un posto casuale
# - quando il punteggio raggiunge 10, il gioco finisce

import turtle
import random

turtle.tracer(0)

s = turtle.Screen()
s.listen()

# --- oggetti ---
giocatore = turtle.Turtle()
giocatore.shape("square")
giocatore.color("green")
giocatore.penup()

mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()
mela.goto(random.randint(-250, 250), random.randint(-250, 250))

# --- punteggio e display ---
punteggio = 0
gioco_attivo = True

display = turtle.Turtle()
display.hideturtle()
display.penup()
display.goto(0, 270)
display.write(f"Punteggio: {punteggio} / 10", font=("Arial", 18), align="center")

# --- stato dei tasti ---
tasti = {"w": False, "a": False, "s": False, "d": False}

def premi(t):
    tasti[t] = True

def alza(t):
    tasti[t] = False

s.onkeypress(lambda: premi("w"), "w")
s.onkeypress(lambda: premi("a"), "a")
s.onkeypress(lambda: premi("s"), "s")
s.onkeypress(lambda: premi("d"), "d")
s.onkeyrelease(lambda: alza("w"), "w")
s.onkeyrelease(lambda: alza("a"), "a")
s.onkeyrelease(lambda: alza("s"), "s")
s.onkeyrelease(lambda: alza("d"), "d")

# --- game loop ---
def aggiorna():
    global punteggio, gioco_attivo

    if not gioco_attivo:
        return           # se il gioco è finito, non fare niente

    # movimento
    if tasti["w"]:
        giocatore.setheading(90)
        giocatore.forward(5)
    if tasti["s"]:
        giocatore.setheading(-90)
        giocatore.forward(5)
    if tasti["a"]:
        giocatore.setheading(180)
        giocatore.forward(5)
    if tasti["d"]:
        giocatore.setheading(0)
        giocatore.forward(5)

    # collisione con la mela
    if giocatore.distance(mela) < 20:
        punteggio += 1
        display.clear()
        display.write(f"Punteggio: {punteggio} / 10", font=("Arial", 18), align="center")
        # sposta la mela in un posto casuale
        mela.goto(random.randint(-250, 250), random.randint(-250, 250))

    # condizione di vittoria
    if punteggio >= 10:
        gioco_attivo = False
        display.clear()
        display.write("Hai vinto!", font=("Arial", 36), align="center")

    turtle.update()
    s.ontimer(aggiorna, 16)   # richiama tra 16ms

aggiorna()
s.mainloop()


# ============================================================
# ESERCIZI
# ============================================================
# 1. Aggiungi al gioco del blocco 6 un timer che conta alla
#    rovescia da 30 secondi. Se il tempo scade prima di
#    raggiungere 10 punti, scrivi "Tempo scaduto!" sullo schermo.
#    Suggerimento: usa una seconda funzione con ontimer(1000)
#    separata dal game loop, come in L13.
#
# 2. Aggiungi un ostacolo: una tartaruga arancione in posizione
#    casuale. Se il giocatore la tocca, perde 1 punto.
#    Suggerimento: usa distance() anche con l'ostacolo,
#    con la stessa soglia della mela.
#
# 3. Modifica il gioco in modo che ci siano 3 mele sullo schermo
#    contemporaneamente invece di una sola.
#    Ogni volta che il giocatore ne raccoglie una, quella si sposta
#    in un posto casuale e il punteggio sale.
#    Suggerimento: metti le tre mele in una lista e usa un for
#    per controllare la distanza da ognuna dentro al game loop.
# ============================================================
