from cmu_112_graphics import *
import levelCreator
from creatorUI import UI
import pygame
from note import Don, Kat, DDon, DKat, Roll


def appStarted(app):
    app.width = app.width
    app.height = app.height
    app.screen = 'creator'
    if app.screen == 'creator':
        app.ui = UI(app)
        app.currently_selected = None
        app.scrollPos = 0
    app.level = None

def mousePressed(app, event):
    if app.currently_selected is None:
        if 243 <= event.x <= 323 and 658 <= event.y <= 738:
            app.currently_selected = 'don'
        if 401 <= event.x <= 481 and 658 <= event.y <= 738:
            app.currently_selected = 'kat'
        if 559 <= event.x <= 639 and 658 <= event.y <= 738:
            app.currently_selected = 'roll'
        if 717 <= event.x <= 838 and 637 <= event.y <= 758:
            app.currently_selected = 'Ddon'
        if 916 <= event.x <= 1037 and 637 <= event.y <= 758:
            app.currently_selected = 'Dkat'

def mouseMoved(app, event):
    if app.currently_selected is not None:
        if 250 <= event.y <= 441:
            app.ui.drawNote(app, app.currently_selected)

def redrawAll(app, canvas):
    levelCreator.drawCreatorUI(app, canvas)

runApp(width=1280, height=800)
