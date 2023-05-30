import turtle as t
import random as rn
import keyboard as kb

score = 0
lvl = 0
a=12
b=12

#game ablakját megcsinálni
window = t.Screen()
window.title('SnakeGame')
window.screensize(800, 600)
window.tracer(0)
window.bgcolor('black')

# kígyócskát létre hozni
snake=t.Turtle()
snake.speed(5)
snake.shape('square')
snake.color('white')
snake.shapesize(stretch_wid=1, stretch_len=1)
snake.penup()
snake.goto(0, 0)
snake_moving_auto=0.1

#almát amit ehet a kígyócska
food = t.Turtle()
food.speed(0)
food.shape('circle')
food.penup()
food.color('red')
food.goto(100, 10)

#scoreboard
score = t.Turtle()
score.speed(0)
score.penup()
score.color('blue')
score.goto(260, 370)
score.hideturtle()
score.write('Eddig evett alma: {}' .format (a), align='center', font=('Monaco', 24, 'normal'))

#felső határ
bordedgeup= t.Turtle()
bordedgeup.goto(-450, 365)
bordedgeup.color('blue')
bordedgeup.write("______________________________________________________________________________________________________________________________________________________")

#a kígyó mozog 
def snake_up():
    y=snake.ycor()
    y=y+40
    snake.sety(y)

def snake_down():
    y=snake.ycor()
    y=y-40
    snake.sety(y)

def snake_turn_left() :
    x=snake.xcor()
    x=x-40
    snake.setx(x)

def snake_turn_right() :
    x=snake.xcor()
    x=x+40
    snake.setx(x)
    

window.listen()
window.onkeypress(snake_up, 'Up')
window.onkeypress(snake_down, 'Down')
window.onkeypress(snake_turn_left, 'Left')
window.onkeypress(snake_turn_right, 'Right')



while True:
    
    window.update()
    
    #határokat megcsinálni, magamat ne egyem meg
    #irányváltás
    #növekedés
    #gyorsulás kajálásonként

    last_key_press = ''
    def on_keypress(event):
        global last_key_press
        last_key_press = event.name
    kb.on_press(on_keypress)
   
       

    if (last_key_press=='Up'):
        snake.sety(snake.ycor() + snake_moving_auto)
    elif (last_key_press=='Down'):
        snake.sety(snake.ycor() + (snake_moving_auto*-1))
    elif (last_key_press=='Left'):
        snake.setx(snake.xcor() + (snake_moving_auto*-1))
    elif (last_key_press=='Right'):
        snake.setx(snake.xcor() + snake_moving_auto)
    else :
        snake.sety(snake.ycor() + snake_moving_auto)
        
    