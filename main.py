from cmu_112_graphics import *
from creator import *
from player import *
import creatorUI
import playerUI
import pygame
from note import Note, Roll
from level import Level

# ALL IMAGES ARE FROM WEBSITE https://www.spriters-resource.com/nintendo_switch/taikonotatsujindrumnfun/
# Yoru ni Kakeru downloaded from https://www.youtube.com/watch?v=vEyPvak2K9o&ab_channel=MidnightSoul

def appStarted(app):
    app.width = app.width
    app.height = app.height
    app.mode = 'player'
    app.level = Level('Yoru Ni Kakeru', dict(), 34, 130, 'yoru_ni_kakeru.mp3', 'normal') # CITE
    app.level.loadNotes()
    print(app.level.getNotes())
    if app.mode == 'creator':
        app.ui = creatorUI.UI(app)
    if app.mode == 'player':
        app.level.initiateSong(app)
        app.ui = playerUI.UI(app)

runApp(width=1280, height=800)
