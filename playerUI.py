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
        app.timerDelay = 10
        app.started = False

        # KEY PRESS
        app.keysPressed = set()

        # FRAME VARIABLES
        app.frameLeft = 0
        app.frameRight = app.frameLeft + 1280
        app.pixelsPerBeat = 90

        # SCORING VARIABLES
        app.score = 0
        app.streak = 0
        app.combo = app.loadImage('image_folder/playerUI/combo.png')
        app.one = app.loadImage('image_folder/numbers/1.png')
        app.two = app.loadImage('image_folder/numbers/2.png')
        app.three = app.loadImage('image_folder/numbers/3.png')
        app.four = app.loadImage('image_folder/numbers/4.png')
        app.five = app.loadImage('image_folder/numbers/5.png')
        app.six = app.loadImage('image_folder/numbers/6.png')
        app.seven = app.loadImage('image_folder/numbers/7.png')
        app.eight = app.loadImage('image_folder/numbers/8.png')
        app.nine = app.loadImage('image_folder/numbers/9.png')
        app.zero = app.loadImage('image_folder/numbers/0.png')
        app.numbers = {1: app.one, 2: app.two, 3: app.three, 4: app.four, \
        5: app.five, 6: app.six, 7: app.seven, 8: app.eight, 9: app.nine, \
        0: app.zero}

        # TAIKO VARIABLES
        app.taiko = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/taiko.png'))
        app.donRight = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/donRight.png'))
        app.donLeft = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/donLeft.png'))
        app.katLeft = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/katLeft.png'))
        app.katRight = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/katRight.png'))

        # VISUAL VARIABLES
        app.noteDecorum = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/noteDecorum.png'))
        app.indicator = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/indicator.png'))
        app.bottomBackground = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/bottomBackground.png'))
        app.bottomDecorum = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/bottomDecorum.png'))
        app.timeline = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/timeline.png'))
        app.clouds = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/clouds.png'))
        app.cloudsx = 0
        app.topWallpaper = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/topWallpaper.png'))
        app.topWallpaperx = 0
        app.scoreBar = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/scoreBar.png'))
        app.difficultyEasy = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/easy.png'))
        app.difficultyNormal = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/normal.png'))
        app.difficultyHard = ImageTk.PhotoImage(app.loadImage('image_folder/playerUI/hard.png'))

    def scoreAdd(self, app, note):
        if note.getType() == 'roll':
            app.score += 100 * note.getRollScore()
        else:
            if app.streak < 10:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    app.score += 1720
                if note.getType() == 'don' or note.getType() == 'kat':
                    app.score += 860
            elif app.streak >= 10:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    app.score += 2160
                if note.getType() == 'don' or note.getType() == 'kat':
                    app.score += 1080
            elif app.streak >= 30:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    app.score += 2712
                if note.getType() == 'don' or note.getType() == 'kat':
                    app.score += 1300
            else:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    app.score += 3480
                if note.getType() == 'don' or note.getType() == 'kat':
                    app.score += 1740

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
        if note == 'rollEnd':
            for y in range(int(x + 44), int(end - 90), 10):
                canvas.create_image(y, 310, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.rollLine, 68/80)))
            if end - 80 > x + 80: canvas.create_image(end - 80, 310, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.rollEnd, 68/80)))
            self.drawNote(app, canvas, 'roll', x)

    def drawClouds(self, app, canvas, x):
        canvas.create_image(x, 0, anchor=NW, image=app.clouds)

    def drawTimeline(self, app, canvas):
        canvas.create_image(0, 276, anchor=NW, image=app.timeline)

    def drawWallpaper(self, app, canvas, x):
        canvas.create_image(x, 0, anchor=NW, image=app.topWallpaper)

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
        canvas.create_image(237, 301, anchor=NW, image=app.donRight)

    def drawDonLeft(self, app, canvas):
        canvas.create_image(204, 301, anchor=NW, image=app.donLeft)

    def drawKatLeft(self, app, canvas):
        canvas.create_image(190, 290, anchor=NW, image=app.katLeft)

    def drawKatRight(self, app, canvas):
        canvas.create_image(240, 290, anchor=NW, image=app.katRight)

    def drawScoreBar(self, app, canvas):
        canvas.create_image(25, 384, anchor=NW, image=app.scoreBar)

    def drawScore(self, app, canvas):
        if app.score >= 10000:
            canvas.create_image(62, 390, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.numbers[app.score // 10000 % 10], 35/57)))
        if app.score >= 1000:
            canvas.create_image(89, 390, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.numbers[app.score // 1000 % 10], 35/57)))
        if app.score >= 100:
            canvas.create_image(116, 390, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.numbers[app.score // 100 % 10], 35/57)))
        if app.score >= 10:
            canvas.create_image(144, 390, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.numbers[app.score // 10 % 10], 35/57)))
        canvas.create_image(170, 390, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.numbers[app.score % 10], 35/57)))

    def drawCombo(self, app, canvas, num):
        if num > 9:
            canvas.create_image(203, 303, anchor=NW, image=app.numbers[num//10%10])
        canvas.create_image(244, 303, anchor=NW, image=app.numbers[num%10])
        canvas.create_image(225, 360, anchor=NW, image=app.combo)

    def drawDifficulty(self, app, canvas):
        if app.level.getDifficulty() == 'easy':
            canvas.create_image(24, 286, anchor=NW, image=app.difficultyEasy)
        elif app.level.getDifficulty() == 'normal':
            canvas.create_image(24, 286, anchor=NW, image=app.difficultyNormal)
        else:
            canvas.create_image(24, 286, anchor=NW, image=app.difficultyHard)
