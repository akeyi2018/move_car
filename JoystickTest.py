import os

#os.environ["SDL_VIDEODRIVER"] = "dummy"
os.putenv('SDL_VIDEODRIVER', 'fbcon')
import pygame
from pygame.locals import *
from time import sleep


def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    pygame.init()
    
    pygame.display.set_mode((1,1))
    #pygame.display.init()
    print ('joystick start')
    
    while True:
         
        eventlist = pygame.event.get()

    
        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYBUTTONDOWN:
                print ('button:' + str(e.button))
        sleep(0.1)
        


 
main()
    