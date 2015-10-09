import random


class Monster:
    sound = "Rarr!"

    def __init__(self, sound="Rarr!", left_hand=None, right_hand=None):
        self.sound = sound
        self.left_hand = left_hand
        self.right_hand = right_hand

    def attack(self):
        print("The monster cries '{}' and attacks!".format(self.sound))

    def give_up(self):
        print("The monster throws down its weapons and runs away!")

    def __getitem__(self, item):
        try:
            return self.__dict__[item]
        except KeyError as err:
            raise err


class Troll(Monster):
    sound = "Well, actually..."
    bridge = False

    def give_up(self):
        print("The troll yells 'Never!' and calls in Twitter reinforcements!")

    def attack(self):
        print("The troll says something mean about you.")
        super().attack()


class Dungeon:
    trouble = []

    def __init__(self, monsters=None):
        if monsters:
            self.trouble.extend(monsters)

    def __iter__(self):
        random.shuffle(self.trouble)
        return (m for m in self.trouble)
