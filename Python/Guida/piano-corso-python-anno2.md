# Piano annuale — Corso di Python (Anno 2)
**Contesto:** Liceo / ITI · 2 ore a settimana · 33 settimane · 66 ore totali
**Prerequisiti:** Contenuti dell'Anno 1 (variabili, condizioni, cicli, liste, funzioni, dizionari, Turtle, Pygame base)
**Materiali:** File `.py` commentati + schede esercizi PDF

---

## Unità 1 — Ripasso e riattivazione
**Settimane 1–3 · 6 ore**

### Obiettivo
Lo studente recupera la sicurezza con i concetti dell'anno precedente (variabili, condizioni, cicli, liste, funzioni, dizionari) e torna operativo sull'ambiente di lavoro.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 1 | Ripasso lampo: variabili, tipi, condizioni, operatori logici — esercizi veloci a difficoltà crescente | nuovo file `L18-ripasso-base.py` |
| 2 | Ripasso cicli, liste, dizionari — mini esercizi che richiedono di combinare più concetti | nuovo file `L19-ripasso-cicli-strutture.py` |
| 3 | Ripasso funzioni + mini-progetto di riscaldamento (es. piccolo programma a menu testuale) | nuovo file `L20-ripasso-funzioni-progetto.py` |

### Struttura tipo di una lezione
- 15 min — richiamo veloce del concetto con un esempio "ti ricordi quando..."
- 35 min — esercizi a coppie per riattivare la memoria muscolare del codice
- 30 min — correzione collettiva, errori tipici dell'anno scorso

### Note didattiche
- Non dare per scontato nulla: trattare il ripasso come se fosse la prima volta, ma andando più rapidi.
- Usare l'errore come diagnostico: far scrivere codice e vedere dove si inceppano per capire da dove ripartire davvero.
- Niente argomenti nuovi in questa unità: l'obiettivo è solo consolidare, non avanzare.
- Il mini-progetto finale dell'unità deve essere risolvibile con i soli strumenti dell'anno scorso, per dare un primo successo immediato.

---

## Unità 2 — Pygame avanzato
**Settimane 4–10 · 14 ore**

### Obiettivo
Lo studente sa costruire un gioco Pygame più completo: con immagini (sprite), suoni, più stati di gioco (menu, gioco, game over) e una struttura del codice più organizzata.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 4–5 | Ripasso Pygame base (game loop, `draw.rect`/`circle`, tasti) + caricare e mostrare immagini (`image.load`), `Rect` per le collisioni | nuovo file `L21-pygame-immagini.py` |
| 6–7 | Suoni ed effetti (`mixer`), testo a schermo (`font`), punteggio persistente durante la partita | nuovo file `L22-pygame-suoni-testo.py` |
| 8–9 | Stati di gioco: menu iniziale, partita, schermata di game over — gestiti con variabili di stato e `if` | nuovo file `L23-pygame-stati-menu.py` |
| 10 | Esercizi misti + scheda verifica | — |

### Struttura tipo di una lezione
- 15 min — demo del risultato finale prima di spiegare il codice
- 45 min — coding insieme passo per passo
- 40 min — personalizzazione autonoma (proprie immagini, suoni, testi)

### Note didattiche
- Riprendere esplicitamente il game loop dell'anno scorso prima di aggiungere complessità: è la base su cui si costruisce tutto.
- Gli stati di gioco (menu/gioco/game over) vanno motivati mostrando *prima* il problema (un gioco che parte subito senza menu è meno professionale) e poi la soluzione.
- Attenzione ai path dei file immagine/suono: è una fonte frequente di errori, va affrontata apposta in classe come nell'anno scorso con gli errori di sintassi.
- Lasciare ampio spazio alla personalizzazione: motiva molto più la grafica/i suoni propri che un esempio standard.

---

## Unità 3 — Programmazione orientata agli oggetti (basi)
**Settimane 11–18 · 16 ore**

