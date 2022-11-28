from cmu_112_graphics import *
from note import Note, Roll
import pygame

class UI:
    def __init__(self, app):
        # NOTE CONSTANTS
        app.don = app.loadImage('image_folder/notes/don.png')
        app.kat = app.loadImage('image_folder/notes/kat.png')
        app.roll = app.loadImage('image_folder/notes/roll.png')
        app.rollEnd = app.loadImage('image_folder/notes/rollEnd.png')
        app.rollLine = app.loadImage('image_folder/notes/rollLine.png')
        app.noteTypes = {'kat', 'don', 'Dkat', 'Ddon', 'roll', 'rollEnd'}
        app.Ddon = app.loadImage('image_folder/notes/Ddon.png')
        app.Dkat = app.loadImage('image_folder/notes/Dkat.png')

        # MUSIC
        pygame.mixer.init()
        app.song = pygame.mixer.music.load('music_folder/charlies_here.mp3')
        app.timerDelay = 10

        # FRAME VARIABLES
        app.frameLeft = 0
        app.frameRight = app.frameLeft + 1280
        app.noteMove = 30
        app.noteQueue = list()

        # TAIKO VARIABLES
        app.taiko = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/taiko.png'))
        app.donRight = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/donLeft.png'))

        # VISUAL VARIABLES
        app.noteDecorum = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/noteDecorum.png'))
        app.indicator = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/indicator.png'))
        app.bottomBackground = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/bottomBackground.png'))
        app.bottomDecorum = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/bottomDecorum.png'))
        app.timeline = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/timeline.png'))
        app.clouds = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/clouds.png'))
        app.cloudsx = 0
        app.topWallpaper = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/topWallpaper.png'))

    def drawNote(self, app, canvas, note, x, end=0):
        if note == 'don':
            canvas.create_image(x, 310, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.don, 68/80)))
        if note == 'kat':
            canvas.create_image(x, 310, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.kat, 68/80)))
        if note == 'Ddon':
            canvas.create_image(x, 295, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Ddon, 96/121)))
        if note == 'Dkat':
            canvas.create_image(x, 295, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Dkat, 96/121)))
        if note == 'roll':
            canvas.create_image(x, 310, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.roll, 68/80)))


    def drawClouds(self, app, canvas, x):
        canvas.create_image(x, 0, anchor=NW, image=app.clouds)

    def drawTimeline(self, app, canvas):
        canvas.create_image(0, 276, anchor=NW, image=app.timeline)

    def drawWallpaper(self, app, canvas):
        canvas.create_image(0, 0, anchor=NW, image=app.topWallpaper)

    def drawBackground(self, app, canvas):
        canvas.create_image(0, 440, anchor=NW, image=app.bottomBackground)

    def drawBottomDecorum(self, app, canvas):
        canvas.create_image(0, 768, anchor=NW, image=app.bottomDecorum)

    def drawIndicator(self, app, canvas):
        canvas.create_image(328, 293, anchor=NW, image=app.indicator)

    def drawNoteDecorum(self, app, canvas):
        canvas.create_image(0, 276, anchor=NW, image=app.noteDecorum)

    def drawTaiko(self, app, canvas):
        canvas.create_image(191, 294, anchor=NW, image=app.taiko)

    def drawDonRight(self, app, canvas):
        canvas.create_image(239, 301, anchor=NW, image=app.donRight)

    def drawLeftDon(self, app, canvas):
        canvas.create_image()
