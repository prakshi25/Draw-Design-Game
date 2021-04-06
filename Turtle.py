import turtle
color = input("Enter your choice of pen color: ")
sides = int(input("Enter the number of sides:"))

for steps in range(sides):
    turtle.color(color)
    turtle.forward(100)
    turtle.right(360/sides)
    for moresteps in range(sides):
        turtle.color(color)
        turtle.forward(50)
        turtle.right(360/sides)
