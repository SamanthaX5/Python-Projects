import turtle
import random
import time

# Ask for user input
import turtle

# Get user inputs
side_length = int(input("Enter the size of the square: "))
char = input("Enter a character to display at each corner: ")
pen_color = input("Enter the pen color: ")
fill_color = input("Enter the fill color: ")

# Turtle Specs
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.color(pen_color, fill_color)
t.speed(2)

# Draw the square with symbols/words at each corner
for _ in range(4):
    t.forward(side_length)
    t.write(char, font=("Arial", 12, "bold"))
    t.right(90)

# Sparkle Drops
for _ in range(25):
    t.penup()
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    t.goto(x, y)
    t.dot(random.randint(6, 12), random.choice(["pink", "purple", "blue", "green", "red"]))

# Animated sparkle
for _ in range(20):
    t.penup()
    start_x = random.randint(-150, 150)
    start_y = random.randint(100, 200)  # Start from higher up
    t.goto(start_x, start_y)

    sparkle_color = random.choice(["white", "yellow", "aqua", "pink", "plum"])
    t.pendown()
    t.color(sparkle_color)

    for _ in range(10):
        t.dot(random.randint(3, 6))
        t.sety(t.ycor() - 10)
        time.sleep(0.05) # Brief pause to create the animation effect

    t.penup()

# Keep window open
turtle.done()