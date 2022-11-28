from cmu_112_graphics import *
from note import Note, Roll
import pygame
import time

class UI:
    def __init__(self, app):

        # NOTE CONSTANTS    # CITE IMAGES
        app.don = app.loadImage('image_folder/notes/don.png')
        app.kat = app.loadImage('image_folder/notes/kat.png')
        app.roll = app.loadImage('image_folder/notes/roll.png')
        app.rollEnd = app.loadImage('image_folder/notes/rollEnd.png')
        app.rollLine = app.loadImage('image_folder/notes/rollLine.png')
        app.noteTypes = {'kat', 'don', 'Dkat', 'Ddon', 'roll', 'rollEnd'}
        app.Ddon = app.loadImage('image_folder/notes/Ddon.png')
        app.Dkat = app.loadImage('image_folder/notes/Dkat.png')
        app.hover = None

        # FRAME VISUALS
        app.scrollBar = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/scrollBar.png'))
        app.scrollMarker = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/scrollMarker.png'))
        app.scrollx = 0   # the default level start position
        app.frameLeft = 0
        app.frameRight = app.frameLeft + 1280
        app.pixelsPerBeat = 90
        app.reached_middle = False
        app.currently_selected = None
        app.beatLine = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/beatLine.png'))

        # MUSIC
        app.level.initiateSong(app)
        app.indicator = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/playbackIndicator.png'))
        app.indicatorx = 0
        app.timerDelay = 10
        app.musicStarted = False

        # ERROR MESSAGES
        app.directions = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/directions.png'))
        app.overlapError = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/overlapError.png'))
        app.playbackError = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/playbackError.png'))
        app.error = None

        # MISCELLANIOUS
        app.noteBar = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/noteBar.png'))
        app.background = app.loadImage('image_folder/creatorUI/creatorBackground.png')
        app.background = ImageTk.PhotoImage(app.scaleImage(app.background, 2.5/2))
        app.errorBox = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/errorBox.png'))
        app.errorMessage = ''
        app.playButton = ImageTk.PhotoImage(app.loadImage('image_folder/creatorUI/playButton.png'))


    def drawTimeline(self, app, canvas):
        canvas.create_rectangle(0, 250, 1280, 400, fill='#383838')

    def drawNoteSelection(self, app, canvas):
        canvas.create_image(183, 615, anchor=NW, image=app.noteBar)
        canvas.create_image(243, 658, anchor=NW,image=ImageTk.PhotoImage(app.don))
        canvas.create_image(401, 658, anchor=NW,image=ImageTk.PhotoImage(app.kat))
        canvas.create_image(559, 658, anchor=NW,image=ImageTk.PhotoImage(app.roll))
        canvas.create_image(717, 637, anchor=NW,image=ImageTk.PhotoImage(app.Ddon))
        canvas.create_image(916, 637, anchor=NW,image=ImageTk.PhotoImage(app.Dkat))

    def drawNote(self, app, canvas, note, x, end=0):
        if note == 'don':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.don))
        if note == 'kat':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.kat))
        if note == 'Ddon':
            canvas.create_image(x, 265, anchor=NW, image=ImageTk.PhotoImage(app.Ddon))
        if note == 'Dkat':
            canvas.create_image(x, 265, anchor=NW, image=ImageTk.PhotoImage(app.Dkat))
        if note == 'roll':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.roll))

        if note == 'rollEnd':
            for y in range(int(x + 44), int(end - 90), 10):
                canvas.create_image(y, 285, anchor=NW, image=ImageTk.PhotoImage(app.rollLine))
            if end - 80 > x + 80: canvas.create_image(end - 80, 285, anchor=NW, image=ImageTk.PhotoImage(app.rollEnd))
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
            if y.getType() == 'roll' or y.getType() == 'rollEnd':
                if y.getNoteStart() <= x <= y.getEnd():
                    return True
        return False

    def playback(self, app):
        if app.indicatorx >= app.frameLeft + 640:
            app.reached_middle = True

        if app.reached_middle is True:
            app.scrollx += (1/600) / (app.level.getLength() / 60) * 900
            self.calcFrame(app)
        app.indicatorx += app.level.getBpm() / 600 * app.pixelsPerBeat

        if app.scrollx >= 897:
            app.currently_selected = None

    def drawErrorBox(self, app, canvas):
        canvas.create_image(183, 429, anchor=NW, image=app.errorBox)

    def drawError(self, app, canvas, error):
        if error == 'overlap':
            canvas.create_image(388, 444, anchor=NW, image=app.overlapError)
        elif error == 'playback':
            canvas.create_image(368, 476, anchor=NW, image=app.playbackError)
        else:
            canvas.create_image(221, 450, anchor=NW, image=app.directions)

    def drawPlayButton(self, app, canvas):
        canvas.create_image(1151, 14, anchor=NW, image=app.playButton)

    def drawIndicator(self, app, canvas):
        canvas.create_image(app.indicatorx - app.frameLeft, 246, anchor=NW, image=app.indicator)

    def drawBeatlines(self, app, canvas):
        for x in range(0, int(app.level.getBpm() * app.level.getLength() / 60) * app.pixelsPerBeat, app.pixelsPerBeat * 4):
            canvas.create_image(x - app.frameLeft, 250, anchor=NW, image=app.beatLine)

    def setBackground(self, app, file):
        app.background = app.loadImage(file)
        app.background = ImageTk.PhotoImage(app.scaleImage(app.background, 2.5/2))

    def drawBackground(self, app, canvas):
        canvas.create_image(0, 0, anchor=NW, image=app.background)
