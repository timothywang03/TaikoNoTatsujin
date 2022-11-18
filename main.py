from cmu_112_graphics import *

def appStarted(app):
    app.width = app.width
    app.height = app.height
    app.background = app.loadImage('image_folder/level_background.png')
    app.background = app.scaleImage(app.background, 2.5/2)

def mousePressed(app, event):
    

def redrawAll(app, canvas):
    canvas.create_image(640, 400, image=ImageTk.PhotoImage(app.background))

runApp(width=1280, height=800)
