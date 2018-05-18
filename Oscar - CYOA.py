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
    def __init__(self, longrange, closerange, name, weapondamage, armor):
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
        super(Consumable, self).__init__(weapon, consumable, armor, name, egg)
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
    def __init__(self, health, regeneration, stamina, MaxHealth,  Regenpot, name, weapon, consumable):
        super(Meat, self).__init__(health, regeneration, stamina, MaxHealth, Strengthpot, Regenpot, armor, name,
                                   weapon, consumable, Meat, Speedpot)
        if self.health < 5:
            if self.stamina < 70:
                print("You eat the meat until there was bone you feel you can run around the whole island in"
                      "two seconds.")


class Speedpot(Consumable):
    def __init__(self, stamina, Regenpot, MaxHealth, weapon, consumable, health, name):
        super(Speedpot, self).__init__(healthpot, Regenpot, stamina, Meat, Strengthpot, Speedpot, MaxHealth, armor,
                                       weapon, consumable, health, name)
        if self.stamina < 20:
            print("You drink the potion your hands start to vibrate rapidly you feel you can outrun a lighting bolt")


class Strengthpot(Consumable):
    def __init__(self, carrymoreweapons, MaxHealth, stamina, health, consumable, name, weapon):
        super(Strengthpot, self).__init__(MaxHealth, stamina, health, Speedpot, Strengthpot, armor, consumable, name,
                                          weapon, Meat, carrymoreweapons, healthpot)
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
    def __init__(self, enchantment, heavyenchantment, slowmovement, durability, fastmovement):
        super(heavyarmor, self).__init__(enchantment, heavyenchantment, slowmovement, durability, armor, slowmovement,
                                         fastmovement, heavyarmor)
        if self.durability < 100:
            if self.slowmovement < 50:
                print("You put on the heavy armor when you take your first step it's slow and heavy but you feel while"
                      "protected.")


class enchant(heavyarmor):
    def __init__(self, enchantment, heavyenchantment, durability, slowmovement, fastmovement):
        super(enchant, self).__init__(enchantment, heavyenchantment, durability, slowmovement, fastmovement)
        if self.enchantment < armor < 50:
            if self.heavyenchantment < durability < 60:
                print("You use a enchanting crystal on your heavy armor you feel more protected.")


class lightarmor(armor):
    def __init__(self, enchantment, heavyenchantment, durability, fastmovement, slowmovement):
        super(lightarmor, self).__init__(enchantment, heavyenchantment, durability, fastmovement, armor, fastmovement,
                                    slowmovement, lightarmor)
        if self.durability < 50:
            if self.fastmovement < 50:
                print("You put on the light armor you feel you can run forever but also feel very open to attacks")


class enchant1(lightarmor):
    def __init__(self, enchantment, heavyenchantment, durability, slowmovement, fastmovement):
        super(enchant1, self).__init__(enchantment, heavyenchantment, durability, fastmovement, slowmovement)
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
    def __init__(self, name, north, south, west, east, attack, desc, items, grabitem):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.attack = attack
        self.description = desc
        self.items = items
        self.grabitem = grabitem

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
SouthBeach = Room("SouthBeach", "NorthGreenLight", None, "WESTTREELINE", None, None,
                  "You wake up felling very lite headed to the south is the ocean to the west is a thick tree line to "
                  "the north is a illuminating green light in a bush.", None, None)
NorthGreenLight = Room("North Green Light", "NORTHSHACK", "SouthBeach", None, None, None,
                       "You walk towards a the green light surrounded by bushes you push them to the side its a bach "
                       "of bright green eggs to the north is a shack on top of a hill.", None, None)
NORTHSHACK = Room("North Shack", None, "NorthGreenLight", None, None, None,
                  "Your inside the you hear something loud roar outside the shack you look outside the window to see a "
                  "giant monster covered in fur with sharp teeth and red skin the only way to go is back.", None, None)
WESTTREELINE = Room("West Tree Line", "FORESTNORTH", "SOUTHBEACH", None, None, None,
                    "You walk towards the trees and having the feeling that your being watched to the north is more of "
                    "the forest and to the east if the same.", None, None)
FORESTNORTH = Room("Forest North", "MOUNTAINNORTH", "WESTTREELINE", None, None, None,
                   "You head north once again and see a large mountain you hear loud roar that's coming from the top "
                   "of the mountain to the north is a bright glow coming from the side of the mountain.", None, None)
MOUNTAINNORTH = Room("North Mountain", None, None, None, "FORESTEAST", None,
                     "You walk closer towards the side of the mountain you see a starched skeleton with a retractable "
                     "sword to the left east is more trees.", None, None)
