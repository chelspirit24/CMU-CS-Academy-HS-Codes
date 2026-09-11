from cmu_graphics import *
# When the mouse moves, the pigs start moving too!

# Sky and sun using helper function. 
def drawSky(x, y):
    Rect(x, y, 400, 85, fill='lightSkyBlue')
    Circle(x, y, 50, fill='yellow'),
    Line(56, 12, 73, 12, fill='yellow'),
    Line(44, 35, 61, 45, fill='yellow'),
    Line(13, 55, 30, 70, fill='yellow'),
    
drawSky(0, 0)

# Ground 
ground = Group(
    Rect(0, 85, 400, 20, fill='forestGreen'),
    Rect(0, 105, 400, 295, fill='sienna'),
    Rect(0, 115, 400, 80, fill='saddleBrown'),
    Rect(0, 205, 400, 90, fill='saddleBrown'),
    Rect(0, 305, 400, 100, fill='saddleBrown'),
    )

# Pigs 
pigone = Group(
    Circle(100, 50, 20, fill='lightPink'),
    Oval(68, 68, 45, 40, fill='lightPink'), 
    Circle(91, 47, 2, fill='black'),
    Circle(110, 47, 2, fill='black'),
    Oval(100, 56, 12, 8, fill='lightCoral'),
    Polygon(84, 37, 80, 30, 94, 34, fill='lightPink'),
    Polygon(113, 36, 125, 35, 118, 44, fill='lightPink'),
    Line(43, 55, 50, 65, fill='lightPink'),
    Line(55, 85, 51, 92, fill='lightPink'),
    Line(80, 56, 84, 90, fill= 'lightPink'),
    )

pigtwo = Group(
     Circle(236, 50, 20, fill='lightPink'),
     Oval(204, 68, 45, 40, fill='lightPink'),
     Circle(227, 47, 2, fill='black'),
     Circle(246, 47, 2, fill='black'),
     Oval(236, 56, 12, 8, fill='lightCoral'),
     Polygon(220, 37, 216, 30, 230, 34, fill='lightPink'),
     Polygon(249, 36, 261, 35, 254, 44, fill='lightPink'),
     Line(179, 55, 186, 65, fill='lightPink'),
     Line(191, 85, 187, 92, fill='lightPink'),
     Line(216, 56, 220, 90, fill='lightPink'),
     )
     
pigthree = Group(
     Circle(372, 50, 20, fill='lightPink'),
     Oval(340, 68, 45, 40, fill='lightPink'),
     Circle(363, 47, 2, fill='black'),
     Circle(382, 47, 2, fill='black'),
     Oval(372, 56, 12, 8, fill='lightCoral'),
     Polygon(356, 37, 352, 30, 366, 34, fill='lightPink'),
     Polygon(385, 36, 397, 35, 390, 44, fill='lightPink'), 
     Line(315, 55, 322, 65, fill='lightPink'),
     Line(327, 85, 323, 92, fill='lightPink'), 
     Line(352, 56, 356, 90, fill='lightPink'), 
     )
     
# The pigs move using one of the Mouse Motion Events: onMouseMove.
# Used multiple if statements so that it can command how the pigs move and when they need to be moved. 
def onMouseMove(mouseX, mouseY):
    if(onMouseMove):
       pigone.centerX += 5
       pigtwo.centerX += 5
       pigthree.centerX += 5
       
    if(pigone.centerX > 400):
       pigone.centerX = 0 
       pigone.centerY +=100
       
    if(pigtwo.centerX > 400): 
       pigtwo.centerX = 0
       pigtwo.centerY +=100
       
    if(pigthree.centerX > 400):
       pigthree.centerX = 0
       pigthree.centerY += 100
       
    if(pigone.centerY > 400):
       pigone.centerY = 68
       
    if(pigtwo.centerY > 400):
       pigtwo.centerY = 68
       
    if(pigthree.centerY > 400):
       pigthree.centerY = 68

cmu_graphics.run()
