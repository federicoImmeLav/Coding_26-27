# # output 
# print("ciao")

# # output di una stringa
# saluto = "ciao"
# print(saluto)

# # input stringa
# nome = input("Come ti chiami? ")

# # input è un numero devo mettere int o float (se con la virgola)
# eta = int(input("In che anno sei nato/a? "))

# # operazioni con i dati
# a = 5
# b = 10
# c = a + b
# print(c)

# # condizioni
# if a == 0:
#     print(a)
# elif a == 1:
#     print(b)
################################################################################
# # Crea programma che chiede nome, mese (in numeri) e anno di nascita
# # in base alla risposta e all'anno in cui siamo e al mese calcola l'età 
# # serve input e serve un if (se il mese è passato o meno)

# # imposto il mese e l'anno in cui siamo
# anno_corrente = 2026
# mese_corrente = 1 # in numero

# # tre input per le info che chiedo
# nome = input("Come ti chiami? ")
# anno_nascita = int(input("In che anno sei nato/a? "))
# mese_nascita = int(input("In che mese sei nato/a? (in numero) "))

# # calcolare l'eta in base all'anno
# eta = anno_corrente - anno_nascita

# # se a seconda del mese dimmi età giusta
# if mese_corrente < mese_nascita:
#     print(eta - 1)
# elif mese_corrente >= mese_nascita:
#     print(eta)

############################################################################

# Creo un programma che stampa i primi 50 numeri 
# però se il numero è pari, di fianco al numero mi scrive (: pari)
# per azione ripetuta un tot di volte si usa for

# range serve a dire quante volte si ripete l'azione
# se divido per 2 un numero pari, ottengo un numero intero
# senza resto (per calcolare il resto in py si usa %)
# for i in range(50):
#     if i % 2 == 0 and i % 3 == 0 : # se il numero diviso 2 da resto 0
#         print(f"{i}: è pari e divisibile per 3")
#     else:
#         print(i)
# mettendo and faccio una condizione che 
# è vera per due cose contemporaneamente
