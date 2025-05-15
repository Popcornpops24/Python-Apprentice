"""functions: 
checking in
checking out
charging
add on services
dictionary bookings
while loop (last thing to code) below functions call functions
do popups or input or print"""
"""*tuples, function arguments and return statements"""
"""name of person checking in is value, key is rooms"""
"""the gist of starting the functions below"""
def check_in():
    check_in = {
    "abecedarian": "a person who is learning the alphabet",
    "blandishment": "flattering speech or actions designed to persuade",
    "cacophony": "a harsh, discordant mixture of sounds",
    "defenestration": "the act of throwing someone out of a window",
    "egregious": "outstandingly bad; shocking",
    "flagitious": "criminal; villainous",
    "grandiloquent": "pompous or extravagant in language, style, or manner",
    "hirsute": "hairy",
    "ignominious": "deserving or causing public disgrace or shame",
    "juxtapose": "to place side by side for contrast or comparison",
    "sesquipedalian": "given to using long words",
    "xerebrose": "dry, uninteresting"
}

word = "cacophony"
definition = check_in[word]
print(f"{word}: {definition}")

word = "xerebrose"
definition = check_in.get(word)
print(f"{word}: {definition}")
def check_out(num1, num2):
    return num1 - num2
def charging(num1, num2):
    if num1 == num2:
        print("Same")
    else:
        print("Different")
result
"""popups below"""
from tkinter import messagebox, simpledialog, Tk # Import the required modules

window = Tk() # Create a window object

window.withdraw() # Hide the window, hint: use the withdraw method

typehere = simpledialog.askinteger("hotel management", "Give me a number")

typehere2 = simpledialog.askinteger("hotel management", "Give me a second number")

operation = simpledialog.askinteger("hotel management", "Give me a math operation, 1 is addition, 2 is subtraction, 3 is multiplication, and 4 is division")