import random

import re


class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items, player_type):
        self.player_type = player_type
        self.items = items
        self.playerName = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkMin = atk - 10
        self.atkMax = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic', 'Items']

    def get_name(self):
        return self.playerName

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def generate_damage(self):
        return random.randrange(self.atkMin, self.atkMax)

    def generate_actions(self):
        iterate = 1
        print("Actions: ")
        for action in self.actions:
            print(str(iterate) + ":", action)
            iterate += 1

    def get_magic(self):
        iterate = 1
        print("---------------------------------------------")
        print("Remaining MP:", self.mp, "/", self.maxMp)
        print("Choose Magic to Attack: ")
        for spells in self.magic:
            if spells.damage > 0:
                print("    ", iterate, ":", bColors.BOLD + bColors.OKGREEN + spells.name + bColors.ENDC, "dmg:",
                      bColors.BOLD + bColors.FAIL + str(spells.damage) + bColors.ENDC)
            else:
                print("    ", iterate, ":", bColors.BOLD + bColors.OKGREEN + spells.name + bColors.ENDC, "heal:",
                      bColors.BOLD + bColors.FAIL + str(spells.healing) + bColors.ENDC)
            iterate += 1

    def get_items(self):
        iterate = 1
        print("Choose Items in your Inventory")
        for item in self.items:
            print("    ", iterate, ":", bColors.OKBLUE + item.name + bColors.ENDC, ">",
                  bColors.OKGREEN + "\"" + item.description + "\"" + bColors.ENDC, "x" + str(item.qty))
            iterate += 1

    def get_magic_class(self, i):
        return self.magic[i]

    def take_manacost(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0

    def take_healing(self, healing):
        self.hp += healing
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def take_mp_healing(self, healing):
        self.mp += healing
        if self.mp > self.maxMp:
            self.mp = self.maxMp

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHp) * 100 / 4

        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxMp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += "  "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        spaces = re.sub('[a-zA-Z0-9]', ' ', self.playerName)
        print("Name", "(", self.player_type, ")")
        print(spaces + "           ________________________________________")
        print(self.playerName + ":" + "   HP :  |" + bColors.OKGREEN + bColors.BOLD + hp_bar + bColors.ENDC)
        print(spaces + "           ________________")
        print(spaces + " " + "   MP :  |" + bColors.OKBLUE + bColors.BOLD + mp_bar + bColors.ENDC)
        print("\n")

