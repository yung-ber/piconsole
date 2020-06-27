from time import*
from os import system
from random import*
try:
    import pygame
except:
    system('python -m pip install pygame --user')
    system('python3 -m pip install pygame --user')
    import pygame
class TextPrint:
    def __init__(self):
        self.reset()
        self.height = 15

    def Print(self, screen, textString, colour=(125,125,125)):
        font = pygame.font.Font(None, self.height)
        textBitmap = font.render(textString, True, colour)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
pygame.init()
white=255,255,255
screen=pygame.display.set_mode([800,600], pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
pygame.display.set_caption('piconsole')
logo=pygame.image.load('logo.png').convert()
tp = TextPrint()
for x in range(-800,0):
    screen.blit(logo,(x,0))
    pygame.display.update()
tp.Print(screen, "Loading...")
pygame.display.update()
pygame.joystick.init()
def unfs():
    pygame.quit()
    pygame.init()
    pygame.joystick.init()
def handle(event):
    global joystick
    if event.type == pygame.JOYBUTTONDOWN:
        if joystick.get_button(8) == 1:
            unfs()
            home()
unfs()
def home():
    global screen, joystick
    screen=pygame.display.set_mode([800,600], pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('piconsole')
    done=False
    clock=pygame.time.Clock()
    g=open('games')
    games=[]
    for game in g:
        games.append(game.replace('\n',''))
    game=1
    done=0
    while not done:
        hatmovement=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done=True
            if event.type == pygame.JOYHATMOTION:
                hatmovement=1
        screen.fill(white)
        tp.reset()
        tp.Print(screen, str(clock.get_fps())+' FPS')
        for x in range(10):
            tp.Print(screen, '')
        tp.indent()
        tp.indent()
        tp.height=40
        tp.Print(screen, games[game-1])
        tp.reset()
        numsticks=pygame.joystick.get_count()
        for i in range(numsticks):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            hats = joystick.get_numhats()
            for i in range(hats):
                if hatmovement:
                    hat = joystick.get_hat(i)
                    if hat == (1,0):
                        if game == len(games): game=1
                        else: game+=1
                    if hat == (-1,0):
                        if game == 1: game=len(games)
                        else: game-=1
            a=joystick.get_button(0)
            if a == 1:
                shade=255
                for x in range(255):
                    screen.fill((shade,shade,shade))
                    shade-=1
                    pygame.display.flip()
                    clock.tick(60)
                c=open('game/'+games[game-1])
                exec(c.read())
        pygame.display.flip()
        clock.tick(60)
home()
pygame.quit()
