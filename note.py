from cmu_112_graphics import *

class Note:
    def __init__(self, type, noteStart, noteEnd=0):
        self.type = type
        self.noteStart = noteStart  # time that the note will start
        self.noteStartTime = None
        if noteEnd == 0:
            self.noteEnd = noteStart
        else:
            self.noteEnd = noteEnd      # time that the note wll end
        self.noteEndTime = None
        self.noteMid = (self.noteStart + self.noteEnd) / 2
        self.noteMidTime = None
        self.hit = False
        self.good = 10 # ms
        self.ok = 30 # ms
        self.bad = 60 # ms

    def hitNote(self, time):
        self.hit = time

    def getHit(self):
        return self.hit

    def translateTime(self, app):
        self.noteStartTime = self.noteStart / app.levelLengthPix * app.level.getLength()
        self.noteMidTime = self.noteMid / app.levelLengthPix * app.level.getLength()
        self.noteEndTime = self.noteEnd / app.levelLengthPix * app.level.getLength()

    def getType(self):
        return self.type

    def getNoteStart(self):
        return self.noteStart

    def getEnd(self):
        return self.noteEnd

    def hitScore(self, app):
        # return the score from hitting a note based on accuracy
        score = 0
        if note.getType() == 'roll':
            score += 100 * note.getRollScore()
        else:
            if app.streak < 10:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    score += 1720
                if note.getType() == 'don' or note.getType() == 'kat':
                    score += 860
            elif app.streak >= 10:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    score += 2160
                if note.getType() == 'don' or note.getType() == 'kat':
                    score += 1080
            elif app.streak >= 30:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    score += 2712
                if note.getType() == 'don' or note.getType() == 'kat':
                    score += 1300
            else:
                if note.getType() == 'Ddon' or note.getType() == 'Dkat':
                    score += 3480
                if note.getType() == 'don' or note.getType() == 'kat':
                    score += 1740
        if self.noteMid - self.good <= self.hit <= self.noteMid + self.good:
            score *= 1
        elif self.noteMid - self.ok <= self.hit <= self.noteMid + self.ok:
            score *= 0.5
        else:
            score *= 0

    def __repr__(self):
        return f'({self.type}, {self.noteStart}, {self.noteEnd})'

    def addEnd(self, timestamp):
        self.noteEnd = timestamp


class Roll(Note):
    def __init__(self, noteStart, noteEnd):
        super().__init__(type, noteStart, noteEnd)
        self.roll_score = 0

    def rollCount(self, rolls):
        self.roll_score = rolls

    def getRollScore(self):
        return self.roll_score

    def upRollScore(self):
        self.roll_score += 1
