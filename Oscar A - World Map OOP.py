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

current_node = world_map = {"South Beach"}
print(current_node)
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node["South Beach"])
    print(current_node["You wake up felling very lite headed to the south is the ocean"
                       "to the west is a thick tree line to the north is a illuminating "
                       "green light in a bush."])
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map["South Beach"]
        except:
            print("You cannot go this way")

        else:
            print('Command not recognized')
