import turtle
import time
import random

# creo la schermata
s = turtle.Screen()

# creo il semaforo rosso 
semaforo = turtle.Turtle()
semaforo.color("red")
semaforo.shape("circle")
semaforo.shapesize(5)
semaforo.hideturtle()

# creo la scritta
testo = turtle.Turtle()
testo.hideturtle()
testo.penup()
testo.goto(0,150)
testo.write("Premi SPAZIO per iniziare", font=("Arial", 20), align="center")

tempo_inizio = 0

# creo la funz che aspetta un tempo casuale
# e poi accende il semaforo
def start():
    attesa = random.randint(1000, 5000)
    testo.clear()
    testo.write("Aspetta la luce...", font=("Arial", 20), align="center")
    s.ontimer(semaforo_on, attesa)

# creo la funz che fa apparire il semaforo quando premo SPAZIO
def semaforo_on():
    global tempo_inizio
    semaforo.showturtle()
    # salvo il tempo di inizio
    tempo_inizio = time.time()
    s.onkey(stop, "space")

# creo la funz che spegne il semaforo, salva l'ora 
# e mi dice quanto tempo ci ho messo a reagire
def stop():
    semaforo.hideturtle()
    tempo_fine = time.time()
    reazione = (tempo_fine - tempo_inizio) * 1000
    testo.clear()
    testo.write(f"Reazione: {int(reazione)} ms", font=("Arial", 20), align="center")
    s.onkey(start, "space")

# quando premo il tasto
s.listen()
s.onkey(start, "space")

# tengo la finestra aperta
s.mainloop()