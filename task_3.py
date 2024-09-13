import sys
from pathlib import Path
from colorama import Fore

def print_structure(path):
    try:
        directory = Path(path)
        if not directory.exists() or not directory.is_dir():
            print(Fore.RED + 'Error: The specified path does not exist or not a directory.')
        for item in directory.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f'📂 {item}')
                print_structure(item)
            else: 
                print(Fore.GREEN + f'📜 {item}') 
    except Exception as e:
        print(Fore.RED + f'Error: {e}')

print_structure(sys.argv[1])


# python task_3.py /Users/mozzhakov/Documents/GitHub/goit-algo-hw-04  