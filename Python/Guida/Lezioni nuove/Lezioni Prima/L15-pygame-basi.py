# ============================================================
# LEZIONE 15 — Pygame: schermata, game loop, disegno, tasti
# Unità 6 · Settimane 29-30
# ============================================================
# Prerequisiti: L14 (collisioni, punteggio, gioco completo in turtle)
# Obiettivo: lo studente sa aprire una finestra con Pygame,
# capisce la differenza tra event-driven e game loop,
# sa disegnare rettangoli e cerchi e muovere un oggetto con i tasti.
# ============================================================


# ------------------------------------------------------------
# 1. EVENT-DRIVEN vs GAME LOOP — il cambio concettuale
# ------------------------------------------------------------

# in turtle il programma ASPETTA che succeda qualcosa:
# non fa niente finché non premi un tasto o clicchi
# questo si chiama "event-driven" (guidato dagli eventi)

# in pygame il programma NON aspetta — gira in continuazione:
# ad ogni giro del while controlla tasti, aggiorna posizioni,
# ridisegna tutto — anche se non sta succedendo niente
# questo si chiama "game loop" (ciclo di gioco)

# analogia:
# event-driven = un cameriere che aspetta che qualcuno chiami
# game loop    = un cameriere che gira tra i tavoli ogni 5 secondi
#                a controllare se qualcuno ha bisogno di qualcosa

# la differenza pratica:
# turtle: onkey() registra una funzione → viene chiamata quando premi
# pygame: ogni frame chiede "quali tasti sono premuti ADESSO?"
#         e agisce subito — nessuna funzione registrata, tutto inline

# questo rende pygame più adatto ai giochi:
# il movimento è continuo (tasto tenuto premuto = si muove)
# in turtle invece ogni pressione è un evento separato


# ------------------------------------------------------------
# 2. SETUP MINIMO — le istruzioni che aprono e chiudono pygame
# ------------------------------------------------------------

# ogni programma pygame ha sempre questa struttura:

import pygame

pygame.init()                               # accende pygame

schermo = pygame.display.set_mode((800, 600))  # crea la finestra
pygame.display.set_caption("Il mio gioco")     # titolo della finestra

# il game loop: gira finché gioco è True
gioco = True
while gioco:

    # 1. EVENTI — controlla se l'utente vuole chiudere
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:      # click sulla X
            gioco = False

    # 2. LOGICA — (aggiornamenti, collisioni, punteggio)

    # 3. DISEGNO — (disegna tutto sullo schermo)

    pygame.display.update()                 # mostra il risultato

pygame.quit()                               # spegne pygame

# questa struttura non cambia mai:
# eventi → logica → disegno → update → ricomincia


# ------------------------------------------------------------
# 3. COLORI RGB — come funzionano i colori in pygame
# ------------------------------------------------------------

# in turtle si scriveva t.color("red")
# in pygame i colori sono tuple di tre numeri: (R, G, B)
# ogni valore va da 0 (assente) a 255 (massimo)

# R = rosso, G = verde, B = blu

BIANCO = (255, 255, 255)   # tutti al massimo = bianco
NERO   = (0,   0,   0)     # tutti a zero = nero
ROSSO  = (255, 0,   0)     # solo rosso
VERDE  = (0,   255, 0)
BLU    = (0,   0,   255)
GIALLO = (255, 255, 0)     # rosso + verde = giallo
GRIGIO = (128, 128, 128)   # valori uguali = grigio

# si usano variabili con nome in maiuscolo per convenzione:
# così è chiaro che sono costanti (non cambiano durante il gioco)

# nota: (255, 0, 0) = rosso puro, acceso
#       (100, 0, 0) = rosso scuro, spento


# ------------------------------------------------------------
# 4. SFONDO E AGGIORNAMENTO — perché servono ad ogni frame
# ------------------------------------------------------------

# ad ogni giro del game loop bisogna:
# 1. riempire lo schermo con il colore di sfondo (cancella il frame precedente)
# 2. disegnare tutti gli oggetti
# 3. chiamare pygame.display.update() per mostrare tutto

