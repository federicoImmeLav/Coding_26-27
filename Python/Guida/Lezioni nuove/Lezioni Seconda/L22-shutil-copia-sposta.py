# ============================================================
# LEZIONE 22 — Copiare, spostare ed eliminare file con shutil
# Tra Unità 1 e Unità 2 · Settimana 3-bis (continua)
# ============================================================
# Prerequisiti: L21 (pathlib, percorsi, exists(), iterdir())
# Obiettivo: lo studente sa copiare, spostare e rinominare file
# con shutil, capisce il rischio delle operazioni distruttive
# e sa scrivere uno script che ordina una cartella in automatico.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA — ordinare 200 file nel Download a mano
# ------------------------------------------------------------

# immagina la cartella Download così:
#
#   foto_mare.jpg        relazione_storia.pdf     setup_gioco.exe
#   vacanze_estate.jpg   appunti_math.pdf         gameplay.mp4
#   foto_gita.jpg        contratto.pdf            archivio.zip
#
# ordinarli a mano: 10 minuti per 30 file, ore per 200.
# uno script Python legge l'estensione di ogni file
# e lo sposta nella sottocartella giusta — in pochi secondi.
#
# per farlo serve shutil (shell utilities):
# il modulo della libreria standard progettato per
# copiare, spostare ed eliminare file e cartelle.

import shutil
import os
from pathlib import Path

# pulizia iniziale: rimuove eventuali resti di esecuzioni precedenti
# così il file si può eseguire più volte senza errori
if Path("test_lezione").exists():
    shutil.rmtree("test_lezione")


# ------------------------------------------------------------
# 2. COPIARE UN FILE — shutil.copy()
# ------------------------------------------------------------

# shutil.copy(sorgente, destinazione)
#   sorgente    → il file da copiare (Path o stringa)
#   destinazione → dove metterlo
#       se è una CARTELLA: il file va dentro con lo stesso nome
#       se è un FILE:      usa quel nome (può anche cambiarlo)
#
# il file originale rimane intatto

# --- prepariamo i file di test ---
Path("test_lezione").mkdir(exist_ok=True)
Path("test_lezione/nota.txt").write_text("appunti della lezione")
Path("test_lezione/dati.csv").write_text("nome,voto\nMarco,8\n")

# copia nota.txt dentro la cartella test_lezione/backup/
backup = Path("test_lezione/backup")
backup.mkdir(exist_ok=True)

shutil.copy("test_lezione/nota.txt", backup)
# risultato: test_lezione/backup/nota.txt
print("Copia con stesso nome:", (backup / "nota.txt").exists())

# copia con nome diverso
shutil.copy("test_lezione/nota.txt", backup / "nota_copia.txt")
# risultato: test_lezione/backup/nota_copia.txt
print("Copia rinominata:     ", (backup / "nota_copia.txt").exists())

# il file originale è ancora lì
print("Originale intatto:   ", Path("test_lezione/nota.txt").is_file())


# ------------------------------------------------------------
# 3. SPOSTARE E RINOMINARE — shutil.move()
# ------------------------------------------------------------

# shutil.move(sorgente, destinazione) funziona come il
# trascinamento nell'Esplora risorse:
#   destinazione è una CARTELLA → il file va lì dentro
#   destinazione è un NOME FILE → rinomina (e sposta se serve)
#
# differenza chiave con copy: il file originale SCOMPARE

# --- spostare in un'altra cartella ---
archivio = Path("test_lezione/archivio")
archivio.mkdir(exist_ok=True)

Path("test_lezione/dati.csv").write_text("nome,voto\nGiulia,9\n")
shutil.move("test_lezione/dati.csv", archivio)
# risultato: test_lezione/archivio/dati.csv
# test_lezione/dati.csv non esiste più
print("\ndati.csv spostato in archivio:", (archivio / "dati.csv").is_file())
print("dati.csv nella cartella originale:", Path("test_lezione/dati.csv").is_file())

# --- rinominare (senza cambiare cartella) ---
Path("test_lezione/bozza.txt").write_text("prima versione")
shutil.move("test_lezione/bozza.txt", "test_lezione/versione_finale.txt")
# bozza.txt scompare, al suo posto c'è versione_finale.txt
print("Rinominato correttamente:", Path("test_lezione/versione_finale.txt").is_file())

