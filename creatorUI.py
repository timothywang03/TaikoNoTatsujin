from cmu_112_graphics import *
from note import Note, Roll

class UI:
    def __init__(self, app):
        # NOTE CONSTANTS
        app.don = app.loadImage('image_folder/don.png')
        app.kat = app.loadImage('image_folder/kat.png')
        app.roll = app.loadImage('image_folder/roll.png')
        app.rollEnd = app.loadImage('image_folder/rollEnd.png')
        app.rollLine = app.loadImage('image_folder/rollLine.png')
        app.noteTypes = {'kat', 'don', 'Dkat', 'Ddon', 'roll'}
        app.Ddon = app.loadImage('image_folder/Ddon.png')
        app.Dkat = app.loadImage('image_folder/Dkat.png')
        app.hover = None

        # SCROLL BAR
        app.scrollBar = ImageTk.PhotoImage(app.loadImage('image_folder/scrollBar.png'))
        app.scrollMarker = ImageTk.PhotoImage(app.loadImage('image_folder/scrollMarker.png'))
        app.scrollx = 0   # the default level start position
        app.scrollConstant = 5

        # MISCELLANIOUS
        app.noteBar = ImageTk.PhotoImage(app.loadImage('image_folder/noteBar.png'))
        app.noteDecorum = ImageTk.PhotoImage(app.loadImage('image_folder/noteDecorum.png'))
        app.background = app.loadImage('image_folder/creatorBackground.png')
        app.background = ImageTk.PhotoImage(app.scaleImage(app.background, 2.5/2))

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
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Ddon, 80/44)))
        if note == 'Dkat':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Dkat, 80/44)))
        if note == 'roll':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.roll, 80/44)))
        if note == 'rollEnd':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.rollEnd, 80/44)))

    def drawScrollBar(self, app, canvas):
        canvas.create_image(190 + app.scrollx, 23, anchor=NW, image=app.scrollBar)

    def drawScrollMarker(self, app, canvas):
        canvas.create_image(app.scrollx, 14, anchor=NW, image=app.scrollMarker)

    def getScrollMarkerX(self, app):
        return app.scrollx

    def drawNoteDecorum(self, app, canvas):
        canvas.create_image(0, 250, anchor=NW, image=app.noteDecorum)

    def setBackground(self, app, file):
        app.background = app.loadImage(file)
        app.background = ImageTk.PhotoImage(app.scaleImage(app.background, 2.5/2))

    def drawBackground(self, app, canvas):
        canvas.create_image(0, 0, anchor=NW, image=app.background)
