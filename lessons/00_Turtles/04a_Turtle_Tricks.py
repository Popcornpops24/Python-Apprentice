"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

import turtle
turtle.setup (width=600, height=600)

tina = turtle.Turtle()

tina.shape('turtle')
tina.speed(2)

tina.pendown()
tina.pencolor('green') 
tina.forward(90)
tina.penup()
tina.left(120) 

tina.pendown()
tina.pencolor('yellow') 
tina.forward(90)
tina.penup()
tina.left(120) 

tina.pendown()
tina.pencolor('blue') 
tina.forward(90)
tina.penup()
tina.left(120)

tina.end_fill() # Your code here

turtle.exitonclick()                    # Close the window when we click on it
