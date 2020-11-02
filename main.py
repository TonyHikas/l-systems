from turtle import *

# settings
axiom = "FF+F-FF-F+FF"
rule = "[3F]-2F++2F-[3F]"
start_angle = 90
angle = 25
nesting = 4
length = 5

# apply rules
stack = []
for j in range(nesting):
    out = ""
    for i in axiom:
        if i == "F":
            out+=rule
        else:
            out+=i
    axiom = out
print(axiom)

# draw
t = Turtle()
t.hideturtle()
t.screen.tracer(False)
t.screen.setup(800, 800)
t.up()
t.setpos(0, -250)
t.down()

t.pencolor("green")
t.left(start_angle)
for i in axiom:
    if i == "F":
        t.forward(length)
    elif i == "b":
        t.up()
        t.forward(length)
        t.down()
    elif i == "[":
        stack.append(t.xcor())
        stack.append(t.ycor())
        stack.append(t.heading())
    elif i == "]":
        t.up()
        t.setheading(stack.pop())
        t.sety(stack.pop())
        t.setx(stack.pop())
        t.down()
    elif i == "+":
        t.right(angle)
    elif i == "-":
        t.left(angle)

t.screen.exitonclick()
t.screen.mainloop()
