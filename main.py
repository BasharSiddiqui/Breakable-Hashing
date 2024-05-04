#options:
#
from colorama import Fore, Back, Style, init
import os

def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems
        os.system('clear')

# Usage
clear_console()

init()
filename = "passwords.txt"
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')
# Fore.CYAN
def hash_func(inp):
    return inp

def save_to_file(inp):
    with open(filename, 'a') as f: 
        f.write(str(inp) + '\n')

def print_file():
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print()
            print(Style.BRIGHT + "Your passwords are:" + Style.RESET_ALL)
            print(Style.BRIGHT + contents + Style.RESET_ALL)
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + "The file does not exist. There are no passwords at this moment." + Style.RESET_ALL)
    print()

def check_file_exists():
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            return True
        else:
            return False
    else:
        return False

def check_if_in_file(imp):
    with open(filename, 'r') as f:
        contents = f.read()
        contents = contents.split("\n")
        print(contents)
        for item in contents:
            if item == imp:
                return True
        return False
while True:

    print(Fore.GREEN + Style.BRIGHT + "Welcome to the control center enter the following number to do what you want:")
    print(Fore.CYAN + "1 to create a new hashed password.")
    print(Fore.BLUE + "2 to view all current hashed passwords.")
    print(Fore.MAGENTA + "3 to authenticate a newly entered password.")
    print(Fore.YELLOW + "0 to quit.\n" + Style.RESET_ALL)

    initial_input = input()
    # print(initial_input)
    match(initial_input):
        case "3":
            if (check_file_exists()):
                print(Fore.CYAN + "Please enter your password" + Style.RESET_ALL)
                to_be_hashed_input = input()
                print(Fore.BLUE + f"Generating Hash..." + Style.RESET_ALL)
                hashed_password = hash_func(to_be_hashed_input)
                print(Fore.GREEN + f"Success!" + Style.RESET_ALL)
                print(Fore.MAGENTA + f"Comparing Hash..." + Style.RESET_ALL)
                if(check_if_in_file(hashed_password)):
                    print(Fore.GREEN + f"\nAuthentication Successful.\n" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"\nAuthentication Unsuccessful.\n" + Style.RESET_ALL)
            else:
                print(Style.BRIGHT + Fore.RED + "There are no passwords at this moment." + Style.RESET_ALL)

            print(Fore.GREEN + f"Press Enter to continue." + Style.RESET_ALL)
            input()
            clear_console()
        case "2":
            print_file()
            print(Fore.GREEN + f"Press Enter to continue." + Style.RESET_ALL)
            input()
            clear_console()
        case "1":
            print(Fore.CYAN + "Please enter your password" + Style.RESET_ALL)
            to_be_hashed_input = input()
            print(Fore.BLUE + f"Generating Hash..." + Style.RESET_ALL)
            hashed_password = hash_func(to_be_hashed_input)
            print(Fore.GREEN + f"Success!" + Style.RESET_ALL)
            print(Fore.MAGENTA + f"Hash generated, saving to file..." + Style.RESET_ALL)
            save_to_file(hashed_password)
            print(Fore.GREEN + f"Success!" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Your hashed password is: {hashed_password}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Press Enter to continue." + Style.RESET_ALL)
            input()
            clear_console()
        case "0":
            print(Fore.RED + Style.BRIGHT + "QUITING..." + Style.RESET_ALL)
            break
        case _:
            print("Unknown input, please try again.")
            clear_console()
