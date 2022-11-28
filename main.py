from cmu_112_graphics import *
from creator import *
from player import *
import creatorUI
import playerUI
import pygame
from note import Note, Roll
from level import Level


def appStarted(app):
    app.width = app.width
    app.height = app.height
    app.mode = 'player'
    app.level = Level('Yoru Ni Kakeru', dict(), 281, 130, 'yoru_ni_kakeru.mp3', 'normal') # CITE
    app.level.loadNotes()
    if app.mode == 'creator':
        app.ui = creatorUI.UI(app)
    if app.mode == 'player':
        app.ui = playerUI.UI(app)

runApp(width=1280, height=800)
