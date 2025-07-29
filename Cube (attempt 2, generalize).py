from ursina import *
import random

app=Ursina(fullscreen=False)
d =.51 #distance from the parent
cubes = {}
directions = ['dir1', 'dir2']
axis = ['x','y','z']
values = [-1,0,1]
rotatePoint = Entity(model='cube', scale=1, position=(0,0,0))
rotateDuration = .4
moveInterval = rotateDuration +.1
for a in range(-1,2):
    for b in range(-1,2):
        for c in range(-1,2):
            if (a, b, c) == (0, 0, 0):
                continue
            cubes[a,b,c] = Entity(
                model='cube',
                scale=1,
                position=(a,b,c),
                color=color.white)
for i in cubes.values():
    if i.x == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0,0,90),
            position=(d,0,0),
            color=color.red,
            parent=i
 )
for i in cubes.values():
    if i.x == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0,0,-90),
            position=(-d,0,0),
            color=color.black,
            parent=i
 )
for i in cubes.values():
    if i.y == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0,0,0),
            position=(0,d,0),
            color=color.yellow,
            parent=i
 )
for i in cubes.values():
    if i.z == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(90,0,0),
            position=(0,0,d),
            color=color.green,
            parent=i
 )
for i in cubes.values():
    if i.y == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0,0,180),
            position=(0,-d,0),
            color=color.blue,
            parent=i
 )
for i in cubes.values():
    if i.z == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(-90,0,0),
            position=(0,0,-d),
            color=color.orange,
            parent=i
 )
for c in cubes.values():
    c.combine()

def rotateCube(direction, axis, point):
    for i in cubes.values():
        if axis == 'x':
            if i.x == point:
                i.parent = rotatePoint
        if axis == 'y':
            if i.y == point:
                i.parent = rotatePoint
        if axis == 'z':
            if i.z == point:
                i.parent = rotatePoint
    if direction.lower() == 'dir1':
        if axis == 'x':
            rotatePoint.animate('rotation_x',rotatePoint.rotation_x + 90, duration = rotateDuration)
        if axis == 'y':
            rotatePoint.animate('rotation_y',rotatePoint.rotation_y + 90, duration = rotateDuration)
        if axis == 'z':
            rotatePoint.animate('rotation_z',rotatePoint.rotation_z + 90, duration = rotateDuration)
    if direction.lower() == 'dir2':
        if axis == 'x':
            rotatePoint.animate('rotation_x',rotatePoint.rotation_x - 90, duration = rotateDuration)
        if axis == 'y':
            rotatePoint.animate('rotation_y',rotatePoint.rotation_y - 90, duration = rotateDuration)
        if axis == 'z':
            rotatePoint.animate('rotation_z',rotatePoint.rotation_z - 90, duration = rotateDuration)
def unparentCubes():
    for cube in cubes.values():
        if cube.parent == rotatePoint:
            cube.world_parent = scene
            cube.position = Vec3(round(cube.x), round(cube.y), round(cube.z))
            cube.rotation = Vec3(round(cube.rotation_x / 90) * 90, round(cube.rotation_y / 90) * 90, round(cube.rotation_z / 90) * 90)
    rotatePoint.rotation = (0, 0, 0)
def scramble():
    rotateCube(random.choice(directions), random.choice(axis), random.choice(values))
scramble_sequence = Sequence(Func(scramble), Wait(.5), Func(unparentCubes), Wait(.5), loop=True)
def input(key):
    if key == 'r':
        scramble_sequence.start()
    if key == 'p':
        scramble_sequence.pause()
EditorCamera()
# to un parent do world_parent = scene
app.run()