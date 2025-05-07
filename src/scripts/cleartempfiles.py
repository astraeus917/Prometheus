import os
import shutil
import sys
from colorama import Fore as fg

# Fixes the directory to use the main features of the tool.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from functions import alert
from settings import _gettext



class ClearTempFiles():
    def __init__(self):
        temp = 'C:\\Windows\\temp'

        self.cleartempfiles(temp)

        os.system('pause')

    def cleartempfiles(self, temp):
        self.temp = temp

        os.system('cls && echo.')
        alert('info', f"Deleting temporary files from the path: {self.temp}")

        self.found = os.listdir(self.temp)

        self.dir_list = []
        self.file_list = []

        for self.item in self.found:
            try:
                self.full_path = os.path.join(self.temp, self.item)

                if os.path.isdir(self.full_path):
                    shutil.rmtree(self.full_path)
                
                elif os.path.isfile(self.full_path):
                    print(self.full_path)
                    shutil.rmtree(self.full_path)
                
                else:
                    alert('error', "Unable to delete temporary files.")
            
            except Exception as error:
                alert('error', error)


if __name__ == '__main__':
    try:
        ClearTempFiles()
    except KeyboardInterrupt:
        alert('info', "Exiting...")

