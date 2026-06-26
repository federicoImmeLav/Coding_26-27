# ============================================================
# LEZIONE 16 — Pygame: clock, FPS, collisioni e testo
# Unità 6 · Settimane 31-32
# ============================================================
# Prerequisiti: L15 (setup pygame, game loop, draw, tasti)
# Obiettivo: lo studente sa usare il clock per controllare
# la velocità del gioco, rilevare collisioni manuali,
# scrivere testo sullo schermo e costruire un gioco con
# un oggetto che cade e un punteggio.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA SENZA CLOCK — velocità fuori controllo
# ------------------------------------------------------------

# senza un limite, il game loop gira il più veloce possibile:
# su un computer veloce fa 2000 giri al secondo,
# su uno lento ne fa 200 — il gioco è incomparabile tra macchine diverse

# se la velocità del quadrato è 5 pixel per frame:
# - computer veloce: 2000 × 5 = 10.000 pixel al secondo
# - computer lento:   200 × 5 =  1.000 pixel al secondo

# la soluzione: limitare il numero di frame al secondo (FPS)
# con un clock che "rallenta" i frame in eccesso


# ------------------------------------------------------------
# 2. CLOCK E FPS — controllare la velocità del gioco
# ------------------------------------------------------------

# pygame.time.Clock() crea un orologio
# clock.tick(60) dice: "aspetta quanto basta per non superare 60 fps"
# a 60 fps ogni frame dura circa 16ms — uguale su tutti i computer

import pygame

pygame.init()
schermo = pygame.display.set_mode((800, 600))
BIANCO = (255, 255, 255)
ROSSO  = (255, 0, 0)

clock = pygame.time.Clock()   # crea l'orologio — va fatto UNA VOLTA fuori dal loop

quad_x = 380
quad_y = 280
lato   = 40
vel    = 5

gioco = True
while gioco:
    clock.tick(60)   # limita a 60 frame al secondo — va chiamato UNA VOLTA per frame

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    tasto = pygame.key.get_pressed()
    if tasto[pygame.K_RIGHT]: quad_x += vel
    if tasto[pygame.K_LEFT]:  quad_x -= vel
    if tasto[pygame.K_UP]:    quad_y -= vel
    if tasto[pygame.K_DOWN]:  quad_y += vel

    schermo.fill(BIANCO)
    pygame.draw.rect(schermo, ROSSO, (quad_x, quad_y, lato, lato))
    pygame.display.update()

pygame.quit()

# convenzione: metti clock.tick() come PRIMA riga del loop
# così il limite si applica sempre, prima di qualsiasi calcolo


# ------------------------------------------------------------
# 3. CONFINI DELLO SCHERMO — rimbalzare o riapparire
# ------------------------------------------------------------

# ci sono due modi per gestire un oggetto che esce dallo schermo:
# a) bloccarlo al bordo (non può uscire)
# b) farlo riapparire dall'altro lato

# modo a — blocco al bordo
largezza = 800
altezza  = 600

# dopo aver aggiornato quad_x e quad_y:
# if quad_x < 0:              quad_x = 0
# if quad_x > largezza - lato: quad_x = largezza - lato
# if quad_y < 0:              quad_y = 0
# if quad_y > altezza - lato:  quad_y = altezza - lato

# modo b — riapparire dall'altro lato (wraparound)
# if quad_x > largezza:  quad_x = 0
# if quad_x < 0:         quad_x = largezza
# if quad_y > altezza:   quad_y = 0
# if quad_y < 0:         quad_y = altezza


# ------------------------------------------------------------
# 4. OGGETTO CHE CADE — aggiornare la posizione ogni frame
# ------------------------------------------------------------

# per fare cadere un oggetto, basta aumentare la sua y ogni frame
# (in pygame y cresce verso il basso)
# quando esce dal fondo, lo riportiamo in alto in posizione casuale

import pygame
import random

pygame.init()
LARGHEZZA = 600
ALTEZZA   = 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
BIANCO = (255, 255, 255)
BLU    = (0, 0, 255)

clock = pygame.time.Clock()

# cerchio che cade
cer_x   = random.randint(20, LARGHEZZA - 20)
cer_y   = 0
raggio  = 20
vel_cad = 4   # pixel per frame verso il basso

gioco = True
while gioco:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    # il cerchio scende di vel_cad pixel ogni frame
    cer_y += vel_cad

    # quando esce dal fondo, riparte dall'alto in posizione casuale
    if cer_y > ALTEZZA + raggio:
        cer_y = -raggio
        cer_x = random.randint(raggio, LARGHEZZA - raggio)

    schermo.fill(BIANCO)
    pygame.draw.circle(schermo, BLU, (cer_x, cer_y), raggio)
    pygame.display.update()

pygame.quit()


# ------------------------------------------------------------
# 5. COLLISIONE MANUALE — distanza tra rettangolo e cerchio
# ------------------------------------------------------------

# in pygame non c'è distance() come in turtle
# si calcola la distanza tra i centri degli oggetti a mano:
# dx = distanza orizzontale tra i centri
# dy = distanza verticale tra i centri
# se dx < soglia AND dy < soglia → collisione!

# centro del quadrato (larghezza / 2 dall'angolo in alto a sinistra):
# centro_x = quad_x + lato / 2
# centro_y = quad_y + lato / 2

# distanza dal cerchio:
# dx = abs(cer_x - centro_x)
# dy = abs(cer_y - centro_y)

# se dx < 30 and dy < 30: → collisione!
# la soglia (30) dipende dalla dimensione degli oggetti

# perché abs()? perché la distanza è sempre positiva:
# se il cerchio è a sinistra del quadrato, dx sarebbe negativo senza abs


