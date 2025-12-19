from components.settings import *


def TITLE_BANNER():
    """
    Desenho ASCII do logo da ferramenta
    """
    return f"""{fg_error}
                              ┏┓┳┓┏┓┳┳┓┏┓┏┳┓┓┏┏┓┳┳┏┓
                              ┃┃┣┫┃┃┃┃┃┣  ┃ ┣┫┣ ┃┃┗┓
                              ┣┛┛┗┗┛┛ ┗┗┛ ┻ ┛┗┗┛┗┛┗┛
                    {fg_text}Developed by {fg_error}{AUTHOR} {fg_text}- ver. {fg_error}{VERSION} ({fg_success}remaster{fg_error})"""


class Prometheus():
    def __init__(self):
        os.system(f'cls && title {TOOL_TITLE}')
        print(TITLE_BANNER())

        while True:
            try:
                self.user_entry = input_cmds()
                self.dispatch()
            
            except KeyboardInterrupt:
                alert('info', "Saindo da ferramenta...")
                exit()
            
            except Exception as e:
                print(e)

    def dispatch(self):
        cmd = self.user_entry[0]
        if cmd == 'test':
            print(config_path())


if __name__ == '__main__':
    Prometheus()