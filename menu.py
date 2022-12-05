from cmu_112_graphics import *
from level import Level
import creatorUI
import playerUI
import twoPlayerUI

def menu_mousePressed(app, event):
    if app.loadScreen is True:
        if 384 <= event.x <= 496 and 394 <= event.y <= 506:
            app.diffSelected = 'easy'
        if 584 <= event.x <= 696 and 394 <= event.y <= 506:
            app.diffSelected = 'normal'
        if 784 <= event.x <= 896 and 394 <= event.y <= 506:
            app.diffSelected = 'hard'
        if 394 <= event.x <= 885 and 317 <= event.y <= 377:
            app.levelEntered = app.getUserInput('')
        if 548 <= event.x <= 732 and 520 <= event.y <= 577:
            if app.clicked == 'creator':
                if app.diffSelected is not None and app.levelEntered is not None:
                    app.level = Level(app.levelEntered, dict(), 34, 130, 'yoru_ni_kakeru.mp3', app.diffSelected)
                    app.level.loadNotes()
                    app.ui = creatorUI.UI(app)
                    app.mode = 'creator'
            if app.clicked == 'player':
                if app.diffSelected is not None and app.levelEntered is not None:

                    # make sure the level selected exists
                    try:
                        app.level = Level(app.levelEntered, dict(), 34, 130, 'yoru_ni_kakeru.mp3', app.diffSelected)
                        app.level.loadNotes()
                        app.ui = playerUI.UI(app)
                        app.level.initiateSong(app)
                        app.mode = 'player'
                    except:
                        app.errorDraw = True
            if app.clicked == 'twoPlayer':
                if app.diffSelected is not None and app.levelEntered is not None:
                    try:
                        app.level = Level(app.levelEntered, dict(), 34, 130, 'yoru_ni_kakeru.mp3', app.diffSelected)
                        app.level.loadNotes()
                        app.ui = twoPlayer.UI(app)
                        app.level.initiateSong(app)
                        app.mode = 'twoPlayer'
                    except:
                        app.errorDraw = True

    if 733 <= event.x <= 1133 and 150 <= event.y <= 250:
        app.loadScreen = True
        app.clicked = 'creator'
    if 733 <= event.x <= 1133 and 350 <= event.y <= 450:
        app.loadScreen = True
        app.clicked = 'player'
    if 733 <= event.x <= 1133 and 550 <= event.y <= 650:
        app.loadScreen = True
        app.clicked = 'twoPlayer'

def menu_redrawAll(app, canvas):
    app.ui.drawMenuBackground(app, canvas)
    if app.loadScreen is True:
        app.ui.drawLoadLevel(app, canvas)
        if app.diffSelected == 'easy':
            app.ui.drawSelection(app, canvas, 376)
        if app.diffSelected == 'normal':
            app.ui.drawSelection(app, canvas, 576)
        if app.diffSelected == 'hard':
            app.ui.drawSelection(app, canvas, 776)
        app.ui.drawDifficulties(app, canvas)
    if app.levelEntered is not None:
        canvas.create_text(640, 340, text=app.levelEntered, font='Arial 36')
    if app.errorDraw is True:
        app.ui.drawError(app, canvas)
