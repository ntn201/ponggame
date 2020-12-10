import pygame
from boxcollider import BoxCollider

class paddle:
    # properties
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Assets\paddle.png")
        self.up_press = False
        self.down_press = False
        self.boxcollider = BoxCollider(self,self.image.get_width(),self.image.get_height())
        self.active = True

    #method
    def move(self):
        if self.up_press:
            self.y -= 10
        if self.down_press:
            self.y += 10
            
    def update(self,canvas):
        self.move()
        self.boxcollider.x = self.x
        self.boxcollider.y = self.y
        width = self.image.get_width()
        height = self.image.get_height()
        render_pos = (self.x - width/2, self.y - height/2)
        canvas.blit(self.image,render_pos)
        self.boxcollider.render(canvas)