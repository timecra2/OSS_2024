import tkinter as tk
import turtle, random
import math
import time

class PlayerTurtle(turtle.RawTurtle):
    def __init__(self,screen,step_move=10):
        super().__init__(screen)
        self.penup()
        self.color("red") 
        self.setx(0)
        self.sety(0)
        self.step_move = step_move
        self.left(90)
        self.shape("turtle")
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        

        screen.onkeypress(lambda: self.set_move_up(True), 'Up')
        screen.onkeyrelease(lambda: self.set_move_up(False),'Up')
        screen.onkeypress(lambda: self.set_move_down(True), 'Down')
        screen.onkeyrelease(lambda: self.set_move_down(False),'Down')
        screen.onkeypress(lambda: self.set_move_left(True), 'Left')
        screen.onkeyrelease(lambda: self.set_move_left(False),'Left')
        screen.onkeypress(lambda: self.set_move_right(True), 'Right')
        screen.onkeyrelease(lambda: self.set_move_right(False),'Right')
        screen.listen()

    def set_move_up(self,keyinput):
        self.move_up = keyinput
    def set_move_down(self,keyinput):
        self.move_down = keyinput
    def set_move_left(self,keyinput):
        self.move_left = keyinput
    def set_move_right(self,keyinput):
        self.move_right = keyinput

    def update_movement(self):

        dx,dy = 0,0

        if(self.move_up):
            dy += self.step_move
        if(self.move_down):
            dy -= self.step_move
        if(self.move_left):
            dx -= self.step_move
        if(self.move_right):
            dx += self.step_move

        if(dx != 0 and dy != 0):
            dx /= math.sqrt(2)
            dy /= math.sqrt(2)

        
        if(self.xcor() < -screen.window_width()/2):
            self.setx(-screen.window_width()/2)   
        elif(self.xcor() > screen.window_width()/2):
            self.setx(screen.window_width()/2)
        elif(self.ycor() < -screen.window_height()/2):
            self.sety(-screen.window_height()/2)
        elif(self.ycor() > screen.window_height()/2):
            self.sety(screen.window_height()/2)
        else:
            self.goto(self.xcor() + dx, self.ycor() + dy)

class EnemyTurtle(turtle.RawTurtle):
    def __init__(self,screen,player_turtle,step_move=5):
        super().__init__(screen)
        
        self.penup()
        self.setx(random.randint(int(-screen.window_width()/2),int(screen.window_width()/2)))
        self.sety(int(screen.window_width()/2)) 
        self.step_move = step_move
        self.shape("turtle")

        self.player_turtle = player_turtle
        self.setheading(math.degrees(math.atan2(player_turtle.ycor() - self.ycor(),player_turtle.xcor() - self.xcor())))

    def update_movement(self): 
        self.setheading(math.degrees(math.atan2(self.player_turtle.ycor() - self.ycor(),self.player_turtle.xcor() - self.xcor())))
        self.forward(self.step_move)

class MainGame:
    def __init__(self,screen,player,catch_radius=20):
        screen.onkeypress(lambda:(turtle.bye()),"Escape")
        self.running = False
        self.catch_radius = catch_radius
        self.clock = 0
        self.timepoint = time.time()
        self.catched = False
        self.screen = screen
        self.player = player
        self.enemyturtles = []
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()
        for i in range(0,1):
            self.enemyturtles.append(EnemyTurtle(screen,self.player))
    def is_catched(self):
        for turtle in self.enemyturtles:
            dx = self.player.xcor() - turtle.xcor()
            dy = self.player.ycor() - turtle.ycor()
            if(math.sqrt(dx*dx + dy * dy) < self.catch_radius):
                self.catched = True

    def start(self):
        self.running = True
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write('')
        self.action()
    
    def action(self):
        
        self.drawer.undo()
        self.drawer.write(f'You are escaping for {time.time() - self.timepoint:.2f} second')
        
        self.is_catched()
        
        if(self.catched):
            self.end()
        if self.running:

            self.player.update_movement()
            for turtle in self.enemyturtles:
                turtle.update_movement()

            self.clock += 1
            if(self.clock % 100 == 99):
                self.enemyturtles.append(EnemyTurtle(self.screen,self.player))
            self.screen.ontimer(self.action,1)
        

    def end(self):
        self.drawer.undo()
        self.drawer.write("You are catched! Press Escape key to exit")
        self.running = False
        
        
        
            

        
        










root = tk.Tk()
canvas = tk.Canvas(root,width=700,height=700)
canvas.pack()
screen = turtle.TurtleScreen(canvas)
t = PlayerTurtle(screen)

game = MainGame(screen,t)
game.start()
screen.mainloop()

