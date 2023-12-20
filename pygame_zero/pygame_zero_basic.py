# Import Pygame Zero game engine
import pgzrun
# For type-hinting support
from typing import Tuple

# Story node keys (each key is optional):
# - image: an image to show. It is also the default name of the story node
# - name: name of the story (overwrites "image" name)2
# - text: text to show on the image. This text should offer the choices,e.g.: "1":"node name_1", "A":"node_A", "b":None (None defaults the node name to chice key name)
# - sound: sound to play only once
# - music: music to play in a loop

story=[
    {"image":"csontváz", "text":"Ha kék cicát szeretnél, nyomj 'K'-t. Lufi kutya: 'L'", "choice":{"k":"kék_cica", "l":"lufi_kutya"}, "sound":"eep.wav"},
    {"image":"kék_cica", "text":"Mars boccci: 'M', lufi kutya: 'L', valami: 'V'", "choice":{"m":"mars_boszi", "l":"lufi_kutya", "v":"pexels-pixabay-40784"}, "sound":"coin_pickup.wav"},
    {"name":"valami", "image":"pexels-pixabay-40784", "text":"Kérlek menjünk a kék cicához, nyomj 'k'-t!", "choice":{"k":"kék_cica"}, "sound":"coin_pickup.wav"},
    {"image":"lufi_kutya", "text":"csontváz? 'C'", "choice":{"c":"csontváz"}},
    {"image":"mars_boszi", "text":"csontváz? 'C'", "choice":{"c":"csontváz"}},
]
story_node = story[0]
prev_story_node = None

# Set the width and height of your output window, in pixels
WIDTH = 600
HEIGHT = 600

# Set up the player
player = Actor("alien_green_stand")
player_position = -100,-100
player.center = player_position

def story_go_to(key):
    global story, story_node
    if "choice" not in story_node:
        return
    
    for k,name in story_node["choice"].items():
        if key==k:
            for node in story:
                if "name" in node and node["name"]==name:
                    story_node=node
                    return
            for node in story:
                if "image" in node and node["image"]==name:
                    story_node=node
                    return

#class StoryNode:
#    def __init__(self,image=None, choice=None, music=None, ):

def on_mouse_down(pos: Tuple, button):
    """Called whenever a mouse buttown is pressed

    Arguments:
        pos {Tuple} -- The current position of the mouse
        button -- None, mouse.[LEFT|RIGHT|MIDDLE]
    """
    if button != mouse.LEFT:
        return

    # Set the player to the mouse position
    set_player_pos(pos)

#def on_mouse_move(pos: Tuple):
#    """Called whenever the mouse changes position"""
#    # Set the player to the mouse position
#    set_player_pos(pos)

def set_player_pos(pos):
    global player_position
    #player_position = (pos[0],300)
    player_position = (pos[0],pos[1])

def on_key_down(key, mod, unicode):
    print(key, mod, unicode)
    global prev_story_node

    # exit
    if key==keys.ESCAPE:
        exit()
    
    if unicode == " ":
        prev_story_node = None
    
    # go to choice
    story_go_to(unicode)

def update(delta_time: float):
    """Called every frame to update game objects

    Arguments:
        delta_time {float} -- Time since the last frame
    """
    # Update the player position
    player.center = player_position
    
def draw():
    """Draw is called once per frame to render everything on the screen"""

    global prev_story_node, story_node
    if prev_story_node != story_node:
        # story_node has changed
        prev_story_node=story_node
        if "sound" in story_node:
            music.play_once(story_node["sound"])
        if "music" in story_node:
            music.play(story_node["music"])

    # Clear the screen first
    screen.clear()  
    if "image" in story_node:
        screen.blit(story_node["image"], (0,0))
    else:
        # Set the background color to white
        screen.fill("white")  
    # Draw the player
    player.draw()

    if "text" in story_node:
        screen.draw.textbox(story_node["text"],
            Rect((0, HEIGHT - 100), (WIDTH, 100)),
            color="black", background="gray", alpha=0.5,
            shadow=(0.1, 0.1),
        )

# Run the program
pgzrun.go()
