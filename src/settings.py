import os, sys, gettext
from colorama import Fore as fg
from colorama import Back as bg



# Global variables:
user = os.getlogin()
current_path = os.getcwd()
current_dir = os.path.basename(current_path)


# Tool details:
title = "PyToolSourceCode"
credit = "Source code by Astraeus"


# Colors:
fg_one = fg.BLUE
fg_text = fg.LIGHTWHITE_EX
fg_error = fg.RED
fg_success = fg.LIGHTGREEN_EX
fg_info = fg.LIGHTBLUE_EX


# Set tool language.
lang = "en_US"
locale_path = "locale"


# Set and load translation.
translation = gettext.translation("messages", localedir=locale_path, languages=[lang], fallback=True) 
translation.install()
_gettext = translation.gettext


# List of commands divided by category:
default = {
    'exit': _gettext("Exit the tool."),
    'clear': _gettext("Clear the tool screen."),
    'help': _gettext("Display the help menu and command list.")
}

tools = {
    'shell': _gettext("Open another window with a custom shell."),
    'ytdownload': _gettext("Open another window with YouTube Downloader.")
}


