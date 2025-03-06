"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


import turtle
turtle.setup (width=600, height=600)
tina = turtle.Turtle()

tina.shape('turtle')
tina.speed(2)

tina.pendown()
tina.pencolor('red') 
tina.forward(60)
tina.penup()
tina.left(72) 

tina.pendown()
tina.pencolor('orange') 
tina.forward(60)
tina.penup()
tina.left(72)

tina.pendown()
tina.pencolor('yellow') 
tina.forward(60)
tina.penup()
tina.left(72)

tina.pendown()
tina.pencolor('green') 
tina.forward(60)
tina.penup()
tina.left(72)

tina.pendown()
tina.pencolor('blue') 
tina.forward(60)
tina.penup()
tina.left(72)# Your code here

turtle.exitonclick()                    # Close the window when we click on it
