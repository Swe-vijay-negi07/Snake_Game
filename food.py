from turtle import Turtle
import random
class Food(Turtle):        
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5,stretch_wid = 0.5) #now the circel will be of 10 by 10 circle size.
        self.color("blue")
        self.speed("fastest")
        self.refresh()

        
    def refresh(self):  #moving food  to random loction
        random_x = random.randint(-280,270) 
        random_y = random.randint(-280,270) 
        self.goto(random_x,random_y)
        
        
