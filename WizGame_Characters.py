import random


class Creature:
    # Magic method -
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
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

    def attack(self, active_creature):
        # print(type(active_creature), active_creature)
        print('----------FIGHT-------------')
        print('The Wizard {} attacks {}!'.format(
            self.name, active_creature.name
        ))

        # red_roll = random.randint(1, 12) * self.level
        red_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1, 12) * active_creature.level
        creature_roll = active_creature.get_defensive_roll()

        print("Red's Power is : {} !!!".format(red_roll))
        print("Enemy {}'s power is : {}".format(active_creature.name, creature_roll))

        if red_roll >= creature_roll:
            print('Red won against enemy {}!!!'.format(active_creature.name))
            return True
        else:
            print('Red has been DEFEATED..')
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breath_fire):
        super().__init__(name, level)
        self.breath_fire = breath_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breath_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1

        # fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breath_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier