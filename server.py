from socketIO_client import SocketIO
import json
import random
def on_connect(): # Function to prompt on server connection
	print('connected to server')

def on_disconnect(): # Funtion to prompt on disconnection from server
	print('disconnected from server')


def find_speed():
	return random.random()*10

def get_current_cordinate():
	return random.random(),random.random()

def find_alcohol_level():
	if random.random() > 0.3:
		return False
	else :
		return True

def on_overspeed():
	x = find_speed()
	if x >= THRESHOLD:
		return x
	else :
		return 0 

def on_alcohol():
	x = find_alcohol_level()
	return x


def should_be_send():
	speed = on_overspeed();
	if speed != 0 :
		dis = {}
		dis['speed'] = speed
		lang,longi = get_current_cordinate()
		dis['langitude'] = lang
		dis['longitude'] = longi
		dis['on_alcohol'] = on_alcohol()
		dis = json.dumps(dis)
		socketIO.emit('overspeading',dis)
		show_alert_to_user()	






socketIO = SocketIO('localhost', 3000)
socketIO.on('connect', on_connect)
while(1):
	should_be_send()
socketIO.on('disconnect', on_disconnect)
socketIO.wait()