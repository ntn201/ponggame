import pygame

BLUE = (244, 66, 92)

class BoxCollider:
    def __init__(self,obj,width,height):
        self.x = obj.x
        self.y = obj.y
        self.width = width
        self.height = height 

    def get_conner(self):
        return (
            self.x - self.width/2,
            self.x + self.width/2,
            self.y - self.height/2,
            self.y + self.height/2,
        )

    def collide_with(self,other):
        left1, right1, top1, bottom1 = self.get_conner()
        left2, right2, top2, bottom2 = other.get_conner()
        x_overlap = right2 >= left1 and left2 <= right1
        y_overlap = top2 <= bottom1 and bottom2 >= top1
        return x_overlap and y_overlap

    def collide_with_vertical(self,other):
        if not self.collide_with(other):
            return False
        top = (other.y + other.height/2) - (self.y - self.height/2) < 6
        bot = (self.y + self.height/2) - (other.y - other.height/2) < 6
        if top or bot:
            return True
        return False

    def collide_with_horizon(self,other):
        if not self.collide_with(other):
            return False
        left = (other.x + other.width/2) - (self.x - self.width/2) < 6
        right = (self.x + self.width/2) - (other.x - other.width/2) < 6 
        if left or right:
            return True
        return False

    def render(self, canvas):
        pygame.draw.rect(canvas,
                         BLUE,
                         (self.x - self.width / 2,
                          self.y - self.height / 2, self.width, self.height),
                         1)