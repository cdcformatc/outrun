import os, sys, pygame
from outrun import Horizon,Grid
os.environ['SDL_VIDEO_CENTERED'] = '1'

#admin settings
FIELD_SIZE = 900

RED = pygame.Color(255, 0 ,0, 100)
BLACK = pygame.Color(0, 0 ,0, 100)
DARKBLUE = pygame.Color(0, 0 ,50, 100)
TRANSPARENT = pygame.Color(0, 0 ,0, 0)
NEONBLUE = pygame.Color(0x67,0xC8,0xFF,100)
NEONPINK = pygame.Color(252,98,208,100)
GOLDENROD = pygame.Color(0xFF,0xB9,0x0F,100)

def read_keyboard():
    x = pygame.key.get_pressed()
    if x[pygame.K_ESCAPE] or x[pygame.K_q] or x[pygame.K_BREAK]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

def main():
    pygame.init()
    clock = pygame.time.Clock()  
    size = width, height = FIELD_SIZE, FIELD_SIZE
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont("Courier New", 18)
    
    horizon = Horizon((300,100,100), (BLACK,DARKBLUE,NEONPINK))
    grid = Grid((450,500),NEONBLUE,5,5)
    
    while 1:
        dt = clock.tick(120) #limit to 60 fps
        read_keyboard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        screen.fill(BLACK)
        horizon.draw(screen)
        grid.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()