from note import Note, Roll
from level import Level
from math import floor
import pygame
import time

def creator_mousePressed(app, event):
    if app.currently_selected == 'playButton':
        if 1151 <= event.x <= 1231 and 14 <= event.y <= 94:
            app.currently_selected = None
            app.reached_middle = False
            pygame.mixer.music.pause()
            app.error = None
        else:
            app.error = 'playback'

    elif app.currently_selected is None:
        if 250 <= event.y <= 400:
            for k, v in app.level.getNotes().items():
                if v.getNoteStart() <= app.frameLeft + event.x <= v.getEnd():
                    app.currently_selected = k

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
        if 14 <= event.y <= 43 and 190 + app.scrollx <= event.x <= app.scrollx + 193:
            app.currently_selected = 'scrollMarker'
        if 1151 <= event.x <= 1231 and 14 <= event.y <= 94:
            app.currently_selected = 'playButton'
            app.indicatorx = app.frameLeft
            pygame.mixer.music.play(0, 281 * app.frameLeft / (app.level.getBpm() * app.level.getLength() / 60 * app.pixelsPerBeat))

    if app.currently_selected in app.noteTypes:
        if app.currently_selected == 'rollEnd':
            app.level.getNotes()[app.rollStart].addEnd(event.x + app.frameLeft)
            app.currently_selected = None
            app.hover = None

        elif app.hover is not None:
            if app.ui.checkOverlap(app, app.hover + app.frameLeft) is False:
                if app.currently_selected == 'don':
                    app.level.addNote(event.x + app.frameLeft, \
                    Note('don', event.x + app.frameLeft, event.x + app.frameLeft + 80))
                elif app.currently_selected == 'kat':
                    app.level.addNote(event.x + app.frameLeft, \
                    Note('kat', event.x + app.frameLeft, event.x + app.frameLeft + 80))
                elif app.currently_selected == 'Ddon':
                    app.level.addNote(event.x + app.frameLeft, \
                    Note('Ddon', event.x + app.frameLeft, event.x + app.frameLeft + 121))
                elif app.currently_selected == 'Dkat':
                    app.level.addNote(event.x + app.frameLeft, \
                    Note('Dkat', event.x + app.frameLeft, event.x + app.frameLeft + 121))
                elif app.currently_selected == 'roll':
                    app.level.addNote(event.x + app.frameLeft, \
                    Note('roll', event.x + app.frameLeft))
                    app.currently_selected = 'rollEnd'
                    app.rollStart = event.x + app.frameLeft

                if app.currently_selected != 'rollEnd':
                    app.currently_selected = None
                    app.hover = None
                app.error = None
            else:
                app.error = 'overlap'
    print(app.currently_selected)

def creator_keyPressed(app, event):
    if event.key == 'Escape':
        app.currently_selected = None
        app.hover = None
    if event.key == 's':
        app.ui.saveLevel(app)
    if event.key == 'BackSpace':
        print(type(app.currently_selected))
        if type(app.currently_selected) == int or type(app.currently_selected == float):
            app.level.removeNote(app.currently_selected)
            app.currently_selected = None

def creator_mouseMoved(app, event):
    if app.currently_selected in app.noteTypes:
        if 250 <= event.y <= 400:
            app.hover = event.x
        else:
            app.hover = None

def creator_mouseDragged(app, event):
    if app.currently_selected == 'scrollMarker':
        if 190 <= event.x <= 1087:
            app.scrollx = event.x - 190
        elif event.x < 190:
            app.scrollx = 0
        elif event.x > 1087:
            app.scrollx = 897

    app.ui.calcFrame(app)

def creator_timerFired(app):
    if app.currently_selected == 'playButton':
        app.ui.playback(app)

def creator_mouseReleased(app, event):
    if app.currently_selected == 'scrollMarker':
        app.currently_selected = None

def creator_redrawAll(app, canvas):
    app.ui.drawBackground(app, canvas)
    app.ui.drawTimeline(app, canvas)
    app.ui.drawNoteSelection(app, canvas)
    app.ui.drawScrollBar(app, canvas)
    app.ui.drawScrollMarker(app, canvas)
    app.ui.drawErrorBox(app, canvas)
    app.ui.drawPlayButton(app, canvas)
    app.ui.drawBeatlines(app, canvas)
    app.ui.drawError(app, canvas, app.error)
    app.ui.drawIndicator(app, canvas)

    for timestamp in sorted(app.level.getNotes(), reverse=True):
        note = app.level.getNotes()[timestamp]
        if note.getHit() is False:
            app.ui.drawNote(app, canvas, note.getType(), timestamp - app.frameLeft, note.getEnd() - app.frameLeft)
            if note.getType() == 'roll':
                app.ui.drawNote(app, canvas, 'rollEnd', timestamp - app.frameLeft, note.getEnd() - app.frameLeft)

    if app.currently_selected in app.noteTypes and app.hover is not None:
        if app.currently_selected == 'rollEnd':
            app.ui.drawNote(app, canvas, app.currently_selected, app.rollStart, app.hover)
        else:
            app.ui.drawNote(app, canvas, app.currently_selected, app.hover)
