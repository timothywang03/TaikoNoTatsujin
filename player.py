from note import Note, Roll
from level import Level
from math import floor
import pygame
import time


def player_keyPressed(app, event):
    if event.key == 'f':
        app.keysPressed.add('donLeft')
        if app.rollStart is not None: app.rollCounter += 1
    if event.key == 'j':
        app.keysPressed.add('donRight')
        if app.rollStart is not None: app.rollCounter += 1
    if event.key == 'd':
        app.keysPressed.add('katLeft')
    if event.key == 'k':
        app.keysPressed.add('katRight')
    app.frameLeft += 20

def player_timerFired(app):
    if app.started is False:
        app.started = True
        pygame.mixer.music.play()

    if app.time > app.noteQueue[0]:
        app.noteQueue.pop(0)
        app.currentNote = None

    if app.noteQueue[0].getNoteStart() <= app.time <= app.noteQueue[0]:
        app.currentNote = app.noteQueue[0]

    if app.currentNote.getType() == 'roll':
        app.rollCounter = 0
        app.rollStart = app.time

    if len(app.keysPressed) is not None:
        app.currentNote.hitNote(app.time)
        if app.keysPressed in app.currentNote.getKeys():
            app.currentNote.hitScore(app)
        app.currentNote = None
        app.noteQueue.pop(0)

    app.keysPressed = set()

    app.cloudsx -= 5
    app.topWallpaperx -= 2
    if app.cloudsx <= -1376:
        app.cloudsx += 492
    if app.topWallpaperx <= -1280:
        app.topWallpaperx = -50
    app.frameLeft += 20
    app.time += 10

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
    app.ui.drawScore(app, canvas)
