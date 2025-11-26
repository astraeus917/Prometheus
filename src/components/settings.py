import os
from colorama import init, Fore as fg
init(convert=True, autoreset=True)

# --- Global vars/constants ---

# Tool
TITLE = 'Prometheus'
VERSION = '2.0'
AUTHOR = 'Astraeus'

# User
USER = os.getlogin()

# Colors
fg_text = fg.LIGHTWHITE_EX
fg_success = fg.GREEN
fg_error = fg.RED
fg_info = fg.BLUE
fg_warning = fg.YELLOW

default_cmds = {
    'exit': "sai da ferramenta",
    'help': "exibe o menu de ajuda e os comandos da ferramenta",
    'clear': "limpa a tela da ferramenta",
    'cleartempfiles': "limpar arquivos temporarios",
}

script_cmds = {
    'ytdownload': "script para baixar músicas e vídeos do YouTube",
}

