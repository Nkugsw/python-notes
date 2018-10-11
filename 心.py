import turtle
import time
def jiajia():
    for i in range (200):
        turtle.right(1)
        turtle.forward(1)
turtle.color('red','pink')
turtle.pensize(2)
turtle.speed(10)
turtle.goto(0,0)

turtle.begin_fill()
turtle.left(140)
turtle.forward(112)
jiajia()
turtle.left(120)
jiajia()
turtle.forward(112)
turtle.end_fill()
turtle.up()
turtle.goto(100,-10)
turtle. write("佳佳", move=True, align="left", font=("宋体", 30, "normal"))
