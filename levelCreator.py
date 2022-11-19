import pygame
from note import Don, Kat, DDon, DKat, Roll
from level import Level
import time
import pygame


def drawCreatorUI(app, canvas):
    app.notes = dict()
    app.ui.drawBackground(app, canvas)
    app.ui.drawTimeline(app, canvas)
    app.ui.drawNoteSelection(app, canvas)
    app.ui.drawScrollBar(app, canvas)
