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
lang = "pt_BR"
locale_path = "locale"


# List of commands divided by category:
default = ['exit', 'clear', 'help']
tools = ['shell', 'ytdownload']

