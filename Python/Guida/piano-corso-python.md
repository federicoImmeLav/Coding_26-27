# Piano annuale — Corso di Python
**Contesto:** Liceo / ITI · 2 ore a settimana · 33 settimane · 66 ore totali  
**Prerequisiti:** Nessuno. Si parte da zero.  
**Materiali:** File `.py` commentati + schede esercizi PDF

---

## Unità 1 — Basi del linguaggio
**Settimane 1–6 · 12 ore**

### Obiettivo
Lo studente sa scrivere un programma che chiede dati all'utente, li elabora e stampa un risultato. Conosce i tipi base e sa usare le condizioni.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 1–2 | Ambiente di lavoro, `print`, variabili, tipi (`str`, `int`, `float`), `input`, f-string | `01-intro.py`, `L1-output-variabili-input.py` |
| 3–4 | Operatori aritmetici e di confronto, condizioni `if` / `elif` / `else` | `02-condizioni.py`, `03-if.py`, `L2-operatori-condizioni.py` |
| 5–6 | Operatori logici (`and`, `or`, `not`), errori comuni (`TypeError`, `NameError`, `SyntaxError`), scheda verifica autonoma | `L3-logici-errori.py` |

### Struttura tipo di una lezione
- 30 min — spiegazione del concetto con esempi minimi
- 30 min — coding insieme (live coding commentato)
- 40 min — esercizi autonomi dalla scheda

### Note didattiche
- Non dare mai per scontato che lo studente sappia già aprire un terminale o creare un file.
- La conversione `int(input(...))` va spiegata bene: è il primo momento in cui si capisce che i tipi esistono.
- Usare esempi concreti e personali (nome, età, anno di nascita) per rendere subito utile quello che si scrive.
- `and` / `or` / `not` vanno introdotti **dopo** `if`/`elif`/`else`: prima lo studente capisce la struttura, poi impara a combinare le condizioni. Mostrare la tabella della verità con esempi reali, non astratti.
- Gli errori comuni (`TypeError`, `NameError`, `SyntaxError`) vanno mostrati **apposta**: provoca l'errore in classe, leggilo ad alta voce insieme, spiega cosa significa ogni parte del messaggio. Togliere la paura del rosso è un obiettivo didattico esplicito.
- La scheda verifica di fine unità deve coprire tutti e tre i blocchi: variabili/tipi, condizioni, operatori logici.

---

## Unità 2 — Cicli e ripetizioni
**Settimane 7–12 · 12 ore**

### Obiettivo
Lo studente sa usare `for` e `while` per ripetere azioni, sa costruire contatori e gestire l'input in loop.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 7–8 | `for`, `range`, iterazione su stringhe e liste semplici | `05-for.py`, `06-for-verifica.py`, `L4-for-range-liste.py` |
| 9–10 | `while`, condizione di stop, contatori, input in loop | `04-while-for.py`, `07-while.py` |
| 11–12 | Esercizi misti `for`/`while` + scheda verifica + mini-progetto (tabellina, somma) | `08-esercizi.py` |

### Struttura tipo di una lezione
- 20 min — analogia concreta per introdurre il concetto
- 40 min — coding insieme con varianti progressive
- 40 min — esercizi autonomi + confronto in classe

### Note didattiche
- Introdurre `for` e `while` con un'analogia fisica: *"fare 10 flessioni"* è un `for`; *"fare flessioni finché si è stanchi"* è un `while`.
- L'errore più comune è dimenticare la condizione di stop nel `while`. Mostrarlo apposta una volta, far vedere cosa succede.
- Non mescolare i due costrutti nella stessa lezione: prima una settimana solo `for`, poi una settimana solo `while`.

---

## Unità 3 — Funzioni e strutture dati
**Settimane 13–20 · 16 ore**

### Obiettivo
Lo studente sa organizzare il codice in funzioni riutilizzabili, gestire liste e dizionari, e costruire programmi strutturati di media complessità.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 13–14 | Liste: creare, `append`, `remove`, `sort`, `reverse`, scorrere con `for` | `09-liste.py` |
| 15–16 | Funzioni: `def`, parametri, `return` — perché separare il codice | `010-funzioni.py`, `012-funz+while.py` |
| 17–18 | Dizionari: chiave/valore, accesso, aggiornamento, lista di dizionari | `013-dizionari.py` |
| 19–20 | Ripasso generale + progetto intermedio (es. gestione lista della spesa) | `011-ripasso.py` |

### Struttura tipo di una lezione
- 20 min — spiegazione con schema visivo alla lavagna
- 40 min — coding insieme
- 40 min — esercizi + mini-progetto guidato

### Note didattiche
- Questa è l'unità più lunga perché i concetti richiedono più tempo per sedimentarsi.
- Le funzioni vanno motivate prima di essere spiegate: mostrare un programma con codice ripetuto, poi riscriverlo con una funzione. Il "perché" deve venire prima del "come".
- I dizionari sono spesso sottovalutati: usare esempi reali (scheda di una persona, ingrediente con quantità) per mostrarne la potenza.
- Il progetto intermedio di fine unità serve come verifica pratica e momento di soddisfazione.

