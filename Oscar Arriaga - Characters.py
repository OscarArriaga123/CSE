class Character(object):
    def __init__(self, takedamage, attack, health, dialogue, statseffect, regeneratehealth):
        self.takedamage = takedamage
        self.attack = attack
        self.dialogue = dialogue
        self.health = health
        self.statseffect = statseffect
        self.regeneratehealth = regeneratehealth

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

    def dialouge(self):
        self.inspect = self.room, self.forest, self.corner
        print("There's a object here of use in this area say's a odd voice in your head")
