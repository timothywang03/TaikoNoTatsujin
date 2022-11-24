from cmu_112_graphics import *

class Note:
    def __init__(self, type, noteStart, noteEnd=0):
        self.type = type
        self.noteStart = noteStart  # time that the note will start
        if noteEnd == 0:
            self.noteEnd = noteStart
        else:
            self.noteEnd = noteEnd      # time that the note wll end
        self.hit = False
        self.great = 10 # ms
        self.good = 30 # ms
        self.ok = 60 # ms

    def hitNote(self):
        self.hit = True

    def getHit(self):
        return self.hit

    def getType(self):
        return self.type

    def getNoteStart(self):
        return self.noteStart

    def getEnd(self):
        return self.noteEnd

    def hitScore(self):
        pass  # return the score from hitting a note based on accuracy

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
