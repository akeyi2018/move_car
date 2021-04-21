import RPi.GPIO as GPIO
from time import sleep
from gpiozero import PWMOutputDevice
import pygame
from pygame.locals import *
from CarControllerV3 import *

#RobotCar Running Instance
moveCar = Move2WD(19,26,6,13)

#Rolling Switch Instance
motorRoll = PWMRollWithPulse(20, 21, 1000)

#rolling status
g_RollingStatus = 0 

def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    #print ('joystick start')
    
    global g_RollingStatus

    pygame.init()

    while True:
        eventlist = pygame.event.get()
        #
        for e in eventlist:
            if e.type == QUIT:
                return
            if e.type == pygame.locals.JOYBUTTONDOWN:
                print ('button:' + str(e.button))
                if e.button == 0:
                    moveCar.forwardDrive()
                    sleep(0.5)
                    moveCar.allStop()
                elif e.button == 2:
                    moveCar.reverseDrive()
                    sleep(0.5)
                    moveCar.allStop()
                elif e.button == 4:
                    moveCar.forwardTurnLeft()
                    sleep(0.5)
                    moveCar.allStop()
                elif e.button == 5:
                    moveCar.forwardTurnRight()
                    sleep(0.5)
                    moveCar.allStop()
                elif e.button == 3:
                    g_RollingStatus = 1
                    print(g_RollingStatus)
                elif e.button == 1:
                    g_RollingStatus = 0
                #End Controll
                elif e.button == 6:
                    print("Quit!")
                    g_RollingStatus = 0
                    return
            #Rolling Switch ON/OFF
            if g_RollingStatus == 1:
                #print("start")
                motorRoll.StartRoll(0.6)
            else:
                #print("stop")
                motorRoll.StopRoll()



try:
    main()
    print("OK")
    motorRoll.StopRoll()
except pygame.error:
    print ('not found joystick.')
except:
    import traceback
    traceback.print_exc()
    
