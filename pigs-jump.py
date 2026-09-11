from cmu_graphics import * 
# Fill me in!

# Hold the right arrow key, then hold the spacebar the for the pig to run and jump over the hurdle
# Hold only the right arrow key for the pig to go under the hurdle

Rect(0,0, 400, 250, fill = 'lightSkyBlue')
Rect(0, 250, 400, 150, fill = 'saddleBrown')
Rect(0, 200, 400, 50, fill = 'forestGreen')

Circle(380, 30, 50, fill = 'yellow')

# fence 
Line(0, 200, 400, 200, fill = 'white', lineWidth = 10)
Line(29, 170, 29, 250, fill = 'white', lineWidth = 10)
Line(79, 170, 79, 250, fill = 'white' , lineWidth = 10)
Line(129, 170, 129, 250, fill = 'white', lineWidth = 10)
Line(179, 170, 179, 250, fill = 'white', lineWidth = 10)
Line(229, 170, 229, 250, fill ='white' , lineWidth = 10)
Line(279, 170, 279, 250, fill = 'white' , lineWidth = 10)
Line(329, 170, 329, 250, fill = 'white' , lineWidth=10)
Line(379, 170, 379, 250, fill = 'white' , lineWidth = 10)

# pig 
pig = Group(
    Circle(100, 306, 20, fill='lightPink'),
    Oval(68, 324, 45, 40, fill='lightPink'), 
    Circle(91, 303, 2, fill='black'),
    Circle(110, 303, 2, fill='black'),
    Oval(100, 312, 12, 8, fill='lightCoral'),
    Polygon(84, 293, 80, 286, 94, 290, fill='lightPink'),
    Polygon(113, 292, 125, 291, 118, 300, fill='lightPink'),
    Line(43, 311, 50, 321, fill='lightPink'),
    Line(55, 341, 51, 348, fill='lightPink'),
    Line(80, 312, 84, 346, fill= 'lightPink'),
    )
    
# hurdles 
hurdles = Group(
          Line(219, 290, 219, 340, fill = 'white', lineWidth = 5),
          Line(179, 276, 179, 320, fill = 'white', lineWidth = 5),
          Line(179, 276, 219, 290, fill = 'blue', lineWidth = 5),
          )
          
app.gameOver = False
app.tryAgainLabel = Label("try again! (Press 'r' to reset)", 200, 100, size=24, bold=True, fill='red', visible=False)

app.pigIsJumped = False
app.jumpTime = 0

pig.initialCenterX = pig.centerX
pig.initialCenterY = pig.centerY
hurdles.initialCenterX = hurdles.centerX

# contains onKeyHold, nested conditionals and compound conditionals
def onKeyHold(keys):
    if app.gameOver:
        return
    
    if 'right' in keys:
        pig.centerX += 5
        hurdles.centerX -= 5 
        
        if pig.hitsShape(hurdles):
            app.gameOver = True
            app.tryAgainLabel.visible = True
        elif (hurdles.centerX < 0) and (pig.centerX > 400):
            hurdles.centerX = 400
            pig.centerX = 0

def onKeyPress(key):
    if app.gameOver:
        if key == 'r':
            app.gameOver = False
            app.tryAgainLabel.visible = False
            pig.centerX = pig.initialCenterX
            pig.centerY = pig.initialCenterY
            hurdles.centerX = hurdles.initialCenterX
            app.pigIsJumped = False
        return

    if key == 'space' and not app.pigIsJumped:
        app.pigIsJumped = True
        app.jumpTime = 0
        pig.centerY -= 90
        pig.centerX += 50
        if pig.hitsShape(hurdles):
            app.gameOver = True
            app.tryAgainLabel.visible = True

def onKeyRelease(key):
    if app.gameOver:
        return
        
    if key == 'space' and app.pigIsJumped:
        app.pigIsJumped = False
        pig.centerY += 90
        if pig.hitsShape(hurdles):
            app.gameOver = True
            app.tryAgainLabel.visible = True

def onStep():
    if app.gameOver:
        return
        
    if app.pigIsJumped:
        app.jumpTime += 1
        # Default is 30 steps per second, so 15 = half-a-second
        if app.jumpTime >= 15:
            app.pigIsJumped = False
            pig.centerY += 90
            if pig.hitsShape(hurdles):
                app.gameOver = True
                app.tryAgainLabel.visible = True

cmu_graphics.run()