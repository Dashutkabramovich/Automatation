from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

def ring(col, rad):
 
    # Set the fill
    my_turtle.fillcolor(col)
 
    # Start filling the color
    my_turtle.begin_fill()
 
    # Draw a circle
    my_turtle.circle(rad)
 
    # Ending the filling of the color
    my_turtle.end_fill()
    
# Draw second ear
my_turtle.up()
my_turtle.setpos(-195, 95)
my_turtle.down()
ring('green', 35)

my_turtle.up()
my_turtle.setpos(-165, 95)
my_turtle.down()
ring('green', 35)

my_turtle.up()
my_turtle.setpos(-135, 95)
my_turtle.down()
ring('green', 35)

my_turtle.up()
my_turtle.setpos(-105, 95)
my_turtle.down()
ring('green', 35)

my_turtle.up()
my_turtle.setpos(-85, 95)
my_turtle.down()
ring('green', 35)

my_turtle.up()
my_turtle.setpos(-55, 95)
my_turtle.down()
ring('green', 35)

# ножки
my_turtle.up()
my_turtle.setpos(-195, 85)
my_turtle.down()
ring('orange', 10)

my_turtle.up()
my_turtle.setpos(-165, 85)
my_turtle.down()
ring('orange', 10)

my_turtle.up()
my_turtle.setpos(-135, 85)
my_turtle.down()
ring('orange', 10)

my_turtle.up()
my_turtle.setpos(-105, 85)
my_turtle.down()
ring('orange', 10)

my_turtle.up()
my_turtle.setpos(-85, 85)
my_turtle.down()
ring('orange', 10)

my_turtle.up()
my_turtle.setpos(-55, 85)
my_turtle.down()
ring('orange', 10)

# фейс) 

my_turtle.up()
my_turtle.setpos(-15, 95)
my_turtle.down()
ring('green', 65)

my_turtle.up()
my_turtle.setpos(-25, 175)
my_turtle.down()
ring('red', 10)

my_turtle.up()
my_turtle.setpos(-5, 175)
my_turtle.down()
ring('red', 10)

my_turtle.up()
my_turtle.setpos(-25, 180)
my_turtle.down()
ring('black', 2)

my_turtle.up()
my_turtle.setpos(-5, 180)
my_turtle.down()
ring('black', 2)


my_turtle.up()
my_turtle.setpos(-15, 150)
my_turtle.down()
my_turtle.right(90)
my_turtle.circle(5, 180)
my_turtle.up()
my_turtle.setpos(-15, 150)
my_turtle.down()
my_turtle.left(360)
my_turtle.circle(5, -180)
my_turtle.hideturtle()



# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()

