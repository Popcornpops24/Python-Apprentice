"""functions: 
checking in
checking out
charging
add on services
dictionary bookings
while loop (last thing to code) below functions, call functions
do popups (below)"""
from tkinter import messagebox, simpledialog, Tk

window = Tk()

window.withdraw()

consent = simpledialog.askstring('Hotel Bookings', 'Welcome to Destiny Suites! Type "Yes" to check in, type "No" to exit.')
if consent == "No" or consent == "no":
    exit()

client = simpledialog.askstring("Hotel Bookings", "Name")

party = simpledialog.askinteger("Hotel Bookings", "Party")

contact_info = simpledialog.askstring("Hotel Bookings", "Please provide phone number and/or email.")

dates = simpledialog.askinteger("Hotel Bookings", "How many days do you like to stay?")

room = simpledialog.askinteger("Hotel Bookings", "Please specify your preferred amount of rooms.")

requests = simpledialog.askstring("Hotel Bookings", "Special requests?")

print(client + party + contact_info + dates, "Is this information correct?")
"""hasnt worked in printing"""
window.mainloop()

if room < 7:
    room_amount = 1
if room > 6 and room < 13:
    room_amount = 2
if room > 12 and room < 19:
    room_amount = 3
if room > 18 and room < 25:
    room_amount = 4
else:
    room_amount = 5

"""*tuples, function arguments and return statements"""
"""name of person checking in is value, key is rooms"""
"""the gist of starting the functions below"""
def check_out():
    check_in = {
    client : room_number,
    client : room_number,
    client : room_number,
}

room_number = check_out[client]
print(f"{client}: {room_number}")

client = "idk_yet"
room_number = check_out.get(client)
print(f"{client}: {room_number}")
def check_out(num1, num2):
    return num1 - num2
def charging(num1, num2):
    if num1 == num2:
        print("Same")
    else:
        print("Different")

from tkinter import messagebox, simpledialog, Tk

window = Tk()

window.withdraw()

checkout_consent = simpledialog.askstring('Hotel Checkout', 'This is Destiny Suites. Type "Yes" to check out, type "No" to exit.')
if checkout_consent == "No" or checkout_consent == "no":
    exit()

client = simpledialog.askstring("Hotel Checkout", "Name")

room_number = simpledialog.askinteger("Hotel Checkout", "Room Number")