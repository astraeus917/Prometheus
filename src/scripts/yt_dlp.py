import yt_dlp
from os import system
from os import getlogin
from os.path import basename, dirname, join
from os import getcwd
from sys import exit
from colorama import Fore as fg


# Function to adjust the ffmpeg directory based on where the tool is located.
def config_tool_path():
    tool_path = getcwd()

    while not basename(tool_path).lower() == 'scyphos':
        tool_path = dirname(tool_path)

    set_ffmpeg_dir = join(tool_path, 'bin', 'ffmpeg')
    
    set_output_path = join(tool_path, 'output')

    return set_ffmpeg_dir, set_output_path


# Tool global variables:
user = getlogin()
ffmpeg_path, output_path = config_tool_path()


# Tool global colors scheme:
one = fg.RED
two = fg.YELLOW
text = fg.LIGHTWHITE_EX
success = fg.LIGHTGREEN_EX


# Music download function.
def music_download(args):
    # music -f mp3 -q 192 url
    url = next((arg for arg in args if "youtu" in arg), None)

    # Returns to the main tool if the url is not valid.
    if url == None:
        print(f"\n{one}ERROR: {text}Please enter a valid YouTube URL.")
        return

    # Check if the user has entered a specific format.
    if '-f' in args:
        i = args.index('-f')
        i = i + 1
        codec = args[i]
    else:
        codec = 'mp3'

    # Check if the user has entered a specific quality.
    if '-q' in args:
        i = args.index('-q')
        i = i + 1
        quality = args[i]
    else:
        quality = '192'

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

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print('')
            ydl.download([url])
            print(f"\n{success}SUCCESS: {text}Your download has been completed successfully, to see it you can use the command: {two}downloads{text}.")
            return
        
        except Exception as error:
            if 'generic' in str(error):
                print(f"\n{one}ERROR: {text}Please enter a valid YouTube URL.")
                return

            else:
                print(f"\n{error}")
                return
            

# Video download function.
def video_download(args):
    # music -f mp3 -q 192 url
    url = next((arg for arg in args if "youtu" in arg), None)

    # Returns to the main tool if the url is not valid.
    if url == None:
        print(f"\n{one}ERROR: {text}Please enter a valid YouTube URL.")
        return

    # Check if the user has entered a specific format.
    if '-f' in args:
        i = args.index('-f')
        i = i + 1
        output_format = args[i]
    else:
        output_format = 'mp4'


    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': output_format,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': output_format,
        }],
        'ffmpeg_location': ffmpeg_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print('')
            ydl.download([url])
            print(f"\n{success}SUCCESS: {text}Your download has been completed successfully, to see it you can use the command: {two}downloads{text}.")
            return
        
        except Exception as error:
            if 'generic' in str(error):
                print(f"\n{one}ERROR: {text}Please enter a valid YouTube URL.")
                return

            else:
                print(f"\n{error}")
                return



def HELP_MENU():
    return f"""{text}
  Welcome to the help menu of the YouTube Downloader tool, which is part of the
  Astraeus project.
  The project is still under development and will soon have many more options.

  {two}exit {text}>> exit the tool | {two}clear {text}>> clear tool screen

  {text}music + options + youtube link
  {text}music options:
    {two}-f {text}>> music output format: mp3, wav, m4a...
    {two}-q {text}>> music output quality: 128, 192, 320

  {text}ex: music -f mp3 -q 320 https://youtu.be/MusIcViDeoDowNLoad

  {text}video + options + youtube link
  {text}video options:
    {two}-f {text}>> video output format: mp4, mkv...

  {text}ps: by default the video will be downloaded in the highest possible quality."""


def BANNER():
    return f"""{one}
                    ┓┏┏┓┳┳┏┳┓┳┳┳┓┏┓      ┳┓┏┓┓ ┏┳┓┓ ┏┓┏┓┳┓┏┓┳┓
                    ┗┫┃┃┃┃ ┃ ┃┃┣┫┣   ━━  ┃┃┃┃┃┃┃┃┃┃ ┃┃┣┫┃┃┣ ┣┫
                    ┗┛┗┛┗┛ ┻ ┗┛┻┛┗┛      ┻┛┗┛┗┻┛┛┗┗┛┗┛┛┗┻┛┗┛┛┗
                            {text}Powered by Astraeus Project
                            
                        type {two}help {text}to display the help menu
                       basic use: {two}music/video + youtube link
                    {text}ex: {two}music https://youtu.be/MusIcViDeoDowNLoad"""


class main:
    def __init__(self):
        system('cls && title YouTube Downloader')
        print(BANNER())
        self.input_commands()

    def input_commands(self):
        while True:
            print(f"\n{one}┌─({text}{user} lets to download anything?{one})")
            cmd = input(f"{one}└───މމމ {text}")
            try:
                args = cmd.split()

                if args[0] == 'exit':
                    exit()

                elif args[0] == 'clear':
                    main()

                elif args[0] == 'help':
                    print(HELP_MENU())
                    
                elif args[0] == 'music':
                    music_download(args)

                elif args[0] == 'video':
                    video_download(args)

                else:
                    print(f"\n{one}ERROR: {text}Please enter a valid command!")

            # Errors.
            except Exception as error:
                if 'list index out of range' in str(error):
                    print(f"\n{one}ERROR: {text}Please enter a valid command!")
                
                else:
                    print(f"\n{one}ERROR: {text}{error}")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()



