# Hi! Welcom to our comments. Here we will go through what everything is doing, enjoy!

# Here we import the necesarry modules, using Ursina for the 3D viaulization and Random for the scrambling.
import random
from ursina import *

# Here is where all of our variable are declarered.

app = Ursina(fullscreen=False)
d = .51  # This is the distance from the parent
cubes = {}  # This is the dictionary that holds all of the cubes.

# These are the lists that Random uses for the scrambling.
directions = ['dir1', 'dir2']
axis = ['x', 'y', 'z']
values = [-1, 0, 1]
# This is where a center of rotating is defined.
rotationPoint = Entity(model='cube', scale=1, position=(0, 0, 0))
rotateDuration = .4
isRotating = False  # This tracks if the cube is currently rotating.
shuffleOn = False

# This is where we make the sky.
sky_texture = load_texture('bg.png')
# We Created a big cube that surrounds everything
sky = Entity(
    model='cube',
    texture=sky_texture,
    scale=8000,   # really big so you never reach the edge
    double_sided=True
)

sky.texture_scale = (1, 1)     # 1 means texture covers the whole face once


# This is where some UI and background music is defined.
window.editor_ui.disable()
background_music = Audio('background_music.mp3',
                         loop=True, autoplay=True,)
background_music.volume = 0.5

my_text = Text(text="CQUIRRELS CUBE!", scale=3, origin=(0.7, -5.5))
my_text = Text(text="Space Bar+LMB: Y axis rotation",
               scale=1, origin=(1.55, -14))
my_text = Text(text="Z+LMB: Z axis rotation", scale=1, origin=(2.34, -13))
my_text = Text(text="Shift+any previous rotation binds: spin in another direction",
               scale=1, origin=(.576, -12))
my_text = Text(text="M to Mute the Music",
               scale=1, origin=(2.5, 1))
button = Button(scale=(.2, .1), text='Toggle Shuffle', origin=(3.2, -2))

button.text_entity.world_scale = 20

# This is where the button is given an action when pressed.


def action():
    global shuffleOn
    if not shuffleOn and not isRotating:
        scrambleSequence.start()
        shuffleOn = True
    elif shuffleOn and not isRotating:
        scrambleSequence.pause()
        shuffleOn = False


button.on_click = action

# This is some of the most important code, which generates all of the smaller squares, which are then added to a dictionary.
for a in range(-1, 2):
    for b in range(-1, 2):
        for c in range(-1, 2):
            # This code makes it so that a cube is not generated at the center.
            if (a, b, c) == (0, 0, 0):
                continue
            cubes[a, b, c] = Entity(  # This code generates the actual cube.
                model='cube',
                scale=1,
                position=(a, b, c),
                color=color.white)

# The following code is also among the most important, adding differently colored sides.
for i in cubes.values():
    if i.x == 1:  # This code selects any cubes with an x of -1 and addes a colored side to it
        cubeSides = Entity(
            model='plane',  # This side is made out of a plane.
            # It has a scale of .9 so there is white space next to it.
            scale=.9,
            # It's rotation is set to 0,0,90 so it is visible.
            rotation=(0, 0, 90),
            # It is generated .51 units from the x of the center cube.
            position=(d, 0, 0),
            color=color.red,  # It is red.
            # It's parent is i (the cube it is next to) so it can be combined.
            parent=i
        )
    # The next 5 sections of cube do similiar things. The only thing of note is that if is used so cubes can have up to 3 colored sides.
    if i.x == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0, 0, -90),
            position=(-d, 0, 0),
            color=color.black,
            parent=i
        )
    if i.y == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0, 0, 0),
            position=(0, d, 0),
            color=color.yellow,
            parent=i
        )
    if i.z == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(90, 0, 0),
            position=(0, 0, d),
            color=color.green,
            parent=i
        )
    if i.y == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0, 0, 180),
            position=(0, -d, 0),
            color=color.blue,
            parent=i
        )
    if i.z == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(-90, 0, 0),
            position=(0, 0, -d),
            color=color.orange,
            parent=i
        )
