'''
Created on 12.05.2017

@author: Effi
'''
from LED import LED
from Belueftung import Belueftung
from datetime import datetime

import time
class Controller(object):
    '''
    classdocs
    '''
    def __init__(self, led, belueftung, heater, temp):
        '''
        Constructor
        '''
        self.LED = led
        self.BELUEFTUNG = belueftung
        self.HEATER = heater
        self.TEMP = temp
    def start(self):
        while True:
            self.LED.update()
            if self.BELUEFTUNG.update() == True:
                self.HEATER.setStartTime(datetime.now())
            self.HEATER.update()
            t,h = self.TEMP.update()
            print "#####", datetime.now(), "#####"
            print "Led" , self.LED.state
            print "Lueftung" , self.BELUEFTUNG.state
            print "Heater" , self.HEATER.state
            print 'Temp: ' + str(t + '\nFeuchtigkeit: ' + str(h)) 
            print "######################################"
            time.sleep(15)

            
            
            
