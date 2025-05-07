from settings import *
from banners import MAIN_BANNER, HELP_BANNER
from functions import alert, login, _gettext, cmd_info, load_scipt
import sys


class Main:
    def __init__(self):
        # If you don't want to use the "Login" function you can comment out the "self.login()" line.
        # login()

        # Calls the command input function.
        self.input_commands()

    # From here on, the functions below are used as command categories.
    def default_commands(self, args):
        if args[0] == 'exit':
            alert('info', _gettext("Exiting..."))
            sys.exit()

        elif args[0] == 'clear':
            os.system(f'cls && title {title}')
            print(MAIN_BANNER())

        elif args[0] == 'help':
            HELP_BANNER()
        
        else:
            return

    def tool_commands(self, args):
        if args[0] == 'shell':
            load_scipt('shell.py')

        elif args[0] == 'ytdownload':
            load_scipt('ytdownload.py')

        elif args[0] == 'cleartempfiles':
            load_scipt('cleartempfiles.py')
        
        else:
            return


    # Function where inputs and commands are processed.
    def input_commands(self):
        os.system(f'cls && title {title}')
        print(MAIN_BANNER())

        while True:
            print()
            text = _gettext(f"Enter the command:")
            cmd = input(f"{fg_one}({fg_text}{user}{fg_one})~ {text} {fg_text}")
            print()

            args = cmd.split() # separting the command into arguments.
            try:
                # Check the inserted commands by categories.
                # To better organize the code, the command structure should be divided into categories.

                if args[0] == 'about':
                    cmd_info(args[1])
                
                elif args[0] in default:
                    self.default_commands(args)

                elif args[0] in tools:
                    self.tool_commands(args)

                else:
                    alert('error', _gettext("Enter a valid command."))

            except Exception as error:
                # Displays a warning if the error is missing arguments.
                if 'list index out of range' in str(error):
                    alert('info', _gettext("Try using the [help] command."))

                else:
                    alert('error', error)


if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print()
        print()
        alert('info', _gettext("Exiting..."))
        sys.exit()