### Obiettivo
Lo studente capisce cos'è una classe, sa definire attributi e metodi, crea e usa oggetti, e capisce perché l'OOP semplifica programmi con più "cose" che si comportano in modo simile (es. più nemici, più proiettili).

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 11–12 | Perché le classi: da codice ripetuto (più dizionari "simili") a una classe — `class`, `__init__`, attributi | nuovo file `L24-oop-perche-classi.py` |
| 13–14 | Metodi, `self`, modificare lo stato di un oggetto tramite i suoi metodi | nuovo file `L25-oop-metodi-self.py` |
| 15–16 | Più oggetti della stessa classe in una lista, ciclare su di essi, confronto con liste di dizionari dell'anno scorso | nuovo file `L26-oop-liste-oggetti.py` |
| 17–18 | Ripasso OOP + piccolo progetto non grafico (es. gestione di una rubrica/inventario con classi) | nuovo file `L27-oop-progetto.py` |

### Struttura tipo di una lezione
- 20 min — motivazione concettuale con schema alla lavagna (oggetto = scatola con dati + azioni)
- 40 min — coding insieme
- 40 min — esercizi autonomi

### Note didattiche
- Questo è il cambio concettuale più importante dell'anno: va introdotto con calma, esattamente come è stato fatto per il passaggio Turtle → Pygame nell'anno scorso.
- Motivare le classi mostrando *prima* il dolore: un programma con tre nemici gestiti come variabili separate (`nemico1_x`, `nemico2_x`...) o come dizionari sparsi, poi la stessa cosa con una classe `Nemico`.
- Far esplicitamente il collegamento con i dizionari dell'anno scorso: una classe è come un dizionario che porta con sé anche le sue funzioni.
- `self` è un punto critico: usare sempre la stessa metafora per tutto l'anno (es. "self è come dire 'il MIO nome', 'la MIA vita'").
- Evitare per ora eredità, polimorfismo, classi astratte: solo classi semplici con attributi e metodi. Sono concetti per un eventuale anno 3.
- Niente Pygame in questa unità: isolare l'OOP dal resto per non sovraccaricare lo studente con due novità insieme.

---

## Unità 4 — Pygame con le classi
**Settimane 19–24 · 12 ore**

### Obiettivo
Lo studente sa riscrivere e ampliare un gioco Pygame usando classi per i personaggi/oggetti di gioco (player, nemici, proiettili), gestendo collisioni e comportamenti tramite metodi.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 19–20 | Da funzioni a classi: riscrivere un gioco dell'Unità 2 usando una classe `Player` | nuovo file `L28-pygame-classe-player.py` |
| 21–22 | Più nemici/oggetti come lista di istanze della stessa classe, collisioni tra oggetti tramite metodi | nuovo file `L29-pygame-classi-nemici.py` |
| 23–24 | `pygame.sprite.Sprite` e `Group` (versione "ufficiale" di Pygame delle classi viste a mano) + esercizi/verifica | nuovo file `L30-pygame-sprite-group.py` |

### Struttura tipo di una lezione
- 20 min — confronto esplicito "come lo facevamo prima / come lo facciamo ora con le classi"
- 40 min — coding insieme
- 40 min — sviluppo autonomo

