# Importo la libreria di python per fare i disegni
import matplotlib.pyplot as plt
# # prima dico le variabili e poi le inserisco nel comando che disegna
# x = 2
# y = 3
# #  scatter disegni i punti alle coordinate che diciamo noi
# plt.scatter(x,y)
# #  per disegnare gli assi si usa:
# plt.axhline(0, color = "red") # per asse x orizzontale
# plt.axvline(0, color = "green") # per asse y verticale
# # color ci permette di cambiare il colore della linea
# # aggiungere la griglia per capire meglio il grafico
# plt.grid()
# #  show fa comparire il disegno
# plt.show()

############################################################################################à
# esempio in cui python chiede all'utente dove vuole disegnare il punto

# x = int(input("Dimmi la coordinata x del punto: "))
# y = int(input("Dimmi la coordinata y del punto: "))

# x2 = int(input("Dimmi la x di un altro punto: "))
# y2 = int(input("Dimmi la y di un altro punto: "))

# plt.scatter(x,y)
# plt.scatter(x2,y2)

# plt.axhline(0, color = "red")
# plt.axvline(0, color = "red")

# plt.grid()
# plt.show()

###########################################################################################
# esempio in cui disegno 5 punti diversi
# per disegnare tanti punti con poco codice posso usare le liste
# x = [1, -5, 12, -3, 7]
# y = [-3, 3, 4, -7, 2]

# plt.scatter(x,y)
# plt.axhline(0, color = "red")
# plt.axvline(0, color = "red")

# plt.grid()
# plt.show()

#####################################################################
# programma che conta fino a 5
for i in range(6):
    plt.scatter(i,i)
# con due i va in diagonale perchè aumentano sia x che y
plt.axhline(0, color = "red")
plt.axvline(0, color = "red")

plt.grid()
plt.show()

