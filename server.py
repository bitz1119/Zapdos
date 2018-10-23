from socketIO_client import SocketIO

socketIO = SocketIO('localhost', 3000)
socketIO.wait()