from ursina import *
import random

app = Ursina(fullscreen=False)
d = .51  # distance from the parent
cubes = {}
directions = ['dir1', 'dir2']
axis = ['x', 'y', 'z']
values = [-1, 0, 1]
rotation_point = Entity(model='cube', scale=1, position=(0, 0, 0))
rotateDuration = .4
moveInterval = rotateDuration + .1
selected_cube = None
drag_start = None
face_normal = None
is_rotating = False
state = "Hrz"

background_music = Audio('good_music.mp3', loop=True, autoplay=True, volume=0.5)

for a in range(-1, 2):
    for b in range(-1, 2):
        for c in range(-1, 2):
            if (a, b, c) == (0, 0, 0):
                continue
            cubes[a, b, c] = Entity(
                model='cube',
                scale=1,
                position=(a, b, c),
                color=color.white)
for i in cubes.values():
    if i.x == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0, 0, 90),
            position=(d, 0, 0),
            # collider='mesh',
            color=color.red,
            parent=i
        )
for i in cubes.values():
    if i.x == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0, 0, -90),
            position=(-d, 0, 0),
            # collider='mesh',
            color=color.black,
            parent=i
        )
for i in cubes.values():
    if i.y == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0, 0, 0),
            position=(0, d, 0),
            # collider='mesh',
            color=color.yellow,
            parent=i
        )
for i in cubes.values():
    if i.z == 1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(90, 0, 0),
            position=(0, 0, d),
            color=color.green,
            # collider='mesh',
            parent=i
        )
for i in cubes.values():
    if i.y == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(0, 0, 180),
            position=(0, -d, 0),
            # collider='mesh',
            color=color.blue,
            parent=i
        )
for i in cubes.values():
    if i.z == -1:
        cubeSides = Entity(
            model='plane',
            scale=.9,
            rotation=(-90, 0, 0),
            position=(0, 0, -d),
            # collider='mesh',
            color=color.orange,
            parent=i
        )
for c in cubes.values():
    c.combine()
    c.collider = 'box'

# print(cubes.values())

Sky (
    color = color.red
)

def rotateCube(direction, axis, point):
    for i in cubes.values():
        if axis == 'x':
            if i.x == point:
                i.parent = rotation_point
        if axis == 'y':
            if i.y == point:
                i.parent = rotation_point
        if axis == 'z':
            if i.z == point:
                i.parent = rotation_point
    if direction.lower() == 'dir1':
        if axis == 'x':
            rotation_point.animate(
                'rotation_x', rotation_point.rotation_x + 90, duration=rotateDuration)
        if axis == 'y':
            rotation_point.animate(
                'rotation_y', rotation_point.rotation_y + 90, duration=rotateDuration)
        if axis == 'z':
            rotation_point.animate(
                'rotation_z', rotation_point.rotation_z + 90, duration=rotateDuration)
    if direction.lower() == 'dir2':
        if axis == 'x':
            rotation_point.animate(
                'rotation_x', rotation_point.rotation_x - 90, duration=rotateDuration)
        if axis == 'y':
            rotation_point.animate(
                'rotation_y', rotation_point.rotation_y - 90, duration=rotateDuration)
        if axis == 'z':
            rotation_point.animate(
                'rotation_z', rotation_point.rotation_z - 90, duration=rotateDuration)


# def input(key):
#     global selected_cube, drag_start, face_normal, is_rotating

#     if is_rotating:
#         return

#     if key == 'left mouse down':
#         if mouse.hovered_entity:
#             selected_cube = mouse.hovered_entity
#             drag_start = mouse.position
#             face_normal = mouse.normal

#     if key == 'left mouse up' and selected_cube and drag_start:
#         drag_end = mouse.position
#         drag_vector = drag_end - drag_start
#         dx = drag_vector.x
#         dy = drag_vector.y

#         if face_normal == Vec3(1, 0, 0) or face_normal == Vec3(-1, 0, 0):
#             if abs(dy) > abs(dx):
#                 rotate_y_layer(selected_cube)

#         elif face_normal == Vec3(0, 1, 0) or face_normal == Vec3(0, -1, 0):
#             if abs(dy) > abs(dx):
#                 rotate_x_layer(selected_cube)

