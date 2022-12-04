# This demos using modes (aka screens).

from cmu_112_graphics import *
import random

##########################################
# Splash Screen Mode
##########################################

def splashScreenMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 150, text='This demos a ModalApp!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 200, text='This is a modal splash screen!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='Press any key for the game!',
                       font=font, fill='black')

def splashScreenMode_keyPressed(app, event):
    app.mode = 'gameMode'

##########################################
# Game Mode
##########################################

def gameMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 20, text=f'Score: {app.score}',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 60, text='Click on the dot!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 100, text='Press h for help screen!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 140, text='Press v for an MVC Violation!',
                       font=font, fill='black')
    canvas.create_oval(app.x-app.r, app.y-app.r, app.x+app.r, app.y+app.r,
                       fill=app.color)
    if app.makeAnMVCViolation:
        app.ohNo = 'This is an MVC Violation!'

def gameMode_timerFired(app):
    moveDot(app)

def gameMode_mousePressed(app, event):
    d = ((app.x - event.x)**2 + (app.y - event.y)**2)**0.5
    if (d <= app.r):
        app.score += 1
        randomizeDot(app)
    elif (app.score > 0):
        app.score -= 1

def gameMode_keyPressed(app, event):
    if (event.key == 'h'):
        app.mode = 'helpMode'
    elif (event.key == 'v'):
        app.makeAnMVCViolation = True

##########################################
# Help Mode
##########################################

def helpMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 150, text='This is the help screen!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 250, text='(Insert helpful message here)',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350, text='Press any key to return to the game!',
                       font=font, fill='black')

def helpMode_keyPressed(app, event):
    app.mode = 'gameMode'

##########################################
# Main App
##########################################

def appStarted(app):
    app.mode = 'splashScreenMode'
    app.score = 0
    app.timerDelay = 50
    app.makeAnMVCViolation = False
    randomizeDot(app)

def randomizeDot(app):
    app.x = random.randint(20, app.width-20)
    app.y = random.randint(20, app.height-20)
    app.r = random.randint(10, 20)
    app.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])
    app.dx = random.choice([+1,-1])*random.randint(3,6)
    app.dy = random.choice([+1,-1])*random.randint(3,6)

def moveDot(app):
    app.x += app.dx
    if (app.x < 0) or (app.x > app.width): app.dx = -app.dx
    app.y += app.dy
    if (app.y < 0) or (app.y > app.height): app.dy = -app.dy

runApp(width=600, height=500)
