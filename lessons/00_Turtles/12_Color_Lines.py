"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors

    tina.color(color)

    tina.forward(90)

    tina.left(90) # Your code here


# 2) Make another square, but put the colors in reverse order, using a negative index. 

forward = 50

for left in [ 45, 60, 90, 45, -90, 60, 22 , -45, 90]:
    print(f"tina.forward({forward})")
    print(f"tina.left({left})")
    print(" ") # Your code here

turtle.exitonclick()                     # Close the window when we click on it