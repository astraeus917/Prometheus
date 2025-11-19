# Components
from components.settings import *
from components.functions import *
from components.banners import *


def default(args):
    if args[0] == 'exit': # EXIT
        alert('info', "Exiting...")
        exit()
        return

    elif args[0] == 'help': # HELP
        all_cmd_list = {**default_cmds, **script_cmds} # Junta todos os comandos em um único dicionário
        print()
        for cmd, desc in all_cmd_list.items():
            print(f"{fg_success}{cmd}: {fg_text}{desc}")
        return


    elif args[0] == 'clear': # CLEAR
        os.system('cls')
        print(TITLE_BANNER())
        return
    
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