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
                time.sleep(3)
                sys.exit()

            except ValueError as e:
                alert('error', e)

            except CommandNotFoundError as e:
                alert('error', e)

            except Exception as e:
                alert('error', e)

    def dispatch(self):
        cmd = self.user_entry[0]

        # Verificar a existencia do comando
        if cmd in DEFAULT_COMMANDS:
            command = DEFAULT_COMMANDS.get(cmd)

        elif cmd in SCRIPT_COMMANDS:
            command = SCRIPT_COMMANDS.get(cmd)

        else:
            raise CommandNotFoundError(cmd)
        
        # Se existir, executa
        command['handler']()


if __name__ == '__main__':
    Prometheus()