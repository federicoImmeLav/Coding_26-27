# ============================================================
# LEZIONE 17 — Progetto finale: costruisci il tuo gioco
# Unità 6 · Settimana 33
# ============================================================
# Prerequisiti: tutto il corso (L1–L16)
# Obiettivo: lo studente porta a termine un gioco originale
# scelto da lui, che usa almeno tre dei concetti visti
# durante l'anno. Il programma deve essere completo:
# schermata iniziale, gameplay, condizione di fine e punteggio.
# ============================================================


# ============================================================
# PARTE 1 — SCEGLIERE IL PROGETTO
# ============================================================

# un gioco è "completo" quando ha:
# - uno scopo chiaro (cosa deve fare il giocatore per vincere/perdere)
# - almeno una cosa che si muove o cambia
# - un punteggio o una condizione di fine
# - una schermata di inizio e una di fine

# idee ordinate per difficoltà:

# ★☆☆ FACILE
# - Indovina il numero: il programma sceglie un numero casuale,
#   l'utente ha 5 tentativi. Conta i tentativi e mostra il punteggio.
# - Quiz a scelta multipla: 5 domande, 3 opzioni ciascuna,
#   punteggio finale e tempo impiegato.

# ★★☆ MEDIO
# - Acchiappa le monete: quadrato controllato con i tasti,
#   monete che cadono, vite limitate, velocità crescente.
# - Snake minimale: un quadrato che si allunga raccogliendo cibo,
#   game over se tocca i bordi.
# - Pong a un giocatore: paletta in basso, palla che rimbalza,
#   game over se la palla tocca il fondo.

# ★★★ DIFFICILE
# - Space invaders semplice: nave in basso, nemici che scendono,
#   proiettile che sale premendo spazio.
# - Labirinto: una griglia con muri, il personaggio si muove
#   cella per cella, deve raggiungere l'uscita.
# - Gioco di memoria: carte coperte, clic per girarle,
#   trova tutte le coppie nel minor tempo possibile.


# ============================================================
# PARTE 2 — SCHELETRO RIUTILIZZABILE
# ============================================================

# questo è il template di partenza: copialo e modificalo
# le sezioni sono marcate con TODO — sostituisci con il tuo codice

import pygame
import random

pygame.init()

LARGHEZZA = 800
ALTEZZA   = 600
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("TODO: nome del tuo gioco")

# --- colori ---
BIANCO = (255, 255, 255)
NERO   = (0,   0,   0)
ROSSO  = (255, 0,   0)
BLU    = (0,   0,   255)
VERDE  = (0,   200, 0)

# --- font ---
font_grande = pygame.font.Font(None, 72)
font_medio  = pygame.font.Font(None, 36)
font_piccolo = pygame.font.Font(None, 24)

clock = pygame.time.Clock()

# --- variabili del gioco ---
# TODO: definisci qui le variabili del tuo gioco
punteggio = 0
vite      = 3


