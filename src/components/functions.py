import os, subprocess, sys, ctypes, yaml

# Componentes
from .constants import TOOL_TITLE, VERSION, AUTHOR, DESCRIPTION
from .constants import fg_error, fg_info, fg_success, fg_text, fg_warning

# Configura os caminhos absolutos conforme onde esta localizado a ferramenta
def config_path(append_path=None):
    tool_path = os.getcwd()
    try:
        while not os.path.basename(tool_path) == 'Prometheus':
            tool_path = os.path.dirname(tool_path)

        if append_path == None:
            configured_path = tool_path

        else:
            configured_path = os.path.join(tool_path, append_path)

    except Exception as e:
        alert('error', e)

    return configured_path

def read_yaml():
    config_yaml = config_path('config\config.yaml')
    
    try:
        with open(config_yaml, 'r', encoding='utf-8') as config_file:
            config_data = yaml.safe_load(config_file)
    
    except Exception as e:
        alert('error', e)
    
    return config_data

def input_cmd():
    print(f"\n {fg_error}┌─({fg_text}{TOOL_TITLE}{fg_error})~[{fg_success}{USER}{fg_error}]")
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

def add_quick_start():
    pass

def quick_start(path):
    os.system('')
