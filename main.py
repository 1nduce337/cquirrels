from ursina import *
import random

colorList=[color.white, color.red, color.blue, color.orange, color.green, color.yellow]

app=Ursina(fullscreen=False)

frontRot=(-90,0,0) #z=-1.5
behindRot=(90,0,0) #z=1.5
upRot=(0,0,0) #y=1.5
downRot=(180,0,0) #y=-1.5 
rightRot=(0,0,90) #x=1.5
leftRot=(0,0,-90) #x=-1.5

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
                        color=colorList[random.randint(0,5)]
                    )
                elif(fix=='x'):
                    thing=Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(fval,i,j),
                        color=colorList[random.randint(0,5)]
                    )
                elif(fix=='z'):
                    thing=Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(i,j,fval),
                        color=colorList[random.randint(0,5)]
                    )
    
cubeSide(frontRot,'z',-1.5)
cubeSide(behindRot,'z',1.5)
cubeSide(upRot,'y',1.5)
cubeSide(downRot,'y',-1.5)
cubeSide(rightRot,'x',1.5)
cubeSide(leftRot,'x',-1.5)


EditorCamera()
app.run()