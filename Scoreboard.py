from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.guessed = 0
        self.correct_guessed = []

    def add_guessed(self, answer):
        if answer not in self.correct_guessed:
            self.guessed += 1
            self.correct_guessed.append(answer)
