##🎧 Vocal-Recovery

A lightweight Python tool that helps recover lost audio recordings by scanning large folders, backups, or server volumes.
Instead of relying on filenames, it filters audio files using metadata such as:

- Duration (seconds)
- File size
- Creation/recording date
- Optional keyword matching

This makes it especially useful for call centers, technicians, or anyone trying to recover specific voice notes or call recordings from messy storage.

📂 Project Structure
Vocal-Recovery/
│
├── main.py             # Entry point – start the program from here
├── tools.py            # Core logic (find, find_CSV, CheckInput, etc.)
├── msg.py              # UI messages, colored prompts, formatting
├── CallsList.csv       # Database for Auto-Search mode
├── ToDo                # Future features, improvements, bug notes
│
└── tests/              # Suggested test folder
    ├── test_lvl0.py
    ├── testlvl1.py
    └── testlvl2.py


##🚀 How It Works

Choose Auto Search (using the CSV database)
or Manual Search (enter duration, size, date yourself).

The program scans the chosen directory and checks each audio file’s metadata.

Matching files are copied to the out_record/items_finds/ folder.

##📌 Notes

This project is still evolving. Check the ToDo file for upcoming features.
