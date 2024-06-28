import turtle

ws = turtle.Screen()
ws.bgcolor("black")
ws.title("The Hidden Treasure")
ws.setup(700, 700)

#create pointer
class Pen(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#create levels list
levels = [""]

#define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",      
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",  
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX        XXXXXXXXXXXXXX",
    "XXXXXXXXX  XXXXXXXXXXXXXX",
    "XXXXXXXXX               X",
    "XX  XXXXX               X",
    "XX  XXXXXXXXXXXX  XXXXXXX",
    "XX    YXXXXXXXXXX  XXXXXX",
    "XX         XXXX         X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#add list
levels.append(level_1)

#create level setup function
def setup_game(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get the character at each x,y coordinate
            #note the order of y and x in the next line
            character = level[y][x]
            #calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                
                #check if it is an Y (representing the player)
            # if character == "Y":
            #     pen.goto(screen_x, screen_y)
            #     pen.stamp()

#create class instances
pen = Pen()

#set up the level
setup_game(levels[1])

#main game loop
while True:
    ws.update()
