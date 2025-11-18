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

msg = [ color('[ERROR]','red') + ' - Incorrect path or Unavailable file !',
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
        color('[NOTICE]', 'cyan') + ' - Please provide the \033[1mCSV file\033[0m with the following format:\n' + #[19]
            color('[NOTICE]', 'cyan') + ' - ' +
            color('\033[1mId(int)\033[0m', 'yellow') + ';' +
            color('\033[1msearch_Key(any)\033[0m', 'green') + ';' +
            color('\033[1mmin_lght_key(second)\033[0m', 'blue') + ';' +
            color('\033[1mdate_Key(YYYY-MM-DD)\033[0m', 'purple') + ';' +
            color('\033[1mmin_size_Key(octet)\033[0m', 'cyan') + ';\n' +
            color('[NOTICE]', 'cyan') + ' - ' +
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
