import os, yaml
from colorama import init, Fore as fg

init(autoreset=True) # colorama

def config_path(append_path=None):
    """
    Configura os paths com base no local raíz da ferramenta
    Específicamente a pasta dela 'Prometheus'
    """
    tool_path = os.path.dirname(os.path.abspath(__file__))
    try:
        while not os.path.basename(tool_path) == 'Prometheus':
            tool_path = os.path.dirname(tool_path)

        if append_path:
            return os.path.join(tool_path, append_path)

        else:
            return tool_path
    
    except Exception as e:
        print(e)

def read_yaml(yaml_path):
    """Faz a leitura do arquivo .yaml de configurações"""
    try:
        with open(yaml_path, 'r', encoding='utf-8') as config_file:
            config_data = yaml.safe_load(config_file)

        return config_data

    except Exception as e:
        print(e)
        return None

# Arquivo de configuração .yaml
yaml_path = config_path('config\\config.yaml')
config_data = read_yaml(yaml_path)

# Informações
TOOL_TITLE = config_data['tool']['name']
VERSION = config_data['tool']['version']
AUTHOR = config_data['tool']['author']
DESCRIPTION = config_data['tool']['description']

# Caminhos do .yaml
FFMPEG = config_data['paths']['ffmpeg']
OUTPUT = config_data['paths']['output']

# Outros
USER = os.getlogin()

# Esquema de cores da ferramenta
fg_text = fg.LIGHTWHITE_EX
fg_success = fg.GREEN
fg_error = fg.RED
fg_info = fg.BLUE
fg_warning = fg.YELLOW