# se salti schermo.fill(), i vecchi disegni rimangono
# e gli oggetti lasciano una scia mentre si muovono

import pygame

pygame.init()
schermo = pygame.display.set_mode((800, 600))
BIANCO = (255, 255, 255)

gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    schermo.fill(BIANCO)        # cancella il frame precedente — primo!

    # qui si disegnano gli oggetti

    pygame.display.update()     # mostra il frame — ultimo!

pygame.quit()


# ------------------------------------------------------------
# 5. DISEGNARE FORME — rect e circle
# ------------------------------------------------------------

# pygame.draw.rect(schermo, colore, (x, y, larghezza, altezza))
# pygame.draw.circle(schermo, colore, (centro_x, centro_y), raggio)

# nota: in pygame y=0 è in ALTO — aumentando y si scende
# è il contrario di turtle (dove y=0 è al centro e sale verso l'alto)

import pygame

pygame.init()
schermo = pygame.display.set_mode((800, 600))
BIANCO = (255, 255, 255)
ROSSO  = (255, 0, 0)
BLU    = (0, 0, 255)
VERDE  = (0, 255, 0)

gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    schermo.fill(BIANCO)

    # rettangolo rosso: angolo in alto a sinistra (100, 200), 80×50 pixel
    pygame.draw.rect(schermo, ROSSO, (100, 200, 80, 50))

    # cerchio blu: centro (400, 300), raggio 40
    pygame.draw.circle(schermo, BLU, (400, 300), 40)

    # rettangolo verde più piccolo
    pygame.draw.rect(schermo, VERDE, (600, 100, 30, 30))

    pygame.display.update()

pygame.quit()


# ------------------------------------------------------------
# 6. TASTI E MOVIMENTO — key.get_pressed() ogni frame
# ------------------------------------------------------------

# pygame.key.get_pressed() restituisce lo stato di TUTTI i tasti
# in quel preciso istante — True se premuto, False se no
# chiamato ad ogni frame, rileva il tasto tenuto premuto in modo fluido

import pygame

pygame.init()
schermo = pygame.display.set_mode((800, 600))
BIANCO = (255, 255, 255)
ROSSO  = (255, 0, 0)

# posizione del quadrato — inizia al centro
quad_x = 380
quad_y = 280
lato   = 40
vel    = 4   # pixel per frame

gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    # leggi i tasti premuti in questo frame
    tasto = pygame.key.get_pressed()

    if tasto[pygame.K_RIGHT]:
        quad_x += vel
    if tasto[pygame.K_LEFT]:
        quad_x -= vel
    if tasto[pygame.K_UP]:
        quad_y -= vel    # in pygame su = y decresce
    if tasto[pygame.K_DOWN]:
        quad_y += vel

    schermo.fill(BIANCO)
    pygame.draw.rect(schermo, ROSSO, (quad_x, quad_y, lato, lato))
    pygame.display.update()

pygame.quit()

# il quadrato esce dallo schermo perché non ci sono limiti —
# il blocco successivo (L16) introduce il clock e i confini


# ============================================================
# ESERCIZI
# ============================================================
# 1. Modifica il programma del blocco 6 in modo che il quadrato
#    sia di colore BLU e si muova con i tasti WASD invece
#    delle frecce.
#    Suggerimento: i codici tasto sono K_w, K_a, K_s, K_d.
#
# 2. Aggiungi al programma del blocco 5 un secondo cerchio
#    di colore arancione (255, 165, 0) posizionato a (200, 150)
#    con raggio 25. Lo sfondo deve essere NERO.
#
# 3. Partendo dal blocco 6, aggiungi un cerchio fisso al centro
#    dello schermo (400, 300) di raggio 20.
#    Il quadrato si muove normalmente con le frecce.
#    Quando il quadrato raggiunge il bordo destro (x > 760),
#    riportalo a x = 0 (esce da destra, rientra da sinistra).
#    Fai lo stesso per il bordo sinistro (x < 0 → x = 760).
# ============================================================
