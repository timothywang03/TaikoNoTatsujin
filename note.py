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
    def __init__(self, type='don', noteStart, noteEnd):
        super().__init__(type, noteStart, noteEnd)


class Kat(Note):
    def __init__(self, type='kat', noteStart, noteEnd):
        super().__init__(type, noteStart, noteEnd)


class DDon(Note):
    def __init__(self, type='Ddon', noteStart, noteEnd):
        super().__init__(type, noteStart, noteEnd)


class DKat(Note):
    def __init__(self, type='Dkat', noteStart, noteEnd):
        super().__init__(type, noteStart, noteEnd)

class Roll(Note):
    def __init__(self, type='Dkat', noteStart, noteEnd):
        super().__init__(type, noteStart, noteEnd)
        self.roll_score = 0

    def rollCount(self, rolls):
        self.roll_score = rolls

    def getRollScore(self):
        return self.roll_score

class DrawNote:
    def __init__(self):
        self.donImage = 'image_folder/don.png'
        self.katImage = 'image_folder/kat.png'
        self.DdonImage = 'image_folder/Ddon.png'
        self.DkatImage = 'image_folder/Dkat.png'

    def getNoteImage(self, noteType):
        if noteType == 'don':
            return self.donImage
        if noteType == 'kat':
            return self.katImage
        if noteType == 'Ddon':
            return self.DdonImage
        if noteType == 'Dkat';
            return self.DkatImage
