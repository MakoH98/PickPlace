import socket
import time

HOST = "192.168.0.15"  # host adress
PORT = 30002         #host port


def main():
    _socket = buildsocket(HOST, PORT)   #Builidng socket


    time.sleep(1)
    _socket.send(("set_digital_out(0,True)"+"\n").encode('utf8'))
    time.sleep(2)
    _socket.send(("set_digital_out(0,False)" + "\n").encode('utf8'))

def buildsocket(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket in stream mode for Robot
    s.connect((ip, port))   #conecting network socket
    return s #returning network socket


if __name__ == '__main__':
    main()
