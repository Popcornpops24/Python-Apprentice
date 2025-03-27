"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk # Import the required modules

window = Tk() # Create a window object

window.withdraw() # Hide the window, hint: use the withdraw method

number1 = simpledialog.askinteger("Infuriating Calculator", "Give me a number") # Ask the user for the first number   

number2 = simpledialog.askinteger("Infuriating Calculator", "Give me a second number") # Ask the user for the second number

operation = simpledialog.askinteger("Infuriating Calculator", "Give me a math operation, 1 is addition, 2 is subtraction, 3 is multiplication, and 4 is division") # Ask the user for the math operation

if operation == 1 :
   print (number1 + number2)
if operation == 2 :
   print (number1 - number2)
if operation == 3 :
   print (number1 * number2)
elif operation == 4 :
   print (number1 / number2)  # Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

else :
   messagebox.showerror() # If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

window.mainloop() # Keep the window open
