import turtle
import random
import time

# schermata
s = turtle.Screen()
s.listen()

# turtle per la scritta
testo = turtle.Turtle()
testo.penup()
testo.hideturtle()
testo.goto(0,-250)
testo.write("Clicca sui bersagli nel minor tempo possibile", font=("Arial", 20), align="center")

# creo il punteggio
punti = 0
punteggio = turtle.Turtle()
punteggio.hideturtle()
punteggio.penup()
punteggio.goto(-250,280)
punteggio.write(f"Punti: {punti}", font=("Arial", 20), align="center")

# creo la scritta del tempo
tempo = 10
cronometro = turtle.Turtle()
cronometro.hideturtle()
cronometro.penup()
cronometro.goto(250,280)
cronometro.write(f"Timer: {tempo}", font=("Arial", 20), align="center")

# creo il bersaglio
bers = turtle.Turtle()
bers.penup()
bers.shape("circle")
bers.color("red")
bers.shapesize(2)

# funzione che legge le coordinate
def coordinate(x,y):
    global punti
    # print(f"Coordinate: {x} e {y}")
    # controllare che le coordinate x e y siano vicine
    # al bersaglio
    if bers.xcor() - 20 < x < bers.xcor() + 20 and bers.ycor() - 20 < y < bers.ycor() + 20:
        print("Vicino")
        # aggiorno il punteggio
        punti += 1
        punteggio.clear()
        punteggio.write(f"Punti: {punti}", font=("Arial", 20), align="center")
        # faccio andare il bersaglio in un posto random
        a = random.randint(-240, 240)
        b = random.randint(-240, 240)
        bers.teleport(a,b)
    else:
        print("lontano")
 
# funzione che diminuisce il timer di 1 ogni secondo
def aggiorna_timer():
    global tempo
    if tempo > 0:
        tempo -= 1
        cronometro.clear()
        cronometro.write(f"Timer: {tempo}", font=("Arial", 20), align="center")
    else:
        stop()
    s.ontimer(aggiorna_timer, 1000)

# creo la funzione stop
def stop():
    bers.hideturtle()
    cronometro.clear()
    testo.clear()
    punteggio.clear()
    testo.teleport(0,0)
    testo.write(f"Tempo scaduto! Hai fatto {punti} punti", font=("Arial",20), align="center")


aggiorna_timer()
s.onscreenclick(coordinate)

# schermata sempre aperta
s.mainloop()

