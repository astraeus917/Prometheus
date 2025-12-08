import os, shutil, time

# Componentes
from components.settings import USER, TITLE, fg_text, fg_warning
from components.functions import alert

# Pastas de arquivos temporarios
temp_path_list = [
        r'C:\Windows\temp',
        f'C:\\Users\\{USER}\\AppData\\Local\\Temp',
        r'C:\Windows\Prefetch',
    ]

class ClearTempFiles:
    def __init__(self):
        alert('info', f"{fg_text}{TITLE} esta deletando os arquivos e pastas temporários do seu computador...")

        for temp in temp_path_list:
            self.clear(temp)

        alert('info', f"{fg_text}Tarefa concluída, saindo em alguns segundos...")
        time.sleep(8)
    
    def clear(self, temp):

        found = os.listdir(temp)

        for i in found:
            try:
                full_path = os.path.join(temp, i)

                if os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                    alert('success', f"{fg_text}Pasta deletada: {fg_warning}{full_path}")
                
                elif os.path.isfile(full_path):
                    os.remove(full_path)
                    alert('success', f"{fg_text}Arquivo deletado: {fg_warning}{full_path}")
                
                else:
                    alert('error', f"{fg_text}Não foi possível deletar os arquivos temporários!")
            
            except Exception as error:
                if 'WinError 32' in str(error):
                    alert('error', f"{fg_text}Não foi possível deletar esse arquivo ou pasta: {fg_warning}{full_path}")
                
                else:
                    alert('error', error)

if __name__ == '__main__':
    try:
        ClearTempFiles()
    except KeyboardInterrupt:
        alert('info', "Saindo...")