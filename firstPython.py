import turtle
import math
import random

# Define block size and margin
BLOCK_SIZE = 24
MARGIN = 50

# Define level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXE  A                 XXXXX",
    "X  XXXXXXX  XXXXXX   XXXX     EXXXX",
    "X       XX  XXXXXX   XXXX     EXXXX",
    "X       XX  XXX        XX  XXXXXXXX",
    "XXXXXX  XX  XXX                  XX",
    "XXXXXX  XX  XXXXXX  XXXXX   XXX  XX",
    "XXXXXX  XX    XXXX  XXXXX   XX    X",
    "X  XXX A      XXXXE XXX          XX",
    "X  XXX  XXXXXXXX          XXXXXXXXX",
    "X         XXXXX  XXXXX          XXX",
    "XE               XXXXX    XX    XXX",
    "XXXXXX  XXXXX    XXXXX    X   XXXXX",
    "XXXXXX  XXXXXX   XXXXX            X",
    "XXXE X  XXXXXXX         X    XX XXX",
    "XXX         A           X         X",
    "XXE        XXXXXXXX   XXXX    XXXXX",
    "XXXXXXXXX  XXXXXXXXXXXXXX   XXXXXXX",
    "XXXXXXXXX               XX  XXE   X",
    "XX  XXXXX               X   XX    X",
    "XX  XXXXXXXXXXXX  XXX       XX    X",
    "XX A  XXXXXXXXXX  XXXEX          XX",
    "XX         XXXX       XXX    XX   X",
    "XXXX                   EXX      XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Calculate screen dimensions with margin
level_width = len(level_1[0])
level_height = len(level_1)

screen_width = level_width * BLOCK_SIZE + MARGIN
screen_height = level_height * BLOCK_SIZE + MARGIN

# Offset to shift the game layout
OFFSET_X = 50
OFFSET_Y = 50

# Set up screen
ws = turtle.Screen()
ws.bgcolor("black")
ws.title("The Hidden Treasure")
ws.setup(screen_width, screen_height)
ws.tracer(0)  # Turn off screen updates initially

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
        move_to_y = self.ycor() + BLOCK_SIZE
        if (move_to_x, move_to_y) not in fence:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - BLOCK_SIZE
        if (move_to_x, move_to_y) not in fence:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - BLOCK_SIZE
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in fence:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + BLOCK_SIZE
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in fence:
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
        if game_running:
            if self.direction == "up":
                dx = 0
                dy = BLOCK_SIZE
            elif self.direction == "down":
                dx = 0
                dy = -BLOCK_SIZE
            elif self.direction == "left":
                dx = -BLOCK_SIZE
                dy = 0
            elif self.direction == "right":
                dx = BLOCK_SIZE
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

            if (move_to_x, move_to_y) not in fence:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(["up", "down", "left", "right"])

            turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        distance = math.sqrt((self.xcor() - other.xcor()) ** 2 + (self.ycor() - other.ycor()) ** 2)
        return distance < 80

    def destroy(self):
        self.goto(1999, 1999)
        self.hideturtle()

# Create levels list
levels = [""]

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
            screen_x = -screen_width // 2 + (x * BLOCK_SIZE) + OFFSET_X
            screen_y = screen_height // 2 - (y * BLOCK_SIZE) - OFFSET_Y

            if character == "X":
                block.goto(screen_x, screen_y)
                block.stamp()
                fence.append((screen_x, screen_y))

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
fence = []

# Set up the level
setup_game(levels[1])
print(fence)

# Keyboard bindings
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-screen_width // 2 + 20, screen_height // 2 - 40)
score_display.write("Score: {}".format(player.gold), align="left", font=("Courier", 24, "normal"))

# Message display
message_display = turtle.Turtle()
message_display.speed(0)
message_display.color("white")
message_display.penup()
message_display.hideturtle()
message_display.goto(screen_width // 2 - 20, screen_height // 2 - 40)

# Turn on screen updates
ws.tracer(1)

# Update functions
def update_score_display():
    score_display.clear()
    score_display.write("Gold: {}".format(player.gold), align="left", font=("Courier", 24, "normal"))

def update_message_display(message):
    message_display.clear()
    message_display.write(message, align="right", font=("Courier", 24, "normal"))

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

# Main game loop
game_running = True

while game_running:
    for egg in eggs:
        if player.is_collision(egg):
            player.gold += egg.gold
            update_score_display()
            egg.destroy()
            eggs.remove(egg)

    if not eggs:
        update_message_display("You won!")
        game_running = False

    for enemy in enemies:
        if player.is_collision(enemy):
            update_message_display("Player Died! You Lose! Try Again")
            game_running = False
            break

    ws.update()

ws.mainloop()
