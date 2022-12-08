from cmu_112_graphics import *


class Note:
    def __init__(self, type, level, noteStart, noteEnd=0):

        # inherent variables
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

        # timing constants
        if self.type == 'don' or self.type == 'kat':
            self.good = 10  # ms
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
        '''Sets the position to the time that the note was hit'''
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
        '''Returns the score that the note yields when hitting it'''
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
        if self.noteMid - self.good <= self.hit + app.frameLeft <= self.noteMid + self.good:
            score *= 1
            app.level.scoreNote('good', 1)
        elif self.noteMid - self.ok <= self.hit + app.frameLeft <= self.noteMid + self.ok:
            score *= 0.5
            app.level.scoreNote('ok', 1)
        else:
            score *= 0.1
            app.level.scoreNote('bad', 1)
        return score

    def __repr__(self):
        return f'({self.type}, {self.noteStart}, {self.noteEnd})'

    def addEnd(self, timestamp):
        self.noteEnd = timestamp


class PlayerOneNote(Note):
    def __init__(self, type, level, noteStart, noteEnd=0):
        super().__init__(type, level, noteStart, noteEnd)

        # changes the notes hit depending on player
        if self.type == 'don':
            self.keys = [{'s'}, {'d'}]
        if self.type == 'kat':
            self.keys = [{'a'}, {'f'}]
        if self.type == 'Ddon':
            self.keys = [{'s', 'd'}]
        if self.type == 'Dkat':
            self.keys = [{'a', 'f'}]
        if self.type == 'roll':
            self.keys = [{'s'}, {'d'}]

    def hitScore(self, app):
        # return the score from hitting a note based on accuracy
        score = 0
        if self.getType() == 'roll':
            return 100
        else:
            if app.topStreak < 10:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 1720
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 860
            elif app.topStreak >= 10:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 2160
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1080
            elif app.topStreak >= 30:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 2712
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1300
            else:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 3480
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1740
        if self.noteMid - self.good <= self.hit + app.frameLeft <= self.noteMid + self.good:
            score *= 1
            app.level.scoreNote('good', 1)
        elif self.noteMid - self.ok <= self.hit + app.frameLeft <= self.noteMid + self.ok:
            score *= 0.5
            app.level.scoreNote('ok', 1)
        else:
            score *= 0.1
            app.level.scoreNote('bad', 1)
        return score


class PlayerTwoNote(Note):
    def __init__(self, type, level, noteStart, noteEnd=0):
        super().__init__(type, level, noteStart, noteEnd)
        if self.type == 'don':
            self.keys = [{'j'}, {'k'}]
        if self.type == 'kat':
            self.keys = [{'h'}, {'l'}]
        if self.type == 'Ddon':
            self.keys = [{'j', 'k'}]
        if self.type == 'Dkat':
            self.keys = [{'h', 'l'}]
        if self.type == 'roll':
            self.keys = [{'j'}, {'k'}]

    def hitScore(self, app):
        # return the score from hitting a note based on accuracy
        score = 0
        if self.getType() == 'roll':
            return 100
        else:
            if app.botStreak < 10:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 1720
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 860
            elif app.botStreak >= 10:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 2160
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1080
            elif app.botStreak >= 30:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 2712
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1300
            else:
                if self.getType() == 'Ddon' or self.getType() == 'Dkat':
                    score += 3480
                if self.getType() == 'don' or self.getType() == 'kat':
                    score += 1740
        if self.noteMid - self.good <= self.hit + app.frameLeft <= self.noteMid + self.good:
            score *= 1
            app.level.scoreNote('good', 2)
        elif self.noteMid - self.ok <= self.hit + app.frameLeft <= self.noteMid + self.ok:
            score *= 0.5
            app.level.scoreNote('ok', 2)
        else:
            score *= 0.1
            app.level.scoreNote('bad', 2)
        return score


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
