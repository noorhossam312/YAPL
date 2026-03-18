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
if not file:
    file = "tests\\hello_world.ypl"
check(file)

with open(file) as f:
    f_split = f.read().splitlines()
    env = {}
    condition_tf = True
    for line_num, line in enumerate(f_split):
        line = line.lstrip()
        space_split = line.split(" ")
        if not condition_tf:
            if not line.startswith(";"):
                continue
            else:
                condition_tf = True
                continue
        if line.startswith("$"):
            v_name = line.split(" ")[0][1:]
            key = " ".join(line.split(" ")[2:])
            if '+' in key:
                key = str(eval(key))
            elif '-' in key:
                key = str(eval(key))
            elif '*' in key:
                key = str(eval(key))
            elif '/' in key:
                key = str(eval(key))
            env[v_name] = key
            continue
        if line.startswith("print"):
            text = space_split[1:]
            for i in text:
                if i.startswith("$"):
                    text[text.index(i)] = env[i[1:]]
            print(" ".join(text))
            continue
        if line.startswith("if"):
            condition = line[2:]
            if condition[0] == " ":
                condition = condition[1:]
            condition = condition[1:-1]
            operator = condition.split(" ")[1]
            var_a = env[condition.split(" ")[0]]
            var_b = env[condition.split(" ")[2][1:]] # It just works, don't ask me how it works
            if operator == "is":
                try:
                    var_a = float(var_a)
                except ValueError:
                    pass
                try:
                    var_b = float(var_b)
                except ValueError:
                    pass
                if var_a != var_b:
                    condition_tf = False
            continue
            # print(f"{var_a} {type(var_a)} {var_b} {type(var_b)}")  # debug
            # print(operator)  # debug

        if not line.startswith(";"):
            raise SyntaxError(f"{RED}Invalid syntax on line number {line_num+1}.\n{line}{RESET}")
