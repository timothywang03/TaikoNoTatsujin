from cmu_112_graphics import *

class Note:
    def __init__(self, type, noteStart, noteEnd):
        self.type = None
        self.noteStart = noteStart  # time that the note will start
        self.noteEnd = noteEnd      # time that the note wll end
        self.hit = False

    def hitNote(self):
        self.hit = True

    def getType(self):
        return self.type

    def getNoteStart(self):
        return self.noteStart

    def getNoteEnd(self):
        return self.noteEnd

    def hitScore(self):
        pass  # return the score from hitting a note based on accuracy

    def __repr__(self):
        return f'{self.type}: {self.noteStart}'


class Don(Note):
    def __init__(self, app, noteStart, noteEnd, type='don'):
        super().__init__(type, noteStart, noteEnd)
        app.don = app.loadImage('image_folder/don.png')


class Kat(Note):
    def __init__(self, app, noteStart, noteEnd, type='kat'):
        super().__init__(type, noteStart, noteEnd)
        app.kat = app.loadImage('image_folder/kat.png')


class DDon(Note):
    def __init__(self, app, noteStart, noteEnd, type='Ddon'):
        super().__init__(type, noteStart, noteEnd)
        app.Ddon = app.loadImage('image_folder/Ddon.png')


class DKat(Note):
    def __init__(self, app, noteStart, noteEnd, type='Dkat'):
        super().__init__(type, noteStart, noteEnd)
        app.Dkat = app.loadImage('image_folder/Dkat.png')

class Roll(Note):
    def __init__(self, app, noteStart, noteEnd, type='Dkat'):
        super().__init__(type, noteStart, noteEnd)
        app.roll = app.loadImage('image_folder/roll.png')
        app.rollEnd = app.loadImage('image_folder/rollEnd.png')
        app.rollLine = app.loadImage('image_folder/rollLine.png')
        app.roll_score = 0

    def rollCount(self, rolls):
        self.roll_score = rolls

    def getRollScore(self):
        return self.roll_score
