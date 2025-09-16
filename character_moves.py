from pico2d import *

open_canvas()

character = load_image('character.png')
def move_rectangle():
    print("Hello World, This is rectangle")
    pass


def move_circle():
    radius = 210
    for i in range(271, -90, -1):
        angle = math.radians(i)
        x = 400 + radius * math.cos(angle)
        y = 300 + radius * math.sin(angle)
        clear_canvas_now()
        character.draw_now(x, y)
        delay(0.01)
    pass

# fill here
while True:
    move_circle()
    move_rectangle()
    break
    #pass


close_canvas()