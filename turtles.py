import turtle

def drawSquare():
    canvass = turtle.Screen()
    canvass.bgcolor('blue')
    brad = turtle.Turtle()
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    canvass.exitonclick()
drawSquare()