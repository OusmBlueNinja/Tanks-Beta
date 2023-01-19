import os
import time
import json
import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame.locals import *
import pygame
import random



class b:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\u001b[31m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        WHITE = '\u001b[37m'



clock = pygame.time.Clock()

global path
path = os.path.dirname(os.path.realpath(__file__))
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
print(f"{b.OKBLUE}[INFO]{b.ENDC} Checking for Updates")
os.system('pip3 install -r ./src/data/config/requirements.txt')
f = open(f'{path}/src/data/config/config.json')
data = json.load(f)
Version = data['config']['version']
WindowName = data['config']['name']
f3 = open(f'{path}/src/data/config/splashData.json')
splashData = json.load(f3)
f3.close()
splashText = splashData[str(random.randint(1,20))]


width = len(splashText) * 20

 
        
print(f"{b.OKBLUE}[INFO]{b.ENDC} Loading Launcher")


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()  # initiates pygame
pygame.mixer.set_num_channels(64)
width, height = 720, 480
WINDOW_SIZE = (width, height)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) 

pygame.display.set_caption(WindowName + " " + Version + " Launcher")
Running = True

#________________________
# Init Font
#________________________
print(f"{b.OKCYAN}[DEBUG]{b.ENDC} Loading Fonts")
pygame.font.init()
Arial = pygame.font.SysFont('Arial', 35)
#try:
monospace = pygame.font.SysFont('monospace', 20)
#except:
 # print(f"{b.FAIL}[ERROR]{b.ENDC} Unable to load font Retros, Please install r#etros into your font derectory")
  #pygame.quit()
#  sys.exit()




#________________________
# Init Images
#________________________




print(f"{b.OKCYAN}[DEBUG]{b.ENDC} Loading Assets")
Title = pygame.image.load(f'{path}//src//assets//images//Title.png')
Splash = pygame.image.load(f'{path}//src//assets//images//Splash.png')
quit_img = pygame.image.load(f'{path}//src//assets//images//play.png')
play_img = pygame.image.load(f'{path}//src//assets//images//exit.png')
StudiosLogo = pygame.image.load(f'{path}//src//assets//images//Logo.png')
logo = pygame.image.load(f'{path}//src//assets//images//WindowLogo.png')

pygame.display.set_icon(logo)


#for song in range(len(songs)):
 # songs[song].set_volume(0.2)

print(f"{b.OKGREEN}[INFO]{b.ENDC} Assets Loaded")
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
  pygame.mixer.music.fadeout(1000)
  pygame.quit()
  print(f'{b.OKGREEN}[INFO] {b.ENDC}Launching {WindowName} {Version}')
  time.sleep(1)
  os.system('python ./src/main.py')
  sys.exit()
  
global shrink, size
size = [720,480]
shrink = True



def splashLenToPX(text):
  return len(text) * 12

screen.blit(StudiosLogo, (0,0))

pygame.display.update()
clock.tick(60)
  
time.sleep(3)



  
print(f"{b.OKCYAN}[DEBUG]{b.ENDC} Loading Sounds")

songs = [
                    "//src//assets//sound//music//(1).wav",
                    "//src//assets//sound//music//(2).wav",
                    "//src//assets//sound//music//(3).wav",
                    "//src//assets//sound//music//(4).wav",
                    "//src//assets//sound//music//(5).wav"
                ]

try:

  pygame.mixer.music.load(f'{path}{songs[random.randint(0,(len(songs)-1))]}')
  pygame.mixer.music.set_volume(0.2)
  pygame.mixer.music.play()  
  print(f"{b.OKGREEN}[INFO]{b.ENDC} Songs Loaded")
            
except:
  print(f'{b.FAIL}[ERROR]{b.ENDC} Unable to find song files, {path}//src//assets//sound//')  
  print(f'{b.FAIL}[ERROR]{b.ENDC} Process ednded with code 1')
  pygame.quit()
  sys.exit()
  

  
    
  
  
play = False
while Running:  # game loop
    screen.fill((0, 0, 0))  # clear screen
    
    if not pygame.mixer.music.get_busy():
        songs = [
                    "//src//assets//sound//music//(1).wav",
                    "//src//assets//sound//music//(2).wav",
                    "//src//assets//sound//music//(3).wav",
                    "//src//assets//sound//music//(4).wav",
                    "//src//assets//sound//music//(5).wav"
                ]
        try:

            pygame.mixer.music.load(f'{path}{songs[random.randint(0,(len(songs)-1))]}')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()  
            
        except:
          print(f'{b.FAIL}[ERROR]{b.ENDC} Unable to find song files, {path}//src//assets//sound//')  
          print(f'{b.FAIL}[ERROR]{b.ENDC} Process ednded with code 1')
          pygame.quit()
          sys.exit()

    #mousePos = pygame.mouse.get_pos()
    # debug(mousePos)
    
    
    if play:
      launch()

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            #save.save((player_rect.x), (player_rect.y))
            Running=False
            print(f"{b.WARNING}[WARNING]{b.ENDC} Closeing Launcher")
            pygame.mixer.music.fadeout(1000)
            pygame.quit()
            sys.exit()
            
    #debug(f"{dt}", 1)

    if Running:
      screen.blit(Title, (0,0))
      
      mouse_pos = pygame.mouse.get_pos()

        # print(mouse_pos)
      mousex = mouse_pos[0]
      mousey = mouse_pos[1]
      x = 0
      y = 0
      
      
                    
      if size[0] >= 1080:
        shrink = True
      elif size[0] <= 720:
        shrink = False

      if shrink:
        size[0] -= 10
        size[1] -= 10
      elif not shrink:
        size[0] += 10
        size[1] += 10
        
      pos = [360-size[0]/2,270-size[1]/2]
      
      Button_Pos = [[width/2-64, (height/2-32) + 160],[width/2-64, ((height/2-32) - 96) + 160]]
      
      if mousex >= Button_Pos[1][0] and mousex <= (Button_Pos[1][0] + 128):
            if mousey >= Button_Pos[1][1] and mousey <= (Button_Pos[1][1] + 64):
                if pygame.mouse.get_pressed() == (True, False, False):
                    play = True
                    
      if mousex >= Button_Pos[0][0] and mousex <= (Button_Pos[0][0] + 128):
            if mousey >= Button_Pos[0][1] and mousey <= (Button_Pos[0][1] + 64):
                if pygame.mouse.get_pressed() == (True, False, False):
                    Running=False
                    
                    print(f"{b.WARNING}[WARNING]{b.ENDC} Closeing Launcher")
                    pygame.quit()
                    sys.exit()
      
      Splash_Image_Animated = pygame.transform.scale(Splash, size)
      screen.blit(Splash_Image_Animated, pos)
      screen.blit(play_img, Button_Pos[0])
      screen.blit(quit_img, Button_Pos[1])
      #screen.blit(Splash.render("lmao"),(0,0,0), (0,0))
      screen.blit(monospace.render("{}".format(splashText),True, (0,0,0)), (width-splashLenToPX(splashText), height-25))
      pygame.display.update()
      clock.tick(60)


