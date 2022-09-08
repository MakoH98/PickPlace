import socket


def buildsocket(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket in stream mode for Robot
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))   #conecting network socket
    return s #returning network socket