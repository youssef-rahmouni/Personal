# This file have variables,data,functions that VocalRecover.py need (it used for test)

## LIBRARYS
import os
import csv
import shutil
from pathlib import Path
import datetime
import mutagen
from msg import msg

## FUNCTIONS 1 (This function comme after VARIABLES because it's need them)
def color(txt,color):
    colors = {
        "red": "\033[1;31m",
        "green": "\033[1;32m",
        "yellow": "\033[1;33m",
        "blue": "\033[1;34m",
        "purple": "\033[1;35m",
        "cyan": "\033[1;36m",
        "white": "\033[1;37m",
        "reset": "\033[0m"
    }
    return f'{colors.get(color, colors['reset'])}{txt}{colors['reset']}'

def AutoSearch():
    while True:
        search_type = input(msg[20])
        if search_type == "1":
            return True  
        elif search_type == "2":
            return get_Keys()  
        else:
            print(msg[8])


## VARIABLES & LISTS
auto_search = AutoSearch()
search_Key_CSV = []
min_lght_Key_CSV =[]
date_Key_CSV =[]
min_size_Key_CSV = []
items_find = []
quit = None
'''msg = [ color('[ERROR]','red') + ' - Incorrect path or Unavailable file !',
        color('[NOTICE]','cyan') + ' - Item is set to \033[1m{}\033[0m',
        color('[ERROR]','red') + ' - Failed copying file \033[1m{}\033[0m — \033[1m{}\033[0m',
        color('[SUCCESS]','green') + ' - Item \033[1m{}\033[0m was copy successfully to \033[1m{}\033[0m',
        color('[INPUT]','purple') + ' - Enter path for \033[1mCSV file\033[0m (\x1B[3mex. C:/Documnets/calls.csv\x1B[0m) : ',
        color('[INPUT]','purple') + ' - Enter path for \033[1mSearch directory\033[0m (default. \033[1m{}\033[0m) : ',
        color('[INPUT]','purple') + ' - Enter path for \033[1mOutput folder\033[0m (default. \033[1m{}\033[0m) : ',
        color('[NOTICE]', 'cyan') + ' - Please confirm that all information is correct\n' + 
            color('[NOTICE]', 'cyan') + ' - CSV file         : \033[1m{}\033[0m\n' + 
            color('[NOTICE]', 'cyan') + ' - Search directory : \033[1m{}\033[0m\n' + 
            color('[NOTICE]', 'cyan') + ' - Output folder    : \033[1m{}\033[0m\n' + 
            color('  [1] ', 'cyan') + 'Yes, all information is correct\n' + 
            color('  [2] ', 'cyan') + 'No, please re-enter\n' + 
            color('[INPUT]', 'purple') + ' - Your Choice: ',
        color('[ERROR]','red') + ' - Invalid input, Please Choise (1 or 2 ) !',
        color('[NOTICE]','cyan') + " - Let's Start Agains",
        color('[NOTICE]','cyan') + " - File dosen't exists \033[1m{}\033[0m",
        color('[NOTICE]', 'cyan') + ' - Would you like to start a new search or exit?\n' +
            color('  [1] ', 'cyan') + 'Start a New Search\n' +
            color('  [X] ', 'cyan') + 'Exit the Program\n' +
            color('[INPUT]', 'purple') + ' - Your Choice (1 or X): ',
        color('\n\n[[ VOCAL RECOVERY ]]\n', 'yellow'), #[12]
        color('[INPUT]', 'purple') + ' - Enter \033[1mKeyword\033[0m to search (\x1B[3mex. mp3, 3310...\x1B[0m) : ',
        color('[INPUT]', 'purple') + ' - Enter \033[1mMin Size\033[0m in octets (default. Ignore) : ',
        color('[INPUT]', 'purple') + " - Enter \033[1mMin Date\033[0m with format 'YYYY-MM-DD' (default. Ignore) : ",
        color('[INPUT]', 'purple') + ' - Enter \033[1mMin Duration\033[0m in seconds (default. \033[1m580\033[0m) : ',
        color('[ERROR]', 'red') + ' - Invalid value, please enter a correct \033[1m{}\033[0m !',
        color('[NOTICE]', 'cyan') + ' - \033[1m{}\033[0m is set to \033[1m{}\033[0m',
        color('[INFO]', 'cyan') + ' - Please provide the \033[1mCSV file\033[0m with the following format:\n' + #[19]
            color('[INFO]', 'cyan') + ' - ' +
            color('\033[1mId(int)\033[0m', 'yellow') + ';' +
            color('\033[1msearch_Key(any)\033[0m', 'green') + ';' +
            color('\033[1mmin_lght_key(second)\033[0m', 'blue') + ';' +
            color('\033[1mdate_Key(YYYY-MM-DD)\033[0m', 'purple') + ';' +
            color('\033[1mmin_size_Key(octet)\033[0m', 'cyan') + ';\n' +
            color('[INFO]', 'cyan') + ' - ' +
            color('\033[1m1\033[0m', 'yellow') + ';' +
            color('\033[1m.mp3\033[0m', 'green') + ';' +
            color('\033[1m600\033[0m', 'blue') + ';' +
            color('\033[1m2025-10-23\033[0m', 'purple') + ';' +
            color('\033[1m1000000\033[0m', 'cyan') + '\n' +
            color('[NOTICE]', 'cyan') + ' - Invalid or empty values will be ignored silently, only valid entries are processed.',
        color('[NOTICE]', 'cyan') + ' - Choose Search Mode:\n' + #[20]
            color('  [1] ', 'cyan') + 'Auto Search using \033[1mCSV file with Search Keys\033[0m\n' +
            color('  [2] ', 'cyan') + 'Manual Search by entering \033[1mSearch Keys manually\033[0m\n' +
            color('[INPUT]', 'purple') + ' - Enter your choice (1 or 2): '
        ]
'''
## FUNCTIONS 2


