from time import sleep
from gpiozero import PWMOutputDevice

class Move2WD:
    
    def __init__(self, P1, P2, P3, P4):
        
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        
        self.forwardLeft = PWMOutputDevice(self.P1, True, 0, 60)
        self.reverseLeft = PWMOutputDevice(self.P2, True, 0, 60)
        self.forwardRight = PWMOutputDevice(self.P3, True, 0, 60)
        self.reverseRight = PWMOutputDevice(self.P4, True, 0, 60)
 
    def allStop(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 0
        self.forwardRight.value = 0
        self.reverseRight.value = 0
 
    def forwardDrive(self):
        self.forwardLeft.value = 1.0
        self.reverseLeft.value = 0
        self.forwardRight.value = 1.0
        self.reverseRight.value = 0
 
    def reverseDrive(self):
        self.forwardLeft.value = 0
        self.reverseLeft.value = 1.0
        self.forwardRight.value = 0
        self.reverseRight.value = 1.0
    
    def forwardTurnLeft(self):
        self.forwardLeft.value = 0.0
        self.reverseLeft.value = 1.0
        self.forwardRight.value = 0.0
        self.reverseRight.value = 0
 
    def forwardTurnRight(self):
        self.forwardLeft.value = 0.0
        self.reverseLeft.value = 0.0
        self.forwardRight.value = 0.0
        self.reverseRight.value = 1.0

class Move2WDWithPWM:
    
    def __init__(self, P1, P2, P3, P4):
        
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        
        self.forwardLeft = PWMOutputDevice(self.P1, True, 0, 60)
        self.reverseLeft = PWMOutputDevice(self.P2, True, 0, 60)
        self.forwardRight = PWMOutputDevice(self.P3, True, 0, 60)
        self.reverseRight = PWMOutputDevice(self.P4, True, 0, 60)
 
    def allStop(self):

        self.forwardLeft.value = 0.0
        self.reverseLeft.value = 0.0
        self.forwardRight.value = 0.0
        self.reverseRight.value = 0.0
 
    def forwardDrive(self, Power):

        #Power value set between 0.0 and 1.0;
        self.Power = Power

        self.forwardLeft.value = self.Power
        self.reverseLeft.value = 0.0
        self.forwardRight.value = self.Power
        self.reverseRight.value = 0.0
 
    def reverseDrive(self, Power):
        
        #Power value set between 0.0 and 1.0;
        self.Power = Power

        self.forwardLeft.value = 0.0
        self.reverseLeft.value = self.Power
        self.forwardRight.value = 0.0
        self.reverseRight.value = self.Power
    
    def forwardTurnLeft(self, Power):
        
        #Power value set between 0.0 and 1.0;
        self.Power = Power

        self.forwardLeft.value = 0.0
        self.reverseLeft.value = self.Power
        self.forwardRight.value = 0.0
        self.reverseRight.value = 0.0
 
    def forwardTurnRight(self, Power):

        #Power value set between 0.0 and 1.0;
        self.Power = Power

        self.forwardLeft.value = 0.0
        self.reverseLeft.value = 0.0
        self.forwardRight.value = 0.0
        self.reverseRight.value = self.Power

#
class PWMRoll:

    def __init__(self, P1, P2):
        
        self.P1 = P1
        self.P2 = P2
        #PWM
        self.Pin1 = PWMOutputDevice(self.P1, True, 0, 1000)
        self.Pin2 = PWMOutputDevice(self.P2, True, 0, 1000)
    
    def StartRoll(self):
        self.Pin1.value = 1.0
        self.Pin2.value = 0.0

    def StopRoll(self):
        self.Pin1.value = 0.0
        self.Pin2.value = 0.0

#
class PWMRollWithPulse:

    def __init__(self, P1, P2, Pulse):
        
        #GP
        self.P1 = P1
        self.P2 = P2
        self.Pulse = Pulse

        #PWM
        self.Pin1 = PWMOutputDevice(self.P1, True, 0, self.Pulse)
        self.Pin2 = PWMOutputDevice(self.P2, True, 0, self.Pulse)
    
    def StartRoll(self, Power):
        
        self.Power = Power

        self.Pin1.value = self.Power
        self.Pin2.value = 0.0

    def StopRoll(self):
        self.Pin1.value = 0.0
        self.Pin2.value = 0.0

if __name__ == '__main__':
        
    
    #SmartDrive = Move2WDWithPWM(19,26,6,13)
    
    #SmartDrive.forwardDrive(1.0)
    #sleep(0.5)
    #SmartDrive.forwardDrive(0.7)
    #sleep(1.0)

    
    
    
    test3 = PWMRollWithPulse(5,11,1000)
    speedChangeList = [round(speed * 0.1, 1) for speed in range(3, 10, 1)]

    #
    for listSpeed in speedChangeList:
        test3.StartRoll(listSpeed)
        sleep(1.0)
    test3.StopRoll()

