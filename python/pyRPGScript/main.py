import random
from pyRPGScript.gameClass.game import Person, bColors
from pyRPGScript.gameClass.Spells import Spell
from pyRPGScript.gameClass.inventory import Items


# Create Magic Attacks
ThunderBolt = Spell("ThunderBolt", 100, 120, 0, "Thunder")
HyperBeam = Spell("Hyper Beam", 120, 160, 0, "Normal")
FireBlast = Spell("Fire Blast", 100, 120, 0, "Fire")
Synthesis = Spell("Synthesis", 40, 0, "Normal", 200)
arrayAttacks = [ThunderBolt, HyperBeam, FireBlast, Synthesis]

# Create Items in Inventory
Potion = Items("Potion", "HP", "Heals 100 of your Hit Points", 100, 5)
Elixir = Items("Elixir", "Restoration", "Heals 100 of your HP and MP", 100, 5)
Grenade = Items("Grenade", "Damage", "Deals 50 HP to your Opponents", 50, 2)
arrayItems = [Potion, Elixir, Grenade]

# Create Player Variables
playerName = input("Enter Player Name: ")
EnemyName = ["Harry", "Potter", "Carlos"]
Player1 = Person(playerName, 500, 250, 100, 10, arrayAttacks, arrayItems, "Player")
Player2 = Person(EnemyName[random.randrange(0, len(EnemyName))], 500, 100, 150, 10,
                 [ThunderBolt, HyperBeam, FireBlast], arrayItems, "Opponent")


# Create Damage Message for Simplicity Passing of Objects
def damage_message(Attacker, Defender, generated_damage, attack_name):
    print(bColors.OKGREEN + bColors.BOLD + "Battle Status: " + bColors.ENDC,
          bColors.OKBLUE + Attacker.get_name() + bColors.ENDC, "uses",
          bColors.OKGREEN + attack_name + bColors.ENDC, "on",
          bColors.WARNING + Defender.get_name() + bColors.ENDC, "!!! damage output:", generated_damage,
          bColors.WARNING + Defender.get_name() + bColors.ENDC, "remaining HP: ",
          bColors.FAIL + str(Defender.hp) + bColors.ENDC, "/", bColors.FAIL + str(Defender.maxHp) + bColors.ENDC)


# Create Healing Message for Simplicity Passing of Objects
def healing_message(Player, attack_name, healing, type_heal):
    content = 'HP'
    if type_heal == 'Restoration':
        content = 'HP and MP'

    print(bColors.OKBLUE + Player.get_name() + bColors.ENDC, "uses",
          bColors.OKGREEN + attack_name + bColors.ENDC, "to Heal",
          bColors.OKGREEN + str(healing) + bColors.ENDC, "of his " + content + ".",
          "remaining HP: ", bColors.FAIL + str(Player.hp) + bColors.ENDC, "/",
          bColors.FAIL + str(Player.maxHp) + bColors.ENDC,
          "remaining MP: ", bColors.OKBLUE + str(Player.mp) + bColors.ENDC, "/",
          bColors.OKBLUE + str(Player.maxMp) + bColors.ENDC)


print("\n")

Player1.get_stats()

# Initial Printing of Enemy Name and Starting the game using the runningGame boolean
print("Your Enemy is:", bColors.WARNING + Player2.get_name() + bColors.ENDC, "HP:",
      bColors.FAIL + str(Player2.hp) + bColors.ENDC, "/", bColors.FAIL + str(Player2.maxHp) + bColors.ENDC)
runningGame = True


# The whole game in While Loop
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
        print("    ", str(len(arrayAttacks) + 1), ": Back To Actions")
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
            healing_message(Player1, SpellClass.get_magic_name(), SpellClass.healing, SpellClass.type)

        Player1.take_manacost(SpellClass.get_magic_cost())
    elif chooseAction == '3':
        Player1.get_items()
        print("    ", str(len(arrayItems) + 1), ": Back To Actions")
        chooseItem = int(input("Choose Item: ")) - 1

        if chooseItem == (len(arrayItems)):
            continue

        ItemClass = Player1.items[chooseItem]

        if ItemClass.type == 'HP':
            Player1.take_healing(ItemClass.deal)
            healing_message(Player1, ItemClass.name, ItemClass.deal, "Normal")
            ItemClass.take_qty(1)
        elif ItemClass.type == 'Restoration':
            Player1.take_healing(ItemClass.deal)
            Player1.take_mp_healing(ItemClass.deal)
            healing_message(Player1, ItemClass.name, ItemClass.deal, ItemClass.type)
            ItemClass.take_qty(1)
        elif ItemClass.type == 'Damage':
            Player2.take_damage(ItemClass.deal)
            damage_message(Player1, Player2, ItemClass.deal, ItemClass.name)
            ItemClass.take_qty(1)

        if ItemClass.qty == 0:
            Player1.items.remove(ItemClass)

    else:
        print(Player1.get_name(), ": ", bColors.BOLD + bColors.FAIL + "Invalid Choice of Action" + bColors.ENDC)
        continue

    if Player2.hp == 0:
        print(bColors.OKBLUE + bColors.BOLD + "You Win! Congratulations! " + bColors.ENDC)
        runningGame = False
        pass
    else:
        generatedDamage = Player2.generate_damage()
        Player1.take_damage(generatedDamage)
        damage_message(Player2, Player1, generatedDamage, "Normal Attack")

    if Player1.hp == 0:
        print(bColors.FAIL + bColors.BOLD + "You Lost to " + Player2.get_name() + ". Please Try Again." + bColors.ENDC)
        runningGame = False
        pass

    print("\n")
    Player1.get_stats()
    Player2.get_stats()


