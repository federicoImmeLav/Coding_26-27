import turtle
import time 

# creo la schermata di gioco
s = turtle.Screen()

# creo il primo cerchio del semaforo
t1 = turtle.Turtle()
t1.shape("circle")
t1.shapesize(5)
t1.color("gray")
t1.teleport(0, 150)

t2 = turtle.Turtle()
t2.shape("circle")
t2.shapesize(5)
t2.color("gray")
t2.teleport(0, 0)

t3 = turtle.Turtle()
t3.shape("circle")
t3.shapesize(5)
t3.color("gray")
t3.teleport(0, -150)

# creo lo stato iniziale
stato = "spento"

# creo la funz semaforo
def semaforo():
    global stato
    # faccio dipendere il colore dallo stato in cui siamo
    if stato == "spento" or stato == "giallo":
        t1.color("red")
        t2.color("gray")
        stato = "rosso"

    elif stato == "rosso":
        t3.color("green")
        t1.color("gray")
        t1.color("gray")
        stato = "verde"

    elif stato == "verde":
        t3.color("gray")
        t2.color("orange")
        stato = "giallo"

def errore():
    global stato
    t1.color("gray")
    t3.color("gray")
    stato = "404"
    while stato == "404":
        t2.color("gray")
        time.sleep(0.2)
        t2.color("orange")
        time.sleep(0.2)

def reset():
    global stato
    t2.color("gray")
    stato = "spento"

# imposto barra spaziatrice come comando che fa iniziare qualcosa
s.listen()
s.onkey(semaforo, "space")
s.onkey(errore, "a")
s.onkey(reset, "r")

s.mainloop()
