import turtle
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("pink")
t2 = turtle.Turtle()
t2.hideturtle()
t2.penup()
t.penup()
t.goto(0,50)
t.write("My Favorites!",font=("arial",30,'bold'),align="center")
t.penup()
t.goto(0,-50)
t.write("By Riya Timsina",font=("arial",20,'bold'),align="center")

t2.goto(-200,0)
turtle.addshape("fav2.gif")
t2.shape("fav2.gif")
a = t2.stamp()
t2.goto(-100,0)

t2.goto(170,0)

turtle.addshape("fav1.gif")
t2.shape("fav1.gif")
a = t2.stamp()



#square
t.penup()
t.goto(0,-5)
t.pendown()
t.fillcolor("purple")
t.penup()
t.goto(-50,-100)
t.pendown()
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.penup()
t.end_fill()

#END OF FIRST SCREEN


enter = input("enter to go to 2nd screen")
t.clear()
t2.clear()
screen.bgcolor("cornflower blue")

 #START OF SECOND SCREEN
t2.goto(-20,0)
turtle.addshape("grapes.gif")
t2.shape("grapes.gif")
a = t2.stamp()


t2.goto(200,0)

turtle.addshape("rice.gif")
t2.shape("rice.gif")
a = t2.stamp()
t2.goto(500,0)

t2.goto(-200,0)

turtle.addshape("dumpling.gif")
t2.shape("dumpling.gif")
a = t2.stamp()
t2.goto(200,0)

t.penup()
t.goto(0,-250)
t.write("Favorite Foods",font=("arial",20,'bold'),align="center")
t.penup()

t.penup()
t.goto(150,-100)
t.write("Rice",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-100)

t.write("grapes",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(-160,-100)
t.write("dumplings",font=("arial",15,'bold'),align="center")
t.penup()


#triangle
t.penup()
t.goto(-50,100)
t.pendown()
t.fillcolor("purple")
t.begin_fill()
t.goto(50,100)
t.goto(0,200)
t.goto(-50,100)
t.end_fill()
t.penup()

#END OF SECOND SCREEN

enter = input("enter to go to 3rd screen")
t.clear()

screen.bgcolor("orange")

t2.hideturtle()
t2.clear()

# START OF THIRD SCREEN
t2.goto(250, 0)

turtle.addshape("sleep.gif")
t2.shape("sleep.gif")
a = t2.stamp()
t2.goto(-100,0)

t2.goto(10,0)

turtle.addshape("dance.gif")
t2.shape("dance.gif")
a = t2.stamp()
t2.goto(500,0)

t2.goto(-200,0)
turtle.addshape("cook.gif")
t2.shape("cook.gif")
a = t2.stamp()
t2.goto(-100,0)

t2.goto(120,0)

turtle.addshape("travel.gif")
t2.shape("travel.gif")
a = t2.stamp()
t2.goto(500,0)



t.penup()
t.goto(0,-250)
t.write("Favorite Hobbies",font=("arial",20,'bold'),align="center")
t.penup()

t.penup()
t.goto(250,-100)
t.write("sleeping",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(150,-100)
t.write("travel",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(10,-100)
t.write("dance",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(-160,-100)
t.write("cooking",font=("arial",15,'bold'),align="center")
t.penup()

#octagon
t.fillcolor('yellow')
t.begin_fill()
t.penup()
t.goto(0,100)
t.pendown()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()

#END OF 3RD SCREEN

enter = input("enter to go to 4th screen")
t.clear()
t2.clear()


screen.bgcolor("purple")

#START OF 4TH SCREEN

t2.goto(100,0)

turtle.addshape("moana1.gif")
t2.shape("moana1.gif")
a = t2.stamp()
t2.goto(800,0)

t2.goto(-200,0)
turtle.addshape("moana2.gif")
t2.shape("moana2.gif")
a = t2.stamp()
t2.goto(-100,0)

t2.goto(120,0)

t.penup()
t.goto(10,-100)
t.write("Moana 2",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-250)
t.write("Favorite Movie",font=("arial",20,'bold'),align="center")
t.penup()

#circle
t.fillcolor('green')
t.begin_fill()
t.goto(0,100)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t2.penup()
#END OF 4TH SCREEN

enter = input("enter to go to 5th screen")
t.clear()
t2.clear()
screen.bgcolor("green")

#STAR OF 5TH SCREEN

t.penup()
t.goto(10,-100)
t.write("dance",font=("arial",15,'bold'),align="center")
t.penup()

t.penup()
t.goto(0,-250)
t.write("Favorite Sport",font=("arial",20,'bold'),align="center")
t.penup()

#diamond
t.fillcolor("cornflower blue")
t.setheading(135)

t.goto(180,0)
t.pendown()
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.penup()
t.end_fill()
t.setheading(0)


t2.goto(-100,0)
turtle.addshape("dance1.gif")
t2.shape("dance1.gif")
a = t2.stamp()
t2.goto(-100,0)

t2.goto(90,-20)

turtle.addshape("dance2.gif")
t2.shape("dance2.gif")
a = t2.stamp()
#END OF 5TH SCREEN



turtle.done()