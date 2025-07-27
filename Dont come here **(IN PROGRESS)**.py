from ursina import *
app = Ursina(fullscreen=False)
window.editor_ui.disable()


rotation_pivot = Entity()
cubies = []

selected_cubie = None
drag_start = None
face_normal = None
is_rotating = False


def input(key):
    global selected_cubie, drag_start, face_normal, is_rotating

    if is_rotating:
        return

    if key == 'left mouse down':
        if mouse.hovered_entity:
            selected_cubie = mouse.hovered_entity
            drag_start = mouse.position
            face_normal = mouse.normal
     if key == 'left mouse up' and selected_cubie and drag_start:
        drag_end = mouse.position
        drag_vector = drag_end - drag_start

        dx = drag_vector.x
        dy = drag_vector.y
        if face_normal == Vec3(1, 0, 0) or face_normal == Vec3(-1, 0, 0):
            if abs(dy) > abs(dx):  # Only if it's a vertical drag
                rotate_y_layer(selected_cubie)

        
        
        selected_cubie = None
        drag_start = None
        face_normal = None


def rotate_y_layer(cubie):
    global is_rotating
    is_rotating = True

pos = cubie.position
face_normal = mouse.normal.normalized()

    if face_normal == Vec3(0, 0, 1) or face_normal == Vec3(0, 0, -1):
        axis = 'y'
        layer_value = round(pos.z)
    elif face_normal == Vec3(1, 0, 0) or face_normal == Vec3(-1, 0, 0):
        axis = 'z'
        layer_value = round(pos.x)
    elif face_normal == Vec3(0, 1, 0) or face_normal == Vec3(0, -1, 0):
        axis = 'x'
        layer_value = round(pos.y)
    else:
        print('Unknown face clicked')
        return


def rotate_x_layer(cubie):
    global is_rotating
    is_rotating = True
    layer_x = round(cubie.x)
    layer_cubies = [c for c in cubies if round(c.x) == layer_x]
    rotation_pivot.rotation = (0, 0, 0)
    for c in layer_cubies:
        c.parent = rotation_pivot
    rotation_pivot.animate_rotation(Vec3(0, 0, 90), duration=0.25, curve=curve.linear)

    def finish():
        for c in layer_cubies:
            c.world_position = c.world_position
            c.world_rotation = c.world_rotation
            c.parent = scene
            c.rotation = Vec3(round(c.rotation_x / 90) * 90,
                              round(c.rotation_y / 90) * 90,
                              round(c.rotation_z / 90) * 90)
            c.position = Vec3(round(c.x), round(c.y), round(c.z))
        is_rotating = False

    invoke(finish, delay=0.25)


def highlight():

