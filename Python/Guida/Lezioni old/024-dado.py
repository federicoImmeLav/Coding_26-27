import random
import turtle

# schermata
s = turtle.Screen()
s.listen()

# turtle per quadrato intorno
bordo = turtle.Turtle()
bordo.hideturtle()
bordo.teleport(150,150)
bordo.pensize(2)
for i in range(4):
    bordo.right(90)
    bordo.forward(300)

# scritta di indicazioni
testo = turtle.Turtle()
testo.hideturtle()
testo.teleport(0,200)
testo.write("Premi SPAZIO per tirare il dado", font=("Arial", 20), align="center")

colore = "gray"
# creo i pallini
c1 = turtle.Turtle()
c1.penup()
c1.shape("circle")
c1.shapesize(3)
c1.color(colore)

c2 = turtle.Turtle()
c2.penup()
c2.shape("circle")
c2.shapesize(3)
c2.color(colore)
c2.goto(100, 0)

c3 = turtle.Turtle()
c3.penup()
c3.shape("circle")
c3.shapesize(3)
c3.color(colore)
c3.goto(-100, 0)

c4 = turtle.Turtle()
c4.penup()
c4.shape("circle")
c4.shapesize(3)
c4.color(colore)
c4.goto(100, 100)

c5 = turtle.Turtle()
c5.penup()
c5.shape("circle")
c5.shapesize(3)
c5.color(colore)
c5.goto(100, -100)

c6 = turtle.Turtle()
c6.penup()
c6.shape("circle")
c6.shapesize(3)
c6.color(colore)
c6.goto(-100, 100)

c7 = turtle.Turtle()
c7.penup()
c7.shape("circle")
c7.shapesize(3)
c7.color(colore)
c7.goto(-100, -100)

c8 = turtle.Turtle()
c8.penup()
c8.shape("circle")
c8.shapesize(3)
c8.color(colore)
c8.goto(0, -100)

c9 = turtle.Turtle()
c9.penup()
c9.shape("circle")
c9.shapesize(3)
c9.color(colore)
c9.goto(0, 100)

# creo funzione che spegne tutto
colore = "white"
def spegni():
    c1.color(colore)
    c2.color(colore)
    c3.color(colore)
    c4.color(colore)
    c5.color(colore)
    c6.color(colore)
    c7.color(colore)
    c8.color(colore)
    c9.color(colore)

# funzioni che accendono i pallini
def acc1():
    c1.color("red")

def acc2():
    c5.color("red")
    c6.color("red")

def acc3():
    acc1()
    acc2()

def acc4():
    acc2()
    c4.color("red")
    c7.color("red")

def acc5():
    acc4()
    acc1()

def acc6():
    acc4()
    c2.color("red")
    c3.color("red")

# funzione che accende a caso i pallini
def dado():
    spegni()
    n = random.randint(1,6)
    if n == 1:
        acc1()
    if n == 2:
        acc2()
    if n == 3:
        acc3()
    if n == 4:
        acc4()
    if n == 5:
        acc5()
    if n == 6:
        acc6()
# se clicco spazio si accende dado
s.onkey(dado, "space")

s.mainloop()
