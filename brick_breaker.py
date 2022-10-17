from asyncio.windows_events import NULL
from graphics_lib import *

CIRCLE_X = 250
CIRCLE_Y = 250
CIRCLE_RADIUS = 10
CIRCLE_X_SPEED = 6
CIRCLE_Y_SPEED = -3

PADDLE_X = 300
PADDLE_Y = 450
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_SPEED = 0

REC_X = 0
REC_Y = 0
REC_WIDTH = 100
REC_HEIGHT = 30

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def key_press(key):
    global PADDLE_SPEED
    if key == "Left":
        PADDLE_SPEED = -7
    if key == "Right":
        PADDLE_SPEED = 7

def draw_frame():
    # Need "global" statements whenever we want to update variables that weren't declared
    # inside the current function. This is considered bad style in real life, but 
    # it will work for now.
    global CIRCLE_X, CIRCLE_Y, CIRCLE_X_SPEED, CIRCLE_Y_SPEED, PADDLE_X, PADDLE_SPEED
    global REC_X, REC_Y,REC_WIDTH, REC_HEIGHT
    rec_x = REC_X
    rec_y = REC_Y
    height = REC_HEIGHT
    # draw the ball and paddle
    draw_circle(CIRCLE_X, CIRCLE_Y, CIRCLE_RADIUS, "red")
    draw_rectangle(PADDLE_X, PADDLE_Y, PADDLE_X + PADDLE_WIDTH, PADDLE_Y + PADDLE_HEIGHT, "black", "paddle")
  
   # draw the first brick on the top left corner and continue to draw the rest of bricks on line 1
    draw_rectangle(rec_x, REC_Y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "green", "f1")
    rec_x +=100
    draw_rectangle(rec_x, REC_Y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "green", "f2")
    rec_x +=100
    draw_rectangle(rec_x, REC_Y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "green", "f3")
    rec_x +=100
    draw_rectangle(rec_x, REC_Y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "green", "f4")
    rec_x +=100
    draw_rectangle(rec_x, REC_Y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "green", "f5")
    

    height +=30
    rec_x = 0
    rec_y +=30

    # draw the first brick on the second line and continue to draw the rest of bricks
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "yellow","s1")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "yellow","s2")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "yellow","s3")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "yellow","s4")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "yellow","s5")


    height +=30
    rec_x = 0
    rec_y += 30

    # draw the first brick on the third line and continue to draw the rest of bricks
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "blue","t1")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "blue","t2")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "blue","t3")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "blue","t4")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "blue","t5")
    
    height +=30
    rec_x = 0
    rec_y += 30

    # draw the first brick on the forth line and continue to draw the rest of bricks
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "white","fr1")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "white","fr2")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "white","fr3")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "white","fr4")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "white","fr5")
    rec_x +=100

    height +=30
    rec_x = 0
    rec_y += 30

    # draw the first brick on the fifth line and continue to draw the rest of bricks
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "red","fi1")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "red","fi2")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "red","fi3")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "red","fi4")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "red","fi5")
    rec_x +=100

    height +=30
    rec_x = 0
    rec_y += 30

    # draw the first brick on the sixth line and continue to draw the rest of bricks
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "orange","se1")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "orange","se2")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "orange","se3")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "orange","se4")
    rec_x +=100
    draw_rectangle(rec_x, rec_y, rec_x+REC_WIDTH, rec_y+REC_HEIGHT, "orange","se5")
    rec_x +=100

    #h6 for height of the row closest to the padle
    h6 = height
    # checks if the ball hits any particular brick, deletes it, ball bounces back, height is updated and so on
    if(CIRCLE_Y + CIRCLE_RADIUS <= h6 and CIRCLE_X + CIRCLE_RADIUS >= 0 and CIRCLE_X + CIRCLE_RADIUS<=100):
        gc.canvas.delete("se1")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h6 and CIRCLE_X + CIRCLE_RADIUS >= 100 and CIRCLE_X + CIRCLE_RADIUS<=200):
        gc.canvas.delete("se2")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h6 and CIRCLE_X + CIRCLE_RADIUS >= 200 and CIRCLE_X + CIRCLE_RADIUS<=300):
        gc.canvas.delete("se3")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h6 and CIRCLE_X + CIRCLE_RADIUS >= 300 and CIRCLE_X + CIRCLE_RADIUS<=400):
        gc.canvas.delete("se4")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h6 and CIRCLE_X + CIRCLE_RADIUS >= 400 and CIRCLE_X + CIRCLE_RADIUS<=500):
        gc.canvas.delete("se5")
        CIRCLE_Y_SPEED *= -1
        height-=30
    #h5 for height of the row closest to the padle
    h5 = height

    if(CIRCLE_Y + CIRCLE_RADIUS <= h5 and CIRCLE_X + CIRCLE_RADIUS >= 0 and CIRCLE_X + CIRCLE_RADIUS<=100):
        gc.canvas.delete("fi1")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h5 and CIRCLE_X + CIRCLE_RADIUS >= 100 and CIRCLE_X + CIRCLE_RADIUS<=200):
        gc.canvas.delete("fi2")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h5 and CIRCLE_X + CIRCLE_RADIUS >= 200 and CIRCLE_X + CIRCLE_RADIUS<=300):
        gc.canvas.delete("fi3")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h5 and CIRCLE_X + CIRCLE_RADIUS >= 300 and CIRCLE_X + CIRCLE_RADIUS<=400):
        gc.canvas.delete("fi4")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h5 and CIRCLE_X + CIRCLE_RADIUS >= 400 and CIRCLE_X + CIRCLE_RADIUS<=500):
        gc.canvas.delete("fi5")
        CIRCLE_Y_SPEED *= -1
        height-=30
    #h4 for height of the row closest to the padle
    h4 = height

    if(CIRCLE_Y + CIRCLE_RADIUS <= h4 and CIRCLE_X + CIRCLE_RADIUS >= 0 and CIRCLE_X + CIRCLE_RADIUS<=100):
        gc.canvas.delete("fr1")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h4 and CIRCLE_X + CIRCLE_RADIUS >= 100 and CIRCLE_X + CIRCLE_RADIUS<=200):
        gc.canvas.delete("fr2")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h4 and CIRCLE_X + CIRCLE_RADIUS >= 200 and CIRCLE_X + CIRCLE_RADIUS<=300):
        gc.canvas.delete("fr3")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h4 and CIRCLE_X + CIRCLE_RADIUS >= 300 and CIRCLE_X + CIRCLE_RADIUS<=400):
        gc.canvas.delete("fr4")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h4 and CIRCLE_X + CIRCLE_RADIUS >= 400 and CIRCLE_X + CIRCLE_RADIUS<=500):
        gc.canvas.delete("fr5")
        CIRCLE_Y_SPEED *= -1
        height-=30
    #h3 for height of the row closest to the padle   
    h3 = height
    if(CIRCLE_Y + CIRCLE_RADIUS <= h3 and CIRCLE_X + CIRCLE_RADIUS >= 0 and CIRCLE_X + CIRCLE_RADIUS<=100):
        gc.canvas.delete("t1")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h3 and CIRCLE_X + CIRCLE_RADIUS >= 100 and CIRCLE_X + CIRCLE_RADIUS<=200):
        gc.canvas.delete("t2")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h3 and CIRCLE_X + CIRCLE_RADIUS >= 200 and CIRCLE_X + CIRCLE_RADIUS<=300):
        gc.canvas.delete("t3")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h3 and CIRCLE_X + CIRCLE_RADIUS >= 300 and CIRCLE_X + CIRCLE_RADIUS<=400):
        gc.canvas.delete("t4")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h3 and CIRCLE_X + CIRCLE_RADIUS >= 400 and CIRCLE_X + CIRCLE_RADIUS<=500):
        gc.canvas.delete("t5")
        CIRCLE_Y_SPEED *= -1
        height-=30
        
    #h2 for height of the row closest to the padle
    h2 = height
    if(CIRCLE_Y + CIRCLE_RADIUS <= h2 and CIRCLE_X + CIRCLE_RADIUS >= 0 and CIRCLE_X + CIRCLE_RADIUS<=100):
        gc.canvas.delete("s1")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h2 and CIRCLE_X + CIRCLE_RADIUS >= 100 and CIRCLE_X + CIRCLE_RADIUS<=200):
        gc.canvas.delete("s2")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h2 and CIRCLE_X + CIRCLE_RADIUS >= 200 and CIRCLE_X + CIRCLE_RADIUS<=300):
        gc.canvas.delete("s3")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h2 and CIRCLE_X + CIRCLE_RADIUS >= 300 and CIRCLE_X + CIRCLE_RADIUS<=400):
        gc.canvas.delete("s4")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h2 and CIRCLE_X + CIRCLE_RADIUS >= 400 and CIRCLE_X + CIRCLE_RADIUS<=500):
        gc.canvas.delete("s5")
        CIRCLE_Y_SPEED *= -1
        height-=30

    #h1 for height of the row closest to the padle
    h1 = height
    if(CIRCLE_Y + CIRCLE_RADIUS <= h1 and CIRCLE_X + CIRCLE_RADIUS >= 0 and CIRCLE_X + CIRCLE_RADIUS<=100):
        gc.canvas.delete("f1")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h1 and CIRCLE_X + CIRCLE_RADIUS >= 100 and CIRCLE_X + CIRCLE_RADIUS<=200):
        gc.canvas.delete("f2")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h1 and CIRCLE_X + CIRCLE_RADIUS >= 200 and CIRCLE_X + CIRCLE_RADIUS<=300):
        gc.canvas.delete("f3")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h1 and CIRCLE_X + CIRCLE_RADIUS >= 300 and CIRCLE_X + CIRCLE_RADIUS<=400):
        gc.canvas.delete("f4")
        CIRCLE_Y_SPEED *= -1
        height-=30
    if(CIRCLE_Y + CIRCLE_RADIUS <= h1 and CIRCLE_X + CIRCLE_RADIUS >= 400 and CIRCLE_X + CIRCLE_RADIUS<=500):
        gc.canvas.delete("f5")
        CIRCLE_Y_SPEED *= -1
        height-=30



    # If the ball hits either side of the screen, it should bounce off
    if CIRCLE_X + CIRCLE_RADIUS >= WINDOW_WIDTH:
        CIRCLE_X_SPEED *= -1
    if CIRCLE_X - CIRCLE_RADIUS <= 0:
        CIRCLE_X_SPEED *= -1
    

    # If the ball hits a paddle, it should bounce off
    if (
        PADDLE_Y <= CIRCLE_Y + CIRCLE_RADIUS < PADDLE_Y + CIRCLE_Y_SPEED and
        PADDLE_X <= CIRCLE_X <= PADDLE_X + PADDLE_WIDTH
    ):
        CIRCLE_Y_SPEED *= -1

    # If the ball hits the bottom, freeze it
    if CIRCLE_Y + CIRCLE_RADIUS >= WINDOW_HEIGHT:
        CIRCLE_Y_SPEED = 0
        CIRCLE_X_SPEED = 0

    # If the ball hits the top of the screen, it bounces off
    if CIRCLE_Y - CIRCLE_RADIUS <= 0:
        CIRCLE_Y_SPEED *= -1
    
    # If the paddle hits the side of the screen, it should stop moving
    # Subtle point: these inequalities must be strict (i.e. not <= 0 or >= 0)
    # This is because we're putting the paddle back at the right or left edge
    # of the screen if it wanders off. If we set the speed to zero whenever the
    # paddle is EXACTLY AT either edge, it will get "stuck" to the side of the screen.
    if PADDLE_X < 0 or PADDLE_X + PADDLE_WIDTH > WINDOW_WIDTH:
        PADDLE_SPEED = 0
        PADDLE_X = max(0, PADDLE_X)
        PADDLE_X = min(WINDOW_WIDTH - PADDLE_WIDTH, PADDLE_X)
    

    # Update the ball and paddle locations
    CIRCLE_X += CIRCLE_X_SPEED
    CIRCLE_Y += CIRCLE_Y_SPEED
    PADDLE_X += PADDLE_SPEED

start_graphics(
    draw_frame,
    window_width=WINDOW_WIDTH,
    window_height=WINDOW_HEIGHT,
    key_press=key_press,
)