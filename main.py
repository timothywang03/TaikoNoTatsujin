from cmu_112_graphics import *
from creator import *
from player import *
from twoPlayer import *
from title import *
from menu import *

# ALL IMAGES ARE FROM WEBSITE https://www.spriters-resource.com/nintendo_switch/taikonotatsujindrumnfun/
# Yoru ni Kakeru downloaded from https://www.youtube.com/watch?v=vEyPvak2K9o&ab_channel=MidnightSoul

def appStarted(app):
    app.width = app.width
    app.height = app.height
    app.titleScreen = app.loadImage('image_folder/title/titleScreen.png')
    app.keyButton = app.loadImage('image_folder/title/keyButton.png')
    app.mode = 'title'

runApp(width=1280, height=800)
