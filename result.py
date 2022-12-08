from cmu_112_graphics import *

class Result:
    def __init__(self, app):
        app.resultBackground = ImageTk.PhotoImage(app.loadImage('image_folder/result/resultBackground.png'))
        app.playerOneScreen = ImageTk.PhotoImage(app.loadImage('image_folder/result/player1.png'))
        app.playerTwoScreen = ImageTk.PhotoImage(app.loadImage('image_folder/result/player2.png'))
        app.win = ImageTk.PhotoImage(app.loadImage('image_folder/result/win.png'))
        app.lose = ImageTk.PhotoImage(app.loadImage('image_folder/result/lose.png'))
        app.topNoteScores = app.level.getNoteScores(1)
        print(app.topNoteScores)
        app.botNoteScores = app.level.getNoteScores(2)

    def drawPlayerOneScore(self, app, canvas):
        if app.topScore >= 10000:
            canvas.create_image(426, 224, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 10000 % 10], 43 / 57)))
        if app.topScore >= 1000:
            canvas.create_image(462, 224, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 1000 % 10], 43 / 57)))
        if app.topScore >= 100:
            canvas.create_image(498, 224, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 100 % 10], 43 / 57)))
        if app.topScore >= 10:
            canvas.create_image(534, 224, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topScore // 10 % 10], 43 / 57)))
        canvas.create_image(570, 224, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topScore % 10], 43 / 57)))

        # draw good
        if app.topNoteScores[0] >= 10:
            canvas.create_image(867, 182, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topNoteScores[0] // 10 % 10], 43 / 57)))
        canvas.create_image(903, 182, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topNoteScores[0] % 10], 43 / 57)))

        # draw ok
        if app.topNoteScores[1] >= 10:
            canvas.create_image(867, 258, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topNoteScores[1] // 10 % 10], 43 / 57)))
        canvas.create_image(903, 258, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topNoteScores[1] % 10], 43 / 57)))

        # draw bad
        if app.topNoteScores[2] >= 10:
            canvas.create_image(867, 328, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.topNoteScores[2] // 10 % 10], 43 / 57)))
        canvas.create_image(903, 328, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.topNoteScores[2] % 10], 43 / 57)))

    def drawPlayerTwoScore(self, app, canvas):
        if app.botScore >= 10000:
            canvas.create_image(426, 464, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 10000 % 10], 43 / 57)))
        if app.botScore >= 1000:
            canvas.create_image(462, 464, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 1000 % 10], 43 / 57)))
        if app.botScore >= 100:
            canvas.create_image(498, 464, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 100 % 10], 43 / 57)))
        if app.botScore >= 10:
            canvas.create_image(534, 464, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botScore // 10 % 10], 43 / 57)))
        canvas.create_image(570, 464, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botScore % 10], 43 / 57)))

        # draw good
        if app.botNoteScores[0] >= 10:
            canvas.create_image(867, 420, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botNoteScores[0] // 10 % 10], 43 / 57)))
        canvas.create_image(903, 420, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botNoteScores[0] % 10], 43 / 57)))

        # draw ok
        if app.botNoteScores[1] >= 10:
            canvas.create_image(867, 496, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botNoteScores[1] // 10 % 10], 43 / 57)))
        canvas.create_image(903, 496, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botNoteScores[1] % 10], 43 / 57)))

        # draw bad
        if app.botNoteScores[2] >= 10:
            canvas.create_image(867, 566, anchor=NW, image=ImageTk.PhotoImage(
                app.scaleImage(app.numbers[app.botNoteScores[2] // 10 % 10], 43 / 57)))
        canvas.create_image(903, 566, anchor=NW, image=ImageTk.PhotoImage(
            app.scaleImage(app.numbers[app.botNoteScores[2] % 10], 43 / 57)))

def result_redrawAll(app, canvas):
    canvas.create_image(0, 0, anchor=NW, image=app.resultBackground)
    canvas.create_image(284, 161, anchor=NW, image=app.playerOneScreen)
    app.ui.drawPlayerOneScore(app, canvas)
    if app.level.getPlayers() == 2:
        canvas.create_image(284, 399, anchor=NW, image=app.playerTwoScreen)
        app.ui.drawPlayerTwoScore(app, canvas)
        if app.topScore > app.botScore:
            canvas.create_image(31, 195, anchor=NW, image=app.win)
            canvas.create_image(42, 475, anchor=NW, image=app.lose)
        else:
            canvas.create_image(31, 475, anchor=NW, image=app.win)
            canvas.create_image(42, 195, anchor=NW, image=app.lose)
