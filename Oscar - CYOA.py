class Item(object):
    def __init__(self, weapon, consumable, armor, name, egg):
        self.weapon = weapon
        self.consumable = consumable
        self.armor = armor
        self.name = name
        self.egg = egg


class egg(Item):
    def __init__(self, crackegg, takeegg, consumable, name):
        super(egg, self).__init__(armor, consumable, name, egg, takeegg)
        self.crackegg = crackegg
        self.takeegg = takeegg
        
    def crackegg(self):
        print("You crack the egg open you can see the baby animal inside you can hear something loud roar in the"
              "background already knowing it has the intent to kill.")
        
        
class Weapon(Item):
    def __init__(self, longrange, closerange, name, weapondamage, armor,):
        super(Weapon, self).__init__(longrange, closerange, armor, name, egg)
        self.closerange = closerange
        self.longrange = longrange
        self.weapondamage = weapondamage
        self.name = name


class Bow(Weapon):
    def __init__(self, longrange, weapondamage, name, closerange):
        super(Bow, self).__init__(longrange, name, weapondamage, armor, closerange)
        self.weapondamage = weapondamage
        self.name = name

    def name(self):
        print("Archers Bow")

    def weapondamage(self):
        if self.weapondamage < 5:
            print()


class Sword(Weapon):
    def __init__(self, closerange, name, weapondamage, longrange):
        super(Sword, self).__init__(closerange, name, weapondamage, armor, longrange)

    def name(self):
        print("Great Toothed Sword ")

    def weapondamage(self):
        if self.closerange < 40:
            print("You inspect the sword it does not of damage")


class Consumable(Item):
    def __init__(self, healthpot, Regenpot, Meat, Speeedpot, Strengthpot, health, stamina, MaxHealth, weapon,
                 consumable, armor, name):
        super(Consumable, self).__init__(weapon,consumable, armor,name, egg)
        self.healthpot = healthpot
        self.Regenpot = Regenpot
        self.Meat = Meat
        self.Speedpot = Speeedpot
        self.Strengthpot = Strengthpot
        self.health = health
        self.stamina = stamina
        self.MaxHealth = MaxHealth


class healthpot(Consumable):
    def __init__(self, health, healthpot,):
        super(healthpot, self).__init__(health,)
        if self.health < 10:
            print("You drink a healthpot you feel good and go back into the fight")

    def regenpot(self):
        if self.health < 30:
            print("You pop the lid of the pot and chug the position you feel good")


class Meat(Consumable):
    def __init__(self, health, regeneration, stamina, ):
        super(Meat, self).__init__(health, regeneration, stamina,)
        if self.health < 5:
            if self.stamina < 70:
                print("You eat the meat until there was bone you feel you can run around the whole island in"
                      "two seconds.")


class Speedpot(Consumable):
    def __init__(self, stamina):
        super(Speedpot, self).__init__(stamina, Speedpot,)
        if self.stamina < 20:
            print("You drink the potion your hands start to vibrate rapidly you feel you can outrun a lighting bolt")


class Strengthpot(Consumable):
    def __init__(self, carrymoreweapons, ):
        super(Strengthpot, self).__init__("Maxhealth", "stamina",)
        self.carrymoreweapons = carrymoreweapons
        if self.MaxHealth < 50:
            if self.carrymoreweapons < 2:
                if self.stamina < 2:
                    print("You drink the potion you fall to your kneels from a surging pain coming from your hart you"
                          "wait until the pain goes away then you feel strong like you can lift the world")


class armor(Item):
    def __init__(self, heavyarmor, lightarmor, durability, enchantment, heavyenchantment, slowmovement, fastmovement,
                 armor):
        super(armor, self).__init__()
        self.heavyarmor = heavyarmor
        self.lightarmor = lightarmor
        self.durability = durability
        self.enchantment = enchantment
        self.heavyenchantment = heavyenchantment
        self.slowmovement = slowmovement
        self.fastmovement = fastmovement


class heavyarmor(armor):
    def __init__(self, enchantment, heavyenchantment, slowmovement, durability, ):
        super(heavyarmor, self).__init__(enchantment, heavyenchantment, slowmovement, durability,)
        if self.durability < 100:
            if self.slowmovement < 50:
                print("You put on the heavy armor when you take your first step it's slow and heavy but you feel while"
                      "protected.")


