import pygame
from note import Note, Roll


class Level:
    def __init__(self, name, notes, length, bpm, song, difficulty, players):
        self.name = name
        self.notes = notes      # notes will be in format (timestamp, noteType)
        self.length = length    # indicates the length of the level (in secs)
        self.difficulty = difficulty
        self.bpm = bpm
        self.song = song
        self.players = [[0, 0, 0], [0, 0, 0]]
        self.numPlayers = players

    def scoreNote(self, score, player):
        if player == 1:
            if score == 'ok':
                self.players[0][0] += 1
            elif score == 'good':
                self.players[0][1] += 1
            else:
                self.players[0][2] += 1
        else:
            if score == 'ok':
                self.players[1][0] += 1
            elif score == 'good':
                self.players[1][1] += 1
            else:
                self.players[1][2] += 1

    def calcScore(self):
        pass

    def getNotes(self):
        return self.notes

    def getLength(self):
        return self.length

    def getBpm(self):
        return self.bpm

    def setBpm(self, bpm):
        self.bpm = bpm

    def getDifficulty(self):
        return self.difficulty

    def setDifficulty(self, difficulty):
        self.difficulty = difficulty

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSong(self):
        return self.song

    def initiateSong(self, app):
        pygame.mixer.init()
        app.song = pygame.mixer.music.load(f'music_folder/{self.song}')

    def addNote(self, timestamp, note):
        self.notes[timestamp] = note

    def removeNote(self, timestamp):
        del self.notes[timestamp]

    def getNoteScores(self, player):
        return self.players[player - 1]

    def getPlayers(self):
        return self.numPlayers

    def saveLevel(self):
        f = open(f'levels/{self.name}_{self.difficulty}.txt', 'w')
        f.write(f'Level Name: {self.name}\n')
        f.write(f'BPM: {self.bpm}\n')
        f.write(f'Song: {self.song}\n')
        f.write(f'Best Score: {self.best_score}\n')
        f.write(f'Difficulty: {self.difficulty}\n')
        for k, v in self.notes.items():
            f.write(f'{v.getType()} {v.getNoteStart()} {v.getEnd()}\n')

    def loadNotes(level):
        f = open(f'levels/{level.name}_{level.difficulty}.txt', 'r')
        for line in f.readlines()[5:]:
            line = line.split()
            level.notes[float(line[1])] = Note(
                line[0], level, float(line[1]), float(line[2]))

    def __str__(self):
        return f'{self.name}, {len(self.notes)}'
