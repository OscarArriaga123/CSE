class Item(object):
    def __init__(self, weapon, consumable, armor, micis, name):
        self.name = name
        self.weapon = weapon
        self.consumable = consumable
        self.armor = armor
        self.micis = micis


class Weapon(Item):
    def __init__(self, longrange, closerange, name, weapondamege):
        super(Weapon, self).__init__(longrange, closerange)
        self.closerange = closerange
        self.longrange = longrange
        self.weapondamege = weapondamege
        self.name = name


class Bow(Weapon):
    def __init__(self, longrange, weapondamage, name):
        super(Bow, self).__init__(longrange, name)
        self.weapondamage = weapondamage
        self.name = name

    def name(self):
        print("Archers Bow")

    def weapondamge(self):
        if self.weapondamage < 5:
            print()


class Sword(Weapon):
    def __init__(self, closerange, name, weapondamage):
        super(Sword, self).__init__(closerange, name, weapondamage)

    def name(self):
        print("Great Toothed Sword ")

    def weapondamage(self):
        if self.closerange < 40:
            print("You inspect the sword it does not of damage")


class Consumable(Item):
    def __init__(self, Healthpot, Regenpot, Meat, Speeedpot, Strengthpot, Health):
        super(Consumable, self).__init__()
        self.Healthpot = Healthpot
        self.Regenpot = Regenpot
        self.Meat = Meat
        self.Speedpot = Speeedpot
        self.Strengthpot = Strengthpot
        self.Health = Health


class Healthpot(Consumable):
    def __init__(self, ):


    def Regenpot(self):
        if self.Health < 30:
            print("You pop the lid of the pot and chug the position you feel good")
