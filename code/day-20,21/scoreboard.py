from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color('White')
        self.write(f"Score: {self.score}", align='center',  font=('Courier', 24, 'normal'))
        self.hideturtle()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align='center',  font=('Courier', 24, 'normal'))       
            
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center',  font=('Courier', 24, 'normal'))

        

