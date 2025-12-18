from .functions import read_yaml

config_data = read_yaml()

# Constantes de configração da ferramenta
TOOL_TITLE = config_data['tool']['name']
VERSION = config_data['tool']['version']
AUTHOR = config_data['tool']['author']
DESCRIPTION = config_data['tool']['description']

# Caminhos
