import os
from .constants import *

def alert(type, text):
    try:
        if type == 'success':
            fg_type = fg_success
        elif type == 'error':
            fg_type = fg_error
        elif type == 'info':
            fg_type = fg_info
        else:
            fg_type = fg_text

        # Quando verificado o tipo de alert, ele exibe na tela
        print(f"{fg_type}[{type.upper()}] {fg_text}{text}")

    except Exception as e:
        print(e)

def input_cmds():
    entry = input(" User entry: ")

    if not entry:
        raise ValueError("Nenhum comando informado!")

    return entry.split()