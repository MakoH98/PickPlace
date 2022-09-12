import socket


def Hostsocket(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket in stream mode for Robot
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))   #conecting network socket
    return s #returning network socket

def Clientsocket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(ip, port)
    s.listen(5)
    c, addr = s.accept()
    msg = c.recv(1024)
    return msg


JointAngles = {  #dictionary with robot positions based on joint angles
    'safe_start': [-90, -90, 90,  -90, -90, 0]

}

MoveParameters = {
    'velocity' : 0.2,
    'acceleration': 0.5,
    'blend_0': 0.,
    'blend_20': 0.02
}

TCPPoses = {

}