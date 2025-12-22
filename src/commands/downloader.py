from ..components.functions import os, input_cmds
from ..components.functions import TOOL_TITLE

def DOWNLOADER_BANNER():
    return """DOWNLOADER """

class DefaultCommands:
    def youtube_dlp(url):
        print('test')
        os.system('pause')


DEFAULT_COMMANDS = {
    'yt': DefaultCommands().youtube_dlp,
}

class Downloader:
    def __init__(self):
        os.system(f'cls && title Downloader powered by {TOOL_TITLE}')
        print(DOWNLOADER_BANNER())
        self.dispatch()

    def dispatch(self):
        while True:
            try:
                user_entry = input_cmds()
                DEFAULT_COMMANDS[user_entry]()

            except Exception as e:
                os.system('pause')
                print(e)

if __name__ == '__main__':
    Downloader()