# creare un programma che mi chiede tre voti
# le tre materie sono mate, ita, eng
# fa la media dei tre voti
# mi dice qual è la media dei tre voti 
# (totale dei numeri, diviso quanti numeri sono)
# a seconda del voto mi dice il giduzio
# meno di 6: insufficiente
# 6: sufficiente
# 7: bene
# 8: distinto
# 9: bravo
# 10: ottimo
mate = int(input("Che voto hai preso in matematica? ")) #int è solo per i numeri interi
ita = int(input("Che voto hai preso in italiano? "))
eng = int(input("Che voto hai preso in inglese? "))
media = (mate + ita + eng) / 3
# print(media)
# siccome faccio una divisione, ora media è un float
print(f"La media dei tuoi voti è {media}")
if media < 6:
    print("La tua media è Insufficiente")
elif 6 <= media < 7:
    print("La tua media è Sufficiente")
elif 7 <= media < 8:
    print("La tua media è Buona")
elif 8 <= media < 9:
    print("La tua media è Piuttosto Buona")
elif 9 <= media < 10:
    print("La tua media è il Top")
elif media == 10:
    print("Sei un Fenomeno")