# ------------------------------------------------------------
# 6. TESTO SULLO SCHERMO — pygame.font
# ------------------------------------------------------------

# per scrivere testo in pygame servono tre passi:
# 1. creare un oggetto font (stile + dimensione)
# 2. renderizzare il testo in una superficie (immagine)
# 3. disegnare quella superficie sullo schermo con blit()

import pygame

pygame.init()
schermo = pygame.display.set_mode((800, 600))
BIANCO = (255, 255, 255)
NERO   = (0, 0, 0)
ROSSO  = (255, 0, 0)

# passo 1: crea il font — None = font di sistema, 36 = dimensione
font_grande = pygame.font.Font(None, 72)
font_medio  = pygame.font.Font(None, 36)

punteggio = 0

gioco = True
while gioco:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            punteggio += 1

    schermo.fill(BIANCO)

    # passo 2: renderizza il testo
    # font.render(testo, antialias, colore_testo)
    testo_punti = font_medio.render(f"Punti: {punteggio}", True, NERO)
    testo_titolo = font_grande.render("GIOCO", True, ROSSO)

    # passo 3: disegna la superficie sullo schermo
    # blit(superficie, (x, y)) — dove (x,y) è l'angolo in alto a sinistra del testo
    schermo.blit(testo_titolo, (300, 50))
    schermo.blit(testo_punti,  (10, 10))

    pygame.display.update()

pygame.quit()


# ------------------------------------------------------------
# 7. GIOCO COMPLETO — acchiappa il cerchio
# ------------------------------------------------------------

# costruiamo il gioco completo: un quadrato controllato con le frecce,
# un cerchio che cade, punteggio se lo prendi, vita persa se cade a terra

import pygame
import random

pygame.init()
LARGHEZZA = 600
ALTEZZA   = 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Acchiappa il cerchio")

BIANCO = (255, 255, 255)
ROSSO  = (255, 0, 0)
BLU    = (0, 100, 255)
NERO   = (0, 0, 0)
VERDE  = (0, 200, 0)

clock = pygame.time.Clock()
font  = pygame.font.Font(None, 36)

# --- giocatore ---
g_x   = LARGHEZZA // 2 - 25
g_y   = ALTEZZA - 60
g_l   = 50
g_vel = 6

# --- cerchio ---
c_x   = random.randint(20, LARGHEZZA - 20)
c_y   = 0
c_r   = 20
c_vel = 4

# --- stato ---
punteggio = 0
vite      = 3

gioco = True
while gioco:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gioco = False

    # movimento giocatore
    tasto = pygame.key.get_pressed()
    if tasto[pygame.K_LEFT]  and g_x > 0:            g_x -= g_vel
    if tasto[pygame.K_RIGHT] and g_x < LARGHEZZA - g_l: g_x += g_vel

    # cerchio che cade
    c_y += c_vel

    # collisione giocatore/cerchio
    centro_x = g_x + g_l // 2
    centro_y = g_y + g_l // 2
    if abs(c_x - centro_x) < 35 and abs(c_y - centro_y) < 35:
        punteggio += 1
        c_vel += 0.5   # ogni raccolta, il cerchio va un po' più veloce
        c_x = random.randint(c_r, LARGHEZZA - c_r)
        c_y = -c_r

    # cerchio arriva a terra
    if c_y > ALTEZZA + c_r:
        vite -= 1
        c_x = random.randint(c_r, LARGHEZZA - c_r)
        c_y = -c_r

    # condizione di fine gioco
    if vite <= 0:
        gioco = False

    # disegno
    schermo.fill(BIANCO)
    pygame.draw.rect(schermo,   ROSSO, (g_x, g_y, g_l, g_l))
    pygame.draw.circle(schermo, BLU,   (c_x, c_y), c_r)

    schermo.blit(font.render(f"Punti: {punteggio}", True, NERO),  (10, 10))
    schermo.blit(font.render(f"Vite:  {vite}",      True, VERDE), (10, 45))

    pygame.display.update()

# schermata di fine gioco
schermo.fill(BIANCO)
fine = pygame.font.Font(None, 60)
schermo.blit(fine.render("GAME OVER", True, ROSSO), (180, 250))
schermo.blit(font.render(f"Punteggio finale: {punteggio}", True, NERO), (200, 330))
pygame.display.update()
pygame.time.wait(3000)   # aspetta 3 secondi prima di chiudere

pygame.quit()


# ============================================================
# ESERCIZI
# ============================================================
# 1. Aggiungi al gioco del blocco 7 un secondo cerchio
#    di colore verde che cade con velocità diversa (es. 6).
#    Se il giocatore lo raccoglie vale 2 punti invece di 1.
#    Suggerimento: usa variabili separate c2_x, c2_y, c2_vel
#    e controlla la collisione anche con il secondo cerchio.
#
# 2. Modifica il gioco in modo che ogni 5 punti la velocità
#    di caduta del cerchio aumenti di 1 (non solo di 0.5
#    ad ogni raccolta). Mostra la velocità attuale sullo schermo.
#    Suggerimento: usa punteggio % 5 == 0 per controllare
#    se si è appena raggiunto un multiplo di 5.
#
# 3. Aggiungi una schermata iniziale: prima di entrare nel game loop,
#    disegna uno schermo con scritto "PREMI SPAZIO PER INIZIARE".
#    Il gioco parte solo quando l'utente preme spazio.
#    Suggerimento: crea un secondo piccolo loop (while not iniziato:)
#    che aspetta solo l'evento K_SPACE, poi esci da quel loop
#    e inizia il game loop principale.
# ============================================================
