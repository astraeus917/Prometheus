import os

# Components
from components.settings import TITLE, fg_text, fg_error
from components.functions import input_cmd, alert

def BANNER_TITLE():
    return f"""
        ┳┓┏┓┓ ┏┳┓┓ ┏┓┏┓┳┓┏┓┳┓
        ┃┃┃┃┃┃┃┃┃┃ ┃┃┣┫┃┃┣ ┣┫
        ┻┛┗┛┗┻┛┛┗┗┛┗┛┛┗┻┛┗┛┛┗
    """

class Downloader():
    def __init__(self):
        os.system(f'cls && title Downloader - Powered by {TITLE}')
        print(BANNER_TITLE())
        self.commands()

    def commands(self):
        while True:
            args = input_cmd()
            if not args:
                alert('error', f"{fg_text}Nenhum comando foi digitado! Tente usar [ {fg_error}help {fg_text}].")
            

if __name__ == '__main__':
    try:
        Downloader()
    except KeyboardInterrupt:
        alert('info', "Saindo...")