# ---- SCHERMATA INIZIALE ----
def schermata_inizio():
    schermo.fill(NERO)
    schermo.blit(font_grande.render("TODO: TITOLO",  True, BIANCO), (LARGHEZZA//2 - 180, 200))
    schermo.blit(font_medio.render("Premi SPAZIO per iniziare", True, VERDE), (LARGHEZZA//2 - 170, 320))
    pygame.display.update()

    aspetta = True
    while aspetta:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                aspetta = False


# ---- SCHERMATA DI FINE ----
def schermata_fine(messaggio):
    schermo.fill(NERO)
    schermo.blit(font_grande.render(messaggio, True, ROSSO), (LARGHEZZA//2 - 180, 200))
    schermo.blit(font_medio.render(f"Punteggio: {punteggio}", True, BIANCO), (LARGHEZZA//2 - 100, 310))
    schermo.blit(font_piccolo.render("Chiudi la finestra per uscire", True, GRIGIO if False else (150,150,150)), (LARGHEZZA//2 - 120, 390))
    pygame.display.update()
    pygame.time.wait(4000)


# ---- GAME LOOP ----
def gioca():
    global punteggio, vite
    punteggio = 0
    vite      = 3

    # TODO: inizializza le posizioni dei tuoi oggetti qui

    gioco = True
    while gioco:
        clock.tick(60)

        # 1. EVENTI
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                gioco = False

        # 2. LOGICA
        tasto = pygame.key.get_pressed()
        # TODO: aggiungi il movimento e la logica del tuo gioco

        # TODO: controlla le collisioni

        # TODO: controlla condizione di fine
        if vite <= 0:
            return "GAME OVER"
        # if punteggio >= 20:
        #     return "HAI VINTO!"

        # 3. DISEGNO
        schermo.fill(BIANCO)
        # TODO: disegna i tuoi oggetti qui

        schermo.blit(font_medio.render(f"Punti: {punteggio}", True, NERO), (10, 10))
        schermo.blit(font_medio.render(f"Vite: {vite}", True, ROSSO),      (10, 45))

        pygame.display.update()

    return "USCITO"


# ---- AVVIO ----
schermata_inizio()
risultato = gioca()
schermata_fine(risultato)
pygame.quit()


# ============================================================
# PARTE 3 — SNIPPET UTILI
# ============================================================

# questi pezzi di codice si usano spesso nei giochi:
# copiali nel tuo progetto quando servono


# --- oggetto che rimbalza sui bordi ---
# vel_x = 3   # velocità orizzontale (positiva = destra)
# vel_y = 2   # velocità verticale   (positiva = giù)
# ...
# x += vel_x
# y += vel_y
# if x < 0 or x > LARGHEZZA - lato:
#     vel_x = -vel_x   # inverti la direzione orizzontale
# if y < 0 or y > ALTEZZA - lato:
#     vel_y = -vel_y   # inverti la direzione verticale


# --- oggetto che riappare in posizione casuale ---
# if y > ALTEZZA:
#     x = random.randint(20, LARGHEZZA - 20)
#     y = 0


# --- timer che conta alla rovescia ---
# tempo = 30
# ultimo_tick = pygame.time.get_ticks()   # millisecondi dall'avvio
# ...
# adesso = pygame.time.get_ticks()
# if adesso - ultimo_tick >= 1000:   # è passato un secondo?
#     tempo -= 1
#     ultimo_tick = adesso
# if tempo <= 0:
#     return "TEMPO SCADUTO"


# --- velocità crescente ogni N punti ---
# velocita_base = 3
# vel = velocita_base + punteggio // 5   # aumenta di 1 ogni 5 punti


# --- proiettile che sale ---
# proiettile_attivo = False
# pr_x = 0
# pr_y = 0
# ...
# if tasto[pygame.K_SPACE] and not proiettile_attivo:
#     proiettile_attivo = True
#     pr_x = giocatore_x + lato // 2
#     pr_y = giocatore_y
# if proiettile_attivo:
#     pr_y -= 8
#     if pr_y < 0:
#         proiettile_attivo = False
#     pygame.draw.circle(schermo, GIALLO, (pr_x, pr_y), 6)


# ============================================================
# PARTE 4 — CHECKLIST DEL PROGETTO FINITO
# ============================================================

# prima di consegnare, verifica che il tuo gioco abbia:
#
# [ ] una schermata iniziale con il nome del gioco
# [ ] il gameplay funzionante (il giocatore può giocare)
# [ ] almeno un oggetto che si muove da solo
# [ ] un punteggio visibile durante il gioco
# [ ] una condizione di fine (vittoria o sconfitta)
# [ ] una schermata finale con il punteggio
# [ ] il gioco si chiude correttamente (niente crash)
# [ ] il codice è leggibile: variabili con nomi chiari,
#     nessun numero "magico" senza nome (usa costanti)
#
# bonus:
# [ ] la difficoltà aumenta col tempo o col punteggio
# [ ] ci sono effetti visivi (colori che cambiano, flash)
# [ ] si può giocare di nuovo senza riavviare il programma
# ============================================================
