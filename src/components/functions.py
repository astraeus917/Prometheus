import os, subprocess, sys, ctypes

# Componentes
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

        else:
            fg_type = fg_text
        
        print(f"{fg_type}[{type.upper()}] {fg_text}{text}")
        
    except Exception as e:
        print(e)

# Executa modulos (scripts) em modo normal
def run_module(module):
    subprocess.Popen(
        [
            sys.executable, "-m", module
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=os.path.abspath("src"),
        env=os.environ.copy()   
    )

# Executa modulos (scripts) em modo Administrador
def run_module_admin(module):
    python = sys.executable
    params = f'-m {module}'
    cwd = os.path.abspath("src")

    ctypes.windll.shell32.ShellExecuteW(
        None,          # hwnd
        "runas",       # força modo administrador
        python,        # executável
        params,        # argumentos
        cwd,           # diretório de trabalho
        1              # SW_SHOWNORMAL
    )
