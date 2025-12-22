from ..components.functions import os, sys, time
from ..components.functions import input_cmds, alert
from ..components.functions import CommandNotFoundError
from ..components.functions import TOOL_TITLE

def DOWNLOADER_BANNER():
    return """DOWNLOADER """

class YoutubeCommands:
    """Trata os downloads do YouTube"""
    def music_download(self):
        pass

    def video_download(self):
        pass

YOUTUBE_COMMANDS = {
    'music': "Musica",
    'video': "Video",
}

class DefaultCommands:
    """Trata os comandos normais"""
    def exit_tool(self, user_entry = None):
        alert('info', "Fechando ferramenta em alguns segundos...")
        time.sleep(2)
        sys.exit()

    def clear_screen(self, user_entry = None):
        os.system('cls')
        print(DOWNLOADER_BANNER())
        return

    def help_menu(self, user_entry = None):
        print("Menu de ajuda")
        return

    def youtube_dlp(self, user_entry = None):
        self.user_entry = user_entry
        print(self.user_entry)
        return

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

            except Exception as e:
                print(e)

    def dispatch(self):
        cmd = self.user_entry[0]

        if cmd in DEFAULT_COMMANDS:
            DEFAULT_COMMANDS[cmd](self.user_entry)

        else:
            raise CommandNotFoundError(cmd)


if __name__ == '__main__':
    Downloader()