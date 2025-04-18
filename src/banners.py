from settings import *
from functions import _gettext, list_commands


# Whenever you add a new command or category, you should use this code structure to list and return them.
def list_commands():
    commands_found = {
        # Whenever you add a new category, also add it as it is below.
        # _gettext("New Category"): [f"{cmd}: {desc}" for cmd, desc in default.items()],
        
        _gettext("Default Commands"): [f"{fg_info}{cmd}: {fg_text}{desc}" for cmd, desc in default.items()],
        _gettext("Tool Commands"): [f"{fg_info}{cmd}: {fg_text}{desc}" for cmd, desc in tools.items()]
    }
    return commands_found


# Tool help banner.
def HELP_BANNER():
    commands = list_commands()

    print()
    print(_gettext(f"Welcome to the tool's help menu, see below the list of available commands."))
    print()
    
    for category, cmds in commands.items():
        print(f"{fg_one}<<< {fg_text}{category} {fg_one}>>>")
        print("\n".join(cmds))
        print()


# Main banner of the tool.
def MAIN_BANNER():
    return f"""{fg_one}
                    ┏┓  ┳┓  ┏┓  ┳┳┓  ┏┓  ┏┳┓  ┓┏  ┏┓  ┳┳  ┏┓
                    ┃┃  ┣┫  ┃┃  ┃┃┃  ┣    ┃   ┣┫  ┣   ┃┃  ┗┓
                    ┣┛  ┛┗  ┗┛  ┛ ┗  ┗┛   ┻   ┛┗  ┗┛  ┗┛  ┗┛
                 Developed by {fg_text}{author} {fg_one}- lang: {fg_text}{lang} {fg_one}- ver. {fg_text}{version}{fg_one}"""


