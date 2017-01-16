import turtle

#draw a square
def draw_square(name):
    
    for i in range(4):
        name.forward(100)
        name.right(90)

#draw a triangle
def draw_triangle(name):
   
    for i in range(3):
        name.forward(100)
        name.left(120)

#draw a circle
def draw_circle(name):
    name.circle(100)

def draw_shapes():
    #open window
    window = turtle.Screen()
    window.bgcolor("blue") 

    #initialize turtles
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(2)

    #angie = turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("yellow")
    #angie.speed(2)

    #call square and triangle functions
    draw_square(brad)
    #draw_triangle(brad)
    #draw_circle(angie)

    window.exitonclick()

def draw_circle_from_square():
    #open window
    window = turtle.Screen()
    window.bgcolor("blue") 

    #initialize turtles
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(5)

    for i in range(0, 360, 10):
        draw_square(brad)
        brad.right(10)

def draw_flower():
    #open window
    window = turtle.Screen()
    window.bgcolor("blue") 

    #initialize turtles
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(10)

    for i in range(0, 360, 5):
        draw_diamond(brad)
        brad.right(5)
    brad.right(90)
    brad.forward(250)

def draw_diamond(name):
    for i in range(2):
        name.forward(100)
        name.right(45)
        name.forward(100)
        name.right(135)

draw_flower()
