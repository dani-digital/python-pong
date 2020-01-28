import turtle
import winsound
import os

wn = turtle.Screen()
wn.title("Pong by @droneal11015")
wn.bgcolor("gray")
wn.setup(width=800, height=600)
wn.tracer(0)


#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("pink")
ball.penup()
ball.goto(0, 0)
ball.dx = .18 #ball speed for x position
ball.dy = .18 #ball speed for y position

#ScoreBoard Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) #default score of 0

#game function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y) #sets paddle to the new y coordinate  

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y) #sets paddle to the new y coordinate  

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking and scoring
    if ball.ycor() > 290:
        ball.sety(290) #if ball hits top of window
        ball.dy *= -1 #reverses direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay bounce.wav&")
    
    if ball.ycor() < -290:
        ball.sety(-290) #if ball hits bottom of window
        ball.dy *= -1 #reverses direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay bounce.wav&")


    if ball.xcor() > 390:
        ball.goto(0, 0) #if ball hits right side of window, goes back to center
        ball.dx *= -1 #reverses direction
        score_a += 1 #adds 1 to Player A's score
        pen.clear() #clears previous score for new score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #new score

    if ball.xcor() < -390:
        ball.goto(0, 0) #if ball hits left side of window, goes back to center
        ball.dx *= -1 #reverses direction
        score_b += 1 #adds 1 to Player B's score
        pen.clear() #clears previous score for new score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #new score
        
    
    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay bounce.wav&")


    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50)):
        ball.setx(-340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        os.system("afplay bounce.wav&")
