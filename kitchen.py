from cmu_graphics import * 
# A Modern Kitchen! 
  
app.background = 'gainsboro'
Rect(0, 300, 400, 100, fill = 'lightGrey')
    
# Cabinets and Drawers + Local Variable <-
color = 'gray'
Rect(0, 0, 150, 300, fill = color)
Rect(150, 210, 250, 90, fill = color) 
Rect(150, 210, 250, 10, fill = 'burlywood')
Line(60, 140, 60, 180)
Line(80, 140, 80, 180)

# For Loops <- 
for i in range(3):
    cy = 234 + 20 * i
    Line(180, cy, 200, cy)
    Line(263, cy, 283, cy)
    Line(346, cy, 366, cy)

# Kitchen Island 
Rect(80, 268, 250, 90, fill = 'darkGrey')
Rect(80, 258, 250, 10, fill = 'burlywood')
Rect(90,280, 230, 77, fill = 'gray')
Rect(95, 0, 210, 10, fill = 'darkGrey')

# Group, Looping Through Groups, Arcs <-
lights = Group(
    Arc(100, 130, 50, 50, 270, 180, fill = 'black'),
    Arc(150, 180, 50, 50, 270, 180, fill = 'darkSlateGrey'),
    Arc(200, 130, 50, 50, 270, 180, fill = 'black'),
    Arc(250, 180, 50, 50, 270, 180, fill = 'darkSlateGrey'),
    Arc(300, 130, 50, 50, 270, 180, fill = 'black'),
    )
for light in lights.children:
    Line(light.centerX, 10, light.centerX, light.top)
    
# Chairs 
Line(110, 300, 170, 300, lineWidth = 5)
Line(128, 300, 116, 359, lineWidth = 5)
Line(148, 300, 160, 359, lineWidth = 5)

Line(223, 300, 283, 300, lineWidth = 5)
Line(241, 300, 229, 359, lineWidth = 5)
Line(261, 300, 273, 359, lineWidth = 5)

cmu_graphics.run()
