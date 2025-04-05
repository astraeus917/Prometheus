import os, gettext, hashlib, json
from colorama import Fore as fg, init


# Init, autoreset colorama.
init(autoreset=True)


# Load config.json file.
with open('config\config.json') as user_file:
    config_json = json.load(user_file)


# Tool global variables.
user = os.getlogin()
current_path = os.getcwd()
current_dir = os.path.basename(current_path)


# Tool details:
title = config_json['title']
author = config_json['author']
version = config_json['version']
lang = config_json['lang']


# Colors:
fg_one = fg.BLUE
fg_text = fg.LIGHTWHITE_EX
fg_error = fg.RED
fg_success = fg.LIGHTGREEN_EX
fg_info = fg.LIGHTBLUE_EX


# Get the full path to access the translation file correctly.
locale_path = os.path.join(current_path, "config", "locale")


# Set and load translation.
translation = gettext.translation("messages", localedir = locale_path, languages = [lang], fallback = True) 
translation.install()
_gettext = translation.gettext


# List of commands divided by category:

# Default category.
default = {
    'exit': _gettext("Exit the tool."),
    'clear': _gettext("Clear the tool screen."),
    'help': _gettext("Display the help menu and command list."),
    'about': _gettext("view command information."),
}

# Tools category.
tools = {
    'shell': _gettext("Open another window with a custom shell."),
    'ytdownload': _gettext("Open another window with YouTube Downloader.")
}


# New category of commands:
# new_commands = {
#     'cmd01': _gettext("comando 01"),
#     'cmd02': _gettext("comando 02"),
#     'cmd0': _gettext("comando 03"),
# }

