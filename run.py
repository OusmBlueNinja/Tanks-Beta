import os
import time
import json
import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame.locals import *
import pygame





clock = pygame.time.Clock()

global path
path = os.path.dirname(os.path.realpath(__file__))
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Downloading aditinal programs')
os.system('pip3 install -r ./src/data/config/requirements.txt')
f = open(f'{path}/src/data/config/config.json')
data = json.load(f)
Version = data['config']['version']
WindowName = data['config']['name']
clear()

pygame.init()
width, height = 720, 402
WINDOW_SIZE = (width, height)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) 

pygame.display.set_caption(WindowName + " " + Version + " Launcher")
Running = True

#________________________
# Init Font
#________________________

Arial = pygame.font.SysFont('Arial', 35)


#________________________
# Button function from Nytron
#________________________


def button_play(x, y, szey, szex, Color, text, hover_color):
        color = Color
        mouse_pos = pygame.mouse.get_pos()

        # print(mouse_pos)
        mousex = mouse_pos[0]
        mousey = mouse_pos[1]
        
        
        if mousex >= x and mousex <= (x + szex):
            if mousey >= y and mousey <= (y + szey):
                color = hover_color
                
                
                
                if pygame.mouse.get_pressed() == (True, False, False):
                    color = (0, 255, 0)
                    rect = pygame.draw.rect(screen, color, (x, y, szex, szey))
                    pygame.draw.rect(screen, color, rect)
                    words = Arial.render(str(text), True,(0,0,0))
                    screen.blit(words, (x+17, y+7.2))
                    return True
                  
                  
                else:
                  rect = pygame.draw.rect(screen, color, (x, y, szex, szey))
                  pygame.draw.rect(screen, color, rect)
                  words = Arial.render(str(text), True,(0,0,0))
                  screen.blit(words, (x+17, y+7.2))
                  return False

        rect = pygame.draw.rect(screen, color, (x, y, szex, szey))
        pygame.draw.rect(screen, color, rect)
        words = Arial.render(str(text), True,(0,0,0))
        screen.blit(words, (x+17, y+7.2))



def launch():
  pygame.quit()
  print(f'Launching {WindowName} {Version}')
  time.sleep(1)
  os.system('python ./src/main.py')
  sys.exit()
  
play = False
while Running:  # game loop
    screen.fill((0, 0, 0))  # clear screen
    

    #mousePos = pygame.mouse.get_pos()
    # debug(mousePos)
    szey, szex = 55,100
    pos = [(width/2)-55,(height/2)-100]
    play = button_play(((width/2 - (szex/2))-pos[0]), ((height/2 - (szey/2)) - pos[1]), szey, szex, (0,230,0), "Play", (0,205,0))
    
    if play:
      launch()

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            #save.save((player_rect.x), (player_rect.y))
            Running=False
            pygame.quit()
            sys.exit()
            
    #debug(f"{dt}", 1)

    if Running:
      pygame.display.update()
      clock.tick(60)


