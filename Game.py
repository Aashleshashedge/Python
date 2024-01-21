from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 900
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def _init_(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def _init_(self, canvas):
        self.canvas = canvas
        self.coordinates = [0, 0]
        self.set_new_food()

    def set_new_food(self):
        x = random.randint(0, (GAME_WIDTH - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE

        self.coordinates = [x, y]

        self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    global direction, score

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score: {}".format(score))

        canvas.delete("food")
        food.set_new_food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(event):
    global direction
    if event.keysym == 'Left':
        if direction != 'right':
            direction = 'left'
    elif event.keysym == 'Right':
        if direction != 'left':
            direction = 'right'
    elif event.keysym == 'Up':
        if direction != 'down':
            direction = 'up'
    elif event.keysym == 'Down':
        if direction != 'up':
            direction = 'down'

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, font=('consolas', 70), text="GAME OVER", fill="red",
                       tag="game over")

def start_game():
    global score, direction
    score = 0
    direction = 'down'
    label.config(text='Score: {}'.format(score))

    canvas.delete("all")
    snake = Snake()
    food = Food(canvas)
    next_turn(snake, food)

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update_idletasks()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int(screen_width/2) - (window_width/2)
y = int(screen_height/2) - (window_height/2)

window.geometry(f"{int(window_width)}x{int(window_height)}+{int(x)}+{int(y)}")

window.bind('<Left>', change_direction)
window.bind('<Right>', change_direction)
window.bind('<Up>', change_direction)
window.bind('<Down>', change_direction)

start_game()

window.mainloop()