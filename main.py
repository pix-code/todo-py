from readchar import readkey
from readchar import key as Key
import os

choice = 0
key = ''
binds = {
        'a': 1,
        'r': 2,
        's': 3,
        't': 4,

        'n': 5,
        'e': 6,
        'i': 7,
        'o': 8,
        }

with open('data/raw', 'r') as file:
    choices = file.read().splitlines()

    for i in range(len(choices)):
        choices[i] = choices[i].split('\\')
        choices[i].pop()


def prntdo():
    os.system('clear')

    for i in range(len(choices)):
        if choice == i:
            print('→ ' + choices[i][0])

        else:
            print(f'{i+1} ' + choices[i][0])

        for j in range(1, len(choices[i])):
            if not j == len(choices[i]) - 1:
                print('  ├─' + choices[i][j])

            else:
                print('  ╰─' + choices[i][j])

        if len(choices[i]) > 1:
            print()


def newtask():
    print(f'\nadding entry for {choices[choice][0][5:]}')
    choices[choice].append(input().strip())
    write()


def tostring(s):
    str1 = ''
    for i in s:
        str1 += i

    return str1


def write():
    with open('data/raw', 'w') as file:
        for i in choices:
            str1 = ''

            for s in i:
                str1 += s + '\\'

            str1 += '\n'

            file.write(str1)


def delete():
    os.system('clear')
    print('Which entry would you like to delete?')
    print(f'  {choices[choice][0]}')

    for j in range(1, len(choices[choice])):
        if not j == len(choices[choice]) - 1:
            print(f'{j} ├─' + choices[choice][j])

        else:
            print(f'{j} ╰─' + choices[choice][j])

    key = readkey()

    if key != 'q':
        if not key.isdigit():
            key = binds[key]
        choices[choice].pop(int(key))

    write()


while True:
    prntdo()
    key = readkey()

    if key == Key.UP or key == 'u':
        if choice == 0:
            choice = 5

        else:
            choice -= 1

    elif key == Key.DOWN or key == 'e':
        if choice == 5:
            choice = 0

        else:
            choice += 1

    elif key == Key.ENTER or key == Key.SPACE:
        newtask()

    elif key.isdigit():
        if 1 <= int(key) <= 6:
            choice = int(key) - 1
            prntdo()
            newtask()

    elif key == 'd':
        delete()

    elif key == 'q':
        break

os.system('clear')
print('Have a productive day!')
