from components.functions import *
import time

class DefaultCommands:
    def exit_tool(self):
        alert('info', "Saindo da ferramenta em alguns segundos...")
        time.sleep(2)
        exit()
    
    def clear_screen(self):
        os.system('cls')
        print(TITLE_BANNER())
        return

    def help_menu(self):
        print('Menu de ajuda!')
        return

DEFAULT_COMMANDS = {
    'exit': DefaultCommands().exit_tool,
    'clear': DefaultCommands().clear_screen,
    'help': DefaultCommands().help_menu,
}
