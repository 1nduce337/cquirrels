from ursina import *
import random


app=Ursina(fullscreen=False)

class cubeSide:
    def __init__(self,rot,fix,fval): #fix is the 'locked value' for that face; fval is the value at which it was locked at. e.g. fix=y fval=5 means this face has y fixed at 5
        for i in range (-1,2):
            for j in range (-1,2):
                if(fix=='y'):
                    thing=Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(i,fval,j),
                        color=color.rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    )
                elif(fix=='x'):
                    thing=Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(fval,i,j),
                        color=color.rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    )
                elif(fix=='z'):
                    thing=Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(i,j,fval),
                        color=color.rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    )
    
cubeSide((-90,0,0),'z',-1.5)


EditorCamera()
app.run()