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
```

Vocal-Recovery/
│
├── main.py             # The main script you run to start the program
├── tools.py            # Contains core functions (find, find_CSV, checkInput)
├── msg.py              # Handles UI text colors and message prompts
├── CallsList.csv       # The example file for "Auto Search" mode (You should use youre own)
├── ToDo                # Your list of future features and fixes
│
├── tests/              # (Suggested grouping for your test files)
│   ├── test_lvl0.py
│   ├── testlvl1.py
│   └── testlvl2.py
│
└── out_record/         # (Created automatically when running the app)
    └── items_finds/    # Where found audio files are copied
```

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
