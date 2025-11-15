import turtle
class enemy:
    def __init__(self, x, y):
      self.x = x
      self.y = y
      self.pos = (0, 0)
      self.alive = True
    def draw(self, pen):
        if not self.alive:
            return
        x, y = self.pos
        pen.color("red4")
        pen.penup()
        pen.goto(x, y-8)
        pen.pendown()
        pen.begin_fill()
        radius = 3
        pen.circle(3)
        pen.end_fill()
    def update(self):
       self.forward(5)
        

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
   def __init__(self):
      self.items = []
      self.enemies = []
      self.towers = []
      self.bullets = []
   def run():
      while True:
        enemy.draw()
        for i in self.enemies:
          i.draw()
        for i in self.towers:
          i.draw()
        for i in self.bullets:
          i.draw()
        for i in self.enemies:
           i.update()
        
pen = turtle.Turtle()
bob = enemy(10, 500)
bob.draw(pen)
pen.speed(0)
tom = tower(50, 60)
tom.draw(pen)
ben = Path()
ben.draw(pen)
turtle.done()

# 0:12, 47:12
#0:21, 47:21