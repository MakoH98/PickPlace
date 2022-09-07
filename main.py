import socket
import time

HOST = "192.168....."  # host adress
PORT = "30002"         #host port


def main():
    buildsocket(HOST, PORT)   #Builidng socket


def buildsocket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket
    s.connect((ip, port))   #conecting network socket



if __name__ == '__main__':
    main()