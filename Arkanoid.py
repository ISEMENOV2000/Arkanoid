#  Arkanoid.py
#  Author: Ivan Semenov (G20967941)
#  Email:  ISemenov@uclan.ac.uk
#  Description: Arkanoid.py is a program that creates a game of arkanoid.
#  The player controls the craft with the mouse. The goal is to bounce the ball off the craft into the bricks
#  at the top if the window. Each broken brick is 10 points. Once the player breaks all bricks, then he will
#  reach the second level. At the second level all bricks reappear and the speed of the ball is increased.
#  The same happens when the second level is complete. Upon completing the third and final level,
#  A message appears "You Won!". If the ball misses the craft, then a "Game Over!!!" message appears.
#  To quit the game the player must press the 'x' key.
#  The Craft class is used to create and move the craft using the mouse.
#  The Ball class is in charge of creating a ball, so the ball moves within the window, so it bounces off the craft
#  in different directions depending on where it hit the craft, so the ball collides with the bricks and bounces off them
#  correctly and destroys the bricks.
#  The Score class is in charge of creating a score and level writing at the bottom left and right corner.
#  It also updates the score upon the ball contact with a brick.
#  The Collisions.py program demonstrates OOP with a Ball class. This class
#  concentrates all necessary data for a Ball: position of the ball (x,y), its speed
#  (speed_x,speed_y), its width, colour, etc. The functionality includes the ability of the ball
#  to update its position based on its speed, and to cycle its colour.
#  The SowingTextOnCanvas.py program demonstrates how to write text on the canvas and how it changes with changes in
#  some values

from tkinter import *

