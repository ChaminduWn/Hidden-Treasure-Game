import turtle
import math
import random

ws = turtle.Screen()
ws.bgcolor("black")
ws.title("The Hidden Treasure")
ws.setup(700, 700)
ws.tracer()

#Register Shapes
#turtle.register_shape("wizard_right.gif")
#turtle.register_shape("wizard_left.gif")
#turtle.register_shape("egg.gif")
#turtle.register_shape("wall.gif")


#create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")     
        self.color("red")  
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):

        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        #self.goto(self.xcor(), self.ycor() + 24)

        #check wall has space ?
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):

        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        #self.goto(self.xcor(), self.ycor() - 24) 

        #check wall has space ?
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 
        #self.goto(self.xcor() - 24, self.ycor())   

       # self.shape("wizard_left.gif")

        #check wall has space ?
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 
        #self.goto(self.xcor() + 24, self.ycor())        

        #self.shape("wizard_right.gif")

        #check wall has space ?
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        i = self.xcor()-other.xcor()
        j = self.ycor()-other.ycor()
        distance = math.sqrt((i ** 2) + (j ** 2))

        if distance < 5:
            return True
        else:
            return False        

class Egg(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")  
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")  
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        self.direction =random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down" :
            dx = 0
            dy = -24
        elif self.direction == "left" :
            dx = -24
            dy = 0
        elif self.direction == "right" :
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0   

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy    

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

        else :
            self.direction = random.choice(["up","down","left","right"])  

        turtle.ontimer(self.move, t = random.randint(100,300))    

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()        

#create levels list
levels = [""]

#define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXX         XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",      
    "X  XXX R      XXXXE XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",  
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX         R           X",
    "XXX        XXXXXXXXXXXXXX",
    "XXXXXXXXX  XXXXXXXXXXXXXX",
    "XXXXXXXXX               X",
    "XX  XXXXX               X",
    "XX  XXXXXXXXXXXX  XXXXXXX",
    "XX R  YXXXXXXXXXX  XXXXXX",
    "XX         XXXX         X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#add a treasure list
eggs = []

enemies = []

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
               # pen.shape("wall.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))

            #check if it is a P (representing the player)    
            if character == "P":
                player.goto(screen_x, screen_y) 
                
                #check if it is an Y (representing the player)
            # if character == "Y":
            #     pen.goto(screen_x, screen_y)
            #     pen.stamp()

            #check if it is a T (representing the treasure)
            if character == "E":
                eggs.append(Egg(screen_x, screen_y))

            if character == "R" :
                enemies.append(Enemy(screen_x, screen_y))   

#create class instances
pen = Pen()
player = Player()

#create walll coordinate
walls = []

#set up the level
setup_game(levels[1])
print (walls)



#keyboard bindings
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

#Turn Off screen updates
ws.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)

#main game loop
while True:
    #check for player collison with eggs
    #Iterate through the eggs

    for egg in eggs:
        if player.is_collision(egg):

            player.gold += egg.gold
            print ("player Gold: {}".format(player.gold))
            
            #destroy egg
            egg.destroy()

            #remove egg from eggs list
            eggs.remove(egg)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player Died !")
            break        

    #update screen        
    ws.update()
