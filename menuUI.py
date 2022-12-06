from cmu_112_graphics import *
from note import Note, Roll
import pygame


class UI:
    def __init__(self, app):
        # pulled image from https://wallpapercave.com/taiko-wallpapers
        app.menuScreen = ImageTk.PhotoImage(
            app.loadImage('image_folder/menu/menu.png'))
        app.difficulties = ImageTk.PhotoImage(
            app.loadImage('image_folder/menu/difficulties.png'))
        app.loadLevel = ImageTk.PhotoImage(
            app.loadImage('image_folder/menu/loadLevel.png'))
        app.selection = ImageTk.PhotoImage(
            app.loadImage('image_folder/menu/selection.png'))
        app.error = ImageTk.PhotoImage(
            app.loadImage('image_folder/menu/error.png'))

        app.loadScreen = False
        app.clicked = None
        app.diffSelected = None
        app.levelEntered = None
        app.errorDraw = False

    def drawMenuBackground(self, app, canvas):
        canvas.create_image(0, 0, anchor=NW, image=app.menuScreen)

    def drawLoadLevel(self, app, canvas):
        canvas.create_image(306, 193, anchor=NW, image=app.loadLevel)

    def drawDifficulties(self, app, canvas):
        canvas.create_image(384, 394, anchor=NW, image=app.difficulties)

    def drawSelection(self, app, canvas, x):
        canvas.create_image(x, 394, anchor=NW, image=app.selection)

    def drawError(self, app, canvas):
        canvas.create_image(470, 204, anchor=NW, image=app.error)
