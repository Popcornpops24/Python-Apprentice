import turtle as turtle

turtle.setup(width=600, height=600)

t = turtle.Turtle()

t.shape("turtle")
t.turtlesize(stretch_wid=10,stretch_len=10, outline=4)

def turtle_clicked(t,x,y):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

print('turtle clicked!')

for i in range(0,360,20):
        t.tilt(20)
    
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done()
"""
Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.
"""