### Note didattiche
- Partire sempre da codice già visto (i giochi dell'Unità 2) e farlo evolvere, non da zero: rende tangibile il vantaggio dell'OOP.
- Introdurre `pygame.sprite.Sprite` solo *dopo* aver fatto vedere come si farebbe "a mano" con classi proprie: altrimenti sembra magia.
- Le collisioni con `pygame.sprite.spritecollide` vanno confrontate con le collisioni manuali con i `Rect` viste nell'anno scorso e in Unità 2.

---

## Unità 5 — File, dati e moduli
**Settimane 25–29 · 10 ore**

### Obiettivo
Lo studente sa salvare e ricaricare dati da file (es. punteggi, salvataggi), sa organizzare il codice in più file con `import`, e ha una prima idea di formati di dati come JSON.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 25–26 | Lettura e scrittura di file di testo (`open`, `read`, `write`, `with`) — es. salvare un log o un elenco | nuovo file `L31-file-lettura-scrittura.py` |
| 27 | JSON: salvare e ricaricare strutture dati (liste/dizionari) — es. salvare il punteggio massimo di un gioco | nuovo file `L32-json-salvataggio.py` |
| 28–29 | Moduli propri: dividere un programma in più file con `import`, perché organizzare il codice in più parti | nuovo file `L33-moduli-import.py` |

### Struttura tipo di una lezione
- 20 min — motivazione concreta ("il punteggio si perde quando chiudo il gioco: come lo salviamo?")
- 40 min — coding insieme
- 40 min — esercizi autonomi

### Note didattiche
- Collegare subito al progetto Pygame: il salvataggio del punteggio massimo è l'esempio più motivante e verrà riusato nel progetto finale.
- `with open(...) as f` va spiegato anche nel "perché" (chiusura automatica del file), non solo come sintassi da copiare.
- I moduli propri vanno introdotti mostrando un file che cresce troppo e diventa difficile da leggere: stesso principio già visto per le funzioni nell'anno scorso, applicato a livello di file.

---

## Unità 6 — Progetto finale
**Settimane 30–33 · 8 ore**

### Obiettivo
Lo studente porta a termine un progetto originale che integra Pygame, classi e salvataggio dati, e lo presenta spiegando le scelte fatte.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 30 | Definizione del progetto: scelta del gioco/programma, requisiti minimi (almeno una classe, salvataggio dati) | — |
| 31–32 | Sviluppo autonomo guidato, supporto individuale | — |
| 33 | Presentazione e verifica orale del progetto | — |

### Struttura tipo di una lezione
- 10 min — punto rapido sullo stato di avanzamento di ciascuno
- 70 min — sviluppo autonomo con supporto del docente
- presentazioni nell'ultima settimana

### Note didattiche
- I requisiti minimi (almeno una classe propria + salvataggio dati su file) garantiscono che il progetto usi davvero i contenuti dell'anno, non solo quelli dell'anno scorso.
- Come per il progetto finale dell'anno 1, vale sia come verifica tecnica che come esposizione orale.
- Suggerire idee di progetto già alla settimana 29, così gli studenti arrivano con un'idea chiara all'inizio dell'unità.

---

## Riepilogo

| Unità | Argomento | Settimane | Ore |
|-------|-----------|-----------|-----|
| 1 | Ripasso e riattivazione | 1–3 | 6 |
| 2 | Pygame avanzato | 4–10 | 14 |
| 3 | OOP (basi) | 11–18 | 16 |
| 4 | Pygame con le classi | 19–24 | 12 |
| 5 | File, dati e moduli | 25–29 | 10 |
| 6 | Progetto finale | 30–33 | 8 |
| | **Totale** | **33 sett.** | **66h** |

---

## Materiali da produrre per ogni unità

- `LXX-lezione-nome.py` — file commentato con esempi progressivi (continua la numerazione `L` dell'anno 1, partendo da `L18`)
- `scheda-unitaXX.pdf` — 3–4 esercizi a difficoltà crescente (il primo quasi già risolto)

---

## Principi di continuità con l'Anno 1 (da mantenere)

- Ogni concetto nuovo va motivato mostrando prima il problema/dolore, poi la soluzione — mai sintassi "calata dall'alto".
- Gli errori vanno provocati apposta in classe per essere normalizzati, come fatto con `TypeError`/`NameError`/`SyntaxError` nell'Unità 1 dell'anno scorso.
- Ogni cambio concettuale importante (qui: OOP, e Pygame con sprite) va trattato con la stessa cura dedicata al passaggio Turtle → Pygame: prima il concetto a parole/schema, poi il codice.
- Non assumere mai nulla per acquisito, nemmeno a inizio anno 2: da qui l'Unità 1 di ripasso.

---

*Piano redatto come prosecuzione di `piano-corso-python.md` (Anno 1), mantenendo lo stesso tono, ritmo e struttura didattica.*
