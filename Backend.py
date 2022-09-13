import socket


def Hostsocket(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #setting up socket in stream mode for Robot
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))   #conecting network socket
    return s #returning network socket




JointAngles = {  #dictionary with robot positions based on joint angles in degrees
    'safe_start': [-90, -90, 90,  -90, -90, 0]

}

MoveParameters = {
    'velocity' : 0.2,
    'acceleration': 0.5,
    'blend_0': 0.,
    'blend_20': 0.02
}

TCPPoses = {  #dict containing poses mm degrees x, y , z , rx ,ry ,rz
    'pose_test': [0, 400, 400, 180, 0, 0]


}

class userprompt:

    def __init__(self):
        pass


    def main(self):
        try:
            key = int(input('1: Free drive mode? 2: Move to safe start angles 3: run program '))
            if key == 1:
                return 'FreeDrive'
            if key == 2:
                return 'SafeStart'
        except:
            print('use int val')

    def freedrive(self):
        input("stop: stops free drive or log: log the current pose")

    def connectFail(self):
        if input('connection failed retry y/n') == 'y':
            return True