FORESTEAST = Room("Forest East", "WYVERNNEST", None, "WESTTREELINE", None, None,
                  "You head towards the trees once again you see a huge foot print about 20 miters across you fallow "
                  "the trail for a few seconds until you notice the trail heads north towards the very top "
                  " of the mountain.", None, None)
WYVERNNEST = Room("Wyvern Nest", None, None, None, "CAVERNEAST", None,
                  "You climb up the mountain you meracuesly make it to the top you see huge pills of bones with a huge "
                  "monster to the side covered in green scales head to toe with fearsome teeth and serrated claws and "
                  "with an enormous wing span it spots you, you grab your sword and ready for battle.", None, None)
WYVERNFIGHT = Room("Wyvern Fight", None, None, None, None, "ATTACK1",
                   "The wyvern turns to face you it close's its mouth and releases a loud and mighty roar it was so "
                   "loud your ears started to ring you recover then the wyvern goes in the air then attacks you with "
                   "it's talons you notice there's a purple substance dripping from it's talons so you avoid it as "
                   "much as you can the wyvern goes back on the ground and charges a huge fire ball it hit's you in "
                   "your chest which knocks you back you ready your attack", None, None)
ATTACK1 = Room("Attack", None, None, None, None, "Attack2",
               "You launch your self on the wyvern attacking it's back ripping it's scales off the wyvern takes flight "
               "trying to knock you off you move towards the monsters head and you stabs it in the eye it falls to the "
               "ground with a hug rumble you get lunched of from the blast the wyvern stands and is ready for it's "
               "attack.", None, None)
ATTACK2 = Room("Attack", None, None, None, "CAVERNEAST", None,
               "The wyvern shots a fire ball but this time it miss but it follows up the missed attack with a burst of "
               "three fire balls two fire balls hit you in the chest one misses the two fire balls that hit set you a "
               "flame you quickly dowsed the fire so no damage was done then the wyvern charges you and knocks you of "
               "the mountain to the east", None, None)
CAVERNEAST = Room("The Cavern", "CAVERNENTERENCENORTH", None, None, None, None,
                  "You side down the mountain as quickly as possible trying to avoid all the rocks on the way down you "
                  "come to a quick stop when you suddenly end up in a cavern lite up with torches you see an entrance "
                  "to the cavern that leads north.", None, None)
CAVERNENTERENCENORTH = Room("Cavern Entrance", None, None, "CAVERNHALLWAYWEST", None, None,
                            "You head towards the door having second thoughts on going in you see one way to go west "
                            "were you hear very faint sound of singing", None, None)
CAVERNHALLWAYWEST = Room("Cavern Hallway", None, None, None, None, "HUGESPIDERFIGHT",
                         "You head west you hear the singing getting louder you make it to a door were you see a "
                         "little girl standing in an empty room singing you notice huge amounts of webbing on the "
                         "walls with bones of animals and people hanging from them the little girl spots you the door "
                         "closes behind you, you prepare for battle.", None, None)
HUGESPIDERFIGHT = Room("Huge Spider", None, None, None, None, "ATTACK3",
                       "The girl starts to transform into a huge spider with huge fangs and multiply eyes all looking "
                       "at you just looking at the spider gives you gooses bumps the spider suddenly shoots huge "
                       "webbing at you but misses it jumps on the wall and starts to climb then it gets to a positions "
                       "when it starts to shot acidic spite from the roof some of it lands on your hand which felt "
                       "like your hand was in a pool of lava you take your crossbow and steady your aim to take the "
                       "shot", None, None)
ATTACK3 = Room("Attack", None, None, None, None, "ATTACK4",
               "You grab an arrow from your quiver then enchant it to set it aflame but you change your target and "
               "aimed for the web so the spider can't go on the ceiling again the spider jumps to the ground a bit "
               "starched from the fire it's eyes starts to glow red you switched to your sword and chopped off two of "
               "it's legs the spider ready's his attack.", None, None)
ATTACK4 = Room("Attack", "EMPTYROOMEXIT", None, None, None, None,
               "The spider jumps on top of you then started to tangle you in it's web you are not able to move the "
               "spider looks up to show it's fangs it goes full force striking you in your shoulder but you felt "
               "nothing you use your that's inside the webbing to cut threw and striked the spider underneath it then "
               "the spider releases a loud roar of pain and falls on it's back you stand up being completely out of "
               "breath you see an exit appear to the north", None, None)
EMPTYROOMEXIT = Room("Empty Room Exit", None, None, "CAVERNHALLWAYWEST2", None, None,
                     "You feel scared realizing that you made it out alive and being scared on what comes next in "
                     "this deadly cavern that you don't think you will escape to the east is another hallway you have "
                     "a feeling of regret.", None, None)
