from __future__ import division
import os, sys, pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'

RED = pygame.Color(255, 0 ,0, 100)
BLACK = pygame.Color(0, 0 ,0, 100)
DARKBLUE = pygame.Color(0, 0 ,50, 100)
TRANSPARENT = pygame.Color(0, 0 ,0, 0)
NEONBLUE = pygame.Color(0x67,0xC8,0xFF,100)
NEONPINK = pygame.Color(252,98,208,100)
GOLDENROD = pygame.Color(0xFF,0xB9,0x0F,100)

#admin settings
FIELD_SIZE = 900
MAX_LEVELS = 1000

class Horizon:
    def __init__(self, positions, colors=(BLACK,DARKBLUE,GOLDENROD)):
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

def draw_grid(screen, vanishing_point, color, divisions):
    screen_rect = screen.get_rect()
    divwidth = screen_rect.width//divisions
    for x in range(screen_rect.left, screen_rect.right+1, divwidth):
        pygame.draw.line(screen, color, (x,screen_rect.bottom), vanishing_point, 5)

def main():
    pygame.init()
    clock = pygame.time.Clock()  
    size = width, height = FIELD_SIZE, FIELD_SIZE
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont("Courier New", 18)
    
    horizon = Horizon((300,100,100), (BLACK,DARKBLUE,NEONPINK))
    
    while 1:
        dt = clock.tick(120) #limit to 60 fps
        read_keyboard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        screen.fill(BLACK)
        horizon.draw(screen)
        # draw_grid(screen, (450,screen.get_rect().height*2/3-50), NEONBLUE, 4)
        
        pygame.display.flip()

def read_keyboard():
    x = pygame.key.get_pressed()
    if x[pygame.K_ESCAPE] or x[pygame.K_q] or x[pygame.K_BREAK]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
if __name__ == "__main__":
    main()