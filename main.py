# This snake will contain 7 section.
# Section 1 -> Create a snake body
# Section 2 -> Move the snake
# Section 3 -> Control the snake
# Section 4 -> Detect collision with food
# Section 5 -> Create a scoreboard
# Section 6 -> Detect collision with wall
# Section 7 -> Detect collision with tail


from turtle import Screen  
from snake import Snake 
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width = 600,height = 600) 
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


#''' ===================================================================================================================================================================================================================================='''

    # Section 1 -> create snake section

snake = Snake() #object of class Snake
food = Food() # object of class food
scoreboard = Scoreboard() #object of class Scoreboard


#'''=========================================================================================================================================================================================================================================='''

#'''================================================================================================================================================

    # Section 3 -> control  section
screen.listen()          
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#'''======================================================================================================================






#'''==============================================================================================================================================================

game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)
    
    
#'''===================================================================================================================================================================================================================================================================================================='''
      # Section 2 -> snake move section
    snake.move()
    
#'''======================================================================================================================================================================================================================================================================================================='''    

#===========================================================================================================================================================

       #Section 4 ->Detect collision with food.

    

    if snake.head.distance(food) < 15:
        food.refresh() 
        snake.extend() 


#==================================================================================================================================================

    #section 5 --> Create a scoreboard 
        scoreboard.increase_score() 
#===========================================================================================================================================================

      # Section 6 -> Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        game_is_on=False
        scoreboard.game_over()
        
#===============================================================================================================================================================
        # Section 7 -> Detect collision with tail

    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()



