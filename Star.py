#Nicolas Tracewell
#ntracewe@ucsc.edu
#programming assignment 2
#This program draws a star with n points (given input n).

import turtle
n=int(input("Enter an odd integer greater than or equal to 3: "))
star=turtle.Turtle()
wn=turtle.Screen()
wn.title(str(n)+"-pointed Star")
star.color("blue","lightgreen")
star.pensize(2)
star.speed(10)
star.hideturtle()
star.penup()
star.goto(-150,0)
star.pendown()
star.showturtle()
star.begin_fill()
for x in range(n):
    star.forward(300)
    star.right(180-180/n)
    star.dot(10,"red")
star.hideturtle()
star.end_fill()
wn.mainloop()
