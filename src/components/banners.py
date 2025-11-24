from .settings import VERSION, fg_info, fg_success, fg_error, fg_text

def TITLE_BANNER():
    return f"""{fg_error}
                              ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                              ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                              ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
                    {fg_text}Developed by {fg_error}Astraeus {fg_text}- ver. {fg_error}{VERSION} ({fg_success}remaster{fg_error})"""