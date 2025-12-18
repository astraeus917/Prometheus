import os
from colorama import init, Fore as fg
init(convert=True, autoreset=True)

# --- Global vars/constants ---

# Constantes
USER = os.getlogin()

# Cores
fg_text = fg.LIGHTWHITE_EX
fg_success = fg.GREEN
fg_error = fg.RED
fg_info = fg.BLUE
fg_warning = fg.YELLOW

# Lista dos comandos normais
default_cmds = {
    'exit': "Fecha a ferramenta",
    'restart': "Reinicia da ferramenta",
    'help': "Exibe o menu de ajuda e os comandos da ferramenta",
    'clear': "Limpa a tela da ferramenta",
    'test': "test command",
}

# Lista dos comandos de script
script_cmds = {
    'cleartempfiles': "Apagas arquivos e pastas temporárias do sistema",
    'downloader': "Ferramenta para baixar música e vídeos do YouTube",
    'filebrowser': "Sistema de compartilhamento de arquivos",
}

