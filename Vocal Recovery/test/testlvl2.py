import os
from pathlib import Path
import datetime
import mutagen
import csv


search_Key_CSV = []
min_lght_Key_CSV =[]
date_Key_CSV =[]
min_size_Key_CSV = []
items_find = []
src_dir_Path = os.getcwd()

def isVocal(file):
    audio_ext = [
    ".mp3", ".wav", ".flac", ".ogg", ".oga",
    ".aac", ".mp4", ".m4b",".ape",".caf",
    ".wma", ".alac", ".opus",".aifc",
    ".amr", ".aiff", ".aif", ".3gp", ".au"
    ]
    if os.path.splitext(file)[1] in audio_ext :
        return True

def find_CSV(src_dir_find, search_Key_CSV_find, min_lght_Key_CSV_find, date_Key_CSV_find, min_size_Key_CSV_find):
    
    for f in Path(src_dir_find).rglob('*'):
        if os.path.isfile(f):
            # Loop through all the lists simultaneously
            for s_key, l_key, d_key, sz_key in zip(search_Key_CSV_find, min_lght_Key_CSV_find, date_Key_CSV_find, min_size_Key_CSV_find):
                
                # --- Your Exact Logic ---
                name_match = str(s_key).lower() in f.name.lower()
                
                # Handle None/Empty conversions safely inside the loop
                sz_val = int(sz_key) if sz_key and str(sz_key).isdigit() else None
                size_match = (sz_val is None or os.stat(f).st_size >= sz_val)
                
                date_match = (d_key is None or d_key == '' or datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y-%m-%d') == d_key)
                
                lght_match = True
                if isVocal(f):
                    l_val = int(l_key) if l_key and str(l_key).isdigit() else 580
                    try: lght_match = (l_val == 580 or mutagen.File(f).info.length >= l_val)
                    except: lght_match = False
                
                if name_match and size_match and date_match and lght_match:
                    items_find.append(f)
                    break # Found a match for this file, stop checking other keys, move to next file
                    
    return items_find

def ExtractKeysCSV(file_CSV):
    with open(file_CSV, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader :
            search_Key_CSV.append(row[1])
            min_lght_Key_CSV.append(row[2])
            date_Key_CSV.append(row[3])
            min_size_Key_CSV.append(row[4])
    
ExtractKeysCSV('CallsList.csv')
find_CSV(src_dir_Path, search_Key_CSV, min_lght_Key_CSV, date_Key_CSV, min_size_Key_CSV)

for i in items_find:
    print(i)
