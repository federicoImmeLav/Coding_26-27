import time
import turtle

s = turtle.Screen()
s.listen()

# testo è la scritta di istruzioni
testo = turtle.Turtle()
testo.hideturtle()
testo.penup()
testo.goto(0,150)
testo.write("Premi SPAZIO per avviare il cronometro", font=("Arial", 20), align="center")

# creo turtle del cronometro (che scrive i numeri)
tempo = 0
crono = turtle.Turtle()
crono.hideturtle()
crono.penup()
crono.write(tempo, font=("Arial", 20), align="center")

tempo_inizio = 0
# funzione che inizia a contare il tempo
def start_tempo(): 
    global tempo_inizio
    tempo_inizio = time.time()
    tempo_scorre()

# comando che fa partire il tempo
def start():
    start_tempo()

# creo una funz che misura il tempo che passa e mi scrive al posto
# dello 0 i secondi che vanno avanti
def tempo_scorre():
    global tempo_inizio, tempo
    tempo_fine = time.time()
    tempo = tempo_fine - tempo_inizio
    crono.clear()
    crono.write(f"{tempo:.2f}", font=("Arial", 20), align="center")
    s.ontimer(tempo_scorre, 100)

# se premo spazio parte start()
s.onkey(start, "space")

s.mainloop()