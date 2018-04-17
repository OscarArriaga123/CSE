world_map = {
    'SOUTHBEACH': {
        'NAME': "South Beach",
        'DESCRIPTION': "You wake up felling very lite headed to the south is the ocean"
                       "to the west is a thick tree line to the north is a illuminating "
                       "green light in a bush.",
        'PATHS': {
            'NORTH': 'NORTHGREENLIGHT',
            'SOUTH': 'SOUTHOCEAN',
            'WEST': 'WESTTREELINE',
        }
    },
    'NORTHGREENLIGHT': {
        'NAME': 'North Green light',
        'DESCRIPTION': "You walk towards a the green light surrounded by bushes you push them to"
                       "the side its a bach of bright green eggs to the north is a shack on top of"
                       "a hill. ",
        'PATHS': {
            'NORTH': 'NORTHSHACK',
        }
    },
    'NORTHSHACK': {
        'NAME': 'North Shack',
        'DESCRIPTION': "Your inside the you hear something loud roar outside the shack you look outside the "
                       "window to see a giant monster covered in fur with sharp teeth and with red skin.",
        'PATHS': {
            'SOUTH': 'NORHTGREENLIGHT',
        }
    },
    'WESTTREELINE': {
        'NAME': 'West Tree Line',
        'DESCRIPTION': "You walk towards the trees and having the feeling that your being watched"
                       "to the north is more of the forest and to the east if the same. ",
        'PATHS': {
            'SOUTH': 'SOUTHBEACH',
        },  'NORTH': 'FORESTNORTH',
    },
    'FORESTNORTH': {
        'NAME': 'Forest North',
        'DESCRIPTION': "You head north once again and see a large mountain you hear loud roar that's coming"
                       "from the top of the mountain to the north is a bright glow coming from the side of the"
                       "mountain. ",
        'PATHS': {
            'NORTH': 'MOUNTAINNORTH',
        },  'SOUTH': 'WESTTREELINE',
    },
    'MOUNTAINNORTH': {
        'NAME': 'North Mountain ',
        'DESCRIPTION': "You walk closer towards the side of the mountain you see a starched skeleton with a"
                       "retractable sword to the left east is more trees ",
        'PATHS': {
        },  'EAST': 'FORESTEAST',
    },
    'FORESTEAST': {
        'NAME': 'Forest East',
        'DESCRIPTION': "You head towards the trees once again you see a huge foot print about 20 miters across"
                       "you fallow the trail for a few seconds until you notice the trail heads north towards the"
                       "very top of the mountain.",
        'PATHS': {
            'NORTH': 'WYVERNNEST',
        },  'WEST': 'WESTTREELINE',
    },
    'WYVERNNEST': {
        'NAME': 'Wyvern Nest',
        'DESCRIPTION': "You climb up the mountain you meracuesly make it to the top you see huge pills of bones with a"
                       "huge monster to the side covered in green scales head to toe with fearsome teeth and serrated"
                       "claws and with an enormess wing span it spots you",
        'PATHS': {
        },   'EAST': 'ENDLESSCAVERNEAST',
    },
    'ENDLESSCAVERNEAST': {
        'NAME': 'The Endless Cavern',
        'DESCRIPTION': "You side down the mountain as quickly as possible trying to avoid all the rocks on the way down"
                       "you come to a quick stop when you suddenly end up in a cavern lite up with torches you see an"
                       "entrance to the cavern that leads north.",
        'PATHS': {
        },   'NORTH': 'CAVERNENTRANCENORTH',
    },
    'CAVERNENTRANCENORTH': {
        'NAME': 'Cavern Entrance',
        'DESCRIPTION': "You head towards the door having second thoughts on going in you see to ways to go west were"
                       "you hear very faint sound of singing to the east your see strange markings on the wall",
        'PATHS': {
             'WEST': 'CAVERNHALLWAYWEST',
        },   'EAST': 'CAVERNHALLWATEAST',
    },
    'CAVERNHALLWAYWEST': {
        'NAME': 'Cavern Hallway',
        'DESCRIPTION': "You head west you hear the singing getting louder you make it to a door were you see a little"
                       "girl standing in an empty room singing you notice huge claw marks on the walls ten feet high"
                       "the little girl spots you the door closes behind you.",
        'PATHS': {
        },     'NORTH': 'EMPTYROOMNORTH',
    },
    'CAVERNHALLWAYEAST': {
        'NAME': 'Cavern Hallway',
        'DESCRIPTION': "You walk towards the symbol it starts to glow a bright blue color you start to realize what"
                       "the symbol means until you hear a loud at the end of the dark hallway the facing your back"
                       "starts to push you towards the dark corner",
        'PATHS': {
        },   'WEST': 'CAVERNHALLWAYWEST',
    },
    'EMPTYROOMNORTH': {
        'NAME': 'Empty Room Exit',
        'DESCRIPTION': "You feel scared realizing that you made it out alive and being scared on what comes next in"
                       "this deadly cavern that you don't think you will escape to the east is another hallway you have"
                       "a feeling of regret.",
        'PATHS': {
        }, 'WEST': 'CAVERNHALLWAYWEST2',
    },
    'CAVERNHALLWEST2': {
        'NAME': 'Cavern Hallway',
        'DESCRIPTION': "You walk down the hallway you start to feel very sick and having the feeling that the hallway"
                       "is getting long with each step you take you feel sharp pain on your right shoulder you pull up "
                       "your sleave to check its a huge sting mark you realize that its from the monster you fought two"
                       "minutes ago you pass out from the pain",
        'PATHS': {
        }, 'WEST': 'CAVERNHALLWAY',
    },
    'CAVERNHALLWAY': {
        'NAME': 'Cavern Hallway',
        'DESCRIPTION': "You wake up feeling very light headed you take a look at you right shoulder seeing that it"
                       "still has the sting mark form that monster you question yourself for a second saying how did"
                       "i get on this island anyway you stand up having the determination you will make it off the"
                       "island",
        'PATHS': {
        }, 'EAST': 'CAVERNINTSECTION',
    },

},


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
