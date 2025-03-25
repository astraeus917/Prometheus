import os, sys, gettext, hashlib
from time import sleep
from colorama import Fore as fg
from colorama import Back as bg


# Global variables:
STORED_USERNAME = "root"
STORED_PASSWORD_HASH = hashlib.sha256("root".encode()).hexdigest()

user = os.getlogin()
current_path = os.getcwd()
current_dir = os.path.basename(current_path)
lang = "pt_BR" # pt_BR


# Tool details:
title = "PyToolSourceCode"
author = "Astraeus"
version = "1.2"


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

