from settings import *
from banners import MAIN_BANNER, HELP_BANNER
from functions import alert, _gettext, cmd_info


# INPUT COMMANDS:

# If you pay attention, the commands are divided into categories.
# To add categories and commands to these categories, visit 'src.settings' and 'src.functions'.

# To better organize user input, check if the command entered is in the list of any category.
# The command categories have been divided into functions.
# For example, the help command is in the 'default' category, thus directing it to the default_commands function.


class Main:
    def __init__(self):
        # If you don't want to use the "Login" function you can comment out the "self.login()" line.
        self.login()
        self.input_commands()

    # Login function.
    def login(self):
        os.system(f'cls && title Login')

        print(useaar)

        while True:
            # Input username.
            text = _gettext("Enter your username:")
            user = input(f'{fg_one}{text} {fg_text}')

            # Input password.
            text = _gettext("Enter your password:")
            passwd = input(f'{fg_one}{text} {fg_text}')

            # Performs user verification.
            if user == STORED_USERNAME and hashlib.sha256(passwd.encode()).hexdigest() == STORED_PASSWORD_HASH:
                alert('success', _gettext("Access authorized!"))
                sleep(3)
                break

            else:
                alert('error', _gettext("Access not authorized!"))

    # Function where inputs and commands are processed.
    def input_commands(self):
        os.system(f'cls && title {title}')
        print(MAIN_BANNER())

        while True:
            print()
            text = _gettext(f"({fg_text}{user}{fg_one})~ Enter the command:")
            cmd = input(f"{fg_one}{text} {fg_text}")
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
            alert('info', 'shell')

        elif args[0] == 'ytdownload':
            alert('info', 'ytdownload')
        
        else:
            return

    # New category of commands:
    # def new_commands(self, args):
    #     if args[0] == 'cmd01':
    #         Here you create the code based on what your command will execute.

    #     elif args[0] == 'cmd02':
    #         Here you create the code based on what your command will execute.

    #     else:
    #         return


if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print()
        print()
        alert('info', _gettext("Exiting..."))
        sys.exit()


