import pygame
from note import Note, Roll

class Level:
    def __init__(self, name, notes, length, bpm, song, difficulty):
        self.name = name
        self.notes = notes      # notes will be in format (timestamp, noteType)
        self.length = length    # indicates the length of the level (in secs)
        self.difficulty = difficulty  # TODO: create algorithm that will assess the diff
        self.bpm = bpm
        self.song = song
        self.best_score = 0
        self.ok = 0
        self.good = 0
        self.bad = 0

    def calcScore(self):
        pass

    def getNotes(self):
        return self.notes

    def getLength(self):
        return self.length

    def getBpm(self):
        return self.bpm

    def getBestScore(self):
        return self.best_score

    def getDifficulty(self):
        return self.difficulty

    def getName(self):
        return self.name

    def getSong(self):
        return self.song

    def initiateSong(self, app):
        pygame.mixer.init()
        app.song = pygame.mixer.music.load(f'music_folder/{self.song}')

    def addNote(self, timestamp, note):
        self.notes[timestamp] = note

    def removeNote(self, timestamp):
        del self.notes[timestamp]

    def saveLevel(self):
        f = open(f'{self.name}.txt', 'w')
        f.write(f'Level Name: {self.name}\n')
        f.write(f'BPM: {self.bpm}\n')
        f.write(f'Song: {self.song}\n')
        f.write(f'Best Score: {self.best_score}\n')
        f.write(f'Difficulty: {self.difficulty}\n')
        for k, v in self.notes.items():
            f.write(f'{v.getType()} {v.getNoteStart()} {v.getEnd()}\n')

    def loadNotes(level):
        try:
            f = open(f'{level.name}.txt', 'r')
        except:
            return -1
        for line in f.readlines()[5:]:
            line = line.split()
            level.notes[float(line[1])] = Note(line[0], level, float(line[1]), float(line[2]))

    def __str__(self):
        return f'{self.name}, {len(self.notes)}'
