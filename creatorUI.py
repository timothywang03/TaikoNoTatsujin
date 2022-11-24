from cmu_112_graphics import *
from note import Note, Roll
import pygame
import time

class UI:
    def __init__(self, app):
        # NOTE CONSTANTS    # CITE IMAGES
        app.don = app.loadImage('image_folder/don.png')
        app.kat = app.loadImage('image_folder/kat.png')
        app.roll = app.loadImage('image_folder/roll.png')
        app.rollEnd = app.loadImage('image_folder/rollEnd.png')
        app.rollLine = app.loadImage('image_folder/rollLine.png')
        app.noteTypes = {'kat', 'don', 'Dkat', 'Ddon', 'roll', 'rollEnd'}
        app.Ddon = app.loadImage('image_folder/Ddon.png')
        app.Dkat = app.loadImage('image_folder/Dkat.png')
        app.hover = None

        # FRAME VISUALS
        app.scrollBar = ImageTk.PhotoImage(app.loadImage('image_folder/scrollBar.png'))
        app.scrollMarker = ImageTk.PhotoImage(app.loadImage('image_folder/scrollMarker.png'))
        app.scrollx = 0   # the default level start position
        app.frameLeft = 0
        app.frameRight = app.frameLeft + 1280
        app.pixelsPerBeat = 60
        app.reached_middle = False
        app.currently_selected = None

        # MUSIC
        app.level.initiateSong(app)
        app.indicator = ImageTk.PhotoImage(app.loadImage('image_folder/playbackIndicator.png'))
        app.indicatorx = 0
        app.timerDelay = 10
        app.musicStarted = False

        # MISCELLANIOUS
        app.noteBar = ImageTk.PhotoImage(app.loadImage('image_folder/noteBar.png'))
        app.noteDecorum = ImageTk.PhotoImage(app.loadImage('image_folder/noteDecorum.png'))
        app.background = app.loadImage('image_folder/creatorBackground.png')
        app.background = ImageTk.PhotoImage(app.scaleImage(app.background, 2.5/2))
        app.errorBox = ImageTk.PhotoImage(app.loadImage('image_folder/errorBox.png'))
        app.errorMessage = ''
        app.playButton = ImageTk.PhotoImage(app.loadImage('image_folder/playButton.png'))

        print(app.level.getBpm() * app.level.getLength() / 60 * app.pixelsPerBeat)

    def drawTimeline(self, app, canvas):
        canvas.create_rectangle(0, 250, 1280, 400, fill='#202020')

    def drawNoteSelection(self, app, canvas):
        canvas.create_image(183, 615, anchor=NW, image=app.noteBar)
        canvas.create_image(243, 658, anchor=NW,image=ImageTk.PhotoImage(app.scaleImage(app.don, 80/44)))
        canvas.create_image(401, 658, anchor=NW,image=ImageTk.PhotoImage(app.scaleImage(app.kat, 80/44)))
        canvas.create_image(559, 658, anchor=NW,image=ImageTk.PhotoImage(app.scaleImage(app.roll, 80/44)))
        canvas.create_image(717, 637, anchor=NW,image=ImageTk.PhotoImage(app.scaleImage(app.Ddon, 121/66)))
        canvas.create_image(916, 637, anchor=NW,image=ImageTk.PhotoImage(app.scaleImage(app.Dkat, 121/66)))

    def drawNote(self, app, canvas, note, x, end=0):
        if note == 'don':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.don, 80/44)))
        if note == 'kat':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.kat, 80/44)))
        if note == 'Ddon':
            canvas.create_image(x, 265, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Ddon, 80/44)))
        if note == 'Dkat':
            canvas.create_image(x, 265, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Dkat, 80/44)))
        if note == 'roll':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.roll, 80/44)))

        if note == 'rollEnd':
            for y in range(int(x + 45), int(end - 90), 10):
                canvas.create_image(y, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.rollLine, 80/44)))
            if end - 44 > x + 44: canvas.create_image(end - 44, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.rollEnd, 80/44)))
            self.drawNote(app, canvas, 'roll', x)
    def drawScrollBar(self, app, canvas):
        canvas.create_image(190, 23, anchor=NW, image=app.scrollBar)

    def drawScrollMarker(self, app, canvas):
        canvas.create_image(190 + app.scrollx, 14, anchor=NW, image=app.scrollMarker)

    def getScrollMarkerX(self, app):
        return app.scrollx

    def calcFrame(self, app):
        app.frameLeft = app.scrollx / 900 * app.level.getBpm() * app.level.getLength() / 60 * app.pixelsPerBeat
        app.frameRight = app.frameLeft + 1280

    def checkOverlap(self, app, x):
        for y in app.level.getNotes().values():
            if y.getNoteStart() <= x <= y.getEnd():
                return True
        return False

    def playback(self, app):
        if app.indicatorx >= app.frameLeft + 640:
            app.reached_middle = True

        if app.reached_middle is False:
            app.indicatorx += 6.5
        else:
            app.scrollx += 0.32028
            self.calcFrame(app)

        if app.scrollx >= 897:
            app.currently_selected = None

    def saveLevel(self, app):
        f = open(f'{app.level.getName()}.txt', 'w')
        f.write(f'Level Name: {app.level.getName()}\n')
        f.write(f'BPM: {app.level.getBpm()}\n')
        f.write(f'Song: {app.level.getSong()}\n')
        f.write(f'Best Score: {app.level.getBestScore()}\n')
        for k, v in app.level.getNotes().items():
            f.write(f'{v.getType()} {v.getNoteStart()} {v.getEnd()}\n')

    def drawErrorBox(self, app, canvas):
        canvas.create_image(183, 429, anchor=NW, image=app.errorBox)

    def drawPlayButton(self, app, canvas):
        canvas.create_image(1151, 14, anchor=NW, image=app.playButton)

    def drawIndicator(self, app, canvas, x):
        canvas.create_image(x, 250, anchor=NW, image=app.indicator)

    def setBackground(self, app, file):
        app.background = app.loadImage(file)
        app.background = ImageTk.PhotoImage(app.scaleImage(app.background, 2.5/2))

    def drawBackground(self, app, canvas):
        canvas.create_image(0, 0, anchor=NW, image=app.background)
