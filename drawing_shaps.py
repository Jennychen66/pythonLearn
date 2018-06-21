import turtle

print "start drawing"

def draw_thing():
    window = turtle.Screen()
    window.bgcolor("green")
        
    brad = turtle.Turtle()
    turtle.speed('slow')
    turtle.shape('circle')
    turtle.color("#285078","#a0c8f0")
    count = 0;
    while(count < 4):
        brad.forward(100)
        brad.right(90)
        count = count + 1
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color('yellow')
    angie.circle(100)

    bike = turtle.Turtle()
    bike.shape('triangle')
    bike.color('#ffffff')
    bike.circle(20)
    window.exitonclick()

draw_thing()
