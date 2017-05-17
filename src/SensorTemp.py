'''
Created on 17.05.2017

@author: Effi
'''

import thingspeak
import time
import Adafruit_DHT
class SensorTemp(object):
    '''
    classdocs
    '''


    def __init__(self, channelID, writeKey, readKey):
        '''
        Constructor
        '''
        self.channelID = channelID
        self.writeKey = writeKey
        self.readKey = readKey
        self.sensor = Adafruit_DHT.DHT22
        self.channel = thingspeak.Channel(id=channelID,write_key=writeKey,api_key=readKey)
    def measure(self, channel):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            # write
            response = channel.update({'field1': temperature, 'field2': humidity})
            
            return [temperature, humidity]
            
            #print 'Temp: ' + str(temperature + '\nFeuchtigkeit: ' + str(humidity)) 
        except:
            print("connection failed")
            return [0,0]
            
    def update(self):
        return self.measure(self.channel)