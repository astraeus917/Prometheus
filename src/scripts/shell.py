import os, sys
from colorama import Fore as fg

# Fixes the directory to use the main features of the tool.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from functions import alert
from settings import _gettext


# Tool details:
title = 'Astraeus Shell'
author = 'Astraeus'
version = '1.0'


# Colors variables:
fg_one = fg.RED
fg_text = fg.WHITE
fg_two = fg.YELLOW


# Command list:
default = {
    'exit': "to exit tool",
    '--help': "show help menu",
    'clear': "limpar tela",
    'cd': "",
    'ls': "",
}


def MAIN_BANNER():
    return f"""{fg_one}
                            ┏┓┏┓┏┳┓┳┓┏┓┏┓┳┳┏┓  ┏┓┓┏┏┓┓ ┓ 
                            ┣┫┗┓ ┃ ┣┫┣┫┣ ┃┃┗┓  ┗┓┣┫┣ ┃ ┃ 
                            ┛┗┗┛ ┻ ┛┗┛┗┗┛┗┛┗┛  ┗┛┛┗┗┛┗┛┗┛
                            {fg_text} Powered by Scyphos Project."""


def HELP_BANNER():
    return f"""
    list of basic commands:
    {default}
    """


class main:
    def __init__(self):
        os.system(f'cls && title {title}')
        print(MAIN_BANNER())
        self.input_commands()


    def input_commands(self):
        # Tool variables.
        user = os.getlogin()
        current_path = os.getcwd()
        current_dir = os.path.basename(current_path)

        while True:
            print(f"\n {fg_one}┌─[{fg_text}{user}{fg_one}]~({fg_text}{current_dir}{fg_one})")
            cmd = input(f" {fg_one}└──╼ ⌁ {fg_one}{fg_text}")
            print()

            # Exec commands.
            args = cmd.split()
            try:
                if args[0] in default:
                    self.default_commands(args)

                else:
                    self.exec_command(cmd)

            except Exception as error:
                # Exibe um aviso se o erro for falta de argumentos.
                if 'list index out of range' in str(error):
                    alert('info', _gettext("Try using the [help] command."))

                else:
                    alert('error', error)

    
    def default_commands(self, args):
        if args[0] == 'exit':
            alert('info', _gettext("Exiting..."))
            sys.exit()

        elif args[0] == '--help':
            print(HELP_BANNER())

        elif args[0] == 'clear':
            main()

        elif args[0] == 'cd':
            os.chdir(args[1])
            main()

        elif args[0] == 'ls':
            list_dir = os.listdir()
            for i in list_dir:
                print(i)
        
        else:
            return

    def exec_command(self, cmd):
        try:
            os.system(cmd)

        except KeyboardInterrupt:
            return

        except Exception as error:
            alert('error', error)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        alert('info', _gettext("Exiting..."))
        sys.exit()


