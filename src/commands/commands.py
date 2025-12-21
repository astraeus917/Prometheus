from components.functions import *
import time

class DefaultCommands:
    """Comandos normais da ferramenta"""
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

class ScriptCommands:
    """Comandos de scripts"""
    def cleartempfiles(self):
        run_module('src.commands.cleartempfiles')

    def downloader(self):
        pass


# --- Listas de comandos da ferramenta ---

DEFAULT_COMMANDS = {
    'exit': DefaultCommands().exit_tool,
    'clear': DefaultCommands().clear_screen,
    'help': DefaultCommands().help_menu,
}

SCRIPT_COMMANDS = {
    'cleartempfiles': ScriptCommands().cleartempfiles,
    'downloader': ScriptCommands().downloader,
}

