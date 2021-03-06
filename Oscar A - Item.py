class Item(object):
    def __init__(self, weapon, consumable, armor, micis, name):
        self.name = name
        self.weapon = weapon
        self.consumable = consumable
        self.armor = armor


class Weapon(Item):
    def __init__(self, longrange, closerange, name, weapondamege, armor, micis):
        super(Weapon, self).__init__(longrange, closerange, armor, micis, name)
        self.closerange = closerange
        self.longrange = longrange
        self.weapondamege = weapondamege
        self.name = name


class Bow(Weapon):
    def __init__(self, longrange, weapondamage, name,):
        super(Bow, self).__init__(longrange, name,)
        self.weapondamage = weapondamage
        self.name = name

    def name(self):
        print("Archers Bow")

    def weapondamge(self):
        if self.weapondamage < 5:
            print()


class Sword(Weapon):
    def __init__(self, closerange, name, weapondamage):
        super(Sword, self).__init__(closerange, name, weapondamage,)

    def name(self):
        print("Great Toothed Sword ")

    def weapondamage(self):
        if self.closerange < 40:
            print("You inspect the sword it does not of damage")


class Consumable(Item):
    def __init__(self, Healthpot, Regenpot, Meat, Speeedpot, Strengthpot, Health, Stamina, MaxHealth):
        super(Consumable, self).__init__()
        self.Healthpot = Healthpot
        self.Regenpot = Regenpot
        self.Meat = Meat
        self.Speedpot = Speeedpot
        self.Strengthpot = Strengthpot
        self.Health = Health
        self.Stamina = Stamina
        self.MaxHealth = MaxHealth


class Healthpot(Consumable):
    def __init__(self, Health, Healthpot,):
        super(Healthpot, self).__init__(Health,)
        if self.Health < 10:
            print("You drink a healthpot you feel good and go back into the fight")
        
    def Regenpot(self):
        if self.Health < 30:
            print("You pop the lid of the pot and chug the position you feel good")
            

class Meat(Consumable):
    def __init__(self, Health, Regeneration, Stamina,):
        super(Meat, self).__init__(Health, Regeneration, Stamina,)
        if self.Health < 5:
            if self.Stamina < 70:
                print("You eat the meat until there was bone you feel you can run around the whole island in"
                      "two seconds.")
       
                
class Speedpot(Consumable):
    def __init__(self, Stamina):
        super(Speedpot, self).__init__(Stamina, Speedpot,)
        if self.Stamina < 20:
            print("You drink the potion your hands start to vibrate rapidly you feel you can outrun a lighting bolt")
            
            
class Strengthpot(Consumable):
    def __init__(self, CarryMoreWeapons,):
        super(Strengthpot, self).__init__("Maxhealth", "Stamina",)
        self.CarryMoreWeapons = CarryMoreWeapons
        if self.MaxHealth < 50:
            if self.CarryMoreWeapons < 2:
                if self.Stamina < 2:
                    print("You drink the potion you fall to your kneels from a surging pain coming from your hart you"
                          "wait until the pain goes away then you feel strong like you can lift the world")


class armor(Item):
    def __init__(self, heavyarmor, lightarmor, durability, enchantment, heavyenchantment, slowmovement, fastmovement,
                 armor,):
        super(armor, self).__init__()
        self.heavyarmor = heavyarmor
        self.lightarmor = lightarmor
        self.durability = durability
        self.enchantment = enchantment
        self.heavyenchantment = heavyenchantment
        self.slowmovement = slowmovement
        self.fastmovement = fastmovement
        

class heavyarmor(armor):
    def __init__(self, enchantment, heavyenchantment, slowmovement, durability,):
        super(heavyarmor, self).__init__(enchantment, heavyenchantment, slowmovement, durability,)
        if self.durability < 100:
            if self.slowmovement < 50:
                print("You put on the heavy armor when you take your first step it's slow and heavy but you feel while"
                      "protected.")


class enchant(heavyarmor):
    def __init__(self, enchantment, heavyenchantment, durability, slowmovement,):
        super(enchant, self).__init__(enchantment, heavyenchantment, durability, slowmovement,)
        if self.enchantment < armor < 50:
            if self.heavyenchantment < durability <60:
                print("You use a enchanting crystal on your heavy armor you feel more protected.")


class lightarmor(armor):
    def __init__(self, enchantment, heavyenchantment, durability, fastmovement,):
        super(lightarmor, self).__init__(enchantment, heavyenchantment, durability, fastmovement,)
        if self.durability < 50:
            if self.fastmovement < 50:
                print("You put on the light armor you feel you can run forever but also feel very open to attacks")


class enchant1(lightarmor):
    def __init__(self, enchantment, heavyenchantment, durability, slowmovement,):
        super(enchant1, self).__init__(enchantment, heavyenchantment, durability, slowmovement,)
        if self.enchantment < armor < 50:
            if self.heavyenchantment < durability <60:
                print("You use a enchanting crystal on your heavy armor you feel more protected.")