---

## Unità 4 — Grafica con Turtle
**Settimane 21–24 · 8 ore**

### Obiettivo
Lo studente sa usare la libreria `turtle` per disegnare forme, gestire il movimento con i tasti e capisce il concetto di event listener.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 21–22 | Comandi base `turtle`, disegnare forme con `for`, colori, velocità | `015-turtle.py`, `014-geometria.py` |
| 23–24 | Controllo con tasti (`onkey`), movimento fluido (`penup`/`pendown`), disegno libero | `016-controlla-turtle.py` |

### Struttura tipo di una lezione
- 15 min — demo live del risultato finale (mostrare prima cosa si costruirà)
- 45 min — coding insieme passo per passo
- 40 min — personalizzazione libera del programma

### Note didattiche
- Questo è il momento più motivante dell'anno: il codice produce qualcosa di visibile immediatamente.
- Iniziare la prima lezione mostrando il risultato finale (una tartaruga che si muove con i tasti) prima di spiegare qualsiasi cosa.
- Lasciare spazio alla personalizzazione: colori, forme, velocità. Lo studente deve sentire il programma come proprio.
- `matplotlib` può essere introdotto brevemente come alternativa grafica per chi è più orientato ai dati.

---

## Unità 5 — Minigiochi e gestione del tempo
**Settimane 25–28 · 8 ore**

### Obiettivo
Lo studente sa usare `time` e `random`, gestire booleani come stato del programma, e costruire minigiochi completi con punteggio e condizioni di vittoria/sconfitta.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 25–26 | Libreria `time`, cronometro, gioco reazione — `ontimer`, booleani come stato | `019-tempo.py`, `020-reazione.py`, `021-cronometro.py` |
| 27–28 | Collisioni con `distance()`, punteggio, `random`, primo gioco completo | `018-collisioni.py`, `022-test-scrittura.py`, `023-fpsaim.py` |

### Struttura tipo di una lezione
- 10 min — presentazione del gioco che si costruirà
- 50 min — coding insieme, aggiungendo funzionalità una alla volta
- 40 min — completamento autonomo + test del gioco

### Note didattiche
- Ogni lezione produce un programma finito e giocabile: ottimo per la motivazione.
- I booleani come stato (`True`/`False` per sapere se un tasto è premuto) vanno spiegati con calma prima di scrivere codice — usare l'esempio di una luce accesa/spenta.
- `global` è necessario ma va usato con consapevolezza: spiegare perché esiste e quando serve.
- Far testare i giochi tra studenti: il feedback reale è il miglior incentivo a migliorare il codice.

---

## Unità 6 — Pygame e progetto finale
**Settimane 29–33 · 10 ore**

### Obiettivo
Lo studente conosce le basi di Pygame, capisce la differenza tra il game loop e l'event-driven di Turtle, e porta a termine un progetto originale di sua scelta.

### Contenuti
| Settimana | Argomento | File di riferimento |
|-----------|-----------|---------------------|
| 29–30 | Pygame: schermata, game loop (`while`), `draw.rect`/`circle`, movimento con tasti | `025-pygame.py`, `026-comandi-pygame.py` |
| 31–32 | Collisioni manuali, velocità, colori dinamici, clock e FPS | `027-acchiappa.py`, `028-semaforo.py`, `029-ascensore.py` |
| 33 | Progetto finale libero: ogni studente porta a termine un gioco scelto | `024-dado.py` (esempio) |

### Struttura tipo di una lezione
- 20 min — confronto esplicito con Turtle (schema alla lavagna)
- 40 min — coding insieme
- 40 min — sviluppo autonomo del progetto finale

### Note didattiche
- Prima di scrivere una riga di Pygame, dedicare almeno 20 minuti a spiegare la differenza tra **event-driven** (Turtle, aspetta che succeda qualcosa) e **game loop** (Pygame, controlla tutto ad ogni frame). È il cambio concettuale più importante dell'unità.
- Il progetto finale è la verifica naturale di tutto l'anno: ogni studente sceglie un gioco, lo implementa e lo spiega. Vale sia come verifica tecnica che come esposizione orale.
- Suggerire idee per il progetto finale nella settimana 28, così lo studente ci pensa in anticipo.

---

## Riepilogo

| Unità | Argomento | Settimane | Ore |
|-------|-----------|-----------|-----|
| 1 | Basi del linguaggio | 1–6 | 12 |
| 2 | Cicli e ripetizioni | 7–12 | 12 |
| 3 | Funzioni e strutture dati | 13–20 | 16 |
| 4 | Grafica con Turtle | 21–24 | 8 |
| 5 | Minigiochi e tempo | 25–28 | 8 |
| 6 | Pygame e progetto finale | 29–33 | 10 |
| | **Totale** | **33 sett.** | **66h** |

---

## Materiali da produrre per ogni unità

- `XX-lezione-nome.py` — file commentato con esempi progressivi
- `scheda-unitaXX.pdf` — 3–4 esercizi a difficoltà crescente (il primo quasi già risolto)

---

*Piano redatto sulla base delle lezioni `01-intro.py` → `029-ascensore.py` già svolte.*
