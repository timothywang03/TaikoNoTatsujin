from note import Note, Roll
from level import Level
from math import floor
import pygame
import time


def player_keyPressed(app, event):
    pass

def player_timerFired(app):
    app.frameLeft += 20

def player_redrawAll(app, canvas):
    app.ui.drawBackground(app, canvas)
    app.ui.drawBottomDecorum(app, canvas)
    app.ui.drawWallpaper(app, canvas)
    app.ui.drawClouds(app, canvas, app.cloudsx)
    app.ui.drawTimeline(app, canvas)
    app.ui.drawIndicator(app, canvas)

    for timestamp in sorted(app.level.getNotes(), reverse=True):
        note = app.level.getNotes()[timestamp]
        if note.getHit() is False:
            app.ui.drawNote(app, canvas, note.getType(), timestamp - app.frameLeft, note.getEnd() - app.frameLeft)
            if note.getType() == 'roll':
                app.ui.drawNote(app, canvas, 'rollEnd', timestamp - app.frameLeft, note.getEnd() - app.frameLeft)

    app.ui.drawNoteDecorum(app, canvas)
    app.ui.drawTaiko(app, canvas)
