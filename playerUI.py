from cmu_112_graphics import *
from note import Note, Roll
import pygame

class UI:
    def __init__(self, app):
        # NOTE CONSTANTS
        app.don = app.loadImage('image_folder/don.png')
        app.kat = app.loadImage('image_folder/kat.png')
        app.roll = app.loadImage('image_folder/roll.png')
        app.rollEnd = app.loadImage('image_folder/rollEnd.png')
        app.rollLine = app.loadImage('image_folder/rollLine.png')
        app.noteTypes = {'kat', 'don', 'Dkat', 'Ddon', 'roll', 'rollEnd'}
        app.Ddon = app.loadImage('image_folder/Ddon.png')
        app.Dkat = app.loadImage('image_folder/Dkat.png')

        # MUSIC
        app.song = pygame.mixer.music.load('music_folder/charlies_here.mp3')
        pygame.mixer.init()
        app.timerDelay = 10

        # FRAME VARIABLES
        app.frameLeft = 0
        app.frameRight = app.frameLeft + 1280
        app.noteMove = 30
        app.noteQueue = list()

        # VISUAL VARIABLES
        app.noteDecorum = ImageTk.PhotoImage(app.loadImage('image_folder/noteDecorum.png'))
        app.indicator = ImageTk.PhotoImage(app.loadImage('image_folder/indicator.png'))

    def drawNote(self, app, canvas, note, x, end=0):
        if note == 'don':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.don, 80/44)))
        if note == 'kat':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.kat, 80/44)))
        if note == 'Ddon':
            canvas.create_image(x, 265, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Ddon, 80/44)))
        if note == 'Dkat':
            canvas.create_image(x, 265, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.Dkat, 80/44)))
        if note == 'roll':
            canvas.create_image(x, 285, anchor=NW, image=ImageTk.PhotoImage(app.scaleImage(app.roll, 80/44)))
