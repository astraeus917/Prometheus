import os, subprocess, sys

# Components
from .settings import TITLE, USER, fg_text, fg_error, fg_success, fg_info

def input_cmd():
    print(f"\n {fg_error}┌─({fg_text}{TITLE}{fg_error})~[{fg_success}{USER}{fg_error}]")
    cmd = input(f" {fg_error}└───$ {fg_text}")
    args = cmd.split()
    return args

def alert(type, text):
    try:
        if type == 'success':
            fg_type = fg_success

        elif type == 'error':
            fg_type = fg_error

        elif type == 'info':
            fg_type = fg_info
        
        print(f"{fg_type}[{type.upper()}] {fg_text}{text}")
        
    except Exception as e:
        print(e)

