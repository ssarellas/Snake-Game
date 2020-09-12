#Snake Game
#based on TokyoEdTech snake game

import turtle, time, random, sys

delay = 0.1

turtle.title('Snake Game')

#Score
score = 0
highScore = 0

#Colour options
options = ['red', 'blue', 'green', 'purple', 'orange', 'pink']
options1 = ['red', 'blue', 'green', 'purple', 'orange', 'pink']
sfood = options[random.randint(0,5)]
shead = options1[random.randint(0,5)]
sfood != shead

#Screen SetUp
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('white')
wn.setup(width=600, height=600)
wn.tracer(0) #turns off screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black',shead)
head.penup()
head.goto(0,0)
head.direction = 'stop'

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('black',sfood)
food.penup()
food.goto(0,100)

segments = []

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score: 0 High Score: 0', align = 'center', font=('Courier', 24, 'normal'))

#Functions
          
def goUp():
    if head.direction != 'down':
        head.direction = 'up'
def goDown():
    if head.direction != 'up':
        head.direction = 'down'
def goLeft():
    if head.direction != 'right':
        head.direction = 'left'
def goRight():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction =='up':
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction =='down':
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction =='left':
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction =='right':
        x = head.xcor()
        head.setx(x + 20)

#Keyboard bindings
wn.listen()
wn.onkeypress(goUp, 'w')
wn.onkeypress(goDown, 's')
wn.onkeypress(goLeft, 'a')
wn.onkeypress(goRight, 'd')


#Main game loop
while True:
    wn.update()
    
    #Collision w/ border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        
        #Hide segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        #Clear segments list
        segments.clear()
        
        #reset score
        score = 0

        #reset the delay
        delay = 0.1

        pen.clear()
        pen.write('Score: {} High Score {}'.format(score, highScore), align='center', font=('Courier', 24, 'normal'))

    #Collision w/ food
    if head.distance(food) < 20:
        
        #Move food to rand spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        
        # Add segment
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape('square')
        newSegment.color('black' ,'grey')
        newSegment.penup()
        newSegment.shapesize(0.8,0.8,0.8)
        segments.append(newSegment)

        # Shorten delay
        delay -= 0.001

        # Increase score
        score += 10

        if score > highScore:
            highScore = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal")) 

    #Move end segment 1st in reverse order
    for index in range(len(segments)-1, 0, -1):
        x =  segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
                                                            
    #Move segment 0 to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    
            
    #Head collision w/ body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
                                                            
            #Clear segments list
            segments.clear()
                                                            
            #Reset score
            score = 0
                                                            
            #Reset delay
            delay = 0.1
                                                            
            #Update score display
            pen.clear()
            pen.write('Score: {} High Score: {}'.format(score, highScore), align='center', font=('Courier', 24, 'normal'))
                                                            
    time.sleep(delay)

wn.mainloop()