#         elif face_normal == Vec3(0, 0, 1) or face_normal == Vec3(0, 0, -1):
#             if abs(dx) > abs(dy):
#                 rotate_z_layer(selected_cube)

#         selected_cube = None
#         drag_start = None
#         face_normal = None


# def rotate_x_layer(cube):
#     global is_rotating
#     is_rotating = True
#     layer_x = round(cube.x)
#     layer_cubes = [c for c in cubes if round(c.x) == layer_x]
#     rotation_point.rotation = (0, 0, 0)
#     for c in layer_cubes:
#         c.parent = rotation_point
#     rotation_point.animate_rotation(
#         Vec3(0, 0, 90), duration=0.25, curve=curve.linear)

#     def finish():
#         for c in layer_cubes:
#             c.world_position = c.world_position
#             c.world_rotation = c.world_rotation
#             c.parent = scene
#             c.rotation = Vec3(round(c.rotation_x / 90) * 90,
#                               round(c.rotation_y / 90) * 90,
#                               round(c.rotation_z / 90) * 90)
#             c.position = Vec3(round(c.x), round(c.y), round(c.z))
#         is_rotating = False

#     invoke(finish, delay=0.25)


# def rotate_y_layer(cube):
#     global is_rotating
#     is_rotating = True
#     layer_y = round(cube.y)
#     layer_cubes = [c for c in cubes if round(c.y) == layer_y]
#     rotation_point.rotation = (0, 0, 0)
#     for c in layer_cubes:
#         c.parent = rotation_point
#     rotation_point.animate_rotation(
#         Vec3(0, 0, 90), duration=0.25, curve=curve.linear)

#     def finish():
#         for c in layer_cubes:
#             c.world_position = c.world_position
#             c.world_rotation = c.world_rotation
#             c.parent = scene
#             c.rotation = Vec3(round(c.rotation_x / 90) * 90,
#                               round(c.rotation_y / 90) * 90,
#                               round(c.rotation_z / 90) * 90)
#             c.position = Vec3(round(c.x), round(c.y), round(c.z))
#         is_rotating = False

#     invoke(finish, delay=0.25)


def rotate_z_layer(cube):
    global is_rotating
    is_rotating = True
    layer_z = round(cube.z)
    layer_cubes = [c for c in cubes if round(c.z) == layer_z]
    rotation_point.rotation = (0, 0, 0)
    for c in layer_cubes:
        c.parent = rotation_point
    rotation_point.animate_rotation(
        Vec3(0, 90, 0), duration=0.25, curve=curve.linear)

    def finish():
        for c in layer_cubes:
            c.world_position = c.world_position
            c.world_rotation = c.world_rotation
            c.parent = scene
            c.rotation = Vec3(round(c.rotation_x / 90) * 90,
                              round(c.rotation_y / 90) * 90,
                              round(c.rotation_z / 90) * 90)
            c.position = Vec3(round(c.x), round(c.y), round(c.z))
        is_rotating = False
        invoke(finish, delay=0.25)


def unparentCubes():
    for cube in cubes.values():
        if cube.parent == rotation_point:
            cube.world_parent = scene
            cube.position = Vec3(round(cube.x), round(cube.y), round(cube.z))
            cube.rotation = Vec3(round(cube.rotation_x / 90) * 90, round(
                cube.rotation_y / 90) * 90, round(cube.rotation_z / 90) * 90)
    rotation_point.rotation = (0, 0, 0)


def scramble():
    rotateCube(random.choice(directions),
               random.choice(axis), random.choice(values))


scramble_sequence = Sequence(Func(scramble), Wait(.5), Func(
    unparentCubes), Wait(.5), loop=True)


