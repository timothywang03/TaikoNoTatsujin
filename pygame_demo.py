import pygame
from cmu_112_graphics import *

def appStarted(app):
    app.paused = True
    app.musicStarted = True
    pygame.mixer.init()
    app.song = pygame.mixer.music.load('music_folder/charlies_here.mp3')

def redrawAll(app, canvas):
    if app.paused is True: playButton(app, canvas)
    else: pauseButton(app, canvas)

def playButton(app, canvas):
    canvas.create_oval(50, 50, 150, 150, width=5)
    canvas.create_polygon(90, 75, 120, 105, 90, 135)

def pauseButton(app, canvas):
    canvas.create_oval(50, 50, 150, 150, width=5)
    canvas.create_rectangle(82, 68, 95, 128, fill='black')
    canvas.create_rectangle(106, 68, 118, 128, fill='black')

def mousePressed(app, event):
    if 50 <= event.x <= 150 and 50 <= event.y <= 150:
        app.paused = not app.paused

    '''
    if app.musicStarted is False:
        pygame.mixer.music.play()
        app.musicStarted = True
        app.paused = False
    '''

    if app.paused is False and app.musicStarted is True:
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.pause()

runApp(width=200, height=200)
