# 🎧 Vocal-Recovery

A lightweight Python tool designed to **recover lost audio recordings** by scanning large folders, backups, or server volumes.  
Instead of relying on filenames, it filters audio files using **metadata**, including:

- Duration (seconds)
- File size
- Creation/recording date
- Optional keyword matching

This makes it especially useful for call centers, technicians, and anyone trying to recover specific voice notes or call recordings from messy storage.

---

## 📂 Project Structure

Vocal-Recovery/
│
├── src/
│   └── vocal_recovery/
│       ├── __init__.py
│       ├── main.py          # Entry point
│       ├── tools.py         # Core logic
│       ├── msg.py           # UI messages
│       └── CallsList.csv    # Static resource
│
├── data/
│   ├── out_record/          # Created at runtime
│   └── items_finds/         # Recovered audio files
│
├── tests/
│   ├── test_lvl0.py
│   ├── test_lvl1.py
│   └── test_lvl2.py
│
├── legacys/                 # Old archived code
├── ToDo                     # Notes
└── pyproject.toml / requirements.txt


---

## 🚀 How It Works

1. Choose **Auto Search** (uses file like `CallsList.csv`)  
   or **Manual Search** (enter duration, size, and date manually).

2. The program scans your selected directory and analyzes each audio file’s metadata.

3. Files that match your criteria are copied into the  
   **`out_record/items_finds/`** folder.

---

## 📌 Notes

This project is under active development.  
Check the **ToDo** file for upcoming improvements and planned features.
