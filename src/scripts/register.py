import os
import keyring
import hashlib
import time
from colorama import Fore as fg, Back as bg


# Global variables:
sys_reg = "PyToolSourceCode"

# Color variables:
one = fg.GREEN
text = fg.WHITE
success = bg.GREEN
error = bg.RED
dark = bg.BLACK


def save_on_system(username, hash_password):
    keyring.set_password(sys_reg, username, hash_password)

    # Register successfully.
    print(f"\n{success}{text}Username and password registered successfully!{dark}")

    # After registration, continue to exit the tool.
    print(f"\n{one}Exiting the tool in a few seconds!")

    time.sleep(3)
    exit()


def encode_to_hash(password):
    """Generate a secure hash to store a password."""
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    while True:
        os.system('cls && title Credentials Register')
        print(f"Credentials registration Tool \nCredentials are saved in the Windows System.")

        username = input(f"{one}\nChoice your username: {text}{dark}")
        if not username:
            print("The username field cannot be empty!")
            return

        password = input(f"{one}\nChoice your password: {text}")
        if not password:
            print(f"\n{error}{text}The password field cannot be empty!.{dark}")
            return
        
        confirm_passwd = input(f"{one}\nConfirm your password: {text}")
        if not confirm_passwd:
            print(f"\n{error}{text}The password field cannot be empty!{dark}")
            return
        
        # If everything was entered correctly, access is registered in the system.
        if confirm_passwd == password:
            hash_password = encode_to_hash(password)
            save_on_system(username, hash_password)

        else:
            print(f"\n{error}{text}Passwords dot not match! Try again...{dark}")
            time.sleep(2)


if __name__ == '__main__':
    try:
        register()
    except KeyboardInterrupt:
        print(f"\n{one}Exiting...")

