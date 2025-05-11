import os
import shutil
import sys
import ctypes
import time

from colorama import Fore as fg

# Fixes the directory to use the main features of the tool.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from functions import alert
from settings import _gettext


class AdminPrivilegeHandler(): # Class to check if the script is running with admin privileges.
    def __init__(self):
        is_admin = self.is_admin() # Calls the function to check if it is admin.

        if not is_admin: # If not admin, run the function to restart the script with admin privileges.
            self.exec_as_admin()
        
        ClearTempFiles() # If have admin privileges, run ClearTempFiles as normal.

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
            
    def exec_as_admin(self):
        alert('info', _gettext("Requesting permission to run the script with admin privileges."))
        params = " ".join([f'"{arg}"' for arg in sys.argv])

        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

        except Exception as error:
            alert('error', error)

        sys.exit()


class ClearTempFiles(): # Main class of the temporary file cleanup tool.
    def __init__(self):
        os.system('cls && title Clear Temporary Files')

        user = os.environ.get('USERNAME') or os.getlogin()

        temp = r'C:\Windows\temp'
        user_temp = f'C:\\Users\\{user}\\AppData\\Local\\Temp'
        prefetch = r'C:\Windows\Prefetch'

        self.clear(temp)
        self.clear(user_temp)
        self.clear(prefetch)

        alert('success', _gettext("Temporary files deletion task completed! (leaving in 5 seconds...)"))
        time.sleep(5)


    def clear(self, temp): # Calling the 'clear' function to clear temporary files.
        text = _gettext("Deleting temporary files from the path:")
        alert('info', f"{text} {temp}.")

        found = os.listdir(temp)

        for item in found:
            try:
                full_path = os.path.join(temp, item)

                if os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                
                elif os.path.isfile(full_path):
                    os.remove(full_path)
                
                else:
                    alert('error', _gettext("Unable to delete temporary files."))
            
            except Exception as error:
                if 'WinError 32' in str(error):
                    text = _gettext("Does not possible delete this file or folder:")
                    alert('error', f"{text} {fg.YELLOW}{full_path}")
                
                else:
                    alert('error', error)


if __name__ == '__main__':
    try:
        AdminPrivilegeHandler()
    except KeyboardInterrupt:
        alert('info', "Exiting...")

