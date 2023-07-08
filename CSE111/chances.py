import math
import random
error = 'That is not a valid answer. Please try again'

def main():
    choice = int(input('Choose a game to calculate chances for: (1:Star rail, 2:Final Fantasy XIV)'))
    if choice == 1:
        print('Which category would you like to calculate?')
        print('1: Relics')
        print('2: Pulls')
        print()
        choice = int(input())
        if choice == 1:
            star_rail_relic_chance()
        elif choice == 2:
            star_rail_pull_chance()
        else:
            print(error)
    elif choice == 2:
        print('Which category would you like to calculate?')
        print('1: Cactbot')
        print('2: Crit/DH')
        print()
        choice = int(input())
        if choice == 1:
            ff14_cactbot_chance()
        elif choice == 2:
            ff14_crit_chance()
        else:
            print(error)
    else:
        print(error)


def star_rail_relic_chance():
    print('Which piece of gear do you want to calculate?')
    print('(Body)')
    print('(Feet)')
    print('(Sphere)')
    print('(Rope)')
    piece = input()
    print()
    if piece.upper() == 'BODY':
        print('The chances of getting the Main Stat you want is:')
        calc = (1 / 7) * 100
        print(f'Approximately {calc:.2f}%')
        substat(calc)
    elif piece.upper() == 'FEET':
        print('The chances of getting the Main Stat you want is:')
        calc = (1 / 4) * 100
        print(f'Approximately {calc:.2f}%')
        substat(calc)
    elif piece.upper() == 'SPHERE':
        print('The chances of getting the Main Stat you want is:')
        calc = (1 / 10) * 100
        print(f'Approximately {calc:.2f}%')
        substat(calc)
    elif piece.upper() == 'ROPE':
        print('The chances of getting the Main Stat you want is:')
        calc = (1 / 5) * 100
        print(f'Approximately {calc:.2f}%')
        substat(calc)
    else:
        print(error)

    return

def star_rail_pull_chance():
    
    return

def ff14_cactbot_chance():

    return

def ff14_crit_chance():

    return

def substat(armor):
    armor = armor / 100
    print()
    choice = input('Do you want to calculate ONE substat chance or FOUR chances: ')
    print()
    if choice.upper() == 'ONE' or choice == '1':
        print('The chances of getting a Sub Stat you want with your main stat is:')
        calc = (1 / 8) * armor * 100
        print(f'Approximately {calc:.2f}%')
    elif choice.upper() == 'FOUR' or choice == '4':
        print('The chances of getting all Sub Stats you want with your main stat is:')
        calc = (1 / 11) * (1 / 10) * (1 / 9) * (1 / 8) * armor * 100
        print(f'Approximately {calc:.4f}%')
    else:
        print(error)
    return

main()