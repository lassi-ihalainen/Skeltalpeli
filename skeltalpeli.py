import pygame
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

display_width = 1280
display_height = 720

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

dooted = 0
Thankscore = 0

DootyFont = pygame.font.SysFont("comicsansms", 40)

gameDisplay = pygame.display.set_mode ((display_width, display_height))
pygame.display.set_caption("DOOT.EXE")
clock = pygame.time.Clock()

DootlessSkeltal = pygame.image.load('C:/Users/lassi/Documents/Python/mrSkeltal.jpg')
DootedSkeltal = pygame.image.load('C:/Users/lassi/Documents/Python/mrSkeltal2.jpg')
DootSound1 = pygame.mixer.Sound("C:/Users/lassi/Documents/Python/Trumpet1.wav")
DootSound2 = pygame.mixer.Sound("C:/Users/lassi/Documents/Python/Trumpet2.wav")
DootSound3 = pygame.mixer.Sound("C:/Users/lassi/Documents/Python/Trumpet3.wav")
DootSound4 = pygame.mixer.Sound("C:/Users/lassi/Documents/Python/Trumpet4.wav")
gameExit = False

def start_screen():
    gameDisplay.fill(white)
    textSurf = DootyFont.render ("Press spacebar to Thank mr. Skeltal", 1, black)
    gameDisplay.blit(textSurf, (300, (display_height/2 - 20)))
    pygame.display.update()
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game(dooted, Thankscore)
                
def score (Thankscore):
    ScoreSurf = DootyFont.render ("Thanked: "+ str(Thankscore), 1, red)
    gameDisplay.blit(ScoreSurf, (20,20))
    pygame.display.update()
    
def game(dooted, Thankscore):
    while not gameExit:
        gameDisplay.blit(DootlessSkeltal, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dooted += 1
                    Thankscore += 1
                    gameDisplay.blit(DootedSkeltal, (0, 0))
                    score (Thankscore)
                    pygame.display.update()
                    
                    if dooted == 1:
                        DootSound1.play()
                    elif dooted == 2:
                        DootSound2.play()
                    elif dooted == 3:
                        DootSound3.play()
                    elif dooted == 4:
                        DootSound4.play()
                        dooted = 0
                        
                    time.sleep(0.5)
                    gameDisplay.blit(DootlessSkeltal, (0, 0))
                    pygame.display.update()
            
        score (Thankscore)
        clock.tick(60)
        game(dooted, Thankscore)
        
start_screen()
pygame.quit()
quit()
