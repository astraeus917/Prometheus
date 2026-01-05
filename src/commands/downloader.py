# Libs
from ..components.functions import os, sys, time

# Funções personalizadas
from ..components.functions import input_cmds, alert, get_args, config_path, fg

# Cores e contantes
from ..components.functions import TOOL_TITLE, FFMPEG, OUTPUT, fg_error, fg_info, fg_success, fg_text, fg_warning
from ..components.functions import CommandNotFoundError

# YouTube DLP
from yt_dlp.utils import DownloadError
import yt_dlp

# ffmpeg e pasta de downloads
ffmpeg_path = config_path(FFMPEG)
output_path = config_path(OUTPUT)

# Mudanças nas cores
fg_one = fg.BLUE

def DOWNLOADER_BANNER():
    return f"""{fg_one}
                             ┳┓┏┓┓ ┏┳┓┓ ┏┓┏┓┳┓┏┓┳┓
                             ┃┃┃┃┃┃┃┃┃┃ ┃┃┣┫┃┃┣ ┣┫
                             ┻┛┗┛┗┻┛┛┗┗┛┗┛┛┗┻┛┗┛┛┗
                        {fg_text}Powered by {fg_one}{TOOL_TITLE} {fg_text}- ver. {fg_one}2.0
    """


class YoutubeCommands:
    """Trata os downloads do YouTube"""
    def run_yt_dlp(self, ydl_opts, url):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def music_download(self, args, url):
        codec = get_args(args, '-f', 'mp3')
        quality = get_args(args, '-q', '320')
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': codec,
                'preferredquality': quality,
            }],
            'ffmpeg_location': ffmpeg_path,
        }
        self.run_yt_dlp(ydl_opts, url)

    def video_download(self, args, url):
        video_format = get_args(args, '-f', 'mp4')
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': video_format,
            'ffmpeg_location': ffmpeg_path,
        }
        self.run_yt_dlp(ydl_opts, url)

# Define uma única constante para chamar os comandos do YoutubeCommands
youtube_cmds = YoutubeCommands()

YOUTUBE_COMMANDS = {
    'music': {
        'description': "Baixar música do YouTube",
        'arguments': "-f (formato, ex: -f mp3) / -q (qualidade, ex: -q 320)",
        'usage': "yt music -f mp3 -q 320 url"
    },
    'video': {
        'description': "Baixar música do YouTube",
        'arguments': "-f (formato, ex: -f mp4)",
        'usage': "yt video -f mp4 url"
    }
}


class DefaultCommands:
    """Trata os comandos normais"""
    def exit_tool(self, args):
        alert('info', "Fechando ferramenta em alguns segundos...")
        time.sleep(2)
        sys.exit()

    def clear_screen(self, args):
        os.system('cls')
        print(DOWNLOADER_BANNER())

    def help_menu(self, args):
        HELP_MENU()

    def open_output(self, args):
        os.system(f'start {output_path}')

    def youtube_dlp(self, args):
        """Verifica a url e encaminha para download se for música ou se for vídeo"""
        url = next((arg for arg in args if 'youtu' in arg), None)

        if not url:
            raise ValueError("Não foi detectado nenhuma url válida do YouTube no argumentos inseridos.")

        elif 'music' in args:
            youtube_cmds.music_download(args, url)

        elif 'video' in args:
            youtube_cmds.video_download(args, url)

# Define uma única constante para chamar os comandos do DefaultCommands
default_cmds = DefaultCommands()

DEFAULT_COMMANDS = {
    'exit': {
        'handler': default_cmds.exit_tool,
        'description': "Fecha a ferramenta"
    },
    'clear': {
        'handler': default_cmds.clear_screen,
        'description': "Limpa a tela da ferramenta"
    },
    'help': {
        'handler': default_cmds.help_menu,
        'description': "Mostra o menu de ajuda e comandos"
    },
    'output': {
        'handler': default_cmds.open_output,
        'description': "Abre a pasta de downloads"
    },
    'yt': {
        'handler': default_cmds.youtube_dlp,
        'description': "Realizar downloads do YouTube"
    }
}


def HELP_MENU():
    """Comandos e exemplos de uso"""
    print(f"{fg_one}┌───── {fg_text}Menu de ajuda e lista de comandos {fg_one}─────┐")

    # Lista os comandos normais
    for cmd, data in DEFAULT_COMMANDS.items():
        desc = data.get('description', '')
        print(f' {fg_text}{cmd:>6} {fg_one}-> {fg_success}{desc}')

    print(f"\n{fg_one}┌───── {fg_text}YouTube {fg_one}─────┐")

    # Lista os comaandos de download do YouTube
    for cmd, data in YOUTUBE_COMMANDS.items():
        desc = data.get('description', '')
        args = data.get('arguments', '')
        usage = data.get('usage', '')
        print(f' {fg_text}{cmd:>6} {fg_one}-> {fg_success}{desc}\n{'':<10}{fg_text}{usage}')

class Downloader:
    def __init__(self):
        os.system(f'cls && title Downloader powered by {TOOL_TITLE}')
        print(DOWNLOADER_BANNER())

        while True:
            try:
                self.user_entry = input_cmds(fg_error)
                self.dispatch()
            
            except KeyboardInterrupt:
                alert('error', "Fechando a ferramenta em alguns segundos...")
                time.sleep(3)
                sys.exit()

            except ValueError as e:
                alert('error', e)

            except CommandNotFoundError as e:
                alert('error', e)

            except DownloadError as e:
                alert('error', f"Erro no download: {e}")

            except Exception as e:
                print(e)

    def dispatch(self):
        """Trata a entrada de comandos"""
        cmd = self.user_entry[0]
        args = self.user_entry[1:]

        command = DEFAULT_COMMANDS.get(cmd)

        if not command:
            raise CommandNotFoundError(cmd)
        
        command['handler'](args)


if __name__ == '__main__':
    Downloader()