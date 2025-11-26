import turtle
import random

class Food():
    """

    """
    
    def __init__(self, win, color='red', shape='circle',step=20):
    
        self.width = win.window_width()
        self.height = win.window_height()
        self.step = step
    
        self.food = turtle.Turtle()
        self.food.shape(shape)
        self.food.color(color)
        self.food.penup()
        self.move()
        
        
    def eat(self, snake):
        return self.food.distance(snake)
    
    def move(self):
        x = random.randint(-self.width//2//self.step+1,self.height//2//self.step-1)*self.step - 5
        y = random.randint(-self.height//2//self.step+1,self.height//2//self.step-1)*self.step - 5
        self.food.goto(x,y)