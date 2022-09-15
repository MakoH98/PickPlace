import socket


def Hostsocket(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket in stream mode for Robot
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))   #conecting network socket
    return s #returning network socket




JointAngles = {  #dictionary with robot positions based on joint angles in degrees
    'safe_start': [-1.57, -1.57, 1.57,  -1.57, -1.57, 0]

}

MoveParameters = {
    'velocity' : 0.2,
    'acceleration': 0.5,
    'blend_0': 0.,
    'blend_20': 0.02
}

TCPPoses = {  #dict containing poses mm degrees x, y , z , rx ,ry ,rz
    'pose_test': [0/1000, 400/1000, 600/1000, 3.14, 0, 0]


}


def mainmenu():
    print('[1] freedrive')
    print('[2] safe start')
    print('[3] move to waypoint')
    print('[0] exit')

def freemenu():
    print('[0] exit')
    print('[1] stop freedrive')
    print('[2] log current pos')

def waypointmenu():
    print('0 exit')
    print('[name] enter name of waypoint')