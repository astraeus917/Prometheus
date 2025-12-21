from commands.commands import *

class Prometheus:
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
                alert('error', e)

    def dispatch(self):
        cmd = self.user_entry[0]

        if cmd in DEFAULT_COMMANDS:
            DEFAULT_COMMANDS[cmd]()

        elif cmd in SCRIPT_COMMANDS:
            SCRIPT_COMMANDS[cmd]()

        else:
            raise CommandNotFoundError(cmd)

if __name__ == '__main__':
    Prometheus()