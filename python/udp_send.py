import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 50353
UDP_MESSAGE = "Hallo Welt!"

print "UDP Target IP: ",UDP_IP
print "UDP Target PORT: ", UDP_PORT
print "Message: ",UDP_MESSAGE

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.sendto(UDP_MESSAGE,(UDP_IP,UDP_PORT)) 
