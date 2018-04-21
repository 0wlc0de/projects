import random
from pyRPGScript.gameClass.game import Person, bColors
from pyRPGScript.gameClass.Spells import Spell


ThunderBolt = Spell("ThunderBolt", 100, 120, 0, "Thunder")
HyperBeam = Spell("Hyper Beam", 120, 160, 0, "Normal")
FireBlast = Spell("Fire Blast", 100, 120, 0, "Fire")
Synthesis = Spell("Synthesis", 40, 0, "Normal", 200)
arrayAttacks = [ThunderBolt, HyperBeam, FireBlast, Synthesis]

playerName = input("Enter Player Name: ")
EnemyName = ["Harry", "Potter", "Carlos"]

Player1 = Person(playerName, 500, 250, 100, 10, arrayAttacks)
Player2 = Person(EnemyName[random.randrange(0, len(EnemyName))], 500, 100, 150, 10, [ThunderBolt, HyperBeam, FireBlast])


def damage_message(Attacker, Defender, generated_damage, attack_name):
    print(bColors.OKBLUE + Attacker.get_name() + bColors.ENDC, "uses",
          bColors.OKGREEN + attack_name + bColors.ENDC, "on",
          bColors.WARNING + Defender.get_name() + bColors.ENDC, "!!! damage output:", generated_damage,
          bColors.WARNING + Defender.get_name() + bColors.ENDC, "remaining HP: ",
          bColors.FAIL + str(Defender.hp) + bColors.ENDC, "/", bColors.FAIL + str(Defender.maxHp) + bColors.ENDC)


def healing_message(Player, attack_name, healing):
    print(bColors.OKBLUE + Player.get_name() + bColors.ENDC, "uses",
          bColors.OKGREEN + attack_name + bColors.ENDC, "to Heal",
          bColors.OKGREEN + str(healing) + bColors.ENDC, "of his health.",
          "remaining HP: ", bColors.FAIL + str(Player.hp) + bColors.ENDC, "/",
          bColors.FAIL + str(Player.maxHp) + bColors.ENDC)


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
        print(str(len(arrayAttacks) + 1), ": Back To Actions")
        chooseMagic = int(input("Choose Magic Attack: ")) - 1

        if chooseMagic == (len(arrayAttacks)):
            continue

        SpellClass = Player1.get_magic_class(chooseMagic)

        if Player1.mp < SpellClass.get_magic_cost():
            print(bColors.BOLD + bColors.FAIL + "Low on MP! Please Choose another Action." + bColors.ENDC)
            continue
        generatedDamage = 0
        if SpellClass.damage > 0:
            generatedDamage = SpellClass.get_magic_damage()
            Player2.take_damage(generatedDamage)
            damage_message(Player1, Player2, generatedDamage, SpellClass.get_magic_name())
        elif SpellClass.healing > 0:
            generateHealing = SpellClass.healing
            Player1.take_healing(generateHealing)
            healing_message(Player1, SpellClass.get_magic_name(), SpellClass.healing)

        Player1.take_manacost(SpellClass.get_magic_cost())
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
