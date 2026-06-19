# succedono cose fino a quando tengo premuti i tasti ho bisogno
# di dizionari e booleane

# studente = {
#     "nome": "Mattia",
#     "anni": 16,
#     "promosso": False
# }

# # io posso cambiare le variabili booleane Vera e Falsa e viceversa
# print(studente)

# studente["promosso"] = True # cambio il valore di promosso
# print(studente)

# luci = {
#     "cucina": False,
#     "bagno": False,
#     "camera": False,
#     "piscina": False
# }

# print(luci["camera"])

# luci["camera"] = True
# print(luci["camera"])
###########################################################
# creo un programma che fa muovere la turtle
# finchè tengo premuti i tasti
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

s = turtle.Screen()
s.listen()

# creo il dizionario dei tasti
tasti = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}
# creo le funzioni che trasformano gli elementi 
# del dizionario tasti da False a True e viceversa 
def tasto_premuto(tasto):
    # prendo elemento che schiaccio e lo trasformo in True
    tasti[tasto] = True 

def tasto_alzato(tasto):
    tasti[tasto] = False

# comando che quando premo attiva la funzione tasto_premuto
s.onkeypress(lambda: tasto_premuto("w"), "w")
s.onkeypress(lambda: tasto_premuto("s"), "s")
s.onkeypress(lambda: tasto_premuto("a"), "a")
s.onkeypress(lambda: tasto_premuto("d"), "d")

# comando che attiva la funzione tasto_alzato
s.onkeyrelease(lambda: tasto_alzato("w"), "w")
s.onkeyrelease(lambda:tasto_alzato("s"), "s")
s.onkeyrelease(lambda:tasto_alzato("a"), "a")
s.onkeyrelease(lambda:tasto_alzato("d"), "d")

# creo la funzione per muovere la turte, finchè i tasti sono True
# la turtle si muove
def movimento():
    if tasti["w"]:
        t.setheading(90)
        t.forward(30)
    elif tasti["s"]:
        t.setheading(-90)
        t.forward(30)
    elif tasti["a"]:
        t.setheading(180)
        t.forward(30)
    elif tasti["d"]:
        t.setheading(0)
        t.forward(30)
    # lancio la funzione per sempre, ogni millisecondo
    s.ontimer(movimento, 1)

# devo chiamare la funzione
movimento()

s.mainloop()