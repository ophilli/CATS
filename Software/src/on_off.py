import time as t
import sys
import RPi.GPIO as io
import buzzer
import led
import os
import configparser
import sql

config = configparser.RawConfigParser() #instantiate config reader
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')) #actually read the config file

led = led.LED()
piezo = buzzer.buzzer()
power = int(config.get('_relay', 'pin'))
# Don't print warnings about the GPIO already being used
io.setwarnings(False)
io.setup(power, io.OUT)
io.output(power, False) # Make sure Powerswitch Tail is off

def TurnPowerOff(ID):
    io.output(power, False)
    eventLog(ID, 2)
    piezo.play(5)
    led.off()

def TurnPowerOn(ID):
    io.output(power, True)
    eventLog(ID, 0)
    piezo.play(1)
    led.on()
