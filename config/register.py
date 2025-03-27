import os
import keyring
import hashlib
import getpass

tool_name = "PyToolSourceCode"

def register():
    while True:
        os.system('cls && ')

        username = input("Choice your username: ")
        if not username:
            print("O campo não pode ficar vazio.")
            return

        password = input("Choice your password: ")
        if not password:
            print("O campo de senha não pode ser vazio.")
            return


if __name__ == '__main__':
    try:
        register()
    except KeyboardInterrupt:
        print("Exiting...")

