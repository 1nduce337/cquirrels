from ursina import *

app = Ursina()

cube = Entity(model='cube', position= (0,0,0))

camera = EditorCamera()
camera.target = Entity(model='cube', position=(0,0,0)) # Make camera focus on the cube
camera.distance = 10 # Set a starting distance from the cube
last_x = mouse.x
last_y = mouse.y
def update():
    global last_x, last_y
    if held_keys['right mouse button']:
        camera.rotation_y -= last_x + mouse.x
        camera.rotation_x -= last_y + mouse.y 
    last_y = mouse.y
    last_x = mouse.x

app.run()