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
SOUTHBEACH = Room("South Beach", "NORTHGREENLIGHT", "SOUTHOCEAN", "WESTTREELINE", None,
                  "You wake up felling very lite headed to the south is the ocean to the west is a thick tree line to "
                  "the north is a illuminating green light in a bush.")

NORTHGREENLIGHT = Room("North Green Light", "NORTHSHACK", None, None, None,
                       "You walk towards a the green light surrounded by bushes you push them to the side its a bach of"
                       "bright green eggs to the north is a shack on top of a hill.")

NORTHSHACK = Room("North Shack", None, "NORTHGREENLIGHT", None, None,
                  "Your inside the you hear something loud roar outside the shack you look outside the window to see a"
                  "giant monster covered in fur with sharp teeth and with red skin.")

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
                  "with an enormess wing span it spots you")

ENDLESSCAVERNEAST = Room("The EndLess Cavern", "CAVERNENTRANCENORTH", None, None, None,
                         "You side down the mountain as quickly as possible trying to avoid all the rocks on the way"
                         "down you come to a quick stop when you suddenly end up in a cavern lite up with torches you"
                         "see an entrance to the cavern that leads north.")

CAVERNENTERENCENORTH = Room("Cavern Entrance", None, None, "CAVERNHALLWAYWEST", "CAVERNHALLWAYEAST",
                            "You head towards the door having second thoughts on going in you see to ways to go west"
                            "were you hear very faint sound of singing to the east your see strange markings on the wall")
