import os
import sys
import ctypes
import subprocess

def is_admin():
    """Verifica se o script está sendo executado como administrador"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Solicitando permissões de administrador...")
    # Reexecuta o script com privilégios de administrador
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    except Exception as e:
        print(f"Erro ao tentar elevar permissões: {e}")
    sys.exit()

# Seu código com privilégios de administrador vai aqui
print("Executando com permissões de administrador!")
os.system('pause')


