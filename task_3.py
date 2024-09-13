import sys
from pathlib import Path
from colorama import Fore

def print_structure(path, indent=""):
    try:
        directory = Path(path)
        if not directory.exists() or not directory.is_dir():
            print(Fore.RED + 'Error: The specified path does not exist or not a directory.')
            return
        for item in directory.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f"{indent}📂 {item.name}")
                print_structure(item, indent + " ┣ ")
            else:
                print(Fore.GREEN + f"{indent}📜 {item.name}")
    except Exception as e:
        print(Fore.RED + f'Error: {e}')

print_structure(sys.argv[1])
# python task_3.py /Users/mozzhakov/Documents/GitHub/goit-algo-hw-04  