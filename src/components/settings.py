from .constants import *
from .errors import *

def TITLE_BANNER():
    """Desenho ASCII do logo da ferramenta"""
    return f"""{fg_error}
                              ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                              ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                              ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
                    {fg_text}Developed by {fg_error}{AUTHOR} {fg_text}- ver. {fg_error}{VERSION} ({fg_success}remaster{fg_error})"""

