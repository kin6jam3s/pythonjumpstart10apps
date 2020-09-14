import random


class Creature:  # This class will be the base for all creature for variable 'name' and 'level'
    # Magic method -
    def __init__(self, name, level):
        self.name = name
        self.level = level

    # This will convert <WizGame_Characters.SmallAnimal object at 0x100d32520> to [Creature: Toad of level 1]
    def __repr__(self):
        # This will show
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):  # For class name should start with CAPITAL letter
    # Magic method - Self is the pointer to the object that actually created in init
    # def __init__(self, name, the_level):
    #     super().__init__(name, the_level)
    # self.name = name
    # self.level = the_level

    # def __repr__(self):
    #     return "Wizard: {} of level {}".format(
    #         self.name, self.level
    #     )
    #
    def __init__(self, name, level, super_power):  # initialise function variable
        super().__init__(name, level)  # declare that it will use Creature parameter for name and level
        self.super_power = super_power  # adding new modifier

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        power_modifier = 10 if self.super_power else 1
        print('Wizard : {}'.format(self.name), base_roll * power_modifier)
        return base_roll * power_modifier

    # Class Creature was called on Wizard class
    def attack(self, active_creature):
        print(type(active_creature), active_creature.name, active_creature.level,
              active_creature)  # <class 'WizGame_Characters.SmallAnimal'> Creature: Toad of level 1
        print('----------FIGHT-------------')
        print('The Wizard {} attacks {}!'.format(
            self.name, active_creature.name
        ))

        # red_roll = random.randint(1, 12) * self.level
        red_roll = self.get_defensive_roll()  # using function under class Creature | self for Wizard
        # creature_roll = random.randint(1, 12) * active_creature.level
        creature_roll = active_creature.get_defensive_roll()  # # using function under class Creature

        print("Red's Power is : {} !!!".format(red_roll))
        print("Enemy {}'s power is : {}".format(active_creature.name, creature_roll))

        # compare the roll and determine the winner
        if red_roll >= creature_roll:
            print('Red won against enemy {}!!!'.format(active_creature.name))
            return True
        else:
            print('Red has been DEFEATED..')
            return False


# This will be use base on the active_creature, if class creature is SmallAnimal
# then it will use this get_defensive_roll
class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # print('----', base_roll / 2, self.name)
        return base_roll / 2


# Creature class imported
class Dragon(Creature):
    #  Magic method
    def __init__(self, name, level, scaliness, breath_fire):  # initialise function variable
        super().__init__(name, level)  # declare that it will use Creature parameter for name and level
        self.breath_fire = breath_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()  # use get_defensive_roll() function under Creature class
        # fire_modifier = None
        # if self.breath_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        # --> Dragon('Dragon', 50, 75, True)
        # fire modifier is 5 if True and 1 for False
        # fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breath_fire else 1
        # print(self.scaliness) - 75
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier
