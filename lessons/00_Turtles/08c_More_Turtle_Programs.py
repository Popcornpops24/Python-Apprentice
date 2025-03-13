import turtle

def set_background_image(window, image_name):

    from pathlib import Path
    from PIL import Image


    image_dir =
Path(_file_).parent / "images"
"images"
    image_path = 
str(image_dir / image_name)

    image =
Image.open(image_path)

window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

import turtle

turtle.setup(width=600, height=600)

tina = turtle.Turtle()

screen = turtle.Screen()

set_background_image(screen,"pikachu.gif")

turtle.exitonclick()