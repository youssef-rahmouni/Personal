from tools import *

while quit != 'x':

    to_recover_Path, src_dir_Path, out_result_Path = get_Paths()
    out_items_find = os.path.join(out_result_Path, 'items_finds')
    if not os.path.isdir(out_items_find):
        os.mkdir(out_items_find)
    if auto_search is True:
        find_CSV(src_dir_Path, search_Key_CSV, min_lght_Key_CSV, date_Key_CSV, min_size_Key_CSV)
    else:
        find(src_dir_Path, search_Key, min_lght_Key, date_Key, min_size_Key)

    for item in items_find:
        try:
            shutil.copy2(item, out_items_find)
            print(msg[3].format(os.path.basename(item), out_items_find))
        except Exception as e:
            print(msg[2].format(os.path.basename(item), e))

    quit = input(msg[11]).lower().strip()


            

            