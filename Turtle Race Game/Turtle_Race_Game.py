from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(1920,1080)#we have adjusted the screen size
user_bet=screen.textinput("Make Your Bet","Wich Turtle Will Win The Race Enter A Color:")#the section where the bet is entered
colors=["red","orange","yellow","green","blue","purple"]
y_postion=[-100,-50,0,50,100,150]
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle("turtle")#we create new turtle with turtle shape
    new_turtle.shapesize(3)#we determine the shape of our turtles
    new_turtle.speed(8)#we determine the speed of our turtles
    new_turtle.color(colors[turtle_index])#we determine the color of our turtles from colors list
    new_turtle.penup()
    new_turtle.goto(x=-900, y=y_postion[turtle_index])  # we send our turtle to the starting coordinate point
    all_turtles.append(new_turtle) #we append the created turtle to our list
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>900:
            winner=(turtle.color())[0]
            if winner==user_bet:
                print("You Win!")
            else:
                print(f"You Lose! {winner} was won!")
            is_race_on=False
        number = random.randint(0, 30)# we create random number
        turtle.forward(number)# turtle moves forward by a random number

screen.exitonclick()
