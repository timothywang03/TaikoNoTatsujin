from cmu_112_graphics import *

class Note:
    def __init__(self, type, noteStart, noteEnd=0):
        self.type = type
        self.noteStart = noteStart  # time that the note will start
        self.noteEnd = noteStart + noteEnd      # time that the note wll end
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
        return f'({self.type}, {self.noteStart})'


class Roll(Note):
    def __init__(self, noteStart, noteEnd):
        super().__init__(type, noteStart, noteEnd)
        self.roll_score = 0

    def rollCount(self, rolls):
        self.roll_score = rolls

    def getRollScore(self):
        return self.roll_score
