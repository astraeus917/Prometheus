import os
import keyring
import hashlib
import getpass
import time

sys_reg = "PyToolSourceCode"


def save_on_system(username, hash_password):
    keyring.set_password(sys_reg, username, hash_password)
    print("Usuário e senha registrado com sucesso!")
    os.system("pause")


def encode_to_hash(password):
    """Generate a secure hash to store a password."""
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    while True:
        os.system('cls && title Register')

        username = input("Choice your username: ")
        if not username:
            print("O campo não pode ficar vazio.")
            return

        password = input("Choice your password: ")
        if not password:
            print("O campo de senha não pode ser vazio.")
            return
        
        confirm_passwd = input("Confirm your password: ")
        if not confirm_passwd:
            print("O campo de senha não pode ser vazio.")
            return
        
        # If everything was entered correctly, access is registered in the system.
        if confirm_passwd == password:
            hash_password = encode_to_hash(password)
            save_on_system(username, hash_password)

        else:
            print("As senhas não coincidem! Tente novamente...")
            time.sleep(2)


if __name__ == '__main__':
    try:
        register()
    except KeyboardInterrupt:
        print("Exiting...")