# attenzione: se il file di destinazione esiste già viene sovrascritto
# senza chiedere conferma — non c'è un cestino intermedio


# ------------------------------------------------------------
# 4. PERICOLO: ELIMINARE FILE E CARTELLE
# ------------------------------------------------------------

# os.remove() e shutil.rmtree() NON mettono i file nel cestino.
# Cancellano direttamente. Non c'è annulla. Non chiedono conferma.
#
# --- mostriamo prima cosa succede se si sbaglia ---
#
#   os.remove("relazione_finale.docx")   → file sparito per sempre
#   shutil.rmtree("Documenti")            → TUTTA la cartella sparita
#
# la regola d'oro: stampa sempre il percorso ASSOLUTO prima di eliminare
# e controllalo a occhio prima di procedere

da_eliminare = Path("test_lezione/backup/nota.txt")
print(f"\nSto per eliminare: {da_eliminare.resolve()}")

# poi — e solo dopo aver guardato — procedi
if da_eliminare.is_file():
    os.remove(da_eliminare)
    print("File eliminato.")

# per una cartella intera: rmtree è la bomba atomica
# usala solo su cartelle temporanee che hai creato tu stesso
# mai su Documenti, Desktop o cartelle che non controlli al 100%

cartella_temp = Path("test_lezione/backup")
if cartella_temp.is_dir():
    shutil.rmtree(cartella_temp)
    print(f"{cartella_temp} rimossa.")


# ------------------------------------------------------------
# 5. PROGETTO — script che organizza una cartella per estensione
# ------------------------------------------------------------

# pattern completo: leggi ogni file, guarda l'estensione,
# spostalo nella sottocartella corrispondente

# --- passo 1: definisci la mappa estensione → categoria ---
CATEGORIE = {
    ".jpg":  "Immagini",
    ".jpeg": "Immagini",
    ".png":  "Immagini",
    ".pdf":  "Documenti",
    ".txt":  "Documenti",
    ".mp4":  "Video",
    ".avi":  "Video",
    ".exe":  "Programmi",
    ".zip":  "Archivi",
}

def organizza_cartella(percorso):
    sorgente = Path(percorso)

    if not sorgente.is_dir():
        print(f"Cartella non trovata: {sorgente}")
        return

    spostati = 0

    # passo 2: scorri ogni elemento nella cartella
    for file in sorgente.iterdir():
        if not file.is_file():
            continue  # salta le sottocartelle già create

        # passo 3: determina la categoria dall'estensione
        estensione = file.suffix.lower()
        categoria  = CATEGORIE.get(estensione, "Altro")

        # passo 4: crea la cartella di destinazione se manca
        destinazione = sorgente / categoria
        destinazione.mkdir(exist_ok=True)

        # passo 5: sposta il file
        shutil.move(str(file), destinazione / file.name)
        print(f"  {file.name:<30} -> {categoria}/")
        spostati += 1

    print(f"\nFatto: {spostati} file spostati.")

# --- test con file di prova ---
test = Path("test_lezione")
Path(test / "mare.jpg").write_text("")
Path(test / "storia.pdf").write_text("")
Path(test / "musica.mp4").write_text("")
Path(test / "sconosciuto.xyz").write_text("")

print("\nOrganizzazione cartella di test:")
organizza_cartella("test_lezione")

# --- pulizia finale ---
shutil.rmtree("test_lezione")
print("\nCartella di test rimossa.")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Crea una cartella "prova" e due file al suo interno
#    ("note.txt" e "bozza.txt") con Path.write_text().
#    Copia "note.txt" nella cartella corrente con il nome
#    "note_backup.txt" usando shutil.copy().
#    Verifica con is_file() che l'originale sia ancora in "prova/".
#
# 2. Scrivi una funzione rinomina_con_prefisso(percorso, prefisso)
#    che riceve il percorso di un file e una stringa (es. "2025-06")
#    e lo rinomina aggiungendo il prefisso davanti al nome:
#    "relazione.pdf" → "2025-06_relazione.pdf"
#    Usa shutil.move() e Path per estrarre nome ed estensione.
#
# 3. Estendi organizza_cartella() in modo che NON sposti i file
#    che si trovano già in una sottocartella categorizzata
#    (es. se un file è già in Immagini/, lo lascia lì).
#    Suggerimento: controlla se il nome della cartella padre
#    (file.parent.name) è già tra i valori di CATEGORIE.
# ============================================================
