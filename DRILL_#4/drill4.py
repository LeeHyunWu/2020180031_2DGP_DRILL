# drill4로 파일 이름을 저장한다.

import turtle

x = 0; y = 0

while y < 500: 
    while x < 500:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        x += 100
    y += 100
    x = 0

turtle.exitonclick()
