import turtle
import random # comandi a caso

turtle.tracer(0) # rendo il gioco più fluido

# creo la schermata
s = turtle.Screen()
s.listen()

# creo il personaggio
personaggio = turtle.Turtle()
personaggio.shape("square")
personaggio.color("green")
personaggio.penup() # evito di disegnare

# creo la mela
mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()
mela.goto(0,100)

# creo il punteggio
punteggio = 0 # creo variabile del punteggio
punti = turtle.Turtle()
punti.hideturtle() # nascondo la turtle
punti.penup()
punti.goto(0,280) # posiziono in alto
punti.write(f"Punteggio: {punteggio}", align = "center")

# creo turtle per quadrato
quadrato = turtle.Turtle()
quadrato.hideturtle()
quadrato.color("purple")
quadrato.penup()
quadrato.goto(300,300)
quadrato.pendown()
quadrato.goto(300,-300)
quadrato.goto(-300,-300)
quadrato.goto(-300,300)
quadrato.goto(300,300)

# creo il dizionario dei tasti
tasti = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

# funzioni per mettere i tasti True e False
def tasto_premuto(tasto):
    tasti[tasto] = True

def tasto_alzato(tasto):
    tasti[tasto] = False

# associo i tasti premuti e rilasciati alle rispettive funzioni
s.onkeypress(lambda: tasto_premuto("w"), "w")
s.onkeypress(lambda: tasto_premuto("a"), "a")
s.onkeypress(lambda: tasto_premuto("s"), "s")
s.onkeypress(lambda: tasto_premuto("d"), "d")

s.onkeyrelease(lambda: tasto_alzato("w"), "w")
s.onkeyrelease(lambda: tasto_alzato("a"), "a")
s.onkeyrelease(lambda: tasto_alzato("s"), "s")
s.onkeyrelease(lambda: tasto_alzato("d"), "d")

def movimento():
    # dico alla funzione di usare la variabile
    # punteggio che sta fuori
    global punteggio
    if tasti["w"]:
        personaggio.setheading(90)
        personaggio.forward(10)
    elif tasti["s"]:
        personaggio.setheading(-90)
        personaggio.forward(10)
    elif tasti["a"]:
        personaggio.setheading(180)
        personaggio.forward(10)
    elif tasti["d"]:
        personaggio.setheading(0)
        personaggio.forward(10)

    # aggiungo un if nel quale controllo quanto sono distanti
    # mela e personaggio
    if personaggio.distance(mela) < 20:
        # diciamo alla mela di andare in un posto
        # casuale sia per x che per y 
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        mela.goto(x, y)
        # aggiorno il punteggio e vado a riscrivere
        # il numero nuovo
        punteggio += 1 # comando che aumenta di 1
        punti.clear() # cancello il punteggio di prima
        punti.write(f"Punteggio: {punteggio}", align = "center")
    if punteggio >= 5:
        personaggio.color("blue")
    if punteggio >= 10:
        personaggio.shape("triangle")

    # controllo che la x del personaggio non superi 300
    if personaggio.xcor() > 300:
        personaggio.setx(290) # riporto la x al valore 290
        punteggio -= 1
        punti.clear() # cancello il punteggio di prima
        punti.write(f"Punteggio: {punteggio}", align = "center")
    # controllo anche verso sinistra con -300
    elif personaggio.xcor() < -300:
        personaggio.setx(-290)
        punteggio -= 1
        punti.clear() # cancello il punteggio di prima
        punti.write(f"Punteggio: {punteggio}", align = "center")

    if personaggio.ycor() > 300:
        personaggio.sety(290)
        punteggio -= 1
        punti.clear() # cancello il punteggio di prima
        punti.write(f"Punteggio: {punteggio}", align = "center")

    elif personaggio.ycor() < -300:
        personaggio.sety(-290)
        punteggio -= 1
        punti.clear() # cancello il punteggio di prima
        punti.write(f"Punteggio: {punteggio}", align = "center")
    


    turtle.update() # aggiorna la schermata ad ogni ciclo
    s.ontimer(movimento,10)

movimento()
# tengo la schermata aperta

s.mainloop()