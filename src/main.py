from settings import *
from banners import MAIN_BANNER, HELP_BANNER
from functions import alert, _gettext


# INPUT COMMANDS:

# If you pay attention, the commands are divided into categories.
# To add categories and commands to these categories, visit 'src.settings' and 'src.functions'.

# To better organize user input, check if the command entered is in the list of any category.
# The command categories have been divided into functions.
# For example, the help command is in the 'default' category, thus directing it to the default_commands function.


class main:
    def __init__(self):
        os.system(f'cls && title {title} - {credit}')
        print(MAIN_BANNER())
        self.input_commands()


    def input_commands(self):
        while True:
            text = _gettext("Enter the command:")
            cmd = input(f"\n {fg_one}{text} {fg_text}")
            args = cmd.split() # separting the command into arguments.

            try:
                # Check the inserted commands by categories.
                # To better organize the code, the command structure should be divided into categories.
                
                if args[0] in default:
                    self.default_commands(args)

                elif args[0] in tools:
                    self.tool_commands(args)

                else:
                    alert('error', _gettext("Enter a valid command."))

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

        elif args[0] == 'clear':
            main()

        elif args[0] == 'help':
            HELP_BANNER()
        
        else:
            return


    def tool_commands(self, args):
        if args[0] == 'shell':
            alert('info', 'shell')

        elif args[0] == 'ytdownload':
            alert('info', 'ytdownload')
        
        else:
            return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        alert('info', _gettext("Exiting..."))
        sys.exit()


