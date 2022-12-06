from note import Note, Roll
from level import Level
from math import floor
import pygame
import time


def player_keyPressed(app, event):
    if event.key == 'f':
        app.keysPressed.add('f')
        if app.currentNote is not None and app.currentNote.getType() == 'roll':
            app.rollCounter += 1
    if event.key == 'j':
        app.keysPressed.add('j')
        if app.currentNote is not None and app.currentNote.getType() == 'roll':
            app.rollCounter += 1
    if event.key == 'd':
        app.keysPressed.add('d')
    if event.key == 'k':
        app.keysPressed.add('k')
    app.frameLeft += 10


def player_timerFired(app):
    if app.started is False:
        app.started = True
        pygame.mixer.music.play()

    if len(app.noteQueue) > 0:
        if app.indicatorx > app.noteQueue[0].getEnd() - app.frameLeft:
            app.noteQueue.pop(0)
            app.currentNote = None
            app.rollStarted = False

    if len(app.noteQueue) > 0:
        if app.noteQueue[0].getNoteStart() - app.frameLeft <= app.indicatorx <= app.noteQueue[0].getEnd() - app.frameLeft:
            app.currentNote = app.noteQueue[0]
            if app.currentNote.getType() == 'roll' and app.rollStarted is False:
                app.rollStarted = True
                app.rollCounter = 0

        if app.currentNote is not None:
            if len(app.keysPressed) != 0:
                if app.currentNote.getType() != 'roll':
                    app.currentNote.hitNote(app.indicatorx)
                    if app.keysPressed in app.currentNote.getKeys():
                        hit = app.currentNote.hitScore(app)
                        app.score += hit
                        app.streak += 1
                    else:
                        app.streak = 0
                    app.currentNote = None
                else:
                    app.score += app.currentNote.hitScore(app)

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
            app.ui.drawNote(app, canvas, note.getType(), timestamp -
                            app.frameLeft, note.getEnd() - app.frameLeft)
            if note.getType() == 'roll':
                app.ui.drawNote(app, canvas, 'rollEnd', timestamp -
                                app.frameLeft, note.getEnd() - app.frameLeft)

    app.ui.drawNoteDecorum(app, canvas)
    app.ui.drawScoreBar(app, canvas)
    app.ui.drawTaiko(app, canvas)

    for x in app.keysPressed:
        if x == 'donLeft':
            app.ui.drawDonLeft(app, canvas)
        if x == 'donRight':
            app.ui.drawDonRight(app, canvas)
        if x == 'katLeft':
            app.ui.drawKatLeft(app, canvas)
        if x == 'katRight':
            app.ui.drawKatRight(app, canvas)

    app.ui.drawDifficulty(app, canvas)
    app.ui.drawScore(app, canvas)
    if app.streak >= 10:
        app.ui.drawCombo(app, canvas)
    if app.currentNote is not None and app.currentNote.getType() == 'roll':
        app.ui.drawRollFan(app, canvas)
