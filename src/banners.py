from src.settings import *
from src.functions import _gettext


# Whenever you add a new command or category, you should use this code structure to list and return them.
def list_commands():
    commands_found = {
        # Whenever you add a new category, also add it as it is below.
        # _gettext("New Category"): [f"{cmd}: {desc}" for cmd, desc in default.items()],
        
        _gettext("Default Commands"): [f"{cmd}: {desc}" for cmd, desc in default.items()],
        _gettext("Tool Commands"): [f"{cmd}: {desc}" for cmd, desc in tools.items()]
    }
    return commands_found


def HELP_BANNER():
    commands = list_commands()

    print()
    print(_gettext(f"Welcome to the tool's help menu, see below the list of available commands."))
    print()
    
    for category, cmds in commands.items():
        print(f"<<< {category} >>>")
        print("\n".join(cmds))
        print()


def MAIN_BANNER():
    return f"""{fg_one}
                         ┏┓  ┏┓  ┏┳┓  ┳┓  ┏┓  ┏┓  ┳┳  ┏┓
                         ┣┫  ┗┓   ┃   ┣┫  ┣┫  ┣   ┃┃  ┗┓
                         ┛┗  ┗┛   ┻   ┛┗  ┛┗  ┗┛  ┗┛  ┗┛
    {fg_text}Source code for the Python tool with shell interface, this code can be used to create tools of this type, which are executed as a shell in some terminal, mainly on Windows."""


