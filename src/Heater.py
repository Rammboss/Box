'''
Created on 11.05.2017

@author: Effi
'''
from Socket import Socket
from datetime import datetime
from Belueftung import Belueftung
class Heater(Socket):
    '''
    classdocs
    '''
    codeOn = 5506385
    codeOff = 5506388
    state = "OFF"

    def __init__(self, name, belueftung, temp):
        '''
        Constructor
        '''
        self.name = name
        self.belueftung = belueftung
        self.startTime = "N.A"
        self.sensorTemp = temp
    def checkTime(self):
        currentTime = datetime.time(datetime.now())
        tmp = False
        for key in self.laufzeit:
            x = datetime.time(key) 
            
            if x <= currentTime and datetime.time(self.laufzeit[key]) >= currentTime:
                tmp = True
            else:
                tmp = False
        
        return tmp
    def turnOn(self):
        self.state = "ON"
        Socket.turnOn(self, self.codeOn, 'Heizung an') 
    def turnOff(self):
        self.state = "OFF" 
        return Socket.turnOff(self, self.codeOff, 'Heizung aus')
    def setStartTime(self, startTime):
        self.startTime = startTime
    def isBetween(self, start, end):
        currentTemp = self.sensorTemp.getLastTemp()
        if(start <= currentTemp <=end):
            return True
        else:
            return False
    def update(self): 
        current =  datetime.now()
           
        if self.state == "OFF" and self.startTime != "N.A" and self.belueftung.state == "OFF" or not(self.isBetween(20, 28)) and self.state == "OFF" and self.belueftung.state == "OFF" and self.sensorTemp.getLastTemp() != -1:
            self.turnOn()
            
        elif isinstance(self.startTime, datetime) and current > datetime.combine(current.today(), Socket.addtoTime(self, self.startTime.strftime("%H:%M:%S"), "00:10:00").time()) or self.isBetween(25, 30) and self.state == "ON" and self.belueftung.state == "ON" and self.sensorTemp.getLastTemp() != -1:
                self.turnOff()
                self.startTime = "N.A"
        else:
            return False
