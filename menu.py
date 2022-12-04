# This demos app.getUserInput(prompt) and app.showMessage(message)

from cmu_112_graphics import *

def appStarted(app):
    app.message = 'Click the mouse to enter your name!'

def mousePressed(app, event):
    name = app.getUserInput('What is your name?')
    if (name == None):
        app.message = 'You canceled!'
    else:
        app.showMessage('You entered: ' + name)
        app.message = f'Hi, {name}!'

def redrawAll(app, canvas):
    font = 'Arial 24 bold'
    canvas.create_text(app.width/2,  app.height/2,
                       text=app.message, font=font, fill='black')

runApp(width=500, height=300)
