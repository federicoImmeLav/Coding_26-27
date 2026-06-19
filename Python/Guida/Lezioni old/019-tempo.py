# importo il tempo
import time

# time.time() ci da i secondi che sono passati dal
#  1 gennaio 1970
# tempo = time.time()
# print(tempo)

# creo un programma che mi chiede 
# come mi chiamo, quanti anni ho, dove sono nato
# salva questa informazioni in una lista
# alla fine mi dice quanto tempo ci ho messo a farlo
# creo la lista
info = []

# salvo il tempo iniziale
tempo_iniziale = time.time()

# chiedo il nome
nome = input("Come ti chiami? ")
# metto il nome nella lista
info.append(nome)
anni = int(input("Quanti anni hai? "))
info.append(anni)
nascita = input("Dove sei nato? ")
info.append(nascita)
print(info)

# salvo il tempo finale
tempo_finale = time.time()

# calcolo il tempo che ci ho messo a fare tutto
tempo_trascorso = tempo_finale - tempo_iniziale

# stampo il tempo trascorso
print(f"Per fare il form ci hai messo {int(tempo_trascorso)} secondi")

