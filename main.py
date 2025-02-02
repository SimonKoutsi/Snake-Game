#Snake Game
import random
from tkinter import *

GAME_WIDTH = 800
GAME_HEIGHT = 700
PIXEL_SIZE = 25
FRAME_TIME = 50
SNAKE_BODY_PARTS = 3
BACKROUND_COLOR = "#b5eef5"
SNAKE_COLOR = "#270870"
FOOD_COLOR = "#e6070b"

class Snake() :
    def __init__(self):
        self.bodyParts = SNAKE_BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, SNAKE_BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + PIXEL_SIZE, y + PIXEL_SIZE, fill= SNAKE_COLOR, tags="snake")
            self.squares.append(square)

class Food() :
    
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // PIXEL_SIZE) - 1) * PIXEL_SIZE
        y = random.randint(0, (GAME_HEIGHT // PIXEL_SIZE) - 1) * PIXEL_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + PIXEL_SIZE, y + PIXEL_SIZE, fill= FOOD_COLOR, tags="food")

def Frame_Update(food, snake):

    x, y = snake.coordinates[0]

    # Check direction
    if direction == "down":
        y += PIXEL_SIZE
    elif direction == "up":
        y -= PIXEL_SIZE
    elif direction == "left":
        x -= PIXEL_SIZE
    elif direction == "right":
        x += PIXEL_SIZE

    # Create the new head of the snake acccording the direction
    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + PIXEL_SIZE, y + PIXEL_SIZE, fill= SNAKE_COLOR, tags="snake")
    snake.squares.insert(0, square)

    # Check if the head collides with the food. If so update the score and the food gameobject
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score +=1
        label.config(text= "Score:{}".format(score))
        # We use the tag that we asigned when we created the food game object
        canvas.delete("food")
        food = Food()
    # Delete the last body part of the snake every time it doesn't eat the food
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if Check_Collisions(snake):
        Game_Over()
    else:
        window.after(FRAME_TIME, Frame_Update, food, snake)

def Change_Direction(newDirection):

    global direction

    if newDirection == "up":
        if direction != "down":
            direction = newDirection
    elif newDirection == "down":
        if direction != "up":
            direction = newDirection
    elif newDirection == "left":
        if direction != "right":
            direction = newDirection
    elif newDirection == "right":
        if direction != "left":
            direction = newDirection

def Check_Collisions(snake):
    
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH :
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for bodyParts in snake.coordinates[1:]:
        if x == bodyParts[0] and y ==bodyParts[1]:
            return True
    
    return False

def Game_Over():
    
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font= ('consolas', 70), text= "GAME OVER", fill= "red", tags= "gameover")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

# voleuei na vazo to .pack se deuteri grammi etsi oste sthn metavliti
# label na ginetai asign o tupos Label. Etsi argotera tha mporo na xrisimopoio
# to label me tis methodous ths klasis Label (label. )
label = Label(window,text="Score:{}".format(score), font= ('consolas', 40))
label.pack()

canvas = Canvas(window, bg= BACKROUND_COLOR, width= GAME_WIDTH, height= GAME_HEIGHT)
canvas.pack()

window.bind('<Up>', lambda event: Change_Direction("up"))
window.bind('<Down>', lambda event: Change_Direction("down"))
window.bind('<Left>', lambda event: Change_Direction("left"))
window.bind('<Right>', lambda event: Change_Direction("right"))

snake = Snake()
food = Food()

Frame_Update(food= food, snake= snake)

window.mainloop()