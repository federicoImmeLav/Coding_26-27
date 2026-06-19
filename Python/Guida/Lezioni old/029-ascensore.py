import turtle

s = turtle.Screen()
s.listen()

# creo 3 variabili che comandando l'ascensore
PIANO_MIN = 0
PIANO_MAX = 2
ALTEZZA_PIANO = 150

# creo turtle della cabina dell'ascensore
cabina = turtle.Turtle()
cabina.shape("square")
cabina.color("steelblue")
cabina.shapesize(4,4)
cabina.penup()

# creo la turtle che andrà a disegnare le linee dei piani
disegno = turtle.Turtle()
disegno.hideturtle()
disegno.pensize(2)
disegno.color("lightgray")
disegno.speed(0)

# creo la turtle che scrive i numeri del piano
numeri = turtle.Turtle()
numeri.hideturtle()
numeri.penup()

# disegno la riga del piano 0
disegno.penup()
disegno.teleport(-300,0)
disegno.pendown()
disegno.goto(300,0)
numeri.goto(-260, -20)
numeri.write("0", align="center", font=("Arial", 48, "normal"))

# piano 1
disegno.penup()
disegno.teleport(-300,150)
disegno.pendown()
disegno.goto(300,150)
numeri.goto(-260, 130)
numeri.write("1", align="center", font=("Arial", 48, "normal"))


# piano 2
disegno.penup()
disegno.teleport(-300,300)
disegno.pendown()
disegno.goto(300,300)
numeri.goto(-260, 280)
numeri.write("2", align="center", font=("Arial", 48, "normal"))


# creo la funzione che sposta l'ascensore da sola
# in base al piano che seleziono

piano = 0
def aggiorna():
    cabina.goto(0, piano * ALTEZZA_PIANO)

aggiorna()

# creo la funzione che fa salire ascensore
def sali():
    global piano
    if piano < PIANO_MAX:
        piano += 1
        aggiorna()
    else:
        print("piano massimo")

def scendi():
    global piano
    if piano > PIANO_MIN:
        piano -= 1
        aggiorna()
    else:
        print("piano minimo")


# creo funzione che imposta piano 2
def vai_a_due():
    global piano
    piano = 2
    aggiorna()

def vai_a_uno():
    global piano
    piano = 1
    aggiorna()

def vai_a_zero():
    global piano
    piano = 0
    aggiorna()

s.onkey(sali, "Up")
s.onkey(scendi, "Down")
s.onkey(vai_a_due, "2")
s.onkey(vai_a_uno, "1")
s.onkey(vai_a_zero, "0")
s.mainloop()