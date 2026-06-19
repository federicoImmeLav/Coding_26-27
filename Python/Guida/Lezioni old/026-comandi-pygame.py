import pygame

# comando che fa partire pygame
pygame.init()

# creo la schermata di gioco
# 800 e 600 è la dimensione in pixel della schermata
schermo = pygame.display.set_mode((800,600))

# imposto le caratteristiche del quadrato rosso
rosso = (255,0,0) # codice RGB
bianco = (255,255,255)
lato = 40
# coordinate x e y del quadrato
quad_x = 0
quad_y = 0

# tutto quello che succede nel mio gioco starà dentro
# a un grande while che si ripete all'infinito fino a quando
# non lo stoppo
# creo una variabile "gioco" e la metto True, fino a quando la variabile
# è True il gioco va avanti, per fermare il gioco deve diventare False
gioco = True
while gioco:
    # controllo che se clicco sulla x del programma, il mio gioco si chiude
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # se clicco sulla x 
            gioco = False # il gioco si stoppa
    
    # sfondo colorato
    schermo.fill(bianco)

    # dico a pygame di controllare che premo i tasti
    tasto = pygame.key.get_pressed()

    # se premo tasto a dx aumenta quad_x
    if tasto[pygame.K_RIGHT]:
        quad_x += 1
    if tasto[pygame.K_LEFT]:
        quad_x -= 1
    if tasto[pygame.K_UP]:
        quad_y -= 1
    if tasto[pygame.K_DOWN]:
        quad_y += 1   

    # disegno un quadrato usando le caratteristiche dette sopra
    pygame.draw.rect(schermo, rosso, (quad_x,quad_y, lato, lato))

    # comando che aggiorna tutto
    pygame.display.update()

# alla fine pygame smette di funzionare
pygame.quit()