import random
error = 'That is not a valid answer. Please try again'
def main():
    choice = int(input('Choose a game to calculate chances for (1: Star rail, 2: Final Fantasy XIV): '))
    print()
    if choice == 1:
        star_rail_relic_chance()
    elif choice == 2:
        ff14_crit_chance()
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

def ff14_crit_chance():
    hit = random.randrange(1,100)
    crit = int(input('What is your Crit stat? '))
    if crit < 400:
        print('Your base stat is more than 400. Please try again.')
        exit()
    crit_rate = (((200 * (crit - 400)/1900) + 50)/1000) * 100
    crit_damage = ((200 * (crit - 400)/1900) + 1400)/1000
    dh_damage = ff14_dh()
    print(f'Your crit chance is {crit_rate:.2f}%')
    print(f'Your expected damage multiplier is {crit_damage:.2f}x damage')
    print(f'Your direct hit chance is {dh_damage:.2f}%')
    print()
    if crit_rate + dh_damage >= hit:
        crit_dh = crit_damage * 1.25
        print('You scored a Direct Crit Hit!')
        print(f'Your damage multiplier is {crit_dh:.2f}x damage!')
    return

def ff14_dh():
    dh = int(input('What is your Direct Hit stat? '))
    if dh < 400:
        print('Your base stat is more than 400. Please try again.')
        exit()
    dh_rate = (550 * (dh - 400)/1900) /1000
    return dh_rate

main()