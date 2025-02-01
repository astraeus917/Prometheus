

from src.settings import *
from src.banners import MAIN_BANNER, HELP_BANNER
from src.functions import *


# Set and load translation.
translation = gettext.translation("messages", localedir=locale_path, languages=[lang], fallback=True) 
translation.install()
_ = translation.gettext


class main:
    def __init__(self):
        os.system(f'cls && title {title} - {credit}')
        print(MAIN_BANNER())
        self.input_commands()


    def input_commands(self):
        while True:
            text = _("Enter the command:")
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
                    alert('error', _("Enter a valid command."))

            except Exception as error:
                # Exibe um aviso se o erro for falta de argumentos.
                if 'list index out of range' in str(error):
                    alert('info', _("Try using the [help] command."))

                else:
                    alert('error', error)

    
    def default_commands(self, args):
        if args[0] == 'exit':
            alert('info', _("Exiting..."))
            sys.exit()

        elif args[0] == 'clear':
            main()

        elif args[0] == 'help':
            print(HELP_BANNER())
        
        else:
            return


    def tool_commands(self, args):
        if args[0] == 'shell':
            alert('info', 'shell')
        
        else:
            return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        alert('info', _("Exiting..."))
        sys.exit()


