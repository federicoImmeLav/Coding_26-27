# ============================================================
# LEZIONE 12 — Turtle: controllo con i tasti e disegno libero
# Unità 4 · Settimane 23-24
# ============================================================
# Prerequisiti: L11 (comandi base turtle, for, penup/pendown)
# Obiettivo: lo studente sa collegare i tasti freccia a funzioni
# di movimento, usare penup/pendown con i tasti e costruire
# un programma di disegno libero interattivo.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA DEL CODICE FISSO — il disegno non risponde
# ------------------------------------------------------------

# nelle lezioni precedenti il programma disegnava e poi finiva:
# il codice scorreva dall'alto in basso, una volta sola

import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
turtle.done()

# questo approccio non permette di interagire col disegno:
# non posso premere un tasto e far muovere la tartaruga
# ho bisogno di un programma che rimanga aperto e aspetti
# quello che faccio con la tastiera


# ------------------------------------------------------------
# 2. SCREEN E MAINLOOP — il programma che aspetta
# ------------------------------------------------------------

# invece di turtle.done(), si usa un oggetto Screen e mainloop()
# mainloop() dice al programma: "rimani aperto e aspetta eventi"
# il programma non finisce finché non si chiude la finestra

import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.Screen()   # crea la schermata (la chiamo s)

# tutto il codice va messo QUI, prima di mainloop()

s.mainloop()          # apre la finestra e la mantiene aperta — va sempre ALLA FINE

# nota: con mainloop() non serve più turtle.done()
# sono due modi alternativi per tenere aperta la finestra


# ------------------------------------------------------------
# 3. LISTEN — dire alla schermata di ascoltare la tastiera
# ------------------------------------------------------------

# per default la schermata non ascolta la tastiera
# s.listen() la "attiva" — deve stare prima di onkey()

import turtle

t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()

s.listen()   # da questo momento la schermata ascolta i tasti

s.mainloop()

# senza s.listen(), i tasti non funzionano anche se li colleghi con onkey()


# ------------------------------------------------------------
# 4. FUNZIONI DI MOVIMENTO — dove si definisce cosa fa ogni tasto
# ------------------------------------------------------------

# ogni tasto deve essere collegato a una funzione
# la funzione descrive cosa succede quando quel tasto viene premuto

# setheading(gradi) punta la tartaruga in una direzione fissa:
#   0   → destra
#   90  → su
#   180 → sinistra
#   -90 → giù  (oppure 270)

# è più comodo di right()/left() perché non dipende dalla direzione attuale

import turtle

t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()

def destra():
    t.setheading(0)     # punta a destra
    t.forward(30)       # avanza

def sinistra():
    t.setheading(180)
    t.forward(30)

def su():
    t.setheading(90)
    t.forward(30)

def giu():
    t.setheading(-90)
    t.forward(30)

s.listen()
s.mainloop()

# le funzioni sono definite, ma non ancora collegate ai tasti
# questo succede nel prossimo blocco


# ------------------------------------------------------------
# 5. ONKEY — collegare un tasto a una funzione
# ------------------------------------------------------------

# s.onkey(funzione, "tasto") collega un tasto a una funzione
# quando l'utente preme quel tasto, viene eseguita la funzione

# i nomi dei tasti freccia sono: "Right", "Left", "Up", "Down"
# per gli altri tasti si usa la lettera: "space", "z", "x", ...

import turtle

t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()

def destra():
    t.setheading(0)
    t.forward(30)

def sinistra():
    t.setheading(180)
    t.forward(30)

def su():
    t.setheading(90)
    t.forward(30)

def giu():
    t.setheading(-90)
    t.forward(30)

s.listen()

# collegamento tasto → funzione:
s.onkey(destra,   "Right")
s.onkey(sinistra, "Left")
s.onkey(su,       "Up")
s.onkey(giu,      "Down")

s.mainloop()

