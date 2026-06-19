import pygame

# comando che fa partire pygame
pygame.init()

# creo la schermata di gioco
# 800 e 600 è la dimensione in pixel della schermata
schermo = pygame.display.set_mode((800,600))


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

    # comando che aggiorna tutto
    pygame.display.update()

# alla fine pygame smette di funzionare
pygame.quit()