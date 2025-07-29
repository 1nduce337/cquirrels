from ursina import *

app = Ursina()
camera.position = (5, 5, -20)
camera.look_at(Vec3(0, 0, 0))

rotation_point = Entity()
s = []

selected_cube = None
drag_start = None
face_normal = None
is_rotating = False


def input(key):
    global selected_cube, drag_start, face_normal, is_rotating

    if is_rotating:
        return

    if key == 'left mouse down':
        if mouse.hovered_entity:
            selected_cube = mouse.hovered_entity
            drag_start = mouse.position
            face_normal = mouse.normal

    if key == 'left mouse up' and selected_cube and drag_start:
        drag_end = mouse.position
        drag_vector = drag_end - drag_start
        dx = drag_vector.x
        dy = drag_vector.y

        if face_normal == Vec3(1, 0, 0) or face_normal == Vec3(-1, 0, 0):
            if abs(dy) > abs(dx):
                rotate_y_layer(selected_cube)

        elif face_normal == Vec3(0, 1, 0) or face_normal == Vec3(0, -1, 0):
            if abs(dy) > abs(dx):
                rotate_x_layer(selected_cube)

        elif face_normal == Vec3(0, 0, 1) or face_normal == Vec3(0, 0, -1):
            if abs(dx) > abs(dy):
                rotate_z_layer(selected_cube)

        selected_cube = None
        drag_start = None
        face_normal = None


def rotate_x_layer(cube):
    global is_rotating
    is_rotating = True
    layer_x = round(cube.x)
    layer_cubes = [c for c in cubes if round(c.x) == layer_x]
    rotation_point.rotation = (0, 0, 0)
    for c in layer_cubes:
        c.parent = rotation_point
    rotation_point.animate_rotation(
        Vec3(0, 0, 90), duration=0.25, curve=curve.linear)

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


def rotate_y_layer(cube):
    global is_rotating
    is_rotating = True
    layer_y = round(cube.y)
    layer_cubes = [c for c in cubes if round(c.y) == layer_y]
    rotation_point.rotation = (0, 0, 0)
    for c in layer_cubes:
        c.parent = rotation_point
    rotation_point.animate_rotation(
        Vec3(0, 0, 90), duration=0.25, curve=curve.linear)

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


app.run()
