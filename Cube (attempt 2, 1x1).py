from ursina import *

app=Ursina(fullscreen=False)

d =.51 #distance from the parent
cube1 = Entity(
    model='cube',
    scale=1,
    rotation=(0,0,0),
    position=(1,1,1),
    color=color.white
    )
side1 = Entity(
    model='plane',
    scale=1,
    position=(0,d,0),
    color=color.red,
    parent=cube1
    )
side2 =Entity(
    model='plane',
    scale=1,
    rotation=(0,0,90),
    position=(d,0,0),
    color=color.green,
    parent=cube1
    )
side3 = Entity(
    model='plane',
    scale=1,
    rotation=(90,0,0),
    position=(0,0,d),
    color=color.blue,
    parent=cube1
    )
side4 = Entity(
    model='plane',
    scale=1,
    rotation=(0,0,180),
    position=(0,-d,0),
    color=color.white,
    parent=cube1
    )
side5 =Entity(
    model='plane',
    scale=1,
    rotation=(0,0,-90),
    position=(-d,0,0),
    color=color.pink,
    parent=cube1
    )
side6 = Entity(
    model='plane',
    scale=1,
    rotation=(-90,0,0),
    position=(0,0,-d),
    color=color.orange,
    parent=cube1
    )
cube1.combine()
def update():
   cube1.rotation_x += 50 * time.dt
EditorCamera()
app.run()