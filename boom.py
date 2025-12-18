import turtle
import random
screen = turtle.Screen()
goal = turtle.Turtle()
goal.shape("square")
player = turtle.Turtle()
player.shape("arrow")
timer = 30000
goal.penup()
def forward():
   player.forward(50)
def right():
   player.right(90)
def left():
   player.left(90)
screen.onkeypress(forward, "Up")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
goal.goto(random.randint(-200, 200), random.randint(-200, 200))


screen.listen()
turtle.mainloop()
