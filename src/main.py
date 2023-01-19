import os
import time
LoadTime = time.time()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import math
import json
import random
import sys
import pygame
from pygame.locals import *



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


global path
path = os.path.dirname(os.path.realpath(__file__))
f = open(f'{path}\\data\\config\\config.json')
data = json.load(f)
DEBUG = data['config']['debug']


def debug(data, sevarity: int):

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
    if sevarity == 0:
        print(f'\r{b.OKGREEN}[OUTPUT]{b.ENDC} {data}')

    elif sevarity == 2:
        print(f'\r{b.WARNING}[WARNING]{b.ENDC} {data}')
    elif sevarity == 3:
        print(f"\r{b.FAIL}[ERROR]{b.ENDC} {data}")
    elif sevarity == 4:
        print(f'\r{b.OKBLUE}[INFO]{b.ENDC} {data}', end="")
    elif DEBUG:
        if sevarity == 1:
            print(f'\r{b.OKCYAN}[DEBUG]{b.ENDC} {data}')


os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


clock = pygame.time.Clock()


debug("Loading Config", 1)
# get Config Files
f2 = open(f'{path}\\data\\config\\config.json')
data = json.load(f2)
f2 = open(f'{path}\\data\\config\\settings.json')
data2 = json.load(f2)
resoloution = data2['Resolution']
width, height = data['config']['resolutions'][resoloution]['width'], data['config']['resolutions'][resoloution]['height']
WindowName = data['config']['name']
Version = data['config']['version']
CHUNK_SIZE = data['config']['Render-Distance']

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()  # initiates pygame
pygame.mixer.set_num_channels(64)

pygame.display.set_caption(WindowName + " " + Version)

WINDOW_SIZE = (width, height)

SURFACE_SIZE = (720, 480)

Velocity = 150


screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window


display = pygame.Surface(
    (720, 480))  # used as the surface for rendering, which is scaled


###########################
#       Load Assets       #
###########################
assets = "/assets"
sound = "/sound"
music = "/music"
tools = "/tools"
entities = "/entities"
images = "/images"
world = "/world"






debug(f"Loading Sounds",1)

songs = [
                    "//assets//sound//music//(1).wav",
                    "//assets//sound//music//(2).wav",
                    "//assets//sound//music//(3).wav",
                    "//assets//sound//music//(4).wav",
                    "//assets//sound//music//(5).wav"
                ]

try:

  pygame.mixer.music.load(f'{path}{songs[random.randint(0,(len(songs)-1))]}')
  pygame.mixer.music.set_volume(0.2)
  pygame.mixer.music.play()  
  debug(f"Songs Loaded", 1)
            
except:
  debug(f'Unable to find song files, {path}//src//assets//sound//', 3)  
  debug(f'Process ednded with code 1', 3)
  pygame.quit()
  sys.exit()
#debug("Loading scope_img",1)
# scope_img = pygame.image.load(
#    f'{path}//{assets}//{images}//{entities}//scope.png')
#debug("Loading treeSmall",1)
# treeSmall = pygame.image.load(
#    f'{path}//{assets}//{images}//{world}//treeSmall.png')

allAssets = []


# file name | folder name
assetList = [
                ["scope", "entities"],
                ["treeSmall", "world"],
                ["tankGreen", "entities"],
                ["barrelGreen", "entities"],
                ["tracksSmall", "entities"]
            ]


for i in range(len(assetList)):
    debug(f"Loading {assetList[i][0]}", 1)
    allAssets.append(pygame.image.load(
        f'{path}//{assets}//{images}//{assetList[i][1]}//{assetList[i][0]}.png'))


###########################
#      Set FX Volume      #
###########################


pygame.mixer.music.set_volume(0.5)


###########################
#      Entity Classes    #
###########################


