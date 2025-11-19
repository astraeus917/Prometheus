import os
from colorama import Fore as fg

# --- Global vars/constants ---

# Tool
title = 'Prometheus'
version = 'new version'
author = 'Astraeus'

# User
user = os.getlogin()

# Colors
fg_text = fg.LIGHTWHITE_EX
fg_success = fg.GREEN
fg_error = fg.RED
fg_info = fg.BLUE

default_cmds = {
    'exit': "sai da ferramenta",
    'help': "exibe o menu de ajuda e os comandos da ferramenta",
    'clear': "limpa a tela da ferramenta",    
}

script_cmds = {
    'ytdownload': "script para baixar músicas e vídeos do YouTube",
}

