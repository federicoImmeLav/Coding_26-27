# ============================================================
# LEZIONE 21 — Percorsi e cartelle con pathlib
# Tra Unità 1 e Unità 2 · Settimana 3-bis
# ============================================================
# Prerequisiti: L20 (funzioni, programma completo)
# Obiettivo: lo studente sa costruire percorsi assoluti,
# verificare se un file/cartella esiste e listare il contenuto
# di una cartella — senza dipendere da dove esegue lo script.
# ============================================================


# ------------------------------------------------------------
# 1. IL PROBLEMA — perché open("foto.jpg") a volte fallisce
# ------------------------------------------------------------

# prova a eseguire questo da due posti diversi:
#
#   from pathlib import Path
#   open("foto.jpg")   # ← funziona dalla cartella giusta
#                      # ← FileNotFoundError da qualsiasi altra
#
# il problema: "foto.jpg" è un percorso RELATIVO.
# Python lo cerca a partire dalla cartella in cui sei ADESSO,
# non da dove si trova lo script.
#
# la soluzione è usare percorsi ASSOLUTI, che partono
# dalla radice del disco e funzionano da ovunque:
#   Windows  → C:\Users\Marco\Documenti\foto.jpg
#   Mac/Linux → /home/marco/documenti/foto.jpg
#
# ma scriverli a mano è fragile: cambiano se sposti la cartella
# o se il programma gira su un altro computer.
# pathlib li costruisce al posto tuo, nel modo giusto.


# ------------------------------------------------------------
# 2. pathlib — l'oggetto Path e come costruire i percorsi
# ------------------------------------------------------------

from pathlib import Path

# Path() non apre nessun file: costruisce solo l'indirizzo
# come un navigatore GPS che calcola il percorso prima di partire

cartella_corrente = Path(".")        # dove sei adesso
cartella_home     = Path.home()      # cartella home dell'utente
questo_script     = Path(__file__)   # percorso di questo file

print("Dove sono adesso:", cartella_corrente.resolve())
print("Home:            ", cartella_home)
print("Questo script:   ", questo_script)

# resolve() trasforma un percorso relativo in assoluto
# da quel momento funziona indipendentemente da dove esegui lo script

# --- costruire percorsi con / ---
# l'operatore / unisce i pezzi mettendo la barra giusta
# per il sistema operativo (\ su Windows, / su Mac/Linux)

documenti  = Path.home() / "Documenti"
file_voti  = documenti / "classe" / "voti.txt"

print("File voti:", file_voti)
# su Windows: C:\Users\Marco\Documenti\classe\voti.txt

# --- risalire di un livello con .parent ---
# utile per trovare la cartella che contiene lo script
cartella_dello_script = Path(__file__).parent
print("Cartella dello script:", cartella_dello_script)

# --- leggere le parti di un percorso ---
p = Path("Documenti/foto_vacanze.jpg")
print(p.name)    # foto_vacanze.jpg   (nome con estensione)
print(p.stem)    # foto_vacanze       (solo il nome)
print(p.suffix)  # .jpg               (solo l'estensione)


# ------------------------------------------------------------
# 3. VERIFICARE SE UN FILE O UNA CARTELLA ESISTE
# ------------------------------------------------------------

# prima di aprire o elaborare un file, controlla che esista
# così dai un messaggio utile invece di un errore criptico

cartella = Path.home() / "Documenti"

if cartella.exists():
    print(f"{cartella.name} trovata")
else:
    print("Cartella Documenti non trovata")

# .is_file() e .is_dir() distinguono tra file e cartella
# un percorso può esistere ma essere una cartella, non un file

if cartella.is_dir():
    print("è una cartella")

# pattern tipico: apri solo se il file esiste
dati = Path("voti.txt")
if dati.is_file():
    with open(dati) as f:
        print(f.read())
else:
    print("voti.txt non esiste ancora — lo creeremo nelle prossime lezioni")


# ------------------------------------------------------------
# 4. ELENCARE I FILE DI UNA CARTELLA
# ------------------------------------------------------------

# iterdir() scorre tutti gli elementi dentro una cartella
# restituisce oggetti Path — uno per ogni file o sottocartella

# giro 1: elemento è il primo file  → controllo → stampa o salta
# giro 2: elemento è il secondo     → stesso controllo → ...
# continua finché non ha visto tutti gli elementi

print("\nFile .py in questa cartella:")

cartella_script = Path(__file__).parent

for elemento in cartella_script.iterdir():
    if elemento.is_file() and elemento.suffix == ".py":
        print(f"  {elemento.name}")

# se vuoi anche la dimensione in byte
print("\nCon dimensione:")
for elemento in cartella_script.iterdir():
    if elemento.is_file() and elemento.suffix == ".py":
        dimensione = elemento.stat().st_size
        print(f"  {elemento.name:<40} {dimensione} byte")


# ------------------------------------------------------------
# 5. CREARE CARTELLE
# ------------------------------------------------------------

# mkdir() crea una cartella
# se esiste già lancia un errore — exist_ok=True lo evita
# parents=True crea anche le cartelle intermedie che mancano

nuova = Path("cartella_test")
nuova.mkdir(exist_ok=True)
print(f"\nCartella creata: {nuova.resolve()}")

# esempio: creare Archivio/2025/Foto in un colpo solo
struttura = Path("Archivio") / "2025" / "Foto"
struttura.mkdir(parents=True, exist_ok=True)
print(f"Struttura creata: {struttura.resolve()}")

# pulizia — rimuoviamo le cartelle di test
# (lo vediamo in dettaglio nella prossima lezione)
import shutil
if Path("cartella_test").exists():
    shutil.rmtree("cartella_test")
if Path("Archivio").exists():
    shutil.rmtree("Archivio")


# ============================================================
# ESERCIZI
# ============================================================
# 1. Controlla se la cartella "Documenti" nella home esiste
#    (usa Path.home() / "Documenti").
#    Se esiste, stampa "Trovata" e il percorso assoluto.
#    Se non esiste, stampa "Non trovata".
#
# 2. Elenca tutti i file .py nella cartella di questo script
#    (usa Path(__file__).parent).
#    Per ognuno stampa: nome (senza estensione) e dimensione
#    in byte (usa .stat().st_size).
#
# 3. Scrivi una funzione crea_struttura_progetto(nome) che
#    riceve il nome di un progetto e crea questa struttura
#    nella cartella corrente:
#       NomeProgetto/
#           dati/
#           output/
#           immagini/
#    Usa mkdir(parents=True, exist_ok=True) per ogni cartella.
#    Testa la funzione con crea_struttura_progetto("ProvaFinale").
# ============================================================
