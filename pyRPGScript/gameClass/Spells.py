import random


class Spell:
    def __init__(self, name, cost, damage, type_attack, healing=0):
        self.healing = healing
        self.type = type_attack
        self.damage = damage
        self.cost = cost
        self.name = name

    def get_magic_damage(self):
        magic_damage_min = self.damage - 10
        magic_damage_max = self.damage + 10
        return random.randrange(magic_damage_min, magic_damage_max)

    def get_magic_cost(self):
        return self.cost

    def get_magic_name(self):
        return self.name
