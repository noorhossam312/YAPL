import os
from exceptions import *

RED = "\033[31m"
RESET = "\033[0m"

def check(file_path):
    if not file_path.endswith(".ypl"):
        raise InvalidExtensionError(f"{RED}Expected {os.path.basename(file_path).split(".")[0]}.ypl, got {os.path.basename(file_path)}{RESET}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{RED}File does not exist{RESET}")

file = input(r"""
 __      __   ______   _______   __
|  \    /  \ /      \ |       \ |  \
 \$$\  /  $$|  $$$$$$\| $$$$$$$\| $$
  \$$\/  $$ | $$__| $$| $$__/ $$| $$
   \$$  $$  | $$    $$| $$    $$| $$
    \$$$$   | $$$$$$$$| $$$$$$$ | $$
    | $$    | $$  | $$| $$      | $$_____
    | $$    | $$  | $$| $$      | $$     \
     \$$     \$$   \$$ \$$       \$$$$$$$$

path to file.ypl
╰─ """)

check(file)

with open(file) as f:
    f_split = f.read().splitlines()
    env = {}
    for line in f_split:
        space_split = line.split(" ")
        if line.startswith("$"):
            v_name = line.split(" ")[0][1:]
            key = " ".join(line.split(" ")[2:])
            if '+' in key:
                _key = str(eval(key))
                key = _key
            elif '-' in key:
                _key = str(eval(key))
                key = _key
            elif '*' in key:
                _key = str(eval(key))
                key = _key
            elif '/' in key:
                _key = str(eval(key))
                key = _key
            env[v_name] = key
        if line.startswith("print"):
            text = space_split[1:]
            for i in text:
                if i.startswith("$"):
                    text[text.index(i)] = env[i[1:]]
            print(" ".join(text))
