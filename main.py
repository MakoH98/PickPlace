import socket
import time

HOST = "192.168.0.15"  # host adress
PORT = 30002         #host port


def main():
    #_socket = buildsocket(HOST, PORT)   #Builidng socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket
    s.connect((HOST, PORT))   #conecting network socket
    time.sleep(2)
    s.send(("Set_digital_out(0,True)"+"\n").encode('utf8'))

def buildsocket(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket
    s.connect((ip, port))   #conecting network socket
    return s


if __name__ == '__main__':
    main()