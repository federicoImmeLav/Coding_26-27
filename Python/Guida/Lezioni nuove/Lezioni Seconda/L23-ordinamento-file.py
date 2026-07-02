# ============================================================
# LEZIONE 23 — Esplorare e ordinare i file di una cartella
# Unità 1-bis · Settimana 3-bis (pratica in classe)
# ============================================================
# Prerequisiti: L21 (pathlib, iterdir, stat), L22 (shutil, move)
# Obiettivo: lo studente sa ordinare una lista di file per nome,
# dimensione, estensione e data usando sorted() con key=,
# e sa raggruppare i file in un dizionario per categoria.
# ============================================================
#
# MATERIALE: apri la cartella materiale_L23/cartella_caotica/
# e osservala prima di eseguire questo file.
# ============================================================


from pathlib import Path

# percorso della cartella di esempio — funziona da qualsiasi
# punto in cui esegui lo script, perché usa __file__
CARTELLA = Path(__file__).parent / "materiale_L23" / "cartella_caotica"


# ------------------------------------------------------------
# 1. ESPLORIAMO LA CARTELLA — quello che già sappiamo
# ------------------------------------------------------------

# iterdir() restituisce tutti gli elementi in ordine di filesystem:
# l'ordine dipende dal sistema operativo, non dall'alfabeto
print("=== Contenuto grezzo ===")
for f in CARTELLA.iterdir():
    kb = f.stat().st_size / 1024
    print(f"  {f.name:<40}  {kb:6.1f} KB")

# risultato: i file appaiono in ordine casuale
# non è sbagliato — è semplicemente l'ordine in cui il disco li tiene
# per visualizzarli in modo utile dobbiamo ordinarli noi


# ------------------------------------------------------------
# 2. ORDINARE PER NOME — sorted() sui percorsi
# ------------------------------------------------------------

# sorted() sa già ordinare stringhe alfabeticamente:
parole = ["zebra", "albero", "mela", "gatto"]
print(sorted(parole))   # ['albero', 'gatto', 'mela', 'zebra']

# con i Path funziona allo stesso modo: li confronta come testo
# e li mette in ordine alfabetico per percorso completo
print("\n=== Ordinati per nome (A -> Z) ===")
for f in sorted(CARTELLA.iterdir()):
    print(f"  {f.name}")

# reverse=True inverte l'ordine
print("\n=== Ordinati per nome (Z -> A) ===")
for f in sorted(CARTELLA.iterdir(), reverse=True):
    print(f"  {f.name}")


# ------------------------------------------------------------
# 3. ORDINARE PER DIMENSIONE — il parametro key=
# ------------------------------------------------------------

# il problema: sorted() confronta gli oggetti Path tra loro
# ma noi vogliamo confrontare le loro DIMENSIONI
# come diciamo a sorted "usa la dimensione, non il nome"?

# --- prima soluzione: una funzione come chiave ---
# key= accetta una funzione: la applica a ogni elemento
# e usa il valore restituito per il confronto

# passo 1: scrivi la funzione che estrae il dato che ti interessa
def dimensione_in_byte(file):
    return file.stat().st_size

# passo 2: passala a sorted con key=
# sorted ora: prende ogni file -> chiama dimensione_in_byte(file)
#             -> ottiene un numero -> confronta i numeri
file_per_dim = sorted(CARTELLA.iterdir(), key=dimensione_in_byte)

print("\n=== Ordinati per dimensione (piccoli prima) ===")
for f in file_per_dim:
    kb = f.stat().st_size / 1024
    print(f"  {kb:7.1f} KB  {f.name}")

# i più grandi prima: basta reverse=True
print("\n=== I 5 file più grandi ===")
file_per_dim_desc = sorted(CARTELLA.iterdir(), key=dimensione_in_byte, reverse=True)
for f in file_per_dim_desc[:5]:
    kb = f.stat().st_size / 1024
    print(f"  {kb:7.1f} KB  {f.name}")


# ------------------------------------------------------------
# 4. lambda — scrivere la chiave in una riga
# ------------------------------------------------------------

# dimensione_in_byte() è una funzione breve che esiste solo
# per essere passata a sorted: non la usiamo da nessun'altra parte.
# Python permette di scrivere funzioni semplici come questa in una riga:
#
#   lambda parametro: espressione da restituire
#
# è identica a:
#   def nome_qualsiasi(parametro):
#       return espressione

# con def:
# def dim(f): return f.stat().st_size
# sorted(files, key=dim)

# con lambda (stesso risultato, una riga):
# sorted(files, key=lambda f: f.stat().st_size)

# si legge: "per ogni f, usa f.stat().st_size come chiave di confronto"

# regola pratica: usa lambda quando la funzione è piccola e la usi
# solo in quel punto. Se la riusi o è complessa, usa def.

# --- ordinare per estensione con lambda ---
print("\n=== Ordinati per estensione ===")
per_estensione = sorted(CARTELLA.iterdir(), key=lambda f: f.suffix)
for f in per_estensione:
    print(f"  {f.suffix:<8}  {f.name}")

