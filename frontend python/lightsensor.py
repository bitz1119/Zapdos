from socketIO_client import SocketIO
import json
import random
import time
def on_connect(): # Function to prompt on server connection
	print('connected to server')
	GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	while(1):
		check_the_light()

def on_disconnect(): # Funtion to prompt on disconnection from server
	print('disconnected from server')

def get_current_cordinate():
	return random.random(),random.random()

def check_the_light():
	while(True):
	    if GPIO.input(33):
	    	dis = {}
	    	x,y = get_current_cordinate()
	    	dis['lang'] = x
	    	dis['long'] = y
	    	dis['isilluminated'] = True
	    	dis['time'] = time.time()
	    	socketIO.emit('overspeeding',dis)


socketIO = SocketIO('localhost', 3000)
socketIO.on('connect', on_connect)
# socketIO.wait()
print('After connect')
# while(1):
# 	should_be_send()
socketIO.on('disconnect', on_disconnect)
socketIO.wait()