import os, yt_dlp

# Components
from components.settings import AUTHOR, TITLE, fg_text, fg_error
from components.functions import input_cmd, alert

def config_path():
    tool_path = os.getcwd()
    
    while not os.path.basename(tool_path).lower() == 'prometheus':
        tool_path = os.path.dirname(tool_path)

    set_ffmpeg_dir = os.path.join(tool_path, 'bin/ffmpeg')
    set_output_dir = os.path.join(tool_path, 'bin/output')

    return set_ffmpeg_dir, set_output_dir

# Constants
ffmpeg_path, output_path = config_path()

def BANNER_TITLE():
    return f"""{fg_error}
                            ┳┓┏┓┓ ┏┳┓┓ ┏┓┏┓┳┓┏┓┳┓
                            ┃┃┃┃┃┃┃┃┃┃ ┃┃┣┫┃┃┣ ┣┫
                            ┻┛┗┛┗┻┛┛┗┗┛┗┛┛┗┻┛┗┛┛┗ ver. 1.0
                  Developed by {AUTHOR} - Powered by {TITLE}
    """

def run_yt_dlp(ydl_options, url):
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        print('')
        try:
           ydl.download([url])
           return

        except Exception as e:
            print(e)

class YouTube():
    def __init__(self, args):
        self.args = args
        self.dispatch()

    def dispatch(self): # Separa para tramento de qual tipo de download vai ser usado
        self.url = next((self.arg for self.arg in self.args if 'youtu' in self.arg), None)

        if 'music' in self.args:
            self.music_download()

        elif 'video' in self.args:
            self.video_download()

        else:
            alert('error', "Comando inválido ou faltando argumentos!")

    def music_download(self):
        # Configuração do download com base nos argumentos
        if '-f' in self.args:
            i = self.args.index('-f')
            i = i + 1
            codec = self.args[i]
        else:
            codec = 'mp3'

        if '-q' in self.args:
            i = self.args.index('-q')
            i = i + 1
            quality = self.args[i]
        else:
            quality = '320'
        
        ydl_options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': codec,
                'preferredquality': quality,
            }],
            'ffmpeg_location': ffmpeg_path,
        }

        # Depois de definir as opções executa o download usando o yt dlp
        run_yt_dlp(ydl_options, self.url)

    def video_download(self):
        if '-f' in self.args:
            i = self.args.index('-f')
            i = i + 1
            output_format = self.args[i]
        else:
            output_format = 'mp4'

        ydl_options = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': output_format,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': output_format,
            }],
            'ffmpeg_location': ffmpeg_path,
        }

        # Depois de definir as opções executa o download usando o yt dlp
        run_yt_dlp(ydl_options, self.url)

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

            elif args[0] == 'output':
                os.system(f'start {output_path}')

            # Tratamento dos comandos de baixar música e vídeo
            elif 'yt' in args:
                YouTube(args)
            
            else:
                alert('error', "Esse comando não existe!")

if __name__ == '__main__':
    try:
        Downloader()
    except KeyboardInterrupt:
        alert('info', "Saindo...")