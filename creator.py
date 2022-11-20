import pygame
from note import Note, Roll
from level import Level
import time
import pygame

def creator_mousePressed(app, event):
    if app.currently_selected is None:
        if 243 <= event.x <= 323 and 658 <= event.y <= 738:
            app.currently_selected = 'don'
        if 401 <= event.x <= 481 and 658 <= event.y <= 738:
            app.currently_selected = 'kat'
        if 559 <= event.x <= 639 and 658 <= event.y <= 738:
            app.currently_selected = 'roll'
        if 717 <= event.x <= 838 and 637 <= event.y <= 758:
            app.currently_selected = 'Ddon'
        if 916 <= event.x <= 1037 and 637 <= event.y <= 758:
            app.currently_selected = 'Dkat'
        if 14 <= event.y <= 43 and app.scrollx <= event.x <= app.scrollx + 3:
            app.currently_selected = 'scrollMarker'

    if app.currently_selected in app.noteTypes:
        if app.hover is not None:
            if app.currently_selected == 'don':
                app.level.addNote(event.x + app.scrollConstant * app.scrollx, \
                Note('don', event.x + app.scrollConstant * app.scrollx))
            elif app.currently_selected == 'kat':
                app.level.addNote(event.x + app.scrollConstant * app.scrollx, \
                Note('kat', event.x + app.scrollConstant * app.scrollx))
            elif app.currently_selected == 'Ddon':
                app.level.addNote(event.x + app.scrollConstant * app.scrollx, \
                Note('Ddon', event.x + app.scrollConstant * app.scrollx))
            elif app.currently_selected == 'Dkat':
                app.level.addNote(event.x + app.scrollConstant * app.scrollx, \
                Note('Dkat', event.x + app.scrollConstant * app.scrollx))
            elif app.currently_selected == 'roll':
                app.level.addNote(event.x + app.scrollConstant * app.scrollx, \
                Note('roll', event.x + app.scrollConstant * app.scrollx))
            app.currently_selected = None
            app.hover = None

def creator_mouseMoved(app, event):
    if app.currently_selected in app.noteTypes:
        if 250 <= event.y <= 400:
            app.hover = event.x
        else: app.hover = None

def creator_mouseDragged(app, event):
    if app.currently_selected == 'scrollMarker':
        if 190 <= event.x <= 1087:
            app.scrollx = event.x
        elif event.x < 190:
            app.scrollx = 190
        elif event.x > 1087:
            app.scrollx = 1087

def creator_redrawAll(app, canvas):
    app.ui.drawBackground(app, canvas)
    app.ui.drawTimeline(app, canvas)
    app.ui.drawNoteSelection(app, canvas)
    app.ui.drawScrollBar(app, canvas)
    app.ui.drawScrollMarker(app, canvas)
    for k, v in app.level.getNotes().items():
        app.ui.drawNote(app, canvas, v.getType(), k)
    if app.currently_selected in app.noteTypes and app.hover is not None:
        app.ui.drawNote(app, canvas, app.currently_selected, app.hover)
