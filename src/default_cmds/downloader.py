import os, yt_dlp

# Componentes
from components.settings import AUTHOR, TITLE, fg_text, fg_error, fg_success
from components.functions import input_cmd, alert

# Configura os caminhos absolutos conforme onde esta localizado a ferramenta
def config_path():
    tool_path = os.getcwd()
    
    while not os.path.basename(tool_path).lower() == 'prometheus':
        tool_path = os.path.dirname(tool_path)

    set_ffmpeg_dir = os.path.join(tool_path, 'bin/ffmpeg')
    set_output_dir = os.path.join(tool_path, 'bin/output')

    return set_ffmpeg_dir, set_output_dir

# Variáveis com os caminhos do ffpmeg e do output de arquivos baixados
ffmpeg_path, output_path = config_path()

# Comandos normais
default_cmds = {
    'exit': "Sair da ferramenta",
    'clear': "Limpar a tela da ferramenta",
    'help': "Menu de ajuda e lista de comandos",
    'yt': "Baixar vídeo/música do YouTube",
}

# Comandos para baixar da plataforma YouTube
youtube_cmds = {
    'music': "Bixar música do YouTube",
    'video': "Baixar vídeo do YouTube",
    '-f': "Formato de saida do arquivo",
    '-q': "Qualidade de saida do arquivo",
}

def BANNER_TITLE():
    return f"""{fg_error}
                            ┳┓┏┓┓ ┏┳┓┓ ┏┓┏┓┳┓┏┓┳┓
                            ┃┃┃┃┃┃┃┃┃┃ ┃┃┣┫┃┃┣ ┣┫
                            ┻┛┗┛┗┻┛┛┗┗┛┗┛┛┗┻┛┗┛┛┗ {fg_text}ver. 1.0
                  Developed by {fg_error}{AUTHOR} {fg_text}- Powered by {fg_error}{TITLE}
    """

# Para exibir os comandos da ferramenta e ajuda
def help_menu():
    print(f"{fg_text}Comandos da ferramenta:")
    for cmd, desc in default_cmds.items():
        print(f"{fg_error}[{fg_text}{cmd}{fg_error}] >> {fg_text}{desc}")

    print(f"\n{fg_text}Comandos do YouTube Downloader:")
    for cmd, desc in youtube_cmds.items():
        print(f"{fg_error}[{fg_text}{cmd}{fg_error}] >> {fg_text}{desc}")
    
    print(f"{fg_text}Exemplo de uso dos comandos: \n{fg_success}yt music -f mp3 -q 320 https://www.youtube.com/")
    return

# Função para pegar o argumento seguido do seu comando
def get_args(args, flag, default):
    if flag in args:
        try:
            return args[args.index(flag) + 1]
        except:
            return default
    return default

# Executa o download usando o YouTubeDLP
def run_yt_dlp(ydl_options, url):
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        print('')
        try:
           ydl.download([url])
           return

        except Exception as e:
            alert('error', f"{e}")

# Faz downloads apenas de vídeos e músicas da plataforma YouTube 
class YouTube():
    def __init__(self, args):
        self.args = args
        self.dispatch()

    def dispatch(self):
        self.url = next((self.arg for self.arg in self.args if 'youtu' in self.arg), None)

        if not self.url:
            alert('error', "Você precisa informar uma url válida!")
            return

        if 'music' in self.args:
            self.music_download()

        elif 'video' in self.args:
            self.video_download()

        else:
            alert('error', "Comando inválido ou faltando argumentos!")

    def music_download(self):
        # Configuração do download com base nos argumentos
        codec = get_args(self.args, '-f', 'mp3')
        quality = get_args(self.args, '-q', '320')
        
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

        # Depois de definir as opções, executa o download usando o yt dlp
        run_yt_dlp(ydl_options, self.url)

    def video_download(self):
        video_format = get_args(self.args, '-f', 'mp4')
        ydl_options = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': video_format,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferredformat': video_format,
            }],
            'ffmpeg_location': ffmpeg_path,
        }
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

            elif args[0] == 'help':
                help_menu()

            elif args[0] == 'output':
                os.system(f'start {output_path}')

            # --- Tratamento dos comandos de baixar música e vídeo ---
            elif 'yt' in args:
                YouTube(args)
            
            else:
                alert('error', "Esse comando não existe!")

if __name__ == '__main__':
    try:
        Downloader()
    except KeyboardInterrupt:
        alert('info', "Saindo...")