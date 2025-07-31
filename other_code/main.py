from ursina import *
import random

colorListNumRemaining=[9,9,9,9,9,9]
colorList=[color.white, color.red, color.blue, color.orange, color.green, color.yellow]
cubeSides = {}
axisConversion = {'x':0,'y':1,'z':2}
app=Ursina(fullscreen=False)

frontRot=(-90,0,0) #z=-1.5
behindRot=(90,0,0) #z=1.5
upRot=(0,0,0) #y=1.5
downRot=(180,0,0) #y=-1.5 
rightRot=(0,0,90) #x=1.5
leftRot=(0,0,-90) #x=-1.5


class cubeSide:
    def __init__(self,rot,fix,fval): #fix is the 'locked value' for that face; fval is the value at which it was locked at. e.g. fix=y fval=5 means this face has y fixed at 5
        self.sides = []
        for i in range (-1,2):
            for j in range (-1,2):
                if(fix=='y'):
                    color = colorList[random.randint(0,5)]
                    while colorListNumRemaining[colorList.index(color)] <= 0:
                        color = colorList[random.randint(0,5)]
                    colorListNumRemaining[colorList.index(color)] -= 1
                    cubeSides[(i,fval,j)] = Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(i,fval,j),
                        color=color
                    )

                    faceColor = [0,1,2,3,4,5,6,7,8,9]
                    # if fval == 1.5:
                        # faceColor


                        
                elif(fix=='x'):
                    color = colorList[random.randint(0,5)]
                    while colorListNumRemaining[colorList.index(color)] <= 0:
                        color = colorList[random.randint(0,5)]
                    colorListNumRemaining[colorList.index(color)] -= 1
                    cubeSides[(fval,i,j)] =Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(fval,i,j),
                        color=color
                    )
                    
                elif(fix=='z'):
                    color = colorList[random.randint(0,5)]
                    while colorListNumRemaining[colorList.index(color)] <= 0:
                        color = colorList[random.randint(0,5)]
                    colorListNumRemaining[colorList.index(color)] -= 1
                    cubeSides[(j,i,fval)] =Entity(
                        model='plane',
                        scale=1,
                        rotation=rot,
                        position=(j,i,fval),
                        color=color)
                    

cubeSide(frontRot,'z',-1.5)
cubeSide(behindRot,'z',1.5)
cubeSide(upRot,'y',1.5)
cubeSide(downRot,'y',-1.5)
cubeSide(rightRot,'x',1.5)
cubeSide(leftRot,'x',-1.5)
def rotateFace(point, axis):
    cubePlane = []
    remainingAxis = []
    cubePlaneSection1 = []
    cubePlaneSection2 = []
    cubePlaneSection3 = []
    cubePlaneSection4 = []
    cubePlaneSection5 = []
    cubePlaneSection6 = []
    for tpl in cubeSides: 
        if tpl[axisConversion[axis]] == point: # checking if the block is on the plane
            cubePlane.append(tpl) # appending the tuple to a list
            for i in axisConversion:
                if i != axisConversion[axis]:
                    remainingAxis.append[i]
            

                    



                        
                

EditorCamera()
app.run()
# Each tuple has -1.5, -1, 0, 1, 1.5 for each value