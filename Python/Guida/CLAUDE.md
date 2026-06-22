# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Cos'è questo progetto

Materiali per un corso annuale di Python per liceo / ITI.
- 2 ore a settimana · 33 settimane · 66 ore totali
- Studenti senza prerequisiti, si parte da zero
- Ogni lezione produce un file `.py` commentato che lo studente
  può rileggere a casa come appunti

Il piano completo del corso è in `piano-corso-python.md`.
Leggilo sempre prima di creare o modificare materiali didattici.

---

## Struttura dei file

```
Guida/
├── CLAUDE.md
├── piano-corso-python.md          ← piano annuale con obiettivi, contenuti, note
├── Lezioni old/                   ← lezioni già svolte in classe (non modificare)
│   ├── 01-intro.py
│   ├── 02-condizioni.py
│   └── ... (fino a 029-ascensore.py)
└── Lezioni nuove/                 ← nuovi materiali da produrre
    ├── L1-output-variabili-input.py
    ├── L2-operatori-condizioni.py
    └── L3-logici-errori.py
```

I file in `Lezioni old/` sono quelli già svolti: non modificarli.
I file in `Lezioni nuove/` con prefisso `LN-` sono i nuovi materiali.

---

## Convenzioni per i file `.py`

Ogni file lezione segue sempre questa struttura:

```python
# ============================================================
# LEZIONE N — Titolo argomento
# Unità X · Settimane X-X
# ============================================================
# Prerequisiti: lezione precedente
# Obiettivo: frase breve su cosa sa fare lo studente alla fine
# ============================================================


# ------------------------------------------------------------
# 1. NOME BLOCCO — una riga che spiega il concetto
# ------------------------------------------------------------

# commento che spiega il perché prima del come
codice_esempio = "valore"
print(codice_esempio)


# ------------------------------------------------------------
# 2. SECONDO BLOCCO
# ------------------------------------------------------------
...


# ============================================================
# ESERCIZI
# ============================================================
# 1. Testo esercizio.
#    Dettaglio se serve.
#
# 2. ...
#
# 3. ...
# ============================================================
```

Regole da rispettare sempre:
- I commenti spiegano il *perché*, non riscrivono il codice in italiano
- Ogni blocco ha 1-2 esempi progressivi, non di più
- Gli esercizi sono sempre 3, a difficoltà crescente
- Il primo esercizio deve essere quasi già risolto dagli esempi
- Usare esempi concreti: nome, età, voti, prezzi — non `x`, `foo`, `variabile1`
- Non commentare MAI ogni singola riga: i commenti devono aggiungere valore

### Ritmo di spiegazione — regola fondamentale

Le lezioni devono andare **lentamente e per gradi**. Non dare mai per scontato nessun passaggio.
Linee guida concrete:

**Prima di introdurre un costrutto nuovo, spiega perché quello vecchio non basta.**
Non scrivere "ecco il while". Scrivi prima "il for non funziona quando non sai quante volte
ripetere — ed è per questo che esiste il while."

**Ogni concetto nuovo ha un blocco dedicato, anche se sembra ovvio.**
Il loop infinito, la differenza tra chiedere fuori e dentro al while, il fatto che
la condizione si controlla prima di entrare: queste cose sembrano ovvie a chi le conosce,
ma non lo sono per chi le vede per la prima volta. Ognuna merita il suo blocco.

**Quando mostri un pattern, numera i passi.**
Esempio per "input in loop":
```
# passo 1: chiedo FUORI dal while
# passo 2: while la risposta è sbagliata:
# passo 3:     avvisa l'utente
# passo 4:     chiedi di nuovo DENTRO al while
```
Questo aiuta lo studente a replicare il pattern in autonomia.

**Se un esempio fa più cose insieme, percorrilo riga per riga nei commenti.**
Esempio: per un while con contatore, aggiungi un commento che simula l'esecuzione:
```
# giro 1: numero vale 0 → 0 < 3 è True → stampa 0 → numero diventa 1
# giro 2: numero vale 1 → 1 < 3 è True → stampa 1 → numero diventa 2
# giro 3: numero vale 2 → 2 < 3 è True → stampa 2 → numero diventa 3
# giro 4: numero vale 3 → 3 < 3 è False → esce
```

**I pericoli vanno spiegati prima della soluzione, non dopo.**
Non scrivere il codice corretto e poi aggiungere "attenzione al loop infinito".
Mostra prima cosa succede se si sbaglia, poi come evitarlo.

**Pattern simili ma diversi vanno in blocchi separati.**
Esempio: "validare un input" e "uscire con una parola di stop" usano entrambi
il while con input, ma la logica è diversa. Non metterli nello stesso blocco.

---

## Come lavorare sul piano del corso

Il file `piano-corso-python.md` va aggiornato ogni volta che:
- si aggiunge un argomento a un'unità
- si crea un nuovo file lezione (va aggiunto nella colonna "File di riferimento")
- si modificano le note didattiche

Quando aggiorni il piano, mantieni esattamente il formato delle tabelle markdown.

---

## Comandi utili

**Eseguire un file per testarlo:**
```bash
python "Lezioni nuove/L3-logici-errori.py"
```

**Creare una nuova lezione:**
```
Crea il file Lezioni nuove/L4-[argomento].py per le settimane X-X dell'unità X.
Argomenti da coprire: [lista].
Aggiorna piano-corso-python.md con il nuovo file.
```

**Analizzare cosa manca:**
```
Confronta i file .py in Lezioni nuove/ con piano-corso-python.md
e dimmi cosa manca per completare l'unità X.
```

---

## Tono e stile dei contenuti

- Italiano semplice, diretto — niente gergo tecnico non spiegato
- Quando si introduce un termine tecnico, lo si spiega subito con
  un'analogia concreta (es. "una variabile è come una scatola con un'etichetta")
- Le note didattiche nel piano sono per il professore, non per lo studente:
  possono essere più dirette e critiche
- Non usare mai "molto semplice" o "banale" nei commenti dei file lezione
