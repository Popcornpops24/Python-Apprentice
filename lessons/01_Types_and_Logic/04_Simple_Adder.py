"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

from tkinter import messagebox, simpledialog, Tk # Import the required modules

window = Tk() # Create a window object

window.withdraw() # Hide the window, hint: use the withdraw method

number1 = simpledialog.askinteger("Two Numbers", "Give me a number") # Ask the user for the first number   

number2 = simpledialog.askinteger("Two Numbers", "Give me another number") # Ask the user for the second number

print(number1 + number2) # Display the sum of the two numbers 

window.mainloop() # Keep the window open

