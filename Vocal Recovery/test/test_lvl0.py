import os
from pathlib import Path
import datetime
import mutagen

def isVocal(file):
    audio_ext = audi_ext = [
    ".mp3", ".wav", ".flac", ".ogg", ".oga",
    ".aac", ".mp4", ".m4b",".ape",".caf",
    ".wma", ".alac", ".opus",".aifc",
    ".amr", ".aiff", ".aif", ".3gp", ".au"
    ]
    if os.path.splitext(file)[1] in audio_ext :
        return True
    
def CheckInput(value, expected):
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

    return None



search_Key = CheckInput(input("Enter keyword: "), "str")
min_size_Key = CheckInput(input("Enter min size with octet (default. Ignore): "), "int")
date_Key = CheckInput(input("Enter min date YYYY-MM-DD (default. Ignore): "), "date")
min_lght_Key = CheckInput(input("Enter min duration in seconds (default 580): "), "int")
if min_lght_Key is None:
    min_lght_Key = 580

result = []
for f in Path(os.getcwd()).rglob('*'):
    if os.path.isfile(f):
        name_match = search_Key.lower() in f.name.lower()
        size_match = (min_size_Key is None or os.stat(f).st_size >= min_size_Key)
        date_match = (date_Key is None or datetime.datetime.fromtimestamp(os.stat(f).st_mtime).strftime('%Y-%m-%d') == date_Key )
        lght_match = True
        if isVocal(f): 
            lght_match = (min_lght_Key == 580 or mutagen.File(f).info.length >= int(min_lght_Key))
        if name_match and size_match and date_match and lght_match :
            result.append(f)  

