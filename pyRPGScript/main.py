import random
from pyRPGScript.gameClass.game import Person, bColors


magic = [{"name": "Thunderbolt", "cost": 60, "damage": 100},
         {"name": "Hyper Beam", "cost": 120, "damage": 160},
         {"name": "Fire Blast", "cost": 120, "damage": 140}]

playerName = input("Enter Player Name: ")
EnemyName = ["Harry", "Potter", "Carlos"]
Player1 = Person(playerName, 500, 250, 100, 10, magic)
Player2 = Person(EnemyName[random.randrange(0, len(EnemyName))], 500, 100, 150, 10, magic)


def damage_message(Attacker, Defender, generated_damage, attack_name):
    print(bColors.OKBLUE + Attacker.get_name() + bColors.ENDC, "uses",
          bColors.OKGREEN + attack_name + bColors.ENDC, "on",
          bColors.WARNING + Defender.get_name() + bColors.ENDC, "!!! damage output:", generated_damage,
          bColors.WARNING + Defender.get_name() + bColors.ENDC, "remaining HP: ",
          bColors.FAIL + str(Defender.hp) + bColors.ENDC, "/", bColors.FAIL + str(Defender.maxHp) + bColors.ENDC)


print("Your Enemy is:", bColors.WARNING + Player2.get_name() + bColors.ENDC, "HP:",
      bColors.FAIL + str(Player2.hp) + bColors.ENDC, "/", bColors.FAIL + str(Player2.maxHp) + bColors.ENDC)
runningGame = True

while runningGame:
    print("=============================================")
    Player1.generate_actions()
    chooseAction = input("Choose Action: ")
    if chooseAction == '1':
        generatedDamage = Player1.generate_damage()
        Player2.take_damage(generatedDamage)
        damage_message(Player1, Player2, generatedDamage, "Normal Attack")
    elif chooseAction == '2':

        Player1.get_magic()
        chooseMagic = int(input("Choose Magic Attack: ")) - 1
        generatedDamage = Player1.get_magic_damage(chooseMagic)
        if Player1.mp < Player1.get_magic_cost(chooseMagic):
            print(bColors.BOLD + bColors.FAIL + "Low on MP! Please Choose another Action." + bColors.ENDC)
            continue
        else:
            Player2.take_damage(generatedDamage)
            Player1.take_manacost(Player1.get_magic_cost(chooseMagic))
            damage_message(Player1, Player2, generatedDamage, Player1.get_magic_name(chooseMagic))
    else:
        print(Player1.get_name(), ": ", bColors.BOLD + bColors.FAIL + "Invalid Choice of Action" + bColors.ENDC)
        continue

    if Player2.hp == 0:
        print(bColors.OKBLUE + bColors.BOLD + "You Win! Congratulations! " + bColors.ENDC)
        runningGame = False
        break

    generatedDamage = Player2.generate_damage()
    Player1.take_damage(generatedDamage)
    damage_message(Player2, Player1, generatedDamage, "Normal Attack")

    if Player1.hp == 0:
        print(bColors.FAIL + bColors.BOLD + "You Lost to " + Player2.get_name() + ". Please Try Again." + bColors.ENDC)
        runningGame = False




