from note import Note, Roll, PlayerOneNote, PlayerTwoNote
from level import Level
from math import floor
import pygame
import time


def twoPlayer_keyPressed(app, event):
    if event.key == 's':
        app.topKeysPressed.add('s')
        if app.topCurrentNote is not None and app.topCurrentNote.getType() == 'roll':
            app.topRollCounter += 1
    if event.key == 'd':
        app.topKeysPressed.add('d')
        if app.topCurrentNote is not None and app.topCurrentNote.getType() == 'roll':
            app.topRollCounter += 1
    if event.key == 'a':
        app.topKeysPressed.add('a')
    if event.key == 'f':
        app.topKeysPressed.add('f')

    if event.key == 'j':
        app.botKeysPressed.add('j')
        if app.botCurrentNote is not None and app.botCurrentNote.getType() == 'roll':
            app.botRollCounter += 1
    if event.key == 'k':
        app.botKeysPressed.add('k')
        if app.botCurrentNote is not None and app.botCurrentNote.getType() == 'roll':
            app.botRollCounter += 1
    if event.key == 'h':
        app.botKeysPressed.add('h')
    if event.key == 'l':
        app.botKeysPressed.add('l')

    app.frameLeft += 10


def twoPlayer_timerFired(app):

    # if the level started playing
    if app.started is False:
        app.started = True
        pygame.mixer.music.play()

    # run as long as there are still notes left
    if len(app.topNoteQueue) > 0:
        if app.indicatorx > app.topNoteQueue[0].getEnd() - app.frameLeft:
            app.topNoteQueue.pop(0)
            app.topCurrentNote = None
            app.rollStarted = False
            app.topRollCounter = 0

    if len(app.botNoteQueue) > 0:
        if app.indicatorx > app.botNoteQueue[0].getEnd() - app.frameLeft:
            app.botNoteQueue.pop(0)
            app.botCurrentNote = None
            app.rollStarted = False
            app.botRollCounter = 0

    # score the current note and hit it moving it on
    if len(app.topNoteQueue) > 0:
        if app.topNoteQueue[0].getNoteStart() - app.frameLeft <= app.indicatorx <= app.topNoteQueue[0].getEnd() - app.frameLeft:
            app.topCurrentNote = app.topNoteQueue[0]
            if app.topCurrentNote.getType() == 'roll' and app.rollStarted is False:
                app.rollStarted = True

        if app.topCurrentNote is not None:
            if len(app.topKeysPressed) != 0:
                if app.topCurrentNote.getType() != 'roll':
                    app.topCurrentNote.hitNote(app.indicatorx)
                    if app.topKeysPressed in app.topCurrentNote.getKeys():
                        hit = app.topCurrentNote.hitScore(app)
                        app.topScore += hit
                        app.topStreak += 1
                    else:
                        app.topStreak = 0
                    app.topCurrentNote = None
                else:
                    app.topScore += app.topCurrentNote.hitScore(app)

    if len(app.botNoteQueue) > 0:
        if app.botNoteQueue[0].getNoteStart() - app.frameLeft <= app.indicatorx <= app.botNoteQueue[0].getEnd() - app.frameLeft:
            app.botCurrentNote = app.botNoteQueue[0]
            if app.botCurrentNote.getType() == 'roll' and app.rollStarted is False:
                app.rollStarted = True

        if app.botCurrentNote is not None:
            if len(app.botKeysPressed) != 0:
                if app.botCurrentNote.getType() != 'roll':
                    app.botCurrentNote.hitNote(app.indicatorx)
                    if app.botKeysPressed in app.botCurrentNote.getKeys():
                        hit = app.botCurrentNote.hitScore(app)
                        app.botScore += hit
                        app.botStreak += 1
                    else:
                        app.botStreak = 0
                    app.botCurrentNote = None
                else:
                    app.botScore += app.botCurrentNote.hitScore(app)

        app.topKeysPressed = set()
        app.botKeysPressed = set()

        # shift the decorum
        app.topDecorumx -= 5
        app.botDecorumx -= 5
        app.topWallpaperx -= 2
        app.botWallpaperx -= 2
        if app.topDecorumx <= -1376:
            app.topDecorumx += 492
        if app.botDecorumx <= -1376:
            app.botDecorumx += 492
        if app.topWallpaperx <= -1280:
            app.topWallpaperx = -50
        if app.botWallpaperx <= -1280:
            app.topWallpaperx = -50
        app.frameLeft += 20
        app.time += 10


def twoPlayer_redrawAll(app, canvas):
    app.ui.drawTopWallpaper(app, canvas, app.topWallpaperx)
    app.ui.drawTopDecorum(app, canvas, app.topDecorumx)
    app.ui.drawTopTimeline(app, canvas)

    app.ui.drawBotWallpaper(app, canvas, app.botWallpaperx)
    app.ui.drawBotDecorum(app, canvas, app.botDecorumx)
    app.ui.drawBotTimeline(app, canvas)

    for timestamp in sorted(app.level.getNotes(), reverse=True):
        topNote = app.topNotes[timestamp]
        botNote = app.botNotes[timestamp]
        if topNote.getHit() is False:
            app.ui.drawTopNote(app, canvas, topNote.getType(
            ), timestamp - app.frameLeft, topNote.getEnd() - app.frameLeft)
            if topNote.getType() == 'roll':
                app.ui.drawTopNote(app, canvas, 'rollEnd', timestamp -
                                   app.frameLeft, topNote.getEnd() - app.frameLeft)

        if botNote.getHit() is False:
            app.ui.drawBotNote(app, canvas, botNote.getType(
            ), timestamp - app.frameLeft, botNote.getEnd() - app.frameLeft)
            if botNote.getType() == 'roll':
                app.ui.drawBotNote(app, canvas, 'rollEnd', timestamp -
                                   app.frameLeft, botNote.getEnd() - app.frameLeft)

    for x in app.topKeysPressed:
        if x == 'donLeft':
            app.ui.drawTopDonLeft(app, canvas)
        if x == 'donRight':
            app.ui.drawTopDonRight(app, canvas)
        if x == 'katLeft':
            app.ui.drawTopKatLeft(app, canvas)
        if x == 'katRight':
            app.ui.drawBotKatRight(app, canvas)

    for x in app.botKeysPressed:
        if x == 'donLeft':
            app.ui.drawBotDonLeft(app, canvas)
        if x == 'donRight':
            app.ui.drawBotDonRight(app, canvas)
        if x == 'katLeft':
            app.ui.drawBotKatLeft(app, canvas)
        if x == 'katRight':
            app.ui.drawBotKatRight(app, canvas)

    app.ui.drawTopNoteDecorum(app, canvas)
    app.ui.drawBotNoteDecorum(app, canvas)

    #app.ui.drawDifficulty(app, canvas)
    app.ui.drawTopScore(app, canvas)
    app.ui.drawBotScore(app, canvas)
    if app.topStreak >= 10:
        app.ui.drawTopCombo(app, canvas)
    if app.botStreak >= 10:
        app.ui.drawBotCombo(app, canvas)
    if app.topCurrentNote is not None and app.topCurrentNote.getType() == 'roll':
        app.ui.drawTopRollFan(app, canvas)
        app.ui.drawBotRollFan(app, canvas)
