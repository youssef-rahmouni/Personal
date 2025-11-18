import datetime
from msg import msg

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
def get_Keys():
    global search_Key, min_lght_Key, date_Key, min_size_Key
    search_Key = CheckInput(input(msg[13]), "str")
    min_lght_Key = CheckInput(input(msg[16]), "int")
    date_Key = CheckInput(input(msg[15]), "date")
    min_size_Key = CheckInput(input(msg[14]), "int")
    if min_lght_Key is None:
        min_lght_Key = 580
    

def AutoSearch():
    while True:
        search_type = input(msg[20])
        if search_type == "1":
            return True  
        elif search_type == "2":
            return get_Keys()
            
        else:
            print(msg[7])

AutoSearch()
list = [search_Key, min_lght_Key, date_Key, min_size_Key]
for i in list:
    print(i)

