from __future__ import division
import pygame

class Grid:
    def __init__(self, vanishing_point, color, width, divisions):
        self.vanishing_point = vanishing_point
        self.color = color
        self.width = width
        self.divisions = divisions
        
    def draw(self, screen):
        screen_rect = screen.get_rect()
        divwidth = screen_rect.width//self.divisions
        for x in range(screen_rect.left, screen_rect.right+1, divwidth):
            pygame.draw.line(screen, self.color, (x,screen_rect.bottom), self.vanishing_point, self.width)
        
class Horizon:
    def __init__(self, positions, colors):
        try:
            self.y1,self.y2,self.y3 = positions
        except (ValueError,TypeError):
            raise TypeError("Invalid Position argument")
    
        try:
            self.c1,self.c2,self.c3 = colors
        except (ValueError,TypeError):
            raise TypeError("Invalid color argument")

    def draw(self, screen):
        screen_rect = screen.get_rect()
        
        top_box = pygame.Rect(screen_rect.left, screen_rect.top, screen_rect.width, self.y1)
        mid_box = pygame.Rect(screen_rect.left, screen_rect.top+self.y1, screen_rect.width, self.y2)
        bot_box = pygame.Rect(screen_rect.left, screen_rect.top+self.y1+self.y2, screen_rect.width, self.y3)
        
        screen.fill(self.c1, top_box)
        fill_gradient(screen, self.c2, self.c1, mid_box)
        fill_gradient(screen, self.c3, self.c2, bot_box) 
        
def fill_gradient(screen, color, gradient, rect=None, vertical=True, forward=False):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse
    
    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = screen.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(screen, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(screen, color, (col,y1), (col,y2))
            