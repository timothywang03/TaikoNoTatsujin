from cmu_112_graphics import *
from note import Note, Roll, PlayerOneNote, PlayerTwoNote
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
        app.topNotes = dict()
        app.botNotes = dict()
        for k, note in app.level.getNotes().items():
            app.topNotes[note.getNoteStart()] = PlayerOneNote(
                note.getType(), app.level, note.getNoteStart(), note.getEnd())
            app.botNotes[note.getNoteStart()] = PlayerTwoNote(
                note.getType(), app.level, note.getNoteStart(), note.getEnd())

        # MUSIC
        pygame.mixer.init()
        app.timerDelay = 30
        app.started = False

        # FRAME VARIABLES
        app.frameLeft = 0
        app.frameRight = app.frameLeft + 1280
        app.pixelsPerBeat = 90
        app.time = 0

        # GAMEPLAY VARIABLES
        app.topKeysPressed = set()
        app.botKeysPressed = set()
        app.rollStart = None
        app.topRollCounter = 0
        app.botRollCounter = 0
        app.topNoteQueue = list()
        app.botNoteQueue = list()
        for timestamp in sorted(app.topNotes):
            note = app.topNotes[timestamp]
            app.topNoteQueue.append(note)
        for timestamp in sorted(app.botNotes):
            note = app.botNotes[timestamp]
            app.botNoteQueue.append(note)
        app.topCurrentNote = None
        app.botCurrentNote = None

        # SCORING VARIABLES
        app.topScore = 0
        app.botScore = 0
        app.topStreak = 0
        app.botStreak = 0
        app.rollStarted = False
        app.combo = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/combo.png'))
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
        app.numbers = {1: app.one, 2: app.two, 3: app.three, 4: app.four,
                       5: app.five, 6: app.six, 7: app.seven, 8: app.eight, 9: app.nine,
                       0: app.zero}

        # TAIKO VARIABLES
        app.taiko = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/taiko.png'))
        app.donRight = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/donRight.png'))
        app.donLeft = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/donLeft.png'))
        app.katLeft = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/katLeft.png'))
        app.katRight = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/katRight.png'))

        # VISUAL VARIABLES
        app.indicatorx = 363
        app.bottomBackground = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/wallpaper2.png'))
        app.bottomDecorum = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/hexagon2.png'))
        app.timeline = ImageTk.PhotoImage(app.loadImage(
            'image_folder/twoPlayerUI/noteLane.png'))
        app.noteDecorum1 = ImageTk.PhotoImage(app.loadImage(
            'image_folder/twoPlayerUI/noteDecorum1.png'))
        app.noteDecorum2 = ImageTk.PhotoImage(app.loadImage(
            'image_folder/twoPlayerUI/noteDecorum2.png'))
        app.topWallpaper = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/wallpaper1.png'))
        app.topDecorum = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/hexagon1.png'))
        app.topDecorumx = 0
        app.topWallpaperx = 0
        app.topNoteDecorum = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/noteDecorum1.png'))
        app.botWallpaper = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/wallpaper2.png'))
        app.botDecorum = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/hexagon2.png'))
        app.botNoteDecorum = ImageTk.PhotoImage(
            app.loadImage('image_folder/twoPlayerUI/noteDecorum2.png'))
        app.botDecorumx = 0
        app.botWallpaperx = 0
        app.difficultyEasy = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/easy.png'))
        app.difficultyNormal = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/normal.png'))
        app.difficultyHard = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/hard.png'))
        app.rollFan = ImageTk.PhotoImage(
            app.loadImage('image_folder/playerUI/Fan.png'))

    def drawTopNote(self, app, canvas, note, x, end=0):
        if note == 'don':
            canvas.create_image(x, 268, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.don, 68 / 80)))
        if note == 'kat':
            canvas.create_image(x, 268, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.kat, 68 / 80)))
        if note == 'Ddon':
            canvas.create_image(x, 253, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.Ddon, 96 / 121)))
        if note == 'Dkat':
            canvas.create_image(x, 253, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.Dkat, 96 / 121)))
        if note == 'roll':
            canvas.create_image(x, 268, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.roll, 68 / 80)))
        if note == 'rollEnd':
            for y in range(int(x + 44), int(end - 90), 10):
                canvas.create_image(y, 268, anchor=NW, image=ImageTk.PhotoImage(
                    app.scaleImage(app.rollLine, 68 / 80)))
            if end - 80 > x + 80:
                canvas.create_image(
                    end - 80, 268, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.rollEnd, 68 / 80)))
            self.drawTopNote(app, canvas, 'roll', x)

    def drawBotNote(self, app, canvas, note, x, end=0):
        if note == 'don':
            canvas.create_image(x, 434, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.don, 68 / 80)))
        if note == 'kat':
            canvas.create_image(x, 434, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.kat, 68 / 80)))
        if note == 'Ddon':
            canvas.create_image(x, 419, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.Ddon, 96 / 121)))
        if note == 'Dkat':
            canvas.create_image(x, 419, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.Dkat, 96 / 121)))
        if note == 'roll':
            canvas.create_image(x, 434, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.roll, 68 / 80)))
        if note == 'rollEnd':
            for y in range(int(x + 44), int(end - 90), 10):
                canvas.create_image(y, 434, anchor=NW, image=ImageTk.PhotoImage(
                    app.scaleImage(app.rollLine, 68 / 80)))
            if end - 80 > x + 80:
                canvas.create_image(
                    end - 80, 434, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.rollEnd, 68 / 80)))
            self.drawBotNote(app, canvas, 'roll', x)

    def drawTopWallpaper(self, app, canvas, x):
        canvas.create_image(x, 0, anchor=NW, image=app.topWallpaper)

    def drawTopTimeline(self, app, canvas):
        canvas.create_image(0, 234, anchor=NW, image=app.timeline)

    def drawTopDecorum(self, app, canvas, x):
        canvas.create_image(x, 0, anchor=NW, image=app.topDecorum)

    def drawTopNoteDecorum(self, app, canvas):
        canvas.create_image(0, 234, anchor=NW, image=app.topNoteDecorum)

    def drawBotWallpaper(self, app, canvas, x):
        canvas.create_image(x, 532, anchor=NW, image=app.botWallpaper)

    def drawBotTimeline(self, app, canvas):
        canvas.create_image(0, 400, anchor=NW, image=app.timeline)

    def drawBotDecorum(self, app, canvas, x):
        canvas.create_image(x, 532, anchor=NW, image=app.botDecorum)

    def drawBotNoteDecorum(self, app, canvas):
        canvas.create_image(0, 400, anchor=NW, image=app.botNoteDecorum)

    def drawTopDonRight(self, app, canvas):
        canvas.create_image(237, 259, anchor=NW, image=app.donRight)

    def drawTopDonLeft(self, app, canvas):
        canvas.create_image(204, 259, anchor=NW, image=app.donLeft)

    def drawTopKatLeft(self, app, canvas):
        canvas.create_image(190, 248, anchor=NW, image=app.katLeft)

    def drawTopKatRight(self, app, canvas):
        canvas.create_image(240, 248, anchor=NW, image=app.katRight)

    def drawBotDonRight(self, app, canvas):
        canvas.create_image(237, 425, anchor=NW, image=app.donRight)

    def drawBotDonLeft(self, app, canvas):
        canvas.create_image(204, 425, anchor=NW, image=app.donLeft)

    def drawBotKatLeft(self, app, canvas):
        canvas.create_image(190, 414, anchor=NW, image=app.katLeft)

    def drawBotKatRight(self, app, canvas):
        canvas.create_image(240, 414, anchor=NW, image=app.katRight)

    def drawScoreBar(self, app, canvas):
        canvas.create_image(25, 384, anchor=NW, image=app.scoreBar)

    def drawTopRollFan(self, app, canvas):
        canvas.create_image(256, 76, anchor=NW, image=app.rollFan)
        canvas.create_image(317, 102, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topRollCounter // 10 % 10], 66 / 57)))
        canvas.create_image(374, 102, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topRollCounter % 10], 66 / 57)))

    def drawBotRollFan(self, app, canvas):
        canvas.create_image(256, 568, anchor=NW, image=app.rollFan)
        canvas.create_image(317, 592, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botRollCounter // 10 % 10], 66 / 57)))
        canvas.create_image(374, 592, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botRollCounter % 10], 66 / 57)))

    def drawTopScore(self, app, canvas):
        if app.topScore >= 10000:
            canvas.create_image(62, 347, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 10000 % 10], 35 / 57)))
        if app.topScore >= 1000:
            canvas.create_image(89, 347, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 1000 % 10], 35 / 57)))
        if app.topScore >= 100:
            canvas.create_image(116, 347, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 100 % 10], 35 / 57)))
        if app.topScore >= 10:
            canvas.create_image(144, 347, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 10 % 10], 35 / 57)))
        canvas.create_image(170, 347, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topScore % 10], 35 / 57)))

    def drawBotScore(self, app, canvas):
        if app.botScore >= 10000:
            canvas.create_image(62, 414, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 10000 % 10], 35 / 57)))
        if app.botScore >= 1000:
            canvas.create_image(89, 414, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 1000 % 10], 35 / 57)))
        if app.botScore >= 100:
            canvas.create_image(116, 414, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 100 % 10], 35 / 57)))
        if app.botScore >= 10:
            canvas.create_image(144, 414, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 10 % 10], 35 / 57)))
        canvas.create_image(170, 414, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botScore % 10], 35 / 57)))

    def drawTopCombo(self, app, canvas):
        if app.topStreak > 9:
            canvas.create_image(203, 268, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topStreak // 10 % 10], 50 / 57)))
        canvas.create_image(244, 268, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topStreak % 10], 50 / 57)))
        canvas.create_image(225, 325, anchor=NW, image=app.combo)

    def drawBotCombo(self, app, canvas):
        if app.botStreak > 9:
            canvas.create_image(203, 432, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botStreak // 10 % 10], 50 / 57)))
        canvas.create_image(244, 432, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botStreak % 10], 50 / 57)))
        canvas.create_image(225, 489, anchor=NW, image=app.combo)

    def drawDifficulty(self, app, canvas):
        if app.level.getDifficulty() == 'easy':
            canvas.create_image(24, 286, anchor=NW, image=app.difficultyEasy)
        elif app.level.getDifficulty() == 'normal':
            canvas.create_image(24, 286, anchor=NW, image=app.difficultyNormal)
        else:
            canvas.create_image(24, 286, anchor=NW, image=app.difficultyHard)
