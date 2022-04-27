import os
from termcolor import colored

size = os.get_terminal_size()
directories, files = os.walk('.').__next__()[1:]
# print(directories, files)
line_length = size.columns
cur_line = 0

colored_items = []
for directory in directories:
    if len(directory) + 2 + cur_line > line_length:
        print()
        cur_line = 0
    cur_line += len(directory) + 3
    colored_items.append(colored(" " + directory + " ", 'yellow', attrs=["reverse"]))
    print(colored_items[-1], end=' ')

for file in files:
    if len(file) + 2 + cur_line > line_length:
        print()
        cur_line = 0
    cur_line += len(file) + 3
    i = len(file)
    track = ""
    while i > 0:
        if file[i - 1] == ".":
            track = track[::-1]
            break
        track += file[i - 1]
        i -= 1
    else:
        track = ""
    match track:
        case 'py':
            last = colored(" " + file + " ", 'cyan', attrs=["reverse"])
            colored_items.append(last)
        case 'txt':
            last = colored(" " + file + " ", 'green', attrs=["reverse"])
            colored_items.append(last)
        case 'lnk':
            last = colored(" " + file + " ", 'white', attrs=["reverse", "underline"])
            colored_items.append(last)
        case 'exe':
            last = colored(" " + file + " ", 'blue', attrs=["reverse"])
            colored_items.append(last)
        case _:
            last = colored(" " + file + " ", 'white', attrs=["reverse"])
            colored_items.append(last)
    print(last, end=' ')

