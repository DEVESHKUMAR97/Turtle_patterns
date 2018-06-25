import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.penup()
turtle.goto(-50,-50)
turtle.pendown()
turtle.left(36)
turtle.color("blue","skyblue")
turtle.begin_fill()

def multiple_stars(turtle,size):
    if size >=10:
        for i in range(5):
            turtle.forward(size)
            multiple_stars(turtle,size/3)
            turtle.left(144)

multiple_stars(turtle,300)

turtle.end_fill()

turtle.penup()
turtle.goto(-140,-250)
turtle.pendown()
turtle.write("Clck here to Exit...")
turtle.exitonclick()
