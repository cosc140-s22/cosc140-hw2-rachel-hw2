#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################

import turtle

joel=turtle.Turtle()
s=joel.getscreen()
s.title("Florence the snowoman")
s.setworldcoordinates(0, 0, 400, 400)
joel.speed('fastest')
s.bgcolor("lightblue")

joel.pu()
joel.setpos(70, 375)
joel.pencolor("orange")
joel.width(4)
joel.pensize(4)
style=('Courier', 10)
joel.write("Florence the Snowoman", font=style)
joel.pd()
joel.pensize(1)

#grass
joel.pu()
joel.setpos(0, 60)
joel.pd()
joel.color("green")
joel.begin_fill()
for i in range(0,2):
  joel.forward(400)
  joel.rt(90)
  joel.forward(60)
  joel.rt(90)
joel.end_fill()

ypos=61
size=70
mid=190

#circle body parts
for i in range(0, 3):
  joel.penup()
  joel.setpos(mid, ypos)
  joel.pd()
  joel.color("black", "white")
  joel.begin_fill()
  joel.circle(size)
  joel.end_fill()
  size-=20
  ypos+=size+60

xpos=141
ypos=320
#hat
joel.color("black")
joel.width(2)
joel.pu()
joel.setpos(xpos, ypos)
joel.pd()
joel.forward(100)

joel.setpos((xpos*1.15), ypos)
joel.begin_fill()
for i in range(0, 3):
  joel.forward(55)
  joel.left(90)
joel.end_fill()

#nose
joel.pu()
joel.setpos(mid, 290)
joel.pd()
joel.color("orange")
joel.begin_fill()
joel.left(180)
joel.forward(5)
for i in range(0, 2):
  joel.right(120)
  joel.forward(15)
joel.end_fill()

#eyes
x=mid-10
for i in range(0, 2):
  joel.pu()
  joel.setpos(x,300)
  joel.pd()
  joel.dot(4, "black")
  x+=22

#buttons
yposbutton=200
for i in range (0,3):
  joel.pu()
  joel.setpos(mid, yposbutton)
  joel.pd()
  joel.dot(6, "black")
  yposbutton+=20

turtle.done()
