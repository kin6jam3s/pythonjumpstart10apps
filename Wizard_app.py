import random
import time

import WizGame_Characters
from WizGame_Characters import Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------')
    print('    Wizard Game')
    print('--------------------')


def game_loop():
    # creatures = [
    #     Creature('Toad', 1),
    #     Creature('Tiger', 12),
    #     Creature('Bat', 3),
    #     Creature('Dragon', 50),
    #     Creature('Evil Wizard', 1000),
    #
    # ]
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        WizGame_Characters.Wizard('Evil Wizard', 1000),

    ]

    # print(type(creatures))
    hero = WizGame_Characters.Wizard('Red Red', 75)

    # print(hero)

    cmd = 'EMPTY'
    while cmd != 'x':

        # print(type(creatures))    <class 'list'>

        active_creature = random.choice(creatures)
        # print('--->', active_creature)
        # print(type(active_creature))  # <class 'WizGame_Characters.Creature'>
        print('A {} of level {} has appear from a dark foggy forest...'.format(
            active_creature.name, active_creature.level
        ))

        cmd = input('Do [a]ttack, [r]unaway, or [l]ookaround: ')
        if 'a' == cmd.lower().strip():
            # print('Attack')
            # Send active_creature variable to attack module under class Wizard
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('Red runs back to his Mommy ADANA to eat Sinigang to recover...')
                time.sleep(5.1)
                print('Bonjing Red recovered!!!')
        elif 'r' == cmd.lower().strip():
            print('Bonjing {} Cries and RunAway'.format(hero.name))
        elif 'l' == cmd.lower().strip():
            # print('Lookaround')
            print('The Bonjing {} Scans the surrounding and sees'.format(hero.name))
            for i in creatures:
                print('* A {} of level {}'.format(i.name, i.level))
        elif cmd != 'x' and cmd:
            print('Input not valid.. Try again')
            # break  <- This could be an alternate option for pressing 'x'

        if not creatures:  # default Empty = False
            print('You defeated all the Enemy')
            break

        print('--------------------------------------')

    print('GoodBye')


if __name__ == "__main__":
    main()