class enchant(heavyarmor):
    def __init__(self, enchantment, heavyenchantment, durability, slowmovement, ):
        super(enchant, self).__init__(enchantment, heavyenchantment, durability, slowmovement, )
        if self.enchantment < armor < 50:
            if self.heavyenchantment < durability < 60:
                print("You use a enchanting crystal on your heavy armor you feel more protected.")


class lightarmor(armor):
    def __init__(self, enchantment, heavyenchantment, durability, fastmovement,):
        super(lightarmor, self).__init__(enchantment, heavyenchantment, durability, fastmovement, )
        if self.durability < 50:
            if self.fastmovement < 50:
                print("You put on the light armor you feel you can run forever but also feel very open to attacks")


class enchant1(lightarmor):
    def __init__(self, enchantment, heavyenchantment, durability, slowmovement, ):
        super(enchant1, self).__init__(enchantment, heavyenchantment, durability, slowmovement, )
        if self.enchantment < armor < 50:
            if self.heavyenchantment < durability < 60:
                print("You use a enchanting crystal on your heavy armor you feel more protected.")


class Character(object):
    def __init__(self, takedamage, attack, health, dialogue, statseffect, regeneratehealth, criticalhit, posion,
                 inspect, room, forest, corner,):
        self.takedamage = takedamage
        self.attack = attack
        self.dialogue = dialogue
        self.health = health
        self.statseffect = statseffect
        self.regeneratehealth = regeneratehealth
        self.criticalhit = criticalhit
        self.posion = posion
        self.inspect = inspect
        self.room = room
        self.forest = forest
        self.corner = corner

    def attack(self):
        if self.attack < 12:
            print("You charge the monster and give a good swing with your sword it hits the monster and backs off")
        else:
            if self.attack < 0:
                print("You attack the monster with a big sword swing the monster backs off and your swing misses")

    def health(self):
        self.health = 200
        self.takedamage = -10

    def takedamage(self, health):
        if self.health < -10:
            print("You get hit by a hug right swing but once you hit the ground you feel fine and continue the fight.")
        else:
            print("You get hit by a hug left swing you get lunched towards a wall full force you get up feeling a pit"
                  "stun from the hit but as soon you get on your feet you continue the fight.")
            self.health = health
            self.criticalhit = -50
            print("You get hit by a devastating right swing it knocks you onto a wall making the wall shatter from the"
                  "impact you fall towards the ground you get up you feel like two cannons hit you in the face full"
                  "force but you overcome the pain and keep fighting.")

    def statseffect(self):
        self.posion = self.health < - 5
        self.regeneratehealth = self.health < 20

    def dialouge(self, room, forest, corner):
        self.inspect = self.room, self.forest, self.corner
        self.room = room
        self.forest = forest
        self.corner = corner
        print("There's a object here of use in this area say's a odd voice in your head")


class Room(object):
    def __init__(self, name, north, south, west, east, desc):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.description = desc

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
SouthBeach = Room("SouthBeach", "NorthGreenLight", None, "WESTTREELINE", None,
                  "You wake up felling very lite headed to the south is the ocean to the west is a thick tree line to "
                  "the north is a illuminating green light in a bush.")
NorthGreenLight = Room("NorthGreenLight", "NORTHSHACK", "SouthBeach", None, None,
                       "You walk towards a the green light surrounded by bushes you push them to the side its a bach "
                       "of bright green eggs to the north is a shack on top of a hill.")
NORTHSHACK = Room("North Shack", None, "NORTHGREENLIGHT", None, None,
                  "Your inside the you hear something loud roar outside the shack you look outside the window to see a"
                  "giant monster covered in fur with sharp teeth and red skin the only way to go is back.")
WESTTREELINE = Room("West Tree Line", "FORESTNORTH", "SOUTHBEACH", None, None,
                    "You walk towards the trees and having the feeling that your being watched to the north is more of "
                    "the forest and to the east if the same.")
FORESTNORTH = Room("Forest North", "MOUNTAINNORTH", "WESTTREELINE", None, None,
                   "You head north once again and see a large mountain you hear loud roar that's coming from the top of"
                   "the mountain to the north is a bright glow coming from the side of the mountain.")
MOUNTAINNORTH = Room("North Mountain", None, None, None, "FORESTEAST",
                     "You walk closer towards the side of the mountain you see a starched skeleton with a retractable"
                     "sword to the left east is more trees.")