def find(src_dir_find, search_Key_find, min_lght_Key_find, date_Key_find, min_size_Key_find):
    for f in Path(src_dir_find).rglob('*'):
        if os.path.isfile(f):
            name_match = search_Key_find.lower() in f.name.lower()
            size_match = (min_size_Key_find is None or os.stat(f).st_size >= min_size_Key_find)
            date_match = (date_Key_find is None or datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y-%m-%d') == date_Key_find )
            lght_match = True
            if isVocal(f): 
                lght_match = (min_lght_Key_find == 580 or mutagen.File(f).info.length >= int(min_lght_Key_find))
            if name_match and size_match and date_match and lght_match :
                items_find.append(f)  
    return items_find

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

def isVocal(file):
    audio_ext = [
    ".mp3", ".wav", ".flac", ".ogg", ".oga",
    ".aac", ".mp4", ".m4b",".ape",".caf",
    ".wma", ".alac", ".opus",".aifc",
    ".amr", ".aiff", ".aif", ".3gp", ".au"
    ]
    if os.path.splitext(file)[1] in audio_ext :
        return True
    
def CheckInput(value, expected):
    if value is None :
        return None
    if value.strip() == '':
        return None
    if expected == "int":
        return int(value) if value.isdigit() else None
    if expected == "date":
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
            return value
        except:
            return None
    if expected == "str":
        return value

def get_Paths():
    if auto_search is True:
        while True:
            print(msg[19])
            to_recover_Path = input(msg[4])
            if os.path.isfile(to_recover_Path):
                print(msg[1].format(to_recover_Path))
                break
            print(msg[0])

    while True:
        default_src_dir_Path = 'F:\\'
        src_dir_Path = input(msg[5].format(default_src_dir_Path))
        if src_dir_Path.strip() == '':
            src_dir_Path = default_src_dir_Path
        if os.path.isdir(src_dir_Path) :
            print(msg[1].format(src_dir_Path))
            break
        print(msg[0])

    while True:
        out_result_Path = input(msg[6].format(os.path.join(os.getcwd(), 'out_result_Path')))
        if out_result_Path.strip() == '':
            out_result_Path = os.path.join(os.getcwd(), 'out_result_Path')
            if not os.path.isdir(out_result_Path):
                os.mkdir(out_result_Path)
        if os.path.isdir(out_result_Path):
            print(msg[1].format(out_result_Path))
            break
        print(msg[0])

    while True:
        confirm = input(msg[7].format(  
            os.path.abspath(to_recover_Path), 
            os.path.abspath(src_dir_Path), 
            os.path.abspath(out_result_Path))).strip().lower()
        if confirm == "1":
            return to_recover_Path, src_dir_Path, out_result_Path
        elif confirm == "2":
            print(msg[9])
            return get_Paths()
        else :
            msg[8]

def get_Keys():
    global search_Key, min_lght_Key, date_Key, min_size_Key
    search_Key = CheckInput(input(msg[12]), "str")
    min_lght_Key = CheckInput(input(msg[15]), "int")
    date_Key = CheckInput(input(msg[14]), "date")
    min_size_Key = CheckInput(input(msg[13]), "int")
    if min_lght_Key is None:
        min_lght_Key = 580

def ExtractKeysCSV(file_CSV):
    with open(file_CSV, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader :
            search_Key_CSV.append(row[1])
            min_lght_Key_CSV.append(row[2])
            date_Key_CSV.append(row[3])
            min_size_Key_CSV.append(row[4])


