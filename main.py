from readchar import readkey
from readchar import key as Key
import os

choices = [
    ['java'],
    ['english'],
    ['apush'],
    ['math'],
    ['cs'],
    ['bio']]

choice = 0
prevchoice = 5


def prntdo():
    os.system('clear')

    for i in range(len(choices)):
        if choice == i:
            print('→ ' + choices[i][0])

        else:
            print(f'{i+1} ' + choices[i][0])

        for j in range(1, len(choices[i])):
            if j == len(choices[i]) - 1:
                print('  ╰─' + choices[i][j])

            else:
                print('  ├─' + choices[i][j])

        if len(choices[i]) > 1:
            print()


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
        print(f'adding entry for {choices[choice][0][5:]}')
        choices[choice].append(input())

    elif key.isdigit():
        if 1 <= int(key) <= 6:
            choice = int(key) - 1
            prntdo()

            print(f'adding entry for {choices[choice][0][5:]}')
            choices[choice].append(input())
