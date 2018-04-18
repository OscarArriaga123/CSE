class Item(object):
    def __init__(self, weapon, consumable, armor, micis, name):
        self.name = name
        self.weapon = weapon
        self.consumable = consumable
        self.armor = armor
        self.micis = micis


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
        super(Speedpot, self).__init__(Stamina, Speedpot)
        if self.Stamina < 20:
            print("You drink the potion your hands start to vibrate rapidly you feel you can outrun a lighting bolt")
            
            
class Strengthpot(Consumable):
    def __init__(self):
        super(Strengthpot, self).__init__()
