from cmu_graphics import *

# A soundboard of notable quotes and sound effects from RuPaul's Drag Race 
# Click on the buttons to play the sound effects

app.background = 'lavender'

# rupaul
rupaul = Group(
    Oval(110, 120, 80, 100, fill = 'peru'),
    Circle(90, 105, 10, fill = 'white'),
    Circle(130, 105, 10, fill = 'white'),
    Circle(130, 109, 5, fill = 'black'),
    Circle(90, 109, 5, fill = 'black'),
    Rect(72, 95, 35, 20, fill = None, border = 'black', borderWidth = 3),
    Rect(112, 95, 35, 20, fill = None, border = 'black', borderWidth = 3),
    Line(107, 105, 112, 105, lineWidth = 3),
    Circle(110, 140, 20, fill = 'crimson'),
    Rect(85, 120, 50, 15, fill = 'peru'),
    Rect(72, 169, 75, 100, fill = 'purple'),
    Rect(100,169,20,100, fill='black'),
    Polygon(100,169,109,180,120,169, fill='peru'),
    Line(85,186,85,230,fill='lavender'),
    Line(132,186,132,230,fill='lavender'),
    Line(90, 136,130, 136, fill = 'white', lineWidth = 3)
    )

# soundboard layout
app.rows = 3
app.cols = 3
app.board = makeList(app.rows, app.cols)

# soundboard buttons
def makeBoard():
    Rect(0, 230, 400, 300, fill = 'mediumPurple')
    for row in range(app.rows):
        for col in range(app.cols):
            x = 11 + 132 * row
            y = 245 + 55 * col
            block = Rect(x, y, 120, 30, fill = 'white')
            if(block.width == 120):
                block.width = 121

makeBoard()

# soundboard button labels
shadeLabel = Label('           SHADE           ', 68, 260, size = 12, bold = True )
whocaresLabel = Label('          WHO CARES         ', 204, 260, size = 12, bold = True)
hiLabel = Label('          HIIII          ', 335, 260, size = 12, bold = True)
backrollsLabel = Label('            BACKROLLS            ', 69, 315, size = 12, bold = True)
callmemotherLabel = Label('        CALL ME MOTHER       ', 204, 315, size = 12, bold = True)
hersesLabel = Label('           HERSES           ', 335, 315, size = 12, bold = True)
peanutbutterLabel = Label('          PEANUT BUTTER           ', 69, 370, size = 12, bold = True)
boomLabel = Label('          BOOM          ', 204, 370, size = 12, bold = True)
laughLabel = Label('          LAUGH          ', 337, 370, size = 12, bold = True)

# sound effects
shade = Sound('sounds/drag-race-shade-sound.mp3')
whoCares = Sound('sounds/who-cares-.mp3')
hi = Sound ('sounds/hieeee.mp3')
backrolls = Sound ('sounds/back-rolls.mp3')
callmeMother = Sound ('sounds/call-me-mother.mp3')
herses = Sound ('sounds/she_done_already_done_had_herses_rupauls_drag_race_all_stars.mp3')
peanutButter = Sound('sounds/peanutbutter-rupaul-clip.mp3')
boom = Sound ('sounds/boom_10.mp3')
laugh = Sound('sounds/rupaul.mp3')
hello = Sound('sounds/ScreenRecording_09-10-2026 22-00-56_1.mp3')


# rupaul intro
def rupaulSpeaks(rupaulSpeech):
    Circle(159, 153, 10, fill = 'white')
    Circle(196, 122, 10, fill = 'white')
    Oval(280, 70, 200, 120, fill='white')
    Label(rupaulSpeech, 280, 70, size = 15, bold = True)

rupaulSpeaks('HELLO HELLO HELLO')
hello.play()

# plays sound when clicked without overlapping
def playSoundOnly(soundToPlay, labelText):
    all_sounds = [shade, whoCares, hi, backrolls, callmeMother, herses, peanutButter, boom, laugh, hello]
    for s in all_sounds:
        if s is not None:
            try:
                s.pause()
            except Exception:
                pass
    if soundToPlay is not None:
        try:
            soundToPlay.play(restart=True)
        except Exception:
            pass
    rupaulSpeaks(labelText)

def onMousePress(mouseX, mouseY):
    appLabels = ['...', 'WHO CARES', 'HIIII', 'BACKROLLS', 'CALL ME MOTHER', 'HERSES', 'PEANUT BUTTER', 'BOOM', 'HAHAHAHA']
    if(shadeLabel.hits(mouseX, mouseY)):
        playSoundOnly(shade, appLabels[0])
    elif(whocaresLabel.hits(mouseX, mouseY)):
         playSoundOnly(whoCares, appLabels[1])
    elif(hiLabel.hits(mouseX, mouseY)):
         playSoundOnly(hi, appLabels[2])
    elif(backrollsLabel.hits(mouseX, mouseY)):
         playSoundOnly(backrolls, appLabels[3])
    elif(callmemotherLabel.hits(mouseX, mouseY)):
         playSoundOnly(callmeMother, appLabels[4])
    elif(hersesLabel.hits(mouseX, mouseY)):
         playSoundOnly(herses, appLabels[5])
    elif(peanutbutterLabel.hits(mouseX, mouseY)):
         playSoundOnly(peanutButter, appLabels[6])
    elif(boomLabel.hits(mouseX, mouseY)):
         playSoundOnly(boom, appLabels[7])
    elif(laughLabel.hits(mouseX, mouseY)):
         playSoundOnly(laugh, appLabels[8])
         
cmu_graphics.run()