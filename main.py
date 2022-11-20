from cmu_112_graphics import *
from creator import *
import creatorUI
import pygame
from note import Note, Roll
from level import Level


def appStarted(app):
    app.width = app.width
    app.height = app.height
    app.mode = 'creator'
    if app.mode == 'creator':
        app.ui = creatorUI.UI(app)
        app.level = Level('Yoru Ni Kakeru', dict(), 281, 130, 'yoru_ni_kakeru.mp3')
        app.currently_selected = None

runApp(width=1280, height=800)
