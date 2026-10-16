import turtle

def MyTurtle(shape, repeat, forward, color):

    t=turtle.Turtle()
    t.shape("turtle")
    t.hideturtle()
    t.speed("fast")
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    t.width(3)

    move = float (360/shape)
    move2 = float (360/repeat)
    t.color(color)

    for i in range(repeat):
        for j in range(shape):
            t.forward(forward)
            t.right(move)
        t.right(move2)
    turtle.exitonclick()