# struttura da ricordare:
# 1. definisci le funzioni (def ...)
# 2. chiama s.listen()
# 3. collega ogni tasto con s.onkey()
# 4. chiudi con s.mainloop()


# ------------------------------------------------------------
# 6. PENUP E PENDOWN CON I TASTI — disegno libero
# ------------------------------------------------------------

# possiamo collegare ai tasti anche le funzioni penup e pendown
# questo trasforma il programma in un vero strumento di disegno:
# si tiene premuto per disegnare, si alza il pennello per spostarsi

import turtle

t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()

def destra():
    t.setheading(0)
    t.forward(30)

def sinistra():
    t.setheading(180)
    t.forward(30)

def su():
    t.setheading(90)
    t.forward(30)

def giu():
    t.setheading(-90)
    t.forward(30)

def alza():
    t.penup()     # smette di disegnare

def abbassa():
    t.pendown()   # riprende a disegnare

def cancella():
    t.reset()     # cancella tutto e rimette la tartaruga al centro

s.listen()
s.onkey(destra,   "Right")
s.onkey(sinistra, "Left")
s.onkey(su,       "Up")
s.onkey(giu,      "Down")
s.onkey(alza,     "z")        # Z = alza pennello
s.onkey(abbassa,  "x")        # X = abbassa pennello
s.onkey(cancella, "space")    # spazio = cancella tutto

s.mainloop()


# ------------------------------------------------------------
# 7. PROGRAMMA COMPLETO — disegno con colori
# ------------------------------------------------------------

# aggiungiamo la possibilità di cambiare colore con i tasti r, g, b

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)        # movimento istantaneo per risposta fluida
s = turtle.Screen()

def destra():
    t.setheading(0)
    t.forward(20)

def sinistra():
    t.setheading(180)
    t.forward(20)

def su():
    t.setheading(90)
    t.forward(20)

def giu():
    t.setheading(-90)
    t.forward(20)

def alza():
    t.penup()

def abbassa():
    t.pendown()

def cancella():
    t.reset()
    t.speed(0)    # reset cancella anche le impostazioni: le rimettiamo

def rosso():
    t.color("red")

def verde():
    t.color("green")

def blu():
    t.color("blue")

s.listen()
s.onkey(destra,   "Right")
s.onkey(sinistra, "Left")
s.onkey(su,       "Up")
s.onkey(giu,      "Down")
s.onkey(alza,     "z")
s.onkey(abbassa,  "x")
s.onkey(cancella, "space")
s.onkey(rosso,    "r")
s.onkey(verde,    "g")
s.onkey(blu,      "b")

s.mainloop()


# ============================================================
# ESERCIZI
# ============================================================
# 1. Partendo dal programma del blocco 5 (frecce + mainloop),
#    aggiungi un tasto "c" che cambia il colore a "orange".
#    Suggerimento: definisci una funzione arancione() e
#    collegala con s.onkey(arancione, "c").
#
# 2. Aggiungi al programma completo del blocco 7 un tasto "n"
#    che cambia il colore a "black" (nero).
#    Poi aggiungi un tasto "+" che aumenta lo spessore del tratto
#    di 2 pixel ogni volta che viene premuto.
#    Suggerimento: usa t.pensize() per impostare lo spessore;
#    puoi leggere il valore attuale con t.pensize() senza argomenti
#    e poi impostarlo con t.pensize(valore + 2).
#
# 3. Crea un programma di disegno libero che abbia:
#    - frecce per muoversi
#    - z/x per alzare/abbassare il pennello
#    - spazio per cancellare
#    - tasti r, g, b, n per quattro colori
#    - tasti 1, 2, 3 per tre spessori di tratto (2, 5, 10 pixel)
#    Suggerimento: per i tasti numerici usa "1", "2", "3"
#    come stringa in s.onkey(), e in ogni funzione chiama
#    t.pensize() con il valore corrispondente.
# ============================================================
