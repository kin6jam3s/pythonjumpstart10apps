import random
import time

import WizGame_Characters
from WizGame_Characters import Creature, SmallAnimal, Dragon


def main():
    # calling function for printing header
    print_header()
    # calling the function for game loop
    game_loop()


# Function for creating the header
def print_header():
    print('--------------------')
    print('    Wizard Game')
    print('--------------------')


#
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
    # This is for initializing the value of cmd | should be not empty
    cmd = 'EMPTY'
    # Loop statement using while cmd not equal to 'x'
    while cmd != 'x':
        # print(type(creatures))    <class 'list'>
        # selecting creature using random module using choice option
        active_creature = random.choice(creatures)
        # print('--->', active_creature)
        # print(type(active_creature))  # <class 'WizGame_Characters.Creature'>
        print('A {} of level {} has appear from a dark foggy forest...'.format(
            active_creature.name, active_creature.level
        ))
        # User input to the action to perform
        cmd = input('Do [a]ttack, [r]unaway, or [l]ookaround: ')
        # if statement when cmd equals to 'a' - str converted to lower and strip space
        if 'a' == cmd.lower().strip():
            # print('Attack')
            # Send active_creature variable to attack module under class Wizard
            if hero.attack(active_creature):  # if return is True proceed to remove that random creature on the list
                creatures.remove(active_creature)
            else:  # if False
                print('Red runs back to his Mommy ADANA to eat Sinigang to recover...')
                time.sleep(5.1)  # import time module and use option sleep for pause
                print('Bonjing Red recovered!!!')
        # if statement when cmd equals to 'r' - str converted to lower and strip space
        elif 'r' == cmd.lower().strip():  # run away and go back to start selecting a new random creature
            print('Bonjing {} Cries and RunAway'.format(hero.name))
        # if statement when cmd equals to 'l' - str converted to lower and strip space
        elif 'l' == cmd.lower().strip():
            # print('Lookaround')
            print('The Bonjing {} Scans the surrounding and sees'.format(hero.name))
            for i in creatures:
                # print('---->',type(creatures), creatures) - <class 'list'> [Creature: Toad of level 1 ..]
                print('* A {} of level {}'.format(i.name, i.level))
        # if statement when cmd not equal to 'a','l' or 'x'
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
