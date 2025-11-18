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
├── main.py # Entry point – start the program from here
├── tools.py # Core logic (find, find_CSV, CheckInput, etc.)
├── msg.py # UI messages, colored prompts, formatting
├── CallsList.csv # Database for Auto-Search mode
├── ToDo # Future features, improvements, bug notes
│
├── tests/ # Suggested test folder
│ ├── test_lvl0.py
│ ├── testlvl1.py
│ └── testlvl2.py
│
├── legacys/ # Old archived code
│
└── out_record/ # Auto-created on first run
└── items_finds/ # Recovered audio files are stored here

yaml
Copy code

---

## 🚀 How It Works

1. Choose **Auto Search** (uses data from `CallsList.csv`)  
   or **Manual Search** (enter duration, size, and date manually).

2. The program scans your selected directory and analyzes each audio file’s metadata.

3. Files that match your criteria are copied into the  
   **`out_record/items_finds/`** folder.

---

## 📌 Notes

This project is under active development.  
Check the **ToDo** file for upcoming improvements and planned features.
