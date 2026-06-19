# importare turtle
import turtle

# creare la turtle
t = turtle.Turtle()
t.shape("turtle")

# creare la schermata di gioco
s = turtle.Screen()

# tutto il codice che riguarda la turtle va messo qui, 
# prima di s.mainloop()

# t.forward(100) va avanti
# t.setheading(-90) punta nell'angolo che scrivo nella parentesi

# devo impostare il programma in modo tale che si aspetti
# che io prema i tasti
s.listen()

# creare le funzioni che muovo la turtle 
# per muoverla a dx
def destra():
    t.setheading(0) # punto in direzione destra
    t.forward(30) # vado avanti di 30

# per andare a sx
def sinistra():
    t.setheading(180)
    t.forward(30)

# per andare su
def su():
    t.setheading(90)
    t.forward(30)

# per andare giù
def giu():
    t.setheading(-90)
    t.forward(30)

# creo la funzione reset del disegno
def reset():
    t.reset()

# funzione per non disegnare 
def penup():
    t.penup()

# funzione per disegnare
def pendown():
    t.pendown()

# devo collegare che quando schiaccio il tasto freccia destra
# si accende la funzione destra()
s.onkey(destra, "Right")
s.onkey(sinistra, "Left")
s.onkey(su, "Up")
s.onkey(giu, "Down")
s.onkey(reset, "space")
s.onkey(penup, "z")
s.onkey(pendown, "x")

# schermata sempre aperta che sta alla fine del codice
s.mainloop()