# This code adds collision and, as mentioned ealier, combines the sides with the cubes.
for c in cubes.values():
    c.combine()
    c.collider = 'box'

# This function makes the cubes rotate.


def rotateCube(direction, axis, point):
    # This calls the global variable isRotating and allows the function to make changes to it.
    global isRotating
    isRotating = True  # This sets the isRotating variable to true.
    for i in cubes.values():
        # This code checks if the point on a given axis of a cube is equal to what is being rotated.
        # If this is the case, the parent of each cube is set to the rotation point, allowing the cubes to rotate with the rotation point.
        # This substantialy reduces the complexity and lines of code necessary.
        if axis == 'x':
            if i.x == point:
                i.parent = rotationPoint
        if axis == 'y':
            if i.y == point:
                i.parent = rotationPoint
        if axis == 'z':
            if i.z == point:
                i.parent = rotationPoint
    # The following code rotates the rotation point, rotating the cube
    # dir1/2 determines which way the center point/cube rotates.
    if direction == 'dir1':
        if axis == 'x':
            rotationPoint.animate(
                # This rotates the center point, animating it to take the provided duration time to move.
                'rotation_x', rotationPoint.rotation_x + 90, duration=rotateDuration)
        # The following code does the same thing for the other axis and directions, and uses elif/else to make it more consolidated and clear.
        elif axis == 'y':
            rotationPoint.animate(
                'rotation_y', rotationPoint.rotation_y + 90, duration=rotateDuration)
        else:
            rotationPoint.animate(
                'rotation_z', rotationPoint.rotation_z + 90, duration=rotateDuration)
    if direction == 'dir2':
        if axis == 'x':
            rotationPoint.animate(
                'rotation_x', rotationPoint.rotation_x - 90, duration=rotateDuration)
        elif axis == 'y':
            rotationPoint.animate(
                'rotation_y', rotationPoint.rotation_y - 90, duration=rotateDuration)
        else:
            rotationPoint.animate(
                'rotation_z', rotationPoint.rotation_z - 90, duration=rotateDuration)
# This function finishes the rotation process.
# It is seperated so the cubes arent uparented before they are supposed to be.


def finishRotation():
    for cube in cubes.values():
        # This code makes sure that we are only doing accessing cubes that have been rotated, improving speed.
        if cube.parent == rotationPoint:
            # This sets the cubes parent to the scene, while keeping their rotation.
            cube.world_parent = scene
            cube.position = Vec3(  # This makes sure there position isn't to effected by floating point.
                round(cube.x), round(cube.y), round(cube.z))
            cube.rotation = Vec3(round(cube.rotation_x / 90) * 90, round(  # This code does the same rounding for rotation.
                cube.rotation_y / 90) * 90, round(cube.rotation_z / 90) * 90)
    rotationPoint.rotation = (0, 0, 0)

# This function scrambles the cube.


def scramble():
    rotateCube(random.choice(directions),
               random.choice(axis), random.choice(values))

# This funciton sets isRotating to false. It is seperated so that it doesn't happen until the roation has actually finished.


def setIsRotating():
    global isRotating
    isRotating = False


# This code defines a scrambling sequence. A sequence should theoretically make it so the next function is not activated till the first finishes.
# It doesnt actually do this though, so we needed to add periods of "Wait", where the code does not move to the next step for a set amount of time.
scrambleSequence = Sequence(Func(scramble), Wait(.5), Func(
    finishRotation), Func(setIsRotating), Wait(.5), loop=True)


