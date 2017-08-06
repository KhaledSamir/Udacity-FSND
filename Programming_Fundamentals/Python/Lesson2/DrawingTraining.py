import turtle;
import random;


def draw_Initial():

    draw_K();
    draw_S();

def draw_K():
    
    window = turtle.Screen()
    window.bgcolor('black')
    k = turtle.Turtle()
    k.shape('turtle');
    
    k.setx(-100)
    #k.sety(-79);
    k.color('yellow')
    k.right(90)
    k.forward(180)
    k.right(180)
    k.forward(90)
    k.right(45)
    k.forward(120)
    k.left(180)
    k.forward(120)
    k.left(90)
    k.forward(120)
    
def draw_S() :
    
    s = turtle.Turtle()
    s.color('yellow')
    
    s.forward(90)
    s.left(180)
    s.forward(90)
   # s.heading()
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.right(90)
    s.forward(90)
    s.right(90)
    s.forward(90)
    
def draw_square():
    
    window = turtle.Screen()
    window.bgcolor('Red')
    brad = turtle.Turtle()
    brad.shape('turtle');
    brad.color('yellow')
    brad.speed(20)
    count = 36;
    
    for angle in range(0 , 500, 5):
        brad.setheading(angle)
        for x in range(0,4) :
            brad.forward(100);
            brad.right(90);
      #  count = count - 1;
      
     

    window.exitonclick()

def draw_Circle():

    mycircle = turtle.Turtle();
    mycircle.setx(20)
    mycircle.sety(50)
    mycircle.shape('circle')
    
    mycircle.circle(100);
    mycircle.color('black')

def draw_Triangle():
    triangle = turtle.Turtle();
    for angle in range(0 , 500, 5):
        triangle.setheading(angle)
        for x in range(0,4) :
            triangle.forward(100);
            triangle.right(45);
    
    triangle.shape('arrow');

def draw_shape():
    for i in range(0 , 200):
        draw_Triangle();
        
        
#draw_shape()
draw_Initial();
#draw_Circle();
#draw_square();
#draw_Triangle();

