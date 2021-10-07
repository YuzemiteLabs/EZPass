from math import floor
import string
import random
from colorama import Fore, Back, Style, init
import os
import webbrowser

def logo():
    os.system("cls")
    print(Fore.CYAN + " "*16 + "███████╗███████╗██████╗  █████╗  ██████╗ ██████╗")
    print(Fore.CYAN + " "*16 + "██╔════╝╚════██║██╔══██╗██╔══██╗██╔════╝██╔════╝")
    print(Fore.CYAN + " "*16 + "█████╗    ███╔═╝██████╔╝███████║╚█████╗ ╚█████╗ ")
    print(Fore.CYAN + " "*16 + "██╔══╝  ██╔══╝  ██╔═══╝ ██╔══██║ ╚═══██╗ ╚═══██╗")
    print(Fore.CYAN + " "*16 + "███████╗███████╗██║     ██║  ██║██████╔╝██████╔╝")
    print(Fore.CYAN + " "*16 + "╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═════╝ ")

def password_gen1(weak1,weak2,medium,strong,very_strong):
    global length
    os.system("cls")
    logo()
    print() 
    print(Fore.CYAN + "[" + Fore.WHITE + "i" + Fore.CYAN + "]" + Fore.WHITE + " " + "Tip: " + Fore.CYAN + "It is recommended to have at least 8 characters in your password.")
    length = int(input(Fore.CYAN + "[" + Fore.WHITE + ">" + Fore.CYAN + "] Enter password length: "))
    if length <= 0:
        print('Not a valid value. Please try again.')
        print('\n')
        input("Press any key to continue...")
        logo()
        password_gen1(weak1,weak2,medium,strong,very_strong)
    password_gen2(weak1,weak2,medium,strong,very_strong)

def password_gen2(weak1,weak2,medium,strong,very_strong):
    print()
    print(Fore.CYAN + "How strong would you like your password to be? Select an option from the list below.")
    print()
    print(Fore.CYAN + "[" + Fore.WHITE + "1" + Fore.CYAN + "] Weak - Lowercase characters only")
    print(Fore.CYAN + "[" + Fore.WHITE + "2" + Fore.CYAN + "] Weak - Uppercase characters only")
    print(Fore.CYAN + "[" + Fore.WHITE + "3" + Fore.CYAN + "] Medium - Lowercase characters + Uppercase characters")
    print(Fore.CYAN + "[" + Fore.WHITE + "4" + Fore.CYAN + "] Strong - Lowercase characters + Uppercase characters + Digits")
    print(Fore.CYAN + "[" + Fore.WHITE + "5" + Fore.CYAN + "] Very strong - Lowercase characters + Uppercase characters + Digits + Special characters")
    print()
    global strength_level 
    password_display = Fore.CYAN + "[" + Fore.WHITE + "i" + Fore.CYAN + "] Your password: "
    strength_level = int(input(Fore.CYAN + "[" + Fore.WHITE + ">" + Fore.CYAN + "] Enter your option: "))
    if strength_level == 1:
        print()
        print(password_display)
        for i in range(length):
                print(''.join(random.choice(weak1)),end='')
    elif strength_level == 2:
        print()
        print(password_display)
        for i in range(length):
                print(''.join(random.choice(weak2)),end='')
    elif strength_level == 3:
        print()
        print(password_display)
        for i in range(length):
                print(''.join(random.choice(medium)),end='')
    elif strength_level == 4:
        print()
        print(password_display)
        for i in range(length):
                print(''.join(random.choice(strong)),end='')
    elif strength_level == 5:
        print()
        print(password_display)
        for i in range(length):
                print(''.join(random.choice(very_strong)),end='')
    else:
        print('Not a valid option. Please try again.')
        exit
    print("\n")
    input("Press any key to continue...")
    print(Style.RESET_ALL)

def main():
    init()
    weak1 = list(string.ascii_lowercase)
    weak2 = list(string.ascii_uppercase)
    medium = list(string.ascii_uppercase + string.ascii_lowercase)
    strong = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    very_strong = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()")
    print(Fore.CYAN + "Welcome to EZPass! Using this program you can generate random passwords in just 5 seconds!")
    print(Fore.CYAN + "To start, please select an option from the list below.")
    print()
    print(Fore.CYAN + "[" + Fore.WHITE + "1" + Fore.CYAN + "] Run the password generator")
    print(Fore.CYAN + "[" + Fore.WHITE + "2" + Fore.CYAN + "] About the program")
    print(Fore.CYAN + "[" + Fore.WHITE + "3" + Fore.CYAN + "] Super Secret Settings")
    print()
    choice = int(input(Fore.CYAN + "[" + Fore.WHITE + ">" + Fore.CYAN + "] Enter your option: "))
    if choice == 1:
        password_gen1(weak1,weak2,medium,strong,very_strong)
    elif choice == 2:
        print()
        print(Fore.CYAN + "Made by yze#7749")
        print(Fore.CYAN + "Huge thanks to my friend for fixing some bugs")
        print(Fore.CYAN + "You're running build-alpha-1.0")
        print("\n")
        input("Press any key to return...")
        print(Style.RESET_ALL)
        logo()
        main()
    elif choice == 3:
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        print('Not a valid option. Please try again.')
        print("\n")
        input("Press any key to continue...")
        print(Style.RESET_ALL)
        logo()
        main()
logo()
main()