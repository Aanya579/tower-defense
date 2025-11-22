import turtle
import math
class enemy:
    def __init__(self, x, y, path):
      self.x = x
      self.y = y
      self.path = path
      self.path_pos = 1
      self.pos = path[0]
      self.alive = True
    def draw(self, pen):
        if not self.alive:
            return
        x, y = self.pos
        #pen.color("red")
        pen.penup()
        pen.goto(x, y-8)
        pen.pendown()
        pen.begin_fill()
        radius = 3
        pen.circle(3)
        pen.end_fill()
    def update(self):
       x, y = self.pos
       p_x, p_y = self.path[self.path_pos]
       dx = p_x - x
       dy = p_y - y
       h = math.sqrt(dx*dx + dy*dy)
       dx/=h
       dy/=h
       dx*=15
       dy*=15
       self.pos = (dx, dy)
       print(self.pos)
        

class tower:
    def __init__(self, x, y):
      self.x = x
      self.y = y
      self.pos = (0, 0)
      self.alive = True
    def draw(self, pen):
        x, y = self.pos
        pen.color("RoyalBlue")
        pen.penup()
        pen.goto(x, y-8)
        pen.pendown()
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

class Path:
   def __init__(self):
      self.path = [(0, 12),
                   (47, 12),
                   (50, 72)]
   def draw(self, pen):
      pen.color("chocolate4")
      pen.width(5)
      pen.penup()
      for p in self.path:
         pen.goto(p)
         pen.pendown()

class game:
   def __init__(self, pen):
      self.items = []
      self.enemies = []
      self.towers = []
      self.bullets = []
      self.pen = pen
   def run(self):
      while True:
        for i in self.enemies:
          i.draw(self.pen)
        for i in self.towers:
          i.draw(self.pen)
        for i in self.bullets:
          i.draw(self.pen)
        for i in self.enemies:
           i.update()
        
pen = turtle.Turtle()

pen.speed(0)
tom = tower(50, 60)
tom.draw(pen)
ben = Path()
ben.draw(pen)
path = [(0, 12),
        (47, 12),
        (50, 72)]
bob = enemy(10, 500, path)
bob.update()
bob.draw(pen)
pen.clear()
bob.update()
bob.draw(pen)
pen.clear()
bob.update()
bob.draw(pen)
pen.clear()
turtle.done()
#turtle.tracer(0, 0)
#main = game(pen)
#main.enemies.append(bob)
#main.run()
# 0:12, 47:12
#0:21, 47:21