import pygame
import random

# accendo pygame
pygame.init()

# creazione della schermata
larghezza = 600
altezza = 600
schermo = pygame.display.set_mode((larghezza,altezza))

# qui si definisco colori, dimensioni, posizioni, etc
# creo il bianco
bianco = (255,255,255)
# creo il rosso
rosso = (255, 0, 0)
blu = (0, 0, 255)

verde = (0,255,0)
viola = (138, 43, 226)
colori = [bianco, verde, viola]
colore_sfondo = random.choice(colori)

# definire le coordinate del quadrato
quad_x = 200
quad_y = 500
# definisco il lato del quadrato
lato = 50

# definisco coordinate del cerchio
cer_x = random.randint(10 , larghezza-50)
cer_y = 10
# raggio del cerchio
raggio = 20
# velocità del cerchio
cer_vel = 3

# imposto il clock per i tick del gioco
clock = pygame.time.Clock()

# creo il loop del gioco, che è un while che fa funzionare tutto
# fino a quando non si decide che deve spegnersi
gioco = True
while gioco: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
    # imposto il colore dello sfondo
    schermo.fill(colore_sfondo)

    # aumento la y del cerchio di cer_vel
    cer_y += cer_vel

    # imposto che pygame si accorge se io schiaccio un tasto
    # e sa che tasto sto schiacciando
    tasto = pygame.key.get_pressed()
    # se premo il tasto a sinistra si muove a sinistra
    if tasto[pygame.K_LEFT]:
        quad_x -= 10
    if tasto[pygame.K_RIGHT]:
        quad_x += 10

    # devo misurare la distanza tra cerchio e quadrato
    # distanza in orizzontale
    centro_x = quad_x + lato / 2
    centro_y = quad_y + lato / 2

    dx = abs(cer_x - centro_x) 
    dy = abs(cer_y - centro_y)

    if dx < 30 and dy < 30: 
        cer_x = random.randint(10 , larghezza-50)
        cer_y = 0
        colore_sfondo = random.choice(colori)

    # imposto che se arrivo al bordo inferiore il pallino torna su
    if cer_y > 580: 
        cer_x = random.randint(10 , larghezza-50)
        cer_y = 0

    # disegna il quadrato
    pygame.draw.rect(schermo, rosso, (quad_x, quad_y, lato,lato))
    # disegno il cerchi
    pygame.draw.circle(schermo, blu, (cer_x,cer_y), raggio)
    # aggiorno tutto quello che succede prima
    pygame.display.update()
    # imposto i tick del gioco al secondo
    clock.tick(60)

pygame.quit()