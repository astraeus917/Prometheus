from components.functions import *

class DefaultCommands:
    """Comandos normais da ferramenta"""
    def exit_tool(self):
        alert('info', "Saindo da ferramenta em alguns segundos...")
        time.sleep(2)
        sys.exit()
    
    def clear_screen(self):
        os.system('cls')
        print(TITLE_BANNER())

    def help_menu(self):
        HELP_MENU()


class ScriptCommands:
    """Comandos de scripts"""
    def cleartempfiles(self):
        run_module_admin('src.commands.cleartempfiles')

    def downloader(self):
        run_module('src.commands.downloader')


# --- Listas de comandos da ferramenta ---

default_cmds = DefaultCommands()
script_cmds = ScriptCommands()

DEFAULT_COMMANDS = {
    'exit': {
        'handler': default_cmds.exit_tool,
        'description': "Fecha a ferramenta"
    },
    'clear': {
        'handler': default_cmds.clear_screen,
        'description': "Limpa a tela da ferramenta"
    },
    'help': {
        'handler': default_cmds.help_menu,
        'description': "Mostra o menu de ajuda e lista de comandos"
    },
}

SCRIPT_COMMANDS = {
    'cleartempfiles': {
        'handler': script_cmds.cleartempfiles,
        'description': "Limpa os arquivos temporários do sistema"
    },
    'downloader': {
        'handler': script_cmds.downloader,
        'description': "Abre a ferramenta de downloads"
    }
}

def HELP_MENU():
    """Menu de ajuda, lista de comandos"""
    print(f"""
    Ferramenta de Automação CLI - developed by Xzhyan

{fg_error}┌───── {fg_text}Lista de comandos {fg_error}─────┐""")

    for cmd, data in DEFAULT_COMMANDS.items():
        desc = data.get('description', '')
        print(f' {fg_text}{cmd:>6} {fg_error}-> {fg_success}{desc}')

    print(f"\n{fg_error}┌───── {fg_text}Modulos/Scripts {fg_error}─────┐")

    for cmd, data in SCRIPT_COMMANDS.items():
        desc = data.get('description', '')
        print(f' {fg_text}{cmd:>15} {fg_error}-> {fg_success}{desc}')
