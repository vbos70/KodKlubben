from turtle import *

circle(100)
for r in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
    circle(r)

seth(180)
for r in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    circle(r)

penup()
goto(100,200)
pendown()
goto(-100,200)
goto(-100,-200)
goto(100,-200)
goto(100,200)

shape('turtle')

penup()
goto(0,0)
pendown()

seth(0)
pencolor("blue")
for r in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    circle(r + 5)

seth(180)
pencolor("yellow")
for r in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    circle(r + 5)
