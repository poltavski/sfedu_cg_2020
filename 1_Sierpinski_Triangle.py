import turtle
import numpy as np

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['yellow','blue', 'white', 'red',  'green','white',
                'violet','orange']
    drawTriangle(points, colormap[degree], myTurtle)
    # n = np.random.choice(6, 1)
    if degree > 0:
        # if n <= 2:
            print("first triangle recursive: ", [points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])])
            sierpinski([points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                       degree-1, myTurtle)
        # if 2 < n and n <=4:
            print("second triangle recursive: ", [points[0],
                   getMid(points[0], points[1]),
                   getMid(points[1], points[2])])
            sierpinski([points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                       degree-1, myTurtle)
        # if 4 < n and n <= 6:
            print("third triangle recursive: ", [points[0],
                   getMid(points[2], points[1]),
                   getMid(points[0], points[2])])
            sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,0],[0,150],[100,0]]
   sierpinski(myPoints, 3, myTurtle)
   myWin.exitonclick()

main()