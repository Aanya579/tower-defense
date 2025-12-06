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
       if self.alive == False:
          return
       x, y = self.pos
       print(self.pos)
       p_x, p_y = self.path[self.path_pos]
       dx = p_x - x
       dy = p_y - y
       h = math.sqrt(dx*dx + dy*dy)
       if h < 5:
          self.path_pos += 1
       if self.path_pos == len(self.path):
          self.alive = False
       dx/=h
       dy/=h
       dx*=10
       dy*=10
       self.pos = (x + dx, y + dy)

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
    def tower_update():
       pass
    
class bullet:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def draw(self, pen):
      x, y = self.pos
      pen.color("Black")
      pen.penup()
      pen.goto(x, y-8)
      pen.pendown()
      pen.forward(5)

class Path:
   def __init__(self):
      self.path = [(100, 100),
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
      self.paths = []
      self.pen = pen
   def run(self, pen):
      while True:
        for i in self.enemies:
          i.draw(pen)
        for i in self.towers:
          i.draw(pen)
        for i in self.bullets:
          i.draw(pen)
        for i in self.enemies:
           i.update()
        for i in self.paths:
           i.draw(pen)
        pen.clear()
        
pen = turtle.Turtle()

pen.speed(0)
tom = tower(50, 60)
tom.draw(pen)
ben = Path()
ben.draw(pen)
path = [(100, 100),
        (47, 200),
        (50, 72)]
bob = enemy(10, 500, path)
# for i in range(100):
#    bob.update()
#    bob.draw(pen)
#   pen.clear()
sid = bullet()
sid.draw(pen)
#turtle.tracer(0, 0)
main = game(pen)
main.paths.append(ben)
main.enemies.append(bob)
main.run(pen)
# 0:12, 47:12
#0:21, 47:21



turtle.done()