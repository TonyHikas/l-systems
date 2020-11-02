from turtle import *

# settings
axiom = "F++F++F"
rule = "-2F3F-"
start_angle = 60
angle = 60
nesting = 12
length = 5

# apply rules
start = axiom
stack = []
for j in range(nesting):
    out = ""
    for i in axiom:
        if i == "F":
            out+=rule
        else:
            out+=i
    axiom = out
# print(axiom)

# draw
t = Turtle()
t.hideturtle()
t.screen.tracer(False)
t.screen.setup(800, 800)
t.pencolor("green")



# draw settings
def down(t):
    t.up()
    t.sety(t.ycor()-30)
    t.down()
t.up()
t.setpos(-380, 360)
t.down()
t.write('axiom = {}'.format(start), align="left", font = ( "Arial", 16, "normal" ))
down(t)
t.write('rule = {}'.format(rule), align="left", font = ( "Arial", 16, "normal" ))
down(t)
t.write('start_angle = {}'.format(start_angle), align="left", font = ( "Arial", 16, "normal" ))
down(t)
t.write('angle = {}'.format(angle), align="left", font = ( "Arial", 16, "normal" ))
down(t)
t.write('nesting = {}'.format(nesting), align="left", font = ( "Arial", 16, "normal" ))
down(t)
t.write('length = {}'.format(length), align="left", font = ( "Arial", 16, "normal" ))

# draw system
t.up()
t.setpos(0, -250) # начальная позиция(изменять, если требуется сместить рисунок)

t.down()
if __name__ == "__main__":
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
