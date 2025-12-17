import os, time

# Componentes
from components.settings import default_cmds, script_cmds, fg_text, fg_error, fg_success, fg_info, VERSION, AUTHOR, TITLE
from components.functions import input_cmd, alert, run_module, run_module_admin

def TITLE_BANNER():
    return f"""{fg_error}
                              ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                              ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                              ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
                    {fg_text}Developed by {fg_error}{AUTHOR} {fg_text}- ver. {fg_error}{VERSION} ({fg_success}remaster{fg_error})"""

# Menu de ajuda e lista de comandos
def help_menu():
    all_cmd_list = {**default_cmds, **script_cmds} # Junta todos os comandos em um único dicionário.
    print(f"""
    Bem-vindo ao menu de ajuda da ferramenta.

    {fg_text}Lista de comandos:""")
    for cmd, desc in all_cmd_list.items():
        print(f"{fg_error}[{fg_text}{cmd}{fg_error}] >> {fg_text}{desc}")

# Comandos padrões
def default(args):
    if args[0] == 'exit': # EXIT
        alert('info', "Saindo...")
        exit()
        return

    elif args[0] == 'restart': # RESTART
        alert('info', "Reiniciando a ferramenta em alguns segundos...")
        time.sleep(2)
        run_module('main')
        exit()

    elif args[0] == 'help': # HELP
        help_menu()
        return

    elif args[0] == 'clear': # CLEAR
        os.system('cls')
        print(TITLE_BANNER())
        return

    else:
        return

# Comandos de Scripts
def scripts(args):
    if args[0] == 'cleartempfiles': # CLEAR TEMP FILES
        run_module_admin('default_cmds.cleartempfiles')

    elif args[0] == 'downloader': # DOWNLOADER
        run_module('default_cmds.downloader')

    elif args[0] == 'filebrowser':
        os.system(r'start src\default_cmds\filebrowser.bat')

    else:
        return

class Main:
    def __init__(self):
        os.system(f'cls && title {TITLE}')
        print(TITLE_BANNER())
        self.commands()

    def commands(self):
        while True:
            args = input_cmd()
            if not args:
                alert('error', f"{fg_text}Nenhum comando foi digitado! Tente usar [ {fg_error}help {fg_text}].")
            
            elif args[0] in default_cmds:
                default(args)

            elif args[0] in script_cmds:
                scripts(args)

            else:
                alert('error', "Esse comando não existe!")

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        alert('info', "Saindo...")
