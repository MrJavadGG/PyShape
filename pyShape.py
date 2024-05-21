import turtle
print("\033[1;37;40m-------------------------")
def ShapeStart():
    color = int(input("The color list:\n\033[1;31;40mRed: 1\n\033[1;32;40mGreen: 2\n\033[1;34;40mBlue: 3\n\033[1;30;40mBlack: 4\n\033[1;33;40mYellow: 5\n\033[1;35;40mPurple: 6\n\033[1;36;40mCyan: 7\n\033[1;37;40mPlease enter the number of the color: "))

    match color:
        case 0:
            return()
        case 1:
            color = "red"
        case 2:
            color = "green"
        case 3:
            color = "blue"
        case 4:
            color = "black"
        case 5:
            color = "yellow"
        case 6:
            color = "purple"
        case 7:
            color = "cyan"

    shape = int(input("Enter the number of sides of shape: "))
    repeat = int(input("Enter the number of repetitions of the resaulting shape: "))
    move = float (360/shape)
    move2 = float (360/repeat)
    forward  = int(input("Enter the length of each side(50~100 recommended): "))

    t=turtle.Turtle()
    t.shape("turtle")
    t.hideturtle()
    t.speed("fast")
    t.color(color)
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    t.width(3)


    for i in range(repeat):
        for j in range(shape):
            t.forward(forward)
            t.right(move)
        t.right(move2)
    turtle.exitonclick()

    print("--------------------")
    print("--------------------")

ShapeStart()