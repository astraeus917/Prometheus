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

<<<<<<< HEAD
    def restart_tool(self):
        p_batchfile = config_path()
        p_batchfile = f'{p_batchfile}/prometheus.bat'

        if not os.path.isfile(p_batchfile):
            raise FileNotFoundError

        os.system(f'start {p_batchfile}')
        sys.exit()

=======
>>>>>>> d6e2b9af52e2c96277a1ae3300d072ff53d9937f

class SpecialCommands:
    """Comandos de scripts"""
    def cleartempfiles(self):
        run_module_admin('src.commands.cleartempfiles')

    def downloader(self):
        run_module('src.commands.downloader')

    def filebrowser(self):
        filebrowser_path = f'{BATCHFILES_PATH}\\filebrowser.bat'
        os.system(f'start {filebrowser_path}')
    
    def easysharing(self):
        easysharing_path = f'{BATCHFILES_PATH}\\easysharing.bat'
        os.system(f'start {easysharing_path}')


# --- Listas de comandos da ferramenta ---

default_cmds = DefaultCommands()
special_cmds = SpecialCommands()

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

SPECIAL_COMMANDS = {
    'cleartempfiles': {
        'handler': special_cmds.cleartempfiles,
        'description': "Limpa os arquivos temporários do sistema"
    },
    'downloader': {
        'handler': special_cmds.downloader,
        'description': "Abre a ferramenta de downloads"
    },
    'filebrowser': {
        'handler': special_cmds.filebrowser,
        'description': "Abre o FileBrowser"
    },
    'easysharing': {
        'handler': special_cmds.easysharing,
        'description': "Abre o EasySharing"
    }
}

def HELP_MENU():
    """Menu de ajuda, lista de comandos"""
    print(f"{fg_error}┌───── {fg_text}Menu de ajuda e lista de comandos {fg_error}─────┐")

    for cmd, data in DEFAULT_COMMANDS.items():
        desc = data.get('description', '')
        print(f' {fg_text}{cmd:>6} {fg_error}-> {fg_success}{desc}')

    print(f"\n{fg_error}┌───── {fg_text}Scripts {fg_error}─────┐")

    for cmd, data in SPECIAL_COMMANDS.items():
        desc = data.get('description', '')
        print(f' {fg_text}{cmd:>15} {fg_error}-> {fg_success}{desc}')
