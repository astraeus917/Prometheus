# Components
from components.settings import default_cmds, script_cmds, fg_text, fg_error, fg_success, fg_info
from components.functions import input_cmd, alert, run_script
from components.banners import TITLE_BANNER

# Others
import os


def default(args):
    if args[0] == 'exit': # EXIT
        alert('info', "Exiting...")
        exit()
        return

    elif args[0] == 'help': # HELP
        all_cmd_list = {**default_cmds, **script_cmds} # Junta todos os comandos em um único dicionário
        print(f"""
    Bem-vindo ao menu de ajuda da ferramenta.

{fg_error}Lista de comandos:""")
        for cmd, desc in all_cmd_list.items():
            print(f"{fg_error}[{fg_text}{cmd}{fg_error}] >> {fg_text}{desc}")
        return

    elif args[0] == 'clear': # CLEAR
        os.system('cls')
        print(TITLE_BANNER())
        return
    
    elif args[0] == 'cleartempfiles':
        run_script('cleartempfiles')
    
    else:
        return

def illegal(args):
    pass

class Main:
    def __init__(self):
        os.system('cls')
        print(TITLE_BANNER())
        self.commands()

    def commands(self):
        while True:
            args = input_cmd()
            if not args:
                alert('error', "Nenhum comando foi digitado!")
            
            elif args[0] in default_cmds:
                default(args)

            elif args[0] in script_cmds:
                illegal(args)

            else:
                alert('error', "Esse comando não existe!")

if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        alert('info', "Exiting...")