def input(key):
    # This code makes is so user input can rotate the cube.

    # This first part declares different variables which are actions the user could take.
    heldSpace = held_keys["space"]
    HeldZ = held_keys['z']
    heldShift = held_keys['left shift']

    if key == 'm':
        if background_music.playing:
            background_music.pause()
            print("Music Paused")
        else:
            background_music.resume()
            print("Music Resumed")

    # THis code detects if just left mouse was pressed, and moves the cube accordingly.
    # This makes sure that the cube only moves if it isn't currently moving, and if the only input is left click.
    if key == 'left mouse down' and not heldSpace and not isRotating and not HeldZ:
        # This check if the mouse is over a none button enity.
        if mouse.hovered_entity != button and mouse.hovered_entity:
            # It then takes that Y, using it for the rotateCube function. This will change the X of each cube.
            mheY = mouse.hovered_entity.y
            # This pauses the scramble if it currently happening.
            scrambleSequence.pause()
            if not heldShift:  # Part moves the cube using dir1 if shift is not helf.
                rotateCube('dir1', 'y', mheY)
                invoke(finishRotation, delay=.5)
                invoke(setIsRotating, delay=.6)
                # It also plays a sound.
                sound_effect = Audio('coin', autoplay=True)

            if heldShift and not isRotating:  # This moves the cube using dir2.
                scrambleSequence.pause()
                rotateCube('dir2', 'y', mheY)
                invoke(finishRotation, delay=.5)
                invoke(setIsRotating, delay=.6)
                sound_effect = Audio('coin', autoplay=True)
    # The following code does similiar actions, but instead rotating Y and Z, using X and Z inputs respectively.
    if heldSpace and key == 'left mouse down' and not isRotating and not HeldZ:
        if mouse.hovered_entity != button:
            mheX = mouse.hovered_entity.x
            if key == 'left mouse down' and not heldShift and not isRotating:
                scrambleSequence.pause()
                rotateCube('dir1', 'x', mheX)
                invoke(finishRotation, delay=.5)
                invoke(setIsRotating, delay=.6)
                sound_effect = Audio('coin', autoplay=True)
            if key == 'left mouse down':
                if heldShift and not isRotating:
                    scrambleSequence.pause()
                    rotateCube('dir2', 'x', mheX)
                    invoke(finishRotation, delay=.5)
                    invoke(setIsRotating, delay=.6)
                    sound_effect = Audio('coin', autoplay=True)
    if key == 'left mouse down' and not heldSpace and not isRotating and HeldZ:
        if mouse.hovered_entity != button:
            mheZ = mouse.hovered_entity.z  # y is horizontal
            scrambleSequence.pause()
            if not heldShift:
                rotateCube('dir1', 'z', mheZ)
                invoke(finishRotation, delay=.5)
                invoke(setIsRotating, delay=.6)
                sound_effect = Audio('coin', autoplay=True)

            if heldShift and not isRotating:
                scrambleSequence.pause()
                rotateCube('dir2', 'z', mheZ)
                invoke(finishRotation, delay=.5)
                invoke(setIsRotating, delay=.6)
                sound_effect = Audio('coin', autoplay=True)


# This turns the editor camera on so you can move around.
camera_editor = EditorCamera()


def back_to_cube():
    camera_editor.position = (.5, 0, 0)
    camera_editor.rotation = (0, 0, 0)

# Moves Editor Cam Back to the Cube


def face_top():
    camera_editor.position = (0, 0, 0)
    camera_editor.rotation = (45, 0, 0)
# This Makes the Cam Face the topp


def face_bottom():
    camera_editor.position = (0, 0, 0)
    camera_editor.rotation = (-45, 0, 0)
# This Makes the Cam Face the bottom


bc = Button(text='Back to Cube', scale=(.2, .1), position=(.2, .4))
bc.on_click = back_to_cube

ft = Button(text='Face Cube top', scale=(.2, .1), position=(.4, .4))
ft.on_click = face_top

fb = Button(text='Face Cube bottom', scale=(.2, .1), position=(.6, .4))
fb.on_click = face_bottom


app.run()  # This runs the code.
# We hope you enjoyed learning how this code works, it was a super hard challenge, but was also really fun!
