import turtle
import math
import random

ws = turtle.Screen()
ws.bgcolor("black")
ws.title("The Hidden Treasure")
ws.setup(700, 700)
ws.tracer(0)  # Turn off screen updates initially

# Register Shapes
# turtle.register_shape("wizard_right.gif")
# turtle.register_shape("wizard_left.gif")
# turtle.register_shape("egg.gif")
# turtle.register_shape("wall.gif")

# Create Pen
class Block(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")     
        self.color("green")  
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        distance = math.sqrt((self.xcor() - other.xcor()) ** 2 + (self.ycor() - other.ycor()) ** 2)
        return distance < 5

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
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        distance = math.sqrt((self.xcor() - other.xcor()) ** 2 + (self.ycor() - other.ycor()) ** 2)
        return distance < 75

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

# Create levels list
levels = [""]

# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX         XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX A      XXXXE XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "XE               XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX         A           X",
    "XXX        XXXXXXXXXXXXXX",
    "XXXXXXXXX  XXXXXXXXXXXXXX",
    "XXXXXXXXX               X",
    "XX  XXXXX               X",
    "XX  XXXXXXXXXXXX  XXXXXXX",
    "XX A  XXXXXXXXXX  XXXXXXX",
    "XX         XXXX         X",
    "XXXX                   EX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Add a treasure list
eggs = []
enemies = []

# Add list
levels.append(level_1)

# Create level setup function
def setup_game(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            character = level[y][x]
            # Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                block.goto(screen_x, screen_y)
                # pen.shape("wall.gif")
                block.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "E":
                eggs.append(Egg(screen_x, screen_y))

            if character == "A":
                enemies.append(Enemy(screen_x, screen_y))

# Create class instances
block = Block()
player = Player()

# Create wall coordinate
walls = []

# Set up the level
setup_game(levels[1])
print(walls)

# Keyboard bindings
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Turn on screen updates
ws.tracer(1)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

# Main game loop
game_running = True

while game_running:
    for egg in eggs:
        if player.is_collision(egg):
            player.gold += egg.gold
            print("Player Gold: {}".format(player.gold))
            egg.destroy()
            eggs.remove(egg)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player Died!")
            game_running = False
            break

    ws.update()
