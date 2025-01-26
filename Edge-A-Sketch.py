import turtle as t

tim = t.Turtle()
screen = t.Screen()


def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen() #to make screen start listening
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