# --- ordinare per estensione, poi per nome a parità di estensione ---
# key= può restituire una TUPLA: Python confronta prima il primo
# elemento, poi il secondo in caso di parità
print("\n=== Ordinati per estensione poi per nome ===")
per_ext_nome = sorted(CARTELLA.iterdir(), key=lambda f: (f.suffix, f.name))
for f in per_ext_nome:
    print(f"  {f.suffix:<8}  {f.name}")


# ------------------------------------------------------------
# 5. ORDINARE PER DATA — st_mtime
# ------------------------------------------------------------

# stat() restituisce anche la data di ultima modifica: st_mtime
# è un numero (secondi dal 1 gennaio 1970): più grande = più recente

import time

print("\n=== Ordinati per data (più recenti prima) ===")
per_data = sorted(CARTELLA.iterdir(), key=lambda f: f.stat().st_mtime, reverse=True)
for f in per_data[:8]:
    timestamp = f.stat().st_mtime
    # ctime converte il numero in una stringa leggibile
    data = time.ctime(timestamp)
    print(f"  {data}  {f.name}")


# ------------------------------------------------------------
# 6. RAGGRUPPARE PER ESTENSIONE — dizionario di liste
# ------------------------------------------------------------

# ordinare è utile, ma spesso vogliamo anche RAGGRUPPARE:
# "tutti i .jpg insieme, tutti i .pdf insieme, ecc."
# uno strumento perfetto per questo è il dizionario

# --- come funziona il pattern "accumula in un dizionario" ---
# passo 1: dizionario vuoto
# passo 2: per ogni file, guarda l'estensione
# passo 3: se l'estensione non è ancora una chiave, aggiungila con []
# passo 4: aggiungi il file alla lista di quella chiave

gruppi = {}

for f in CARTELLA.iterdir():
    ext = f.suffix.lower()          # .JPG e .jpg -> stesso gruppo
    if ext not in gruppi:
        gruppi[ext] = []
    gruppi[ext].append(f)

# ora gruppi è un dizionario tipo:
# {".jpg": [Path(...), Path(...), ...], ".pdf": [...], ...}

print("\n=== File raggruppati per estensione ===")
for ext in sorted(gruppi):
    file_gruppo = gruppi[ext]
    totale_kb   = sum(f.stat().st_size for f in file_gruppo) / 1024
    print(f"  {ext:<8}  {len(file_gruppo):2} file  {totale_kb:7.1f} KB totali")
    for f in sorted(file_gruppo):
        kb = f.stat().st_size / 1024
        print(f"           {f.name:<38} {kb:6.1f} KB")


# ------------------------------------------------------------
# 7. FUNZIONE REPORT — tutto insieme
# ------------------------------------------------------------

def report_cartella(percorso):
    cartella = Path(percorso)
    if not cartella.is_dir():
        print(f"Cartella non trovata: {cartella}")
        return

    tutti  = [f for f in cartella.iterdir() if f.is_file()]
    totale = sum(f.stat().st_size for f in tutti)

    print(f"\n{'='*55}")
    print(f"  Cartella: {cartella.name}")
    print(f"  File totali:   {len(tutti)}")
    print(f"  Spazio totale: {totale / 1024:.1f} KB")
    print(f"{'='*55}")

    # top 3 più grandi
    print("  File più grandi:")
    for f in sorted(tutti, key=lambda f: f.stat().st_size, reverse=True)[:3]:
        print(f"    {f.stat().st_size/1024:7.1f} KB  {f.name}")

    # riepilogo per estensione
    gruppi = {}
    for f in tutti:
        ext = f.suffix.lower()
        gruppi.setdefault(ext, []).append(f)

    print("  Per estensione:")
    for ext in sorted(gruppi):
        n  = len(gruppi[ext])
        kb = sum(f.stat().st_size for f in gruppi[ext]) / 1024
        print(f"    {ext:<8}  {n:2} file  {kb:7.1f} KB")

    print(f"{'='*55}")

report_cartella(CARTELLA)


# ============================================================
# ESERCIZI
# ============================================================
# 1. Stampa solo i file .txt della cartella_caotica, ordinati
#    per dimensione dal più piccolo al più grande.
#    Per ognuno mostra nome e dimensione in byte.
#
# 2. Scrivi una funzione file_piu_vecchio(percorso) che riceve
#    il percorso di una cartella e restituisce il Path del file
#    con la data di modifica più antica (usa st_mtime).
#    Testa la funzione su cartella_caotica.
#
# 3. Scrivi una funzione duplica_struttura(sorgente, destinazione)
#    che legge tutti i file di "sorgente", li raggruppa per
#    estensione e crea nella cartella "destinazione" una
#    sottocartella per ogni estensione trovata (solo le cartelle,
#    non copiare i file).
#    Usa mkdir(parents=True, exist_ok=True).
#    Testa la funzione con cartella_caotica come sorgente e
#    "struttura_vuota" come destinazione.
# ============================================================
