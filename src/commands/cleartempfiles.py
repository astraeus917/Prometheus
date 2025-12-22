from ..components.functions import USER, fg_error, fg_info, fg_success, fg_text, fg_warning
from ..components.functions import os, alert, time, sys, shutil

# Autoreset do colorama para corrigir erro no novo console


temp_path_list = [
    r'C:\Windows\temp',
    f'C:\\Users\\{USER}\\AppData\\Local\\Temp',
    r'C:\Windows\Prefetch',
]

def clear_temp_files(temp):
    """Apaga os arquivos e pastas temporárias do sistema"""
    if not os.path.exists(temp):
        raise FileNotFoundError(temp)

    for i in os.listdir(temp):
        full_path = os.path.join(temp, i)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
            alert('success', f"Pasta deletada: {fg_warning}{full_path}")

        elif os.path.isfile(full_path):
            os.remove(full_path)
            alert('success', f"Arquivo deletado: {fg_warning}{full_path}")

class ClearTempFiles:
    def __init__(self):
        alert('info', "Iniciando a limpeza e remoção de arquivos e pastas temporárias do sistema.")
        self.run_clear()

    def run_clear(self):
        for temp in temp_path_list:
            try:
                clear_temp_files(temp)

            except FileNotFoundError:
                alert('error', f"Caminho não encontrado: {temp}")
                time.sleep(5)

            except PermissionError:
                alert('info', "Permissão negada! Execute como administrador.")
                time.sleep(3)

            except Exception as e:
                print(e)
                time.sleep(5)

        alert('success', "Limpeza de arquivos e pastas temporárias concluído! Saindo em alguns segundos...")
        time.sleep(5)
        sys.exit()

if __name__ == '__main__':
    ClearTempFiles()