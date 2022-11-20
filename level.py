class Level:
    def __init__(self, name, notes, length, song):
        self.name = name
        self.notes = notes      # notes will be in format (timestamp, noteType)
        self.length = length    # indicates the length of the level (in secs)
        self.difficulty = None  # TODO: create algorithm that will assess the diff
        self.song = None
        self.best_score = 0
        self.ok = 0
        self.good = 0
        self.great = 0

    def calcScore(self):
        pass

    def getNotes(self):
        return self.notes

    def getBestScore(self):
        return self.best_score

    def getName(self):
        return self.name

    def getSong(self):
        return self.song

    def addNote(self, timestamp, note):
        self.notes[timestamp] = note

    def __str__(self):
        return f'{self.name}, {len(self.notes)}'
