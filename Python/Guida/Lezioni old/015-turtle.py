# Libreria che si chiama turtle, serve a disegnare
# import turtle

# # carico la libreria nel comando t
# t = turtle.Turtle()

# # muovo la t avanti di 100
# t.forward(100)
# # giro a destra (il numero è l'angolo)
# t.right(90) 
# # dopo aver girato devo comunque andare avanti
# t.forward(100)

# t.left(120)
# t.forward(100)
# # la t può anche tornare indietro
# t.backward(200)

# turtle.done()

##########################################################################
# Programma che disegna un quadrato in due modi diversi

# import turtle
# t = turtle.Turtle()

# # ripeto 4 volte il comando avanti e a destra
# # t.forward(100)
# # t.right(90)

# # t.forward(100)
# # t.right(90)

# # t.forward(100)
# # t.right(90)

# # t.forward(100)
# # t.right(90)

# # c'è un comando per ripetere quante volte voglio una azione? 
# # posso ripetere quante volte voglio un comando con for
# # posso cambiare il colore, prima di disegnare
# t.color("blue")
# t.speed(10) # posso cambiare la velocità della turtle

# for i in range(4):
#     t.forward(100)
#     t.right(90)

# # per disegnare un altro quadrato devo spostarmi con la turtle
# t.left(120)
# # prima di spostare la turtle devo alzarla così non disegna
# t.penup()
# t.forward(200)

# # rigiro la turtle in orizzontale
# t.left(-120)
# # prima di disegnare devo appoggiare la turtle così che disegni
# t.pendown()

# t.color("purple")
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# turtle.done()

##############################################################################
# programma con cui utente iteragisce per disegnare
# colore = input("Di che colore vuoi il disegno? (in inglese) ")
# lunghezza = int(input("Di quanto è la lunghezza della riga? "))

# import turtle
# t = turtle.Turtle()

# # imposto il colore che ho scelto sopra
# t.color(colore)
# # imposto il comando per disegnare
# t.forward(lunghezza)

# turtle.done()
#############################################################################
# programma che mi chiede se voglio un quadrato o un triangolo, 
# poi mi chiede di che colore e poi disegna
# forma = input("Vuoi un quadrato o un triangolo? ")
# colore = input("Di che colore? ")

# import turtle
# t = turtle.Turtle()

# t.shape("turtle")

# t.forward(100)
# # comando per cambiare il colore
# t.color(colore)

# if forma == "quadrato":
#     for i in range(4):
#         t.forward(100)
#         t.right(90)

# elif forma == "triangolo":
#     for i in range(3): 
#         t.forward(100)
#         t.right(-120) # per fare il triangolo dobbiamo girarci di 180 - 60

# turtle.done()
