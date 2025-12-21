from .settings import *
import sys, ctypes, subprocess

def alert(type, text):
    """Print personalizado para alertas"""
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
    """Captura as entradas do usuário"""
    print(f"\n {fg_error}┌─({fg_text}{TOOL_TITLE}{fg_error})~[{fg_success}{USER}{fg_error}]")
    entry = input(f" {fg_error}└───$ {fg_text}")

    if not entry:
        raise ValueError("Nenhum comando informado!")

    return entry.split()

def run_module(module):
    """Executa um modulo em terminal separado"""
    subprocess.Popen(
        [
            sys.executable, "-m", module
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=os.path.abspath('.'),
        env=os.environ.copy()
    )

def run_module_admin(module):
    """Executa um modulo em terminal separado como administrador"""
    python = sys.executable
    params = f'-m {module}'
    cwd = os.path.abspath(".")

    ctypes.windll.shell32.ShellExecuteW(
        None,          # hwnd
        "runas",       # força modo administrador
        python,        # executável
        params,        # argumentos
        cwd,           # diretório de trabalho
        1              # SW_SHOWNORMAL
    )
