from socketIO_client import SocketIO
def on_connect(): # Function to prompt on server connection
	print('connected to server')

def on_disconnect(): # Funtion to prompt on disconnection from server
	print('disconnected from server')
def on_overspeed():
	print('')






socketIO = SocketIO('localhost', 3000)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.wait()