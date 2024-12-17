
import turtle as trtl
trtl.speed(0)


class Turtles:
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

  def __init__(self):
    self.my_turtles = []



  def draw(self):
    for s in self.turtle_shapes:
      t = trtl.Turtle(shape=s)
      self.my_turtles.append(t)

    #  starting positional and heading and movementvariables
    startx = 0
    starty = 0
    heading = 0
    move = 50
    
    for t in self.my_turtles:
      tcolor = self.turtle_colors.pop()
      t.penup()
      t.goto(startx, starty)
      t.pendown()
      t.setheading(heading)
      t.pencolor(tcolor)
      t.fillcolor(tcolor)
      t.begin_fill()
      t.right(45)     
      t.forward(move)
      t.end_fill()

   
      startx = t.xcor()
      starty = t.ycor()
      heading  = t.heading()
      move = move*1.1
  
  def __str__(self):
    seen = [] #list  that checks for duplicates
    Turtles = [] #List  to store turtles
    for shape in self.turtle_shapes: 
      if shape not in seen: #checks for duplicates and then only adds once
       seen.append(shape)
       Turtles.append(shape)
    return f"All the unique shapes visible are {Turtles}"

draw = Turtles()
draw.draw()
print(draw)

wn = trtl.Screen()
wn.mainloop()
