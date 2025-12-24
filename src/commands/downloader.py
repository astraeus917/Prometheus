from ..components.functions import os, sys, time
from ..components.functions import input_cmds, alert, get_args, config_path
from ..components.functions import CommandNotFoundError
from ..components.functions import TOOL_TITLE
import yt_dlp
from yt_dlp.utils import DownloadError

ffmpeg_path = config_path('bin/ffmpeg')
output_path = config_path('bin/output')

def DOWNLOADER_BANNER():
    return """DOWNLOADER """

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
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': video_format,
            'ffmpeg_location': ffmpeg_path,
        }
        self.run_yt_dlp(ydl_opts, url)

# Define uma única constante para chamar os comandos do YoutubeCommands
youtube_cmds = YoutubeCommands()

YOUTUBE_COMMANDS = {
    'music': "Musica",
    'video': "Video",
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
        print("Menu de ajuda")

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
    'exit': default_cmds.exit_tool,
    'clear': default_cmds.clear_screen,
    'help': default_cmds.help_menu,
    'yt': default_cmds.youtube_dlp,
}


class Downloader:
    def __init__(self):
        os.system(f'cls && title Downloader powered by {TOOL_TITLE}')
        print(DOWNLOADER_BANNER())

        while True:
            try:
                self.user_entry = input_cmds()
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
        cmd = self.user_entry[0]
        args = self.user_entry[1:]

        if cmd in DEFAULT_COMMANDS:
            DEFAULT_COMMANDS[cmd](args)

        else:
            raise CommandNotFoundError(cmd)


if __name__ == '__main__':
    Downloader()