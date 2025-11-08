import turtle
class enemy:
    def __init__(self):
      self.pos = (0, 0)
      self.alive = True
    def draw(self, pen):
        if not self.alive:
            return
        x, y = self.pos
        pen.penup()
        pen.goto(x, y-8)
        pen.pendown()
        pen.color("red")
        pen.begin_fill()
        radius = 3
        pen.circle(3)
        pen.end_fill()
        

class tower:
    def __init__(self):
      self.pos = (0, 0)
      self.alive = True
    def draw(self, pen):
        x, y = self.pos
        pen.penup()
        pen.goto(x, y-8)
        pen.pendown()
        pen.color("red")
        pen.begin_fill()
        pen.forward(5)
        pen.right(90)
        pen.forward(5)
        pen.right(90)
        pen.forward(5)
        pen.right(90)
        pen.forward(5)
        pen.right(90)
        pen.end_fill()
        
pen = turtle.Turtle()
bob = enemy()
bob.draw(pen)
pen.speed(0)
tom = tower()
tom.draw(pen)
turtle.done()

# 0:12, 47:12
#0:21, 47:21