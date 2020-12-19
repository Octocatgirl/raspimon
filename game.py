from sense_hat import SenseHat
import time
import random

s = SenseHat()
s.clear()

# colors 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0) #blank
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PINK = (255, 128, 128)
PURPLE = (128, 0, 128)
DARKPINK = (255, 0, 128)
LIGHTGREEN = (128, 255, 128)



# s.set_pixel(player_x,player_y, PINK)

#food positioning

# s.set_pixel(food_x,food_y, PURPLE)

# is_hungry = True


class Game:
    def __init__(self):
        self.time = 0
        self.player_x = 1 
        self.player_y = 1

        self.max_coor = 7
        self.min_coor = 0

        self.food_x = 0
        self.food_y = 0
        
        self.is_hungry = True
        pass

    def move_player_down(self):
        self.player_y 
        if self.player_y < 7:
            self.player_y += 1
            print("y:" + str(self.player_y))

    def move_player_up(self):
        if self.player_y > 0:
            self.player_y -= 1
            print("y:" + str(self.player_y))
    
    def move_player_left(self):
        if self.player_x > 0:
            self.player_x -= 1
            print("x:" + str(self.player_x))

    def move_player_right(self):
        if self.player_x < 7:
            self.player_x += 1
            print("x:" + str(self.player_x))

    def move_food_down(self):
        self.food_y 
        if self.food_y < 7:
            self.food_y += 1
            print("y:" + str(self.food_y))

    def move_food_up(self):
        if self.food_y > 0:
            self.food_y -= 1
            print("y:" + str(self.food_y))
    
    def move_food_left(self):
        if self.food_x > 0:
            self.food_x -= 1
            print("x:" + str(self.food_x))
        

    def move_food_right(self):
        if self.food_x < 7:
            self.food_x += 1
            print("x:" + str(self.food_x))

    def set_food(self):

        self.food_x = random.randint(0,7)
        self.food_y = random.randint(0,7)

        print("food y : " + str(self.food_y))
        print("food x : " + str(self.food_x))
        self.update()

        if self.food_x == self.player_x and self.food_y == self.player_y:
            self.set_food()

    def update(self):
        s.clear()
        s.set_pixel(self.player_x,self.player_y, RED)
        s.set_pixel(self.food_x,self.food_y, GREEN)

    def move_food(self):
        self.num = random.randint(0,3)
        
        if self.num == 0:
            self.move_food_down()
            
        if self.num == 1:
            self.move_food_right()
            
        if self.num == 2:
            self.move_food_left()
        
        if self.num == 3:
            self.move_food_up()
        
        self.update()
        time.sleep(0.5)

    def reset(self):
        s.clear()
        self.player_x = random.randint(0,7)
        self.player_y = random.randint(0,7)

    def run(self):
        self.reset()
        self.update()
        self.set_food()

    def timer(self):
        self.time += 1
        time.sleep(1)

        while self.is_hungry:
            self.move_food()
            timer()
            for event in s.stick.get_events():
                #print(event)
                if event.direction == "down" and event.action == "released":
                    self.move_player_down()
    
                    self.update()
                elif event.direction == "up" and event.action == "released":
                    self.move_player_up()
                    
                    self.update()
                elif event.direction == "right" and event.action == "released":
                    self.move_player_right()
               
                    self.update()
                elif event.direction == "left" and event.action == "released":
                    self.move_player_left()
        
                    self.update()

                elif self.player_x == self.food_x and self.player_y == self.food_y:
                    self.score += 1
                    s.show_message("YOU WIN!   Time (secs): ")
                    s.show_letter(str(self.time))
                    self.is_hungry = False

# my_game = Game()
# my_game.run()


### Old Code 
# def down():
#     global player_y 
#     if player_y < 7:
#         player_y += 1
#         print("y:" + str(player_y))

# def up():
#     global player_y 
#     if player_y >= 0:
#         player_y -= 1
#         print("y:" + str(player_y))

# while is_hungry:
#     for event in s.stick.get_events():
#         #print(event)
        
#         if event.direction == "down" and event.action == "released":
#             down()
#             update()

#         elif event.direction == "up" and event.action == "released":
#             up()
#             update()

#         elif event.direction == "right" and event.action == "released":
#             print("right")
#         elif event.direction == "left" and event.action == "released":
#             print("left")

# def update():
#     s.clear()
#     s.set_pixel(player_x,player_y, PINK)
#     s.set_pixel(food_x,food_y, PURPLE)       