CAVERNHALLWAYEAST = Room("Cavern Hallway", None, None, "CAVERNHALLWAYWEST", None, None,
                         "You walk towards the symbol it starts to glow a bright blue color you start to realize what "
                         "the symbol means until you hear a loud roar at the end of the dark hallway the wall facing "
                         "your back starts to push you towards the dark corner until it was pict black", None, None)
EMPTYROOMNORTH = Room("Empty Room Exit", None, None, "CAVERNHALLWAYWEST2", None, None,
                      "You feel scared realizing that you made it out alive and being scared on what comes next in "
                      "this deadly cavern that you don't think you will escape to the east is another hallway you have "
                      "a feeling of regret.", None, None)
CAVERNHALLWAYWEST2 = Room("Cavern Hallway", None, None, "CAVERNHALLWAY", None, None,
                          "You walk down the hallway you start to feel very sick and having the feeling that the "
                          "hallway is getting long with each step you take you feel sharp pain on your right shoulder "
                          "you pull up your sleave to check its a huge sting mark you realize that its from the "
                          "monster you fought in the other room you pass out from the pain", None, None)
CAVERNHALLWAY = Room("Cavern Hallway", None, None, None, "CAVERNEXITEAST", None,
                     "You wake up feeling very light headed you take a look at you right shoulder seeing that it "
                     "still has the sting mark form that monster you question yourself for a second saying how did "
                     "i get on this island anyway you stand up having the determination you will make it off the "
                     "island", None, None)
CAVERNEXITEAST = Room("Cavern Exit", "ABANDONEDTOWN", None, None, None, None,
                      "You turn the corner you see the exit and feeling happy you made it out as soon as you come out "
                      "side you spot a abandoned town to the north you realize you could find supplies to heal your "
                      "wounds from your last battle.", None, None)
ABANDONEDTOWN = Room("Abandoned Town", "FEVERSWAP", None, None, None, None,
                     "You walk into the town you feel a presents that your not in the town alone you look at a window "
                     "of a destroyed houses for a split second you saw a white figure starring right back at you, you "
                     "stop for a second looking around waiting for monsters to attack but nothing came once you "
                     "reached the towns center to heal you wounds once you are done you spot a swap to the "
                     "north", None, None)
FEVERSWAP = Room("Fever Swap", None, None, None, None, "ANACONDAFIGHT",
                 "You walk into the swap feel sick when you took one step into the water you walked threw the swap "
                 "feeling something is moving underneath you, you spot a huge snake like animal with three heads and "
                 "fangs the size of your sword you prepare for battle.", None, None)
ANACONDAFIGHT = Room("Anaconda Fight", None, None, None, None, "STRIK",
                     "You feel intimidated with all of the three heads looking back at you one snake head "
                     "strikes you evade it another head follows up from the attack striking you on you left arm you "
                     "use the hilt of your sword to knock it back the last head strikes showing it's poisons fangs but "
                     "you doge the attack you get ready for you attack", None, None)
Attack = Room("Attack", None, None, None, "ABANDONEDDOCKS", None,
              "As soon you were about to charge the snake you noticed a blue gem in the center of it's chest you "
              "assume it's a weak spot you so charge into the snake with your sword pointing towards the gem you "
              "penetrate the snake with in a second the snake turned into dust you look around and see a docks not "
              "to far from you", None, None)
ABANDONEDDOCKS = Room("Abandoned Docks", None, None, "WOODENBOAT", None, None,
                      "You arrive to the docks you stand still and look around you spot a boat you are filled with "
                      "joy but then a huge troll that appears from the tree's it see's you and say's you will never "
                      "leave the island and you will not be the last to try and fail you feel overwhelmed with fear "
                      "but you come to your senses and threw your sword at the trolls eye you look to the east and "
                      "you see a wooden boat", None, None)
WOODENBOAT = Room("Wooden Boat", None, None, None, None, None,
                  "You run towards the boat you unroll the rope connected to the dock when doing this you hear the "
                  "troll saying you will stay here for the rest of your days he run's towards you he trys to grab the "
                  "boat but his arm wasn't very long your boat starts to drift far from the beach you look back and "
                  "see the troll turn around and disappear into the woods you turn back around and you try to find the "
                  "rower for the boat but no luck you decided to let the boat drift and see were it takes "
                  "you. ", None, None)
STRIK = Room("Attack", None, None, None, "ABANDONEDDOCKS", None,
             "As soon you were about to charge the snake you noticed a blue gem in the center of it's chest you assume "
             "it's a weak spot so charge into the snake with your sword pointing towards the gem you penetrate "
             "the snake with in a second the snake turned into dust you look around and see a docks not to far from "
             "you", None, None)

current_node = SouthBeach
print(current_node)
directions = ['north', 'south', 'east', 'west', 'attack', ]
short_direction = ['n', 's', 'e', 'w', 'a', ]

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
