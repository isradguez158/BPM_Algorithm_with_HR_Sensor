import time
import os
import RPi.GPIO as GPIO

class HR:
    def __init__(self, pin) -> None:
        self.HR_Pin = pin
        self.oldSample=0
        self.prevtime=0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.HR_Pin, GPIO.IN)
        self.sample=0
        self.StartTime=0
        self.BPM=0
        
    def Read_HR(self):
        self.sample = GPIO.input(self.HR_Pin)
        
        if self.sample and (self.oldSample != self.sample):
            self.TimeDiff = (time.time() - self.StartTime)
            self.freq = (1 / self.TimeDiff)
            self.BPM = self.freq * 60.0
            self.StartTime = time.time()

            #print("BPM = " + str(self.BPM))
    
        self.oldSample = self.sample