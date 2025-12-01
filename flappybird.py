import turtle as t
import random

# Setup
t.setup(900, 300)
t.tracer(0, 0)
t.hideturtle()
t.penup()

# Initial positions
bx = -300
by = 0
pu1x = 300

# Bird properties
bird_velocity = 0
gravity = -0.5
jump_strength = 10

# Pipe properties
pipe_width = 40
pipe_height = 100
gap_size = 200  # Space between pipes

def bird():
    global bird_velocity, by
    
    # Apply gravity
    bird_velocity += gravity
    by += bird_velocity
    
    # Draw bird
    t.goto(bx, by)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    
    # Ground collision
    if by < -140:
        by = -140
        bird_velocity = 0
    
    # Ceiling collision
    if by > 140:
        by = 140
        bird_velocity = 0

def jump(x=0, y=0):
    global bird_velocity
    bird_velocity = jump_strength

def upipe(px, py):
    """Draw upper pipe"""
    t.goto(px, py)
    t.setheading(0)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.forward(pipe_width)
    t.right(90)
    t.forward(pipe_height)
    t.right(90)
    t.forward(pipe_width)
    t.right(90)
    t.forward(pipe_height)
    t.end_fill()
    t.penup()

def lpipe(px, py):
    """Draw lower pipe"""
    t.goto(px, py)
    t.setheading(0)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.forward(pipe_width)
    t.left(90)
    t.forward(pipe_height)
    t.left(90)
    t.forward(pipe_width)
    t.left(90)
    t.forward(pipe_height)
    t.end_fill()
    t.penup()

def twopipes(px, upper_pipe_y):
    """Draw both pipes at given position and height"""
    # Upper pipe
    upipe(px, upper_pipe_y)
    # Lower pipe (automatically maintains gap)
    lpipe(px, upper_pipe_y - pipe_height - gap_size)

def update_game():
    global pu1x, upper_pipe_y
    
    # Clear the screen
    t.clear()
    
    # Move pipes to the left
    pu1x -= 10
    
    # Reset pipe position with new random height when it goes off screen
    if pu1x < -450:
        pu1x = 450
        # Random height for upper pipe (between 100 and 250)
        upper_pipe_y = random.randint(100, 250)
    
    # Draw pipes
    twopipes(pu1x, upper_pipe_y)
    
    # Draw bird
    bird()
    
    # Update screen
    t.update()
    
    # Schedule next frame
    t.ontimer(update_game, 33)

# Initial random height for first pipe
upper_pipe_y = random.randint(100, 250)

# Set up mouse click for jumping
t.onscreenclick(jump)

# Set up keyboard for jumping
t.listen()
t.onkeypress(jump, "space")
t.onkeypress(jump, "Up")

# Start the game loop
update_game()

t.mainloop()