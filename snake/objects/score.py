import turtle

class Score():
    """

    """
    def __init__(self, win):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("black")
        self.pen.penup()
        
        self.pen.goto(0,win.window_height()//2-50)
        
        self.score = 0
        self.games = 1
        self.pen.write(f"Score: {self.score}, Games: {self.games}", align="center", font=("Arial", 18, "bold"))

        

    def update(self):
        self.score += 1

        self.pen.clear()
        self.pen.write(f"Score: {self.score}, Games: {self.games}", align="center", font=("Arial", 18, "bold"))
    
    def reset(self):
        self.score = 0
        self.games += 1
        self.pen.clear()
        self.pen.write(f"Score: {self.score}, Games: {self.games}", align="center", font=("Arial", 18, "bold"))
        