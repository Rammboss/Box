#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Main -- shortdesc

Main is a description

It defines classes_and_methods

@author:     Effi

@copyright:  2017 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''
from LED import LED
from Socket import Socket
from datetime import datetime, time
from Controller import Controller
from Belueftung import Belueftung
from Heater import Heater

lichtData = {
     time(06,00) : time(23,59)
    ,
    }
led = LED("LED Saga", lichtData)
belueftung = Belueftung("Luefter", '00:30:00', '03:00:00')
heater = Heater("Handy Heater", belueftung)
belueftung.setHeater(heater)
controller = Controller(led, belueftung, heater)
controller.BELUEFTUNG.turnOff()
controller.HEATER.turnOff()
controller.LED.turnOff()
controller.start()


