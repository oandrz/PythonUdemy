from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.read_high_score()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.refresh()

    def plus_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.cache_high_score()

        self.score = 0
        self.refresh()

    def cache_high_score(self):
        with open("score.txt", mode='w') as file:
            file.write(f"{self.high_score}")

    def read_high_score(self):
        try:
            with open("score.txt") as file:
                cached_score = file.read()
                if cached_score != "":
                    return int(cached_score)
        except FileNotFoundError:
            print("File Not Found")
