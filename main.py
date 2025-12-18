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
    def tower_update(self, enemies, game):
      timer = 5
      minimum_distance = 10,000
      minimum_index = 0
      for e in enemies:
         p_x = self.x
         p_y = self.y
         x = e.x
         y = e.y
         dx = p_x - x
         dy = p_y - y
         h = math.sqrt(dx*dx + dy*dy)
         if minimum_distance > h:
            minimum_distance = h
            minimum_enemy =  e
      b = bullet(p_x, p_y, minimum_enemy)
      game.bullets.append(b)


      
    
class bullet:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def draw(self, pen):
      x, y = self.x, self.y
      pen.color("Black")
      pen.penup()
      pen.goto(x, y-8)
      pen.pendown()
      pen.forward(5)
   def __init__(self, x, y, enemy):
      self.x = x
      self.y = y
      self.enemy = enemy
   def bullet_update(self, enemies, game):
      x, y = self.pos
      print(self.pos)
      p_x, p_y = self.enemy.pos
      dx = p_x - x
      dy = p_y - y
      h = math.sqrt(dx*dx + dy*dy)
      if h < 5:
        self.enemy_pos += 1
      dx/=h
      dy/=h
      dx*=10
      dy*=10
      self.pos = (x + dx, y + dy)

      



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
          i.update()
        for i in self.towers:
          i.draw(pen)
          i.tower_update()
        for i in self.bullets:
          i.draw(pen)
          
          i.bullet_update()

        for i in self.enemies:
           self.a = input("press m to move")
           if self.a == "m":
            i.x += 100
            i.y += 100
           i.draw(pen)

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
for i in range(100):
   bob.update()
   bob.draw(pen)
   pen.clear()
turtle.tracer(0, 0)
main = game(pen)
main.paths.append(ben)
main.enemies.append(bob)
main.run(pen)
# 0:12, 47:12
#0:21, 47:21



turtle.done()