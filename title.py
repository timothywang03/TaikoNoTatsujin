from cmu_112_graphics import *
import menuUI


def title_keyPressed(app, event):
    app.mode = 'menu'
    app.ui = menuUI.UI(app)


def title_redrawAll(app, canvas):
    canvas.create_image(
        0, 0, anchor=NW, image=ImageTk.PhotoImage(app.titleScreen))
    canvas.create_image(384, 621, anchor=NW,
                        image=ImageTk.PhotoImage(app.keyButton))
