# ============================================================
# SCRIPT DI SETUP — genera la cartella di esempio per L23
# Eseguire UNA VOLTA prima della lezione:
#   python crea_cartella.py
# ============================================================
# Crea "cartella_caotica/" con 20 file di dimensioni diverse,
# simulando una cartella Download disordinata.
# I file sono testo ASCII, non file binari veri.
# ============================================================

from pathlib import Path

CARTELLA = Path("cartella_caotica")
CARTELLA.mkdir(exist_ok=True)


def crea_fake(nome, kb):
    """Crea un file con contenuto fittizio di circa kb kilobyte."""
    header = f"[FILE DI ESEMPIO - {nome}]\n"
    riga   = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-\n"
    righe  = max(1, (kb * 1024 - len(header)) // len(riga))
    (CARTELLA / nome).write_text(header + riga * righe, encoding="utf-8")


def crea_testo(nome, contenuto):
    (CARTELLA / nome).write_text(contenuto, encoding="utf-8")


# --- file di testo con contenuto reale ---
crea_testo("lista_spesa.txt",
    "Lista della spesa\n"
    "- pane\n- latte\n- uova\n- pasta\n- pomodori\n- olio\n")

crea_testo("appunti_storia.txt",
    "Appunti di storia — Rinascimento\n\n"
    "Il Rinascimento è un periodo storico che va dal XIV al XVII secolo.\n"
    "Nasce in Italia e si diffonde in tutta Europa.\n\n"
    "Caratteristiche principali:\n"
    "- Ritorno ai valori della classicità greca e romana\n"
    "- Fiducia nell'uomo e nella ragione (Umanesimo)\n"
    "- Grande sviluppo delle arti: pittura, scultura, architettura\n"
    "- Protagonisti: Leonardo da Vinci, Michelangelo, Raffaello\n\n"
    "Date importanti:\n"
    "- 1452: nascita di Leonardo da Vinci\n"
    "- 1492: scoperta dell'America da parte di Colombo\n"
    "- 1517: Riforma protestante di Lutero\n")

crea_testo("compiti_matematica.txt",
    "Esercizi di matematica — capitolo 5\n\n"
    "1. Calcola il perimetro di un rettangolo con base 12 cm e altezza 7 cm.\n"
    "   Soluzione: P = 2*(12+7) = 38 cm\n\n"
    "2. Qual è l'area di un cerchio con raggio 5 cm?\n"
    "   Soluzione: A = pi * r^2 = 3.14 * 25 = 78.5 cm²\n\n"
    "3. Risolvi l'equazione: 3x + 7 = 22\n"
    "   Soluzione: 3x = 15, x = 5\n\n"
    "4. Semplifica la frazione 18/24.\n"
    "   Soluzione: MCD(18,24) = 6, risultato = 3/4\n")

crea_testo("bozza_presentazione.txt",
    "PRESENTAZIONE PROGETTO FINALE — bozza\n\n"
    "Titolo: Sistema di gestione biblioteca scolastica\n"
    "Autore: Marco Rossi, classe 3B\n\n"
    "INTRODUZIONE\n"
    "Il progetto consiste in un programma Python per gestire\n"
    "il prestito dei libri della biblioteca scolastica.\n\n"
    "FUNZIONALITÀ PREVISTE\n"
    "- Aggiunta di nuovi libri al catalogo\n"
    "- Registrazione dei prestiti (chi ha preso quale libro)\n"
    "- Restituzione dei libri con aggiornamento automatico\n"
    "- Ricerca per titolo, autore o categoria\n"
    "- Report mensile dei libri più richiesti\n\n"
    "STRUTTURA DEL CODICE\n"
    "- Classe Libro: titolo, autore, disponibile (bool)\n"
    "- Classe Biblioteca: lista di libri, metodi per cercare/prestare\n"
    "- File JSON per salvare lo stato tra una sessione e l'altra\n"
    "- Menu testuale principale\n\n"
    "TODO\n"
    "- Aggiungere la gestione delle date di restituzione\n"
    "- Creare la funzione di report\n"
    "- Testare con dati reali della biblioteca\n")

# --- file simulati con dimensioni crescenti ---
crea_fake("foto_compleanno.jpg",       1)
crea_fake("screenshot_partita.jpg",    2)
crea_fake("foto_gita_scolastica.jpg",  3)
crea_fake("selfie_spiaggia.jpg",       5)
crea_fake("vacanze_luglio.jpg",        8)
crea_fake("canzone_estate.mp3",       10)
crea_fake("programma_gita.pdf",       12)
crea_fake("archivio_vecchi.zip",      18)
crea_fake("progetto_informatica.pdf", 25)
crea_fake("relazione_chimica.pdf",    35)
crea_fake("backup_documenti.zip",     45)
crea_fake("tesina_italiano.pdf",      60)
crea_fake("tutorial_python.mp4",      90)
crea_fake("installer_vscode.exe",    110)
crea_fake("film_spiderman.mp4",      150)
crea_fake("setup_minecraft.exe",     200)

print(f"Cartella '{CARTELLA}' creata con {len(list(CARTELLA.iterdir()))} file.")