class Entity:
    def __init__(self, x, y, width, height, image):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.image = image
        self.Zero = (((SURFACE_SIZE[0]/2)-(75/2)), (SURFACE_SIZE[1]/2)-(70/2))
        self.Gun_image = pygame.transform.rotate(allAssets[3], 0)
        self.offset = [ self.image.get_width() / 2  , self.image.get_height() / 2 ]
      

    def WeaponRotation(self, display):
        
        mousePos = pygame.mouse.get_pos()
        
        
        

        rel_x, rel_y = mousePos[0] - self.x, mousePos[1] - self.y
        angle = -math.atan2(self.Zero[1] + self.offset[1]- mousePos[1], self.Zero[0] + self.offset[0] - mousePos[0]) * ( 180 / math.pi )
        angle = angle + 90
        
        #debug(f"{angle}", 0)

        self.Gun_image = pygame.transform.rotate(allAssets[3], angle)
        
        axis = ( (self.Zero[0] - int(self.Gun_image.get_width() / 2 ) + self.offset[0]) , (self.Zero[1] - int(self.Gun_image.get_height() / 2 ) + self.offset[1])  )
        
        pygame.Surface.blit(display, self.Gun_image, axis)

    def main(self, display):
        
        
        obj_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.Surface.blit(display, self.image, self.Zero)
        
    def rotateImage(self, direction: int):
        
        angle = 45 * direction
        
        self.image = pygame.transform.rotate(allAssets[2], angle)
        


# init
# X Y ( Size )
player = Entity(100, 100, 64, 64, allAssets[2])


###########################
#      Display Scroll     #
###########################

scroll = [0, 0]


###########################
#       Game Loop         #debug
###########################


rockLock = []

debug("Generating Map", 1)

for i in range(100):
    newRock = [random.randint(-999, 999), random.randint(-999, 999)]
    rockLock.append(newRock)
debug("Map Generated", 1)


TimeThen = time.time()

LoadClear = time.time()
runTime = 0


TimeNow = time.time()
Load = TimeNow - LoadTime
debug(f"Loaded in {Load} Seconds", 1)
while True:  # game loop
    display.fill((0, 255, 0))  # clear screen by filling it with blue

    #mousePos = pygame.mouse.get_pos()
    # debug(mousePos)

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            #save.save((player_rect.x), (player_rect.y))
            debug('\n')
            debug("Closing Program with exit code 0", 2)
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        scroll[0] -= Velocity * dt
        player.rotateImage(2)
    if keys[pygame.K_d]:
        scroll[0] += Velocity * dt
        player.rotateImage(6)
    if keys[pygame.K_w]:
        scroll[1] -= Velocity * dt
        player.rotateImage(0)
    if keys[pygame.K_s]:
        scroll[1] += Velocity * dt  
        player.rotateImage(4)   
    if keys == None:
        player.rotateImage(0)
    for i in range(100):
        pygame.Surface.blit(display, allAssets[1], ((
            rockLock[i][0]-scroll[0]), (rockLock[i][1]-scroll[1])))
    
    
    
    player.main(display)
    player.WeaponRotation(display)

    if not pygame.mixer.music.get_busy():
        debug(f"Loading Sounds",1)

        songs = [
                            "//assets//sound//music//(1).wav",
                            "//assets//sound//music//(2).wav",
                            "//assets//sound//music//(3).wav",
                            "//assets//sound//music//(4).wav",
                            "//assets//sound//music//(5).wav"
                        ]
        
        try:
        
          pygame.mixer.music.load(f'{path}{songs[random.randint(0,(len(songs)-1))]}')
          pygame.mixer.music.set_volume(0.2)
          pygame.mixer.music.play()  
          debug(f"Songs Loaded", 1)
                    
        except:
          debug(f'Unable to find song files, {path}//src//assets//sound//', 3)  
          debug(f'Process ednded with code 1', 3)
          pygame.quit()
          sys.exit()

    TimeNow = time.time()
    dt = TimeNow - TimeThen
    runTime = TimeNow - LoadClear

    FPS = clock.get_fps()
    if FPS < 60 and runTime > 2:
        debug(
            f"High Frame Render Time, it takes {dt} sconds to render a frame.  fps: {FPS}", 2)
    debug(f'FPS: {FPS}', 4)

    TimeThen = time.time()
    #debug(f"{dt}", 1)

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick()
