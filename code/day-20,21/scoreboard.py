from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.color('White')
        self.write(f"Score: {self.score}", align='center',  font=('Courier', 24, 'normal'))
        self.hideturtle()
        
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center',  font=('Courier', 24, 'normal'))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update()
    
            
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center',  font=('Courier', 24, 'normal'))

        

