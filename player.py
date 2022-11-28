from note import Note, Roll
from level import Level
from math import floor
import pygame
import time


def player_keyPressed(app, event):
    if event.key == 'f':
        app.keysPressed.add('donLeft')
    if event.key == 'j':
        app.keysPressed.add('donRight')
    if event.key == 'd':
        app.keysPressed.add('katLeft')
    if event.key == 'k':
        app.keysPressed.add('katRight')
    app.frameLeft += 20

def player_timerFired(app):
    app.keysPressed = set()
    app.cloudsx -= 5
    app.topWallpaperx -= 10
    if app.cloudsx <= -1376:
        app.cloudsx += 492
    if app.topWallpaperx <= -1280:
        app.topWallpaperx = -50
    app.frameLeft += 20

def player_redrawAll(app, canvas):
    app.ui.drawBackground(app, canvas)
    app.ui.drawBottomDecorum(app, canvas)
    app.ui.drawWallpaper(app, canvas, app.topWallpaperx)
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
    app.ui.drawScoreBar(app, canvas)
    app.ui.drawTaiko(app, canvas)

    for x in app.keysPressed:
        if x == 'donLeft': app.ui.drawDonLeft(app, canvas)
        if x == 'donRight': app.ui.drawDonRight(app, canvas)
        if x == 'katLeft': app.ui.drawKatLeft(app, canvas)
        if x == 'katRight': app.ui.drawKatRight(app, canvas)

    app.ui.drawDifficulty(app, canvas)
