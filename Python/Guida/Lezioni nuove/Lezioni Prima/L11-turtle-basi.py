# ============================================================
# LEZIONE 11 — Disegnare con Turtle: basi
# Unità 4 · Settimane 21-22
# ============================================================
# Prerequisiti: L10 (funzioni, liste, dizionari)
# Obiettivo: lo studente sa aprire una finestra grafica con turtle,
# muovere la tartaruga, cambiare colore e velocità, e disegnare
# forme geometriche usando il ciclo for.
# ============================================================


# ------------------------------------------------------------
# 1. UNA NUOVA FINESTRA — il codice che produce qualcosa di visibile
# ------------------------------------------------------------

# finora print() produceva testo nel terminale
# turtle fa qualcosa di diverso: apre una finestra e ci disegna dentro

# la tartaruga è una "penna" che si muove sullo schermo —
# dove passa, lascia una traccia

# le tre righe minime per far funzionare turtle:

import turtle             # carica la libreria
t = turtle.Turtle()       # crea la tartaruga (la chiamo t per comodità)

t.forward(100)            # muovo la tartaruga avanti di 100 pixel

turtle.done()             # mantiene la finestra aperta finché non la chiudi


# ------------------------------------------------------------
# 2. COMANDI DI MOVIMENTO — avanti, indietro, gira
# ------------------------------------------------------------

# la tartaruga parte al centro, puntata verso destra
# i comandi base di movimento:

# t.forward(n)   → avanza di n pixel nella direzione in cui punta
# t.backward(n)  → torna indietro di n pixel
# t.right(gradi) → ruota a destra di tot gradi
# t.left(gradi)  → ruota a sinistra di tot gradi

# gli "gradi" sono quelli della geometria: un giro completo è 360°
# girare a destra di 90° = 90° in senso orario

import turtle
t = turtle.Turtle()

t.forward(100)    # va avanti
t.right(90)       # gira a destra di 90°
t.forward(100)    # va avanti nella nuova direzione

turtle.done()

# prova mentale: dove si trova la tartaruga adesso?
# è partita verso destra, ha disegnato 100px, ha girato in giù, ha disegnato altri 100px
# ha tracciato una L


# ------------------------------------------------------------
# 3. VELOCITÀ E COLORE — personalizzare il disegno
# ------------------------------------------------------------

# di default la tartaruga è lenta e disegna in nero
# questi due comandi cambiano tutto:

import turtle
t = turtle.Turtle()

t.speed(10)           # velocità da 1 (lentissima) a 10 (veloce) — 0 = istantanea
t.color("blue")       # colore del tratto (in inglese: "red", "green", "purple"...)
t.shape("turtle")     # mostra la forma di una tartaruga invece della freccia

t.forward(200)

turtle.done()

# nota: t.color() imposta il colore PRIMA di iniziare a disegnare
# se lo chiami dopo aver già mosso, cambia colore da quel punto in poi


# ------------------------------------------------------------
# 4. DISEGNARE UN QUADRATO — il problema della ripetizione
# ------------------------------------------------------------

# per disegnare un quadrato a mano devo ripetere 4 volte
# "avanti + gira di 90°"

# senza for, il codice è così:
import turtle
t = turtle.Turtle()
t.speed(5)
t.color("red")

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

turtle.done()

# quattro righe identiche ripetute — esattamente il problema che risolve il for


# ------------------------------------------------------------
# 5. FORME CON IL FOR — il pattern del poligono
# ------------------------------------------------------------

# un poligono regolare ha tutti i lati uguali e tutti gli angoli uguali
# in ogni punto la tartaruga gira sempre dello stesso angolo esterno
# angolo esterno = 360 / numero di lati

# quadrato:   360 / 4 = 90°
# triangolo:  360 / 3 = 120°
# esagono:    360 / 6 = 60°

import turtle
t = turtle.Turtle()
t.speed(5)

# quadrato con il for
t.color("blue")
for i in range(4):
    t.forward(100)
    t.right(90)       # 360 / 4 = 90

turtle.done()

# versione con il triangolo
import turtle
t = turtle.Turtle()
t.speed(5)

t.color("green")
for i in range(3):
    t.forward(100)
    t.right(120)      # 360 / 3 = 120

turtle.done()


# ------------------------------------------------------------
# 6. PENUP E PENDOWN — spostare la tartaruga senza disegnare
# ------------------------------------------------------------

# di default la tartaruga disegna sempre mentre si muove
# se vuoi spostarla senza lasciare traccia, devi "alzare il pennello"

# t.penup()    → alza il pennello: la tartaruga si muove ma non disegna
# t.pendown()  → abbassa il pennello: la tartaruga ricomincia a disegnare

# esempio: due quadrati separati

import turtle
t = turtle.Turtle()
t.speed(10)

# disegno il primo quadrato
t.color("blue")
for i in range(4):
    t.forward(100)
    t.right(90)

# mi sposto senza disegnare
t.penup()
t.forward(150)    # mi sposto di 150 pixel a destra
t.pendown()

# disegno il secondo quadrato in un colore diverso
t.color("red")
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()

# schema da ricordare:
# passo 1: penup()     → alza il pennello
# passo 2: forward()   → spostati dove vuoi
# passo 3: pendown()   → abbassa il pennello
# passo 4: disegna


# ============================================================
# ESERCIZI
# ============================================================
# 1. Chiedi all'utente la lunghezza del lato (es. 80 o 150)
#    e disegna un quadrato di quella dimensione in colore verde.
#    Suggerimento: metti int(input(...)) prima di import turtle,
#    poi usa la variabile dentro al for.
#
# 2. Disegna un triangolo e, separato da uno spazio,
#    un quadrato dello stesso lato (es. 100).
#    I due poligoni non devono toccarsi.
#    Suggerimento: usa penup() e pendown() per spostarti tra i due.
#
# 3. Disegna una "casa": un quadrato come base e un triangolo
#    come tetto, senza staccare il pennello tra i due.
#    Suggerimento: dopo aver disegnato il quadrato, la tartaruga
#    è tornata al punto di partenza. Da lì, ruotala in modo che
#    il triangolo si appoggi al lato superiore del quadrato.
# ============================================================
