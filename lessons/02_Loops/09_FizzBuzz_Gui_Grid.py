"""Fizzbuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by neither, print the number.

Additionally, If you are displaying a number  color the numbers as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

Here is how you can display a number in your grid. Call this function in your loop
to display the number in the grid cell at the row and column you specify.

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger: 
    
    Text(app, text='🦡', grid=[col, row], color=color)

HINT: You can use % and // to get the first and last digit of a number, 
our you can convert the number to a string and iterate over the digits

"""
from guizero import App, Box, Text

app = App("Numbers Grid", layout="grid")

# Create a 10x10 grid using nested loops
# Or you can use a single loop and calculate the row and column

for i in range(1, 101):    
    row = (i-1) // 10
    col = (i-1) % 10

# In the loop, calculate or increment the number
# Use % determing the display, using fizzbuzz rules
if i % 15 == 0:
        text = '🐍'
        color = "green"
elif i % 5 == 0:
        text = '🦡'
        color = "black"
        digit_sum = sum(int(num) for num in str(i))
elif i % 3 == 0:
        text = '🍄'
        color = "red"
else:
        text = str(i)
# If you are displaying a number, calculate the sum of the digits and determine the color

color = "blue" if digit_sum % 2 == 0 else "red"
# Call Text(app, text='...', grid=[col, row], color=...) to display something. 
Text(app, text='text', grid=[col, row],color=color)
app.display()