FORESTEAST = Room("Forest East", "WYVERNNEST", None, "WESTTREELINE", None,
                  "You head towards the trees once again you see a huge foot print about 20 miters across you fallow "
                  "the trail for a few seconds until you notice the trail heads north towards the very top"
                  "of the mountain.")
WYVERNNEST = Room("Wyvern Nest", None, None, None, "ENDLESSCAVERNEAST",
                  "You climb up the mountain you meracuesly make it to the top you see huge pills of bones with a huge"
                  "monster to the side covered in green scales head to toe with fearsome teeth and serrated claws and"
                  "with an enormous wing span it spots you")
ENDLESSCAVERNEAST = Room("The EndLess Cavern", "CAVERNENTRANCENORTH", None, None, None,
                         "You side down the mountain as quickly as possible trying to avoid all the rocks on the way"
                         "down you come to a quick stop when you suddenly end up in a cavern lite up with torches you"
                         "see an entrance to the cavern that leads north.")
CAVERNENTERENCENORTH = Room("Cavern Entrance", None, None, "CAVERNHALLWAYWEST", "CAVERNHALLWAYEAST",
                            "You head towards the door having second thoughts on going in you see to ways to go west"
                            "were you hear very faint sound of singing to the east your see strange markings on the"
                            "wall")
CAVERNHALLWAYWEST = Room("Cavern Hallway", "EMPTYROOMNORTH", None, None, None,
                         "You head west you hear the singing getting louder you make it to a door were you see a little"
                         "girl standing in an emtey room singing you notice huge claw markes on the walls ten feet high"
                         "the little girl spots you the door closes behind you.")
CAVERNHALLWAYEAST = Room("Cavern Hallway", None, None, "CAVERNHALLWAYWEST", None,
                         "You walk towards the symbol it starts to glow a bright blue color you start to realize what"
                         "the symbol means until you hear a loud at the end of the dark hallway the facing your back"
                         "starts to push you towards the dark corner")
EMPTYROOMNORTH = Room("Empty Room Exit", None, None, "CAVERNHALLWAYWEST2", None,
                      "You feel scared realizing that you made it out alive and being scared on what comes next in"
                      "this deadly cavern that you don't think you will escape to the east is another hallway you have"
                      "a feeling of regret.")
CAVERNHALLWAYWEST2 = Room("Cavern Hallway", None, None, "CAVERNHALLWAY", None,
                          "You walk down the hallway you start to feel very sick and having the feeling that the"
                          "hallway is getting long with each step you take you feel sharp pain on your right shoulder"
                          "you pull up your sleave to check its a huge sting mark you realize that its from the monster"
                          "you fought two minutes ago you pass out from the pain")
CAVERNHALLWAY = Room("Cavern Hallway", None, None, None, "CAVERNINTERSECTIONEAST",
                     "You wake up feeling very light headed you take a look at you right shoulder seeing that it"
                     "still has the sting mark form that monster you question yourself for a second saying how did"
                     "i get on this island anyway you stand up having the determination you will make it off the"
                     "island")
CAVERNEXIT = Room("Cavern Exit", "ABANDONEDTOWN", None, None, None,
                  "You turn the corner you see the exit and feeling happy you made it out as soon as you come out side"
                  "you spot a abandoned town to the north you realize you could find supplies to heal your wounds from"
                  "your last battle.")
ABANDONEDTOWN = Room("Abandoned Town", "FEVERSWAP", None, None, None,
                     "You walk into the town you feel a presents that your not in the town alone you look at a window"
                     "of a destroyed houses for a split second you saw a white figure starring right back at you, you"
                     "stop for a second looking around waiting for monsters to attack but nothing came once you"
                     "reached the towns center to heal you wounds once you are done you spot a swap to the north.")
FEVERSWAP = Room("Fever Swap", None, None, None, "ABANDONEDDOCKS",
                 "")
ABANDONEDDOCKS = Room("Abandoned Docks", None, None, "WOODENBOAT",None ,
                      "")
WOODENBOAT = Room("Wooden Boat", None, None, None, None,
                  "")
current_node = SouthBeach
print(current_node)
directions = ['north', 'south', 'east', 'west']
short_direction = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        pos = short_direction.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
