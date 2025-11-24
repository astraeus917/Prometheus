import os, shutil, sys, ctypes, time

# Componentes
from components.settings import USER, fg_text, fg_success, fg_error, fg_info
from components.functions import alert

# Pastas de arquivos temporarios
temp_path_list = [
        r'C:\Windows\temp',
        f'C:\\Users\\{USER}\\AppData\\Local\\Temp',
        r'C:\Windows\Prefetch',
    ]

class ClearTempFiles:
    def __init__(self):
        print("Deletando arquivos temporarios")

        for temp in temp_path_list:
            self.clear(temp)

        os.system('pause')
    
    def clear(self, temp):

        found = os.listdir(temp)

        for i in found:
            try:
                full_path = os.path.join(temp, i)

                if os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                
                elif os.path.isfile(full_path):
                    os.remove(full_path)
                
                else:
                    alert('error', "Unable to delete temporary files.")
            
            except Exception as error:
                if 'WinError 32' in str(error):
                    text = "Does not possible delete this file or folder:"
                    alert('error', f"{text} {full_path}")
                
                else:
                    alert('error', error)

if __name__ == '__main__':
    ClearTempFiles()