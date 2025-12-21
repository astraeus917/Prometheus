from ..components.functions import USER
from ..components.functions import os, alert

temp_path_list = [
    r'C:\Windows\temp',
    f'C:\\Users\\{USER}\\AppData\\Local\\Temp',
    r'C:\Windows\Prefetch',
]

def clear_temp_files():
    """Apaga os arquivos e pastas temporárias do sistema"""

class ClearTempFiles:
    def __init__(self):
        alert('info', "A ferramenta esta limpando os arquivos e pastas temporárias do sistema...")
        self.run_clear()

    def run_clear(self):
        for temp in temp_path_list:
            clear_temp_files(temp)

if __name__ == '__main__':
    ClearTempFiles()