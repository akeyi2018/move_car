from pynput import keyboard
from pynput.keyboard import Key, Listener
from time import sleep
from gpiozero import PWMOutputDevice
from CarControllerV3 import *

#RobotCar Running Instance
moveCar = Move2WD(19,26,6,13)

#Rolling Switch Instance
motorRoll = PWMRollWithPulse(9, 10, 100)

#rolling status
g_RollingStatus = 0 

def on_press(key):
    
    runningTime = 0.2
    global g_RollingStatus
    
    try:
        
        if key.char == "a":
            moveCar.forwardTurnLeft()
             
        elif key.char == "w":
            moveCar.reverseDrive()
             
        elif key.char == "d":
            moveCar.forwardTurnRight()

        elif key.char == "s":
            moveCar.forwardDrive()

        elif key.char == "z":
            g_RollingStatus = 1

        elif key.char == "x":
            g_RollingStatus = 0
            
        sleep(runningTime)
        moveCar.allStop()

        #Rolling Switch ON/OFF
        if g_RollingStatus == 1:
            motorRoll.StartRoll(0.6)
        else:
            motorRoll.StopRoll()
    
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        print("END")

        moveCar.allStop()
        motorRoll.StopRoll()

        return False


with Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()