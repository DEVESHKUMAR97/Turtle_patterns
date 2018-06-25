import turtle

turtle.color("red","yellow")
turtle.begin_fill()

for i in range(50):
    turtle.forward(200)
    turtle.right(170)
    if abs(turtle.pos()) < 1:
        break

turtle.end_fill()

turtle.penup()
turtle.goto(-140,-250)
turtle.pendown()
turtle.write("Clck here to Exit...")
turtle.exitonclick()