def input(key):
    if key == 'r':
        scramble_sequence.start()
    elif key == 'p':
        scramble_sequence.pause()
    # if key == 'up arrow':
    #     print("something")
    elif key == 'left arrow':
        # print('pressed mouse')
        # print(mouse)
        if mouse.hovered_entity:
            mhe_y = mouse.hovered_entity.y  # y is horizontal
            # print(mouse.hovered_entity)
            for k in cubes.keys():
                e = cubes[k]
                axis = 0
                # print(e.y, mouse.hovered_entity.y,
                #   e.y == mouse.hovered_entity.y)
                rotateSequence = Sequence(
                    Func(rotateCube('dir1', 'y', mhe_y)), Wait(.5), Func(unparentCubes()), Wait(.5))
                sound_effect = Audio('coin', autoplay=True)
                # if e.y == mhe_y:
                #     print('\t', e.position)
                #     print('\t', cubes[k].position)
                #     cubes[k].y = 5
                #     print('\t', cubes[k].position)
                # print(e.position, e.y)
                # if e.position.Y_getter() == mouse.hovered_entity.position.Y_getter():
                #     cubes[k].y = 5
                # print(cubes[k].position.Y_getter())
                # print(e.position())
            # print()
    elif key == 'right arrow':
        # print('pressed mouse')
        # print(mouse)
        if mouse.hovered_entity:
            mhe_y = mouse.hovered_entity.y  # y is horizontal
            # print(mouse.hovered_entity)
            for k in cubes.keys():
                e = cubes[k]
                axis = 0
                # print(e.y, mouse.hovered_entity.y,
                #   e.y == mouse.hovered_entity.y)
                rotateSequence = Sequence(
                    Func(rotateCube('dir2', 'y', mhe_y)), Wait(.5), Func(unparentCubes()), Wait(.5))
                sound_effect = Audio('coin', autoplay=True)
                # if e.y == mhe_y:
                #     print('\t', e.position)
                #     print('\t', cubes[k].position)
                #     cubes[k].y = 5
                #     print('\t', cubes[k].position)
                # print(e.position, e.y)
                # if e.position.Y_getter() == mouse.hovered_entity.position.Y_getter():
                #     cubes[k].y = 5
                # print(cubes[k].position.Y_getter())
                # print(e.position())
            # print()
    elif key == 'up arrow':
        if mouse.hovered_entity:
            mhe_x = mouse.hovered_entity.x  # y is horizontal
            # print(mouse.hovered_entity)
            for k in cubes.keys():
                e = cubes[k]
                axis = 0
                # print(e.y, mouse.hovered_entity.y,
                #   e.y == mouse.hovered_entity.y)
                rotateSequence = Sequence(
                    Func(rotateCube('dir1', 'x', mhe_x)), Wait(.5), Func(unparentCubes()), Wait(.5))
                sound_effect = Audio('coin', autoplay=True)
                # if e.y == mhe_y:
                #     print('\t', e.position)
                #     print('\t', cubes[k].position)
                #     cubes[k].y = 5
                #     print('\t', cubes[k].position)
                # print(e.position, e.y)
                # if e.position.Y_getter() == mouse.hovered_entity.position.Y_getter():
                #     cubes[k].y = 5
                # print(cubes[k].position.Y_getter())
                # print(e.position())
            # print()
   
    elif key == 'down arrow':
        if mouse.hovered_entity:
            mhe_x = mouse.hovered_entity.x  # y is horizontal
            # print(mouse.hovered_entity)
            for k in cubes.keys():
                e = cubes[k]
                axis = 0
                # print(e.y, mouse.hovered_entity.y,
                #   e.y == mouse.hovered_entity.y)
                rotateSequence = Sequence(
                    Func(rotateCube('dir2', 'x', mhe_x)), Wait(.5), Func(unparentCubes()), Wait(.5))
                sound_effect = Audio('coin', autoplay=True)
                # if e.y == mhe_y:
                #     print('\t', e.position)
                #     print('\t', cubes[k].position)
                #     cubes[k].y = 5
                #     print('\t', cubes[k].position)
                # print(e.position, e.y)
                # if e.position.Y_getter() == mouse.hovered_entity.position.Y_getter():
                #     cubes[k].y = 5
                # print(cubes[k].position.Y_getter())
                # print(e.position())
            # print()
            

            # print(mouse.hovered_entity)
            # print('here')
            # selected_cube = mouse.hovered_entity
            # drag_start = mouse.position
            # face_normal = mouse.normal

    # if key == 'left mouse up' and selected_cube and drag_start:
    #     drag_end = mouse.position
    #     drag_vector = drag_end - drag_start
    #     dx = drag_vector.x
    #     dy = drag_vector.y/


EditorCamera()
# to un parent do world_parent = scene
app.run()