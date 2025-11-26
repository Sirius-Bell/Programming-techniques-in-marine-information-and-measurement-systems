import turtle as t

class Snake():
    """
    :param head: str, head color
    :param tail: str, tail color
    """
    
    def __init__(self, head: str, tail: str, win, controls, score):
        self.head = t.Turtle()
        self.head.penup()
        self.head.shape('turtle')
        self.head.color(head)
        self.tail = []
        self.tail_color = tail
        self.win = win
        self.score = score
        
        self.direction = '0'
        
        self.win.onkeypress(lambda: setattr(self, "direction", '90'), controls[0])
        self.win.onkeypress(lambda: setattr(self, "direction", '270'), controls[1])
        self.win.onkeypress(lambda: setattr(self, "direction", '180'), controls[2])
        self.win.onkeypress(lambda: setattr(self, "direction", '0'), controls[3])
        self.win.onkeypress(lambda: setattr(self, "direction", '-1'), controls[4])
        
        for i in range(3,0,-1):
            q = t.Turtle()
            q.penup()
            q.shape('circle')
            q.color(self.tail_color)
            q.goto((i+1)*30, 0)
            self.tail.insert(0,q)
    
    def move(self):
        if self.direction=='-1':
            t.bye()
    
        self.head.setheading(int(self.direction)) 

        for i in range(0,len(self.tail)-1):
            (x,y) = self.tail[i+1].pos()
            self.tail[i].goto(x,y)
        
        self.tail[-1].goto(self.head.pos())
            
        self.head.forward(20)        
        
        t.update()
        
        for segment in self.tail:
            if self.head.distance(segment) < 10:
                self.catch()

    
    def grow(self):
        q = t.Turtle()
        q.penup()
        q.shape('circle')
        q.color(self.tail_color)
        (x,y) = self.tail[1].pos()
        h = self.tail[1].heading()
        q.goto(x,y)
        q.setheading(h)
        self.tail.insert(0,q)
    
    def catch(self):
        self.head.goto(0,0)
        self.direction = '0'
        while len(self.tail) > 3:
            self.tail[-1].hideturtle()
            self.tail.pop()
        self.score.reset()