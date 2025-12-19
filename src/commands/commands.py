from components.settings import *

def default_commands(command):
    """Trata os comandos normais da ferramenta"""

    if command == 'exit':
        alert('info', "Fechando a ferramenta em alguns segundos...")
        time.sleep(2)
        exit()

    elif command == 'help':
        print('help')
    
    elif command == 'clear':
        pass

    else:
        raise CommandNotFoundError(command)

class NewCommands:
    def test(self):
        print('test aaa')