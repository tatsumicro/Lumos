# -*- coding: utf-8 -*-

"""
@author  = "m.tatsumi"
@version = "1.0"
@date    = "19 Sep 2019"
"""


# Built-in/Generic Imports
import json
#[...]

# Libs
import termcolor
import serial
#[...]

# Own modules
#[...]


class SerialLed:
	ser = None
	
	def __init__(self, port, baudrate=115200):
		notice = "Serial initialization was successful: "+port
		print(termcolor.colored(notice, "green"))
		self.ser = serial.Serial(port, baudrate, timeout=0.1)
		
	def __del__(self):
		print(termcolor.colored("finalizing", "yellow"))
		self.ser.close()
		
	def makeJson(self, r, g, b, speed=50):
		r = max(0, min(255, r))
		g = max(0, min(255, g))
		b = max(0, min(255, b))
		speed = max(0, min(1000, speed))
		json_led = {
			"r": int(r),
			"g": int(g),
			"b": int(b),
			"speed": int(speed)
		}
		return json_led
	
	def setColor(self, r, g, b, speed=50):
		json_data = self.makeJson(r, g, b, speed)
		json_str = json.dumps(json_data)+";"
		self.ser.write(json_str)
		
	def termInput(self):
		r = input(termcolor.colored("Prease write color red: ", "red"))
		g = input(termcolor.colored("Prease write color green: ", "green"))
		b = input(termcolor.colored("Prease write color blue: ", "blue"))
		speed = input(termcolor.colored("Prease write speed: ", "yellow"))
		self.setColor(r, g, b, speed)
		print(termcolor.colored("LED was changed!", "yellow"))
        
        
def example():
	"""
	This is usage example.
	"""
	port = "COM4"
	baudrate = 115200
	led = SerialLed(port, baudrate)
	while True:
		led.termInput()
		
		