TITLE = 'Arkanoid'
WIDTH = 800  # Initializes the width of the window
HEIGHT = 600  # Initializes the height of the window
DELAY = 20  # Initializes the delay between animations in milliseconds
DEFAULT_SPEED = 5  # Initialises the initial speed if the ball
color = 'cyan'  # Initializes the colour of craft
BRICK_COLORS = ['yellow', 'orange', 'purple', 'blue', 'green']  # Creates a list with colours
# Create the Window.
win = Tk()
win.title(TITLE)
Bricks = []  # Creates a list for Bricks
# Create and pack the canvas.
canvas = Canvas(win, width=WIDTH, height=HEIGHT)  # Creates a canvas
canvas.pack()
drawn_rectangles = []  # Creates a list where the coordinates of the bricks will be stored
drawn_circles = []  # Creates a list for circle animations
MAX_SIZE = 5  # Initializes the amount of balls for the trail
side = 50  # Initializes the length of the side of the bricks
width = 100  # Initializes the length of the width of the craft
height = 10  # Initializes the length of the height of the craft
x = (WIDTH // 2)  # x and y values are the center of the window
y = (HEIGHT // 2)
rect = canvas.create_rectangle(x - width // 2, HEIGHT, x + width // 2, HEIGHT - height, fill=color)  # creates a rectangle
score1 = 0  # Initialises the value for the score
score_text = score1
text_id = canvas.create_text(20, HEIGHT - 20, text=str(score_text), font=('Arial Bold', 12), fill='white')  # Creates a score at the bottom left of window
text_id2 = canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 1', font=('Arial Bold', 12), fill='white')  # Creates a level at the bottom right of window

canvas.config(bg='black')  # Sets a custom background
print('use the mouse to move the rectangle left and right across the window')
print('Press "x" to exit')


class Craft:  # Creates a class for the craft which moves at the bottom of the screen

    @staticmethod
    def move(event):  # Event binds the mouse movement
        global x, rect
        x = event.x
        if WIDTH - (width/2) - 1 > x > (width/2) + 1:  # if statement that creates the craft and moves it
            drawn_rectangles.append(rect)
            canvas.delete(drawn_rectangles.pop(0))
            rect = canvas.create_rectangle(x - width//2, HEIGHT, x + width//2, HEIGHT - height, fill=color)


# The definition of the Ball Class is reused from the
# Collisions.py code provided under Week03, step0306.
class Ball:  # Creates a clss for the ball which handles the ball movement, animation, collision with craft and collision and deletion of Bricks

    # __init__ function declares the values
    def __init__(self, xx, yy, speed_x, speed_y, radius, color2):
        self.xx = xx
        self.yy = yy
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color2 = color2
        self.score = 0
        self.rect = rect

    def move_ball(self):  # function that moves the ball inside the window
        # first update the X...
        self.xx = self.xx + self.speed_x
        # ...then make sure that if it bounces, the horizontal speed is reversed
        if self.xx >= WIDTH - self.radius:
            self.speed_x = -abs(self.speed_x)
        if self.xx <= self.radius:
            self.speed_x = abs(self.speed_x)
        # next update the Y...
        self.yy = self.yy + self.speed_y
        # ...and make sure that if it bounces, the vertical speed is reversed
        if self.yy <= self.radius:
            self.speed_y = abs(self.speed_y)

    def brick_bounce(self):  # this function is in charge of the ball bouncing off bricks,
        # deletion off bricks and starting the next level when the score reaches a certain value.
        for i in Bricks:
            x1, y1, x2, y2 = canvas.coords(i)  # extracts coordinate of bricks from canvas.coords
            if x1 <= self.xx <= x2 and y1 <= self.yy - self.radius <= y2 and self.speed_y <= 1:  # checks if there was contact with the bottom side of the brick
                self.speed_y = abs(self.speed_y)  # changes only the vertical speed
                canvas.delete(i)  # deletes the brick from the canvas
                Bricks.pop(Bricks.index(i))  # removes the brick from Bricks
                self.score += 10  # increases the score by 10
                if b.score == 1000:  # Checks if score reaches 1000
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 2', font=('Arial Bold', 12), fill='white')  # re prints new level
                if b.score == 2000:  # Checks if score reaches 2000
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 3', font=('Arial Bold', 12), fill='white')  # re prints new level
            elif x1 <= self.xx <= x2 and y1 <= self.yy + self.radius <= y2 and self.speed_y >= 1:  # checks if there was contact with the top side of the brick
                self.speed_y = -abs(self.speed_y)  # changes only the vertical speed
                canvas.delete(i)  # deletes the brick from the canvas
                Bricks.pop(Bricks.index(i))  # removes the brick from Bricks
                self.score += 10  # increases the score by 10
                if b.score == 1000:  # Checks if score reaches 1000
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 2', font=('Arial Bold', 12), fill='white')  # re prints new level
                if b.score == 2000:
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 3', font=('Arial Bold', 12), fill='white')  # re prints new level
            elif x1 <= self.xx - self.radius <= x2 and y1 <= self.yy <= y2 and self.speed_x <= 1:
                self.speed_x = abs(self.speed_x)  # changes only the horizontal speed
                canvas.delete(i)  # deletes the brick from the canvas
                Bricks.pop(Bricks.index(i))  # removes the brick from Bricks
                self.score += 10  # increases the score by 10
                if b.score == 1000:  # Checks if score reaches 1000
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 2', font=('Arial Bold', 12), fill='white')  # re prints new level
                if b.score == 2000:
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 3', font=('Arial Bold', 12), fill='white')  # re prints new level
            elif x1 <= self.xx + self.radius <= x2 and y1 <= self.yy <= y2 and self.speed_x >= 1:
                self.speed_x = -abs(self.speed_x)  # changes only the horizontal speed
                canvas.delete(i)  # deletes the brick from the canvas
                Bricks.pop(Bricks.index(i))  # removes the brick from Bricks
                self.score += 10  # increases the score by 10
                if b.score == 1000:  # Checks if score reaches 1000
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 2', font=('Arial Bold', 12), fill='white')  # re prints new level
                if b.score == 2000:
                    B.draw_rectangle()  # redraws all bricks
                    self.xx = WIDTH / 2  # moves the ball to the center
                    self.yy = HEIGHT / 2
                    self.speed_y = 5  # changes the speed of the ball
                    self.speed_x = 0
                    canvas.delete(text_id2)  # deletes the level at the bottom right
                    canvas.create_text(WIDTH - 50, HEIGHT - 20, text='LEVEL 3', font=('Arial Bold', 12), fill='white')  # re prints new level

    def draw(self):  # function that draws the ball and the trail of the ball
        circle_id = canvas.create_oval(self.xx - self.radius, self.yy - self.radius, self.xx + self.radius, self.yy + self.radius, fill='red', outline='black')  # draws the ball
        drawn_circles.append(circle_id)  # ads new coordinates of ball
        # the is statement for the tail of the ball is reused from the ManyCircles.py code provided under Week02, step0206
        if len(drawn_circles) > MAX_SIZE:  # checks if the amount of drawn circles on canvas is less than 6
            id_of_circle_to_be_deleted = drawn_circles.pop(0)  # removes the coordinates last drawn circle
            canvas.delete(id_of_circle_to_be_deleted)  # removes circle from canvas

    def bounce(self):  # function that bounces the ball in different directions depending on where on the craft the ball landed
        if x - width // 2 + 94 <= self.xx <= x + width // 2 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 10  # ball horizontal speed changed to 10
        if x - width // 2 + 89 <= self.xx <= x + width // 2 - 5 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 9  # ball horizontal speed changed to 9
        if x - width // 2 + 84 <= self.xx <= x + width // 2 - 10 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 8  # ball horizontal speed changed to 8
        if x - width // 2 + 81 <= self.xx <= x + width // 2 - 15 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 7  # ball horizontal speed changed to 7
        if x - width // 2 + 74 <= self.xx <= x + width // 2 - 20 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 6  # ball horizontal speed changed to 6
        if x - width // 2 + 69 <= self.xx <= x + width // 2 - 25 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 5  # ball horizontal speed changed to 5
        if x - width // 2 + 64 <= self.xx <= x + width // 2 - 30 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 4  # ball horizontal speed changed to 4
        if x - width // 2 + 59 <= self.xx <= x + width // 2 - 35 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 3  # ball horizontal speed changed to 3
        if x - width // 2 + 55 <= self.xx <= x + width // 2 - 40 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)
            self.speed_x = 2  # ball horizontal speed changed to 2
        if x - width // 2 + 49 <= self.xx <= x + width // 2 - 45 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = 0  # ball horizontal speed changed to 0
        if x - width // 2 + 39 <= self.xx <= x + width // 2 - 55 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 2  # ball horizontal speed changed to -2
        if x - width // 2 + 34 <= self.xx <= x + width // 2 - 60 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 3  # ball horizontal speed changed to -3
        if x - width // 2 + 29 <= self.xx <= x + width // 2 - 65 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 4  # ball horizontal speed changed to -4
        if x - width // 2 + 24 <= self.xx <= x + width // 2 - 70 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 5  # ball horizontal speed changed to -5
        if x - width // 2 + 19 <= self.xx <= x + width // 2 - 75 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 6  # ball horizontal speed changed to -6
        if x - width // 2 + 14 <= self.xx <= x + width // 2 - 80 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 7  # ball horizontal speed changed to -7
        if x - width // 2 + 9 <= self.xx <= x + width // 2 - 85 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 8  # ball horizontal speed changed to -8
        if x - width // 2 + 6 <= self.xx <= x + width // 2 - 90 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 9  # ball horizontal speed changed to -9
        if x - width // 2 <= self.xx <= x + width // 2 - 95 and self.yy >= HEIGHT - height - self.radius:
            self.speed_y = -abs(self.speed_y)  # ball vertical speed reversed
            self.speed_x = - 10  # ball horizontal speed changed to -10

    def extra(self):  # function that upon the ball passing the craft, stops the ball, prints game over. if player won the game
        # stops ball and prints you won. and if next level os reached increases speed of the ball
        global DELAY
        if self.yy == HEIGHT:  # If ball reaches bottom of window than game ends
            self.speed_y = 0
            self.speed_x = 0
            canvas.create_text(WIDTH/2, 250, text='Game Over!!!', font=('Arial Bold', 20), fill='red')
            print('Game Over!!!')
        if 1000 <= self.score < 2000:  # If score is between 1000 and 2000 speed of ball increase due to smaller delay between animations
            DELAY = 10
        if self.score >= 2000:  # If score is higher than 2000 then speed of ball is further increased
            DELAY = 5
        if self.score == 3000:  # if score reaches 3000 ball is stopped, and you won message is printed on canvas
            self.speed_y = 0
            self.speed_x = 0
            canvas.create_text(WIDTH/2, 250, text='You Won!', font=('Arial Bold', 30), fill='white')
            print('You Won!')


class Brick:  # Brick class creates the bricks at the top are of the window

    def __init__(self, x_2, y_2, col):  # function initialises values
        self.x_2 = x_2
        self.y_2 = y_2
        self.col = col

    def draw_rectangle(self):  # this function draws and colours five rows of 20 bricks
        for h in range(5):
            self.col = BRICK_COLORS[h]
            for g in range(20):
                x_1 = g * 40
                y_1 = h * 24
                # Start by computing the 'top-left' and 'bottom-right' coordinates.
                x1 = x_1 + 5
                y1 = y_1 + 5
                x2 = x_1 + self.x_2    # square center minus side/2
                y2 = y_1 + self.y_2  # square center plus side/2
                # Then, draw the square.
                Bricks.append(canvas.create_rectangle(x1, y1, x2, y2, fill=self.col))
                # This is the end of the function. Remember, 2 empty lines are expected before resuming


# The code for printing and changing text on canvas was reused from the
# SowingTextOnCanvas.py code provided under Week03, step0303
class Score:  # Score class counts and draws the score in the bottom left corner of the window and the levels in the bottom right

    def __init__(self):
        self.score = 0

    def count(self):  # function that counts and draws the score
        self.score = b.score
        canvas.itemconfig(text_id, text=str(self.score), font=('Arial Bold', 12), fill='white')

    def stage(self):  # function checks the score and draws the according level
        self.score = b.score
        if b.score == 1000:  # checks if score is 1000
            canvas.delete(text_id2)  # deletes old level
            canvas.itemconfig(text_id2, text='LEVEL 2', font=('Arial Bold', 12), fill='white')  # prints new level
        if self.score == 2000:  # checks if score is 1000
            canvas.delete(text_id2)  # deletes old level
            canvas.itemconfig(text_id2, text='Level 3', font=('Arial Bold', 12), fill='white')  # prints new level


ball = []  # ball coordinates list

b = Ball(WIDTH / 2, 300, 0, DEFAULT_SPEED, 6, 'red')  # ball coordinates
ball.append(b)  # ads ball coordinates to list


def animation():  # function that runs all the functions in ball class and score
    global ball
    for b_i in ball:
        b_i.move_ball()
        b_i.bounce()
        b_i.draw()
        b_i.brick_bounce()
        b_i.extra()
    S.count()
    canvas.after(DELAY, animation)


def key_press(event):  # function that if x is pressed then the program terminates.
    if event.char == 'x':
        quit()


B = Brick(40, 25, BRICK_COLORS)  # coordinates of brick
C = Craft()  # initializes craft class into C
S = Score()  # initializes score class into S
win.bind('<Motion>', C.move)  # binds the mouse to the craft class move function
win.bind('<KeyPress>', key_press)  # binds key_press function and calls it upon a press of a key
animation()  # calls the animation function
S.count()  # calls the count function in Score class
S.stage()  # calls the stage function in Score class
B.draw_rectangle()  # class the draw_rectangle function in Brick class
win.mainloop()  # loops the program so it keeps running
