import turtle as t
import time
from objects.snake import Snake
from objects.food import Food
from objects.score import Score
from objects.ll import logger

class Board():
    """
    Draw a board GUI
    
    :param SIZE_X: int, size_x of board
    :param SIZE_Y: int, size_y of board
    """
    def __init__(self, SIZE_X: int, SIZE_Y: int, MINU: int = 20):
        self.SIZE_X = SIZE_X
        self.SIZE_Y = SIZE_Y
        self.MINU = MINU
 
        self.win = t.Screen()
        self.win.tracer(0)

        self.food = Food(self.win)
        self.score = Score(self.win)
        
        self.snakes = [Snake('black', 'green', self.win, ('Up', 'Down', 'Left', 'Right', 'Escape'), self.score)]
        
        self.borders()
        self.win.listen()
        self.win.update()

    def borders(self):
        border = t.Turtle()
        border.hideturtle()
        border.speed(0)
        border.color("black")
        border.pensize(10)
        border.penup()
        
        
        self.half_w = self.win.window_width()//2 - self.MINU
        self.half_h = self.win.window_height()//2 - self.MINU
        logger.debug(self.half_w)
        logger.debug(self.half_h)
        
        border.goto(-self.half_w, self.half_h)
        border.pendown()
        border.goto(self.half_w, self.half_h)
        border.goto(self.half_w, -self.half_h)
        border.goto(-self.half_w, -self.half_h)
        border.goto(-self.half_w, self.half_h)

    def game(self):
        while True:
            for i in self.snakes:                
                i.move()
                if self.food.eat(i.head)<15:
                    self.food.move()
                    i.grow()
                    self.score.update()
                
                x,y = i.head.xcor(), i.head.ycor()
                
                if abs(x) >= abs(self.half_w) or abs(y) >= abs(self.half_h):
                    i.catch()
                
            time.sleep(0.1)
            
        self.win.mainloop()
        
    def reset(self):
        pass