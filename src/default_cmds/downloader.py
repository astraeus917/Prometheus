import os, yt_dlp

# Components
from components.settings import TITLE, fg_text, fg_error
from components.functions import input_cmd, alert

def BANNER_TITLE():
    return f"""{fg_error}
        ┳┓┏┓┓ ┏┳┓┓ ┏┓┏┓┳┓┏┓┳┓
        ┃┃┃┃┃┃┃┃┃┃ ┃┃┣┫┃┃┣ ┣┫
        ┻┛┗┛┗┻┛┛┗┗┛┗┛┛┗┻┛┗┛┛┗ ver. 1.0
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

            elif args[0] == 'exit':
                alert('info', "Saindo...")
                exit()

            elif args[0] == 'clear':
                os.system('cls')
                print(BANNER_TITLE())

            # Tratamento dos comandos de baixar música e vídeo
            
            else:
                alert('error', "Esse comando não existe!")

if __name__ == '__main__':
    try:
        Downloader()
    except KeyboardInterrupt:
        alert('info', "Saindo...")