class Level:
    def __init__(self, notes, length):
        self.notes = notes      # notes will be in format (timestamp, noteType)
        self.length = length    # indicates the length of the level (in secs)
        self.difficulty = None  # TODO: create algorithm that will assess the diff


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
