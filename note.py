from cmu_112_graphics import *

class Note:
    def __init__(self, type, level, noteStart, noteEnd=0):
        self.type = type
        self.level = level
        self.levelLengthPix = level.getLength() ** 2 / 60 * level.getBpm() * 5
        self.noteStart = noteStart  # pixel that the note will start
        if noteEnd == 0:
            self.noteEnd = noteStart
        else:
            self.noteEnd = noteEnd      # pixel that the note wll end
        self.noteMid = (self.noteStart + self.noteEnd) / 2
        self.hit = False
        if self.type == 'don' or self.type == 'kat':
            self.good = 10 # ms
            self.ok = 15
            self.bad = 20
        else:
            self.good = 10
            self.ok = 20
            self.bad = 30

        if self.type == 'don':
            self.keys = [{'f'}, {'j'}]
        if self.type == 'kat':
            self.keys = [{'d'}, {'k'}]
        if self.type == 'Ddon':
            self.keys = [{'f', 'j'}]
        if self.type == 'Dkat':
            self.keys = [{'d', 'k'}]
        if self.type == 'roll':
            self.keys = [{'f'}, {'j'}]

    def hitNote(self, position):
        self.hit = position

    def getHit(self):
        return self.hit

    def getType(self):
        return self.type

    def getNoteStart(self):
        return self.noteStart

    def getKeys(self):
        return self.keys

    def getEnd(self):
        return self.noteEnd

    def hitScore(self, app):
        # return the score from hitting a note based on accuracy
        score = 0
        if self.getType() == 'roll':
            return 100
        else:
            if app.streak < 10:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 1720
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 860
            elif app.streak >= 10:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 2160
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1080
            elif app.streak >= 30:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 2712
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1300
            else:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 3480
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1740
        if self.noteMid - self.good <= self.hit <= self.noteMid + self.good:
            score *= 1
        elif self.noteMid - self.ok <= self.hit <= self.noteMid + self.ok:
            score *= 0.5
        else:
            score *= 0.1
        return score

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
