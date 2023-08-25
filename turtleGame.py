import turtle
import random

turtle_board=turtle.Screen()
turtle_board.bgcolor("light blue")
turtle_board.title("turtle game")
turtle_list=[]
score_turtle=turtle.Turtle()
timer=turtle.Turtle()
gameover: bool = False

score_turtle.penup()
score_turtle.setposition(-350,300)
score_turtle.hideturtle()
score_turtle.color("red")
score_turtle.width(7)
score=0



def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        print(x,y)
        global score
        score=score+1
        score_turtle.clear()
        score_turtle.write(f"score: {score}",font=8)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.goto(x,y)
    turtle_list.append(t)
def setup_turtle():
  i=0
  j=300
  while i<5:
    i=i+1
    j=j-100
    make_turtle(j,200)
    make_turtle(j,100)
    make_turtle(j, 0)
    make_turtle(j,-100)

def hide_turtle():
    for t in turtle_list:
        t.hideturtle()


def turtles_random():
    if not gameover:
       turtle.ontimer(hide_turtle,400)
       random.choice(turtle_list).showturtle()
       turtle.ontimer(turtles_random, 800)


def turtle_timer_count(time):

    timer.penup()
    timer.setposition(-200, 300)
    timer.hideturtle()
    timer.color("red")

    if time>0:
        timer.clear()
        timer.write(f"timer: {time}",font=8)
        turtle.ontimer(lambda: turtle_timer_count(time-1),1000)
    else:
        gameover=True
        timer.clear()
        hide_turtle()
        timer.write(f"timer: {time}",font=8)




turtle.tracer(0)
setup_turtle()
hide_turtle()
turtles_random()
turtle_timer_count(15)
turtle.tracer(1)
turtle.mainloop()
turtle.done()
