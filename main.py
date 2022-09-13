from Backend import Hostsocket, JointAngles, userprompt, TCPPoses
import time
import rtde_control, rtde_io, rtde_receive

URIP = "192.168.0.15"  # robot adress NB IP ADRESS FOR CLIENT NEEDS TO BE 192.168.0.XX
URPORT = 30002         #robot port for UR comms
PCIP = "192.168.0.14" #pc adress
PCPORT = 30000          #listing on port


def main():
    c = False
    rtde_c = None
    rtde_i = None
    rtde_r = None
    menu = userprompt()
    while not c:
        # try:            #attempting to connect to robot
            rtde_c = rtde_control.RTDEControlInterface(URIP)
            time.sleep(1)
            # rtde_c, rtde_r, rtde_i = setup(URIP) #calling setup function for control recieve and IO conections
            print(f'Connection Estabalished current joint postition =') #test to see if actual joint position of robot on powerup is passed back might change to actual tcp
            c = True
        # except:
        #     if not menu.connectFail():
        #         break
    while c:
        pick = menu.main()
        if pick == 'FreeDrive':
            rtde_c.freedriveMode([1,1,1,1,1,1])
            com = input('proceed y/log')
            if com == 'y':

                rtde_c.endFreedriveMode()
            if com == 'log':
                log = rtde_c.getActualToolFlangePose()
                TCPPoses.update({input('name'):log})
                time.sleep(2)

        elif pick == "SafeStart":
            print(f'moving robot...{JointAngles["safe_start"]}')
            rtde_c.moveJ(JointAngles['safe_start'])

    print('end of program') #keep at the end


def setup(HOST): #setting up all the conections
    c = rtde_control.RTDEControlInterface(HOST)
    r = rtde_receive.RTDEReceiveInterface(HOST)
    i = rtde_io.RTDEIOInterface(HOST)

    return c





def pc_host(HOST, PORT): #old code making sockets
    _socket = Hostsocket(HOST, PORT)   #Builidng socket

    #
    # time.sleep(1)
    # _socket.send(("set_digital_out(0,True)" + "\n").encode('utf8'))
    # time.sleep(2)
    # _socket.send(("set_digital_out(0,False)" + "\n").encode('utf8'))
    count = 0
    while count < 1:
        poses = [
        "p[0.6,0.6,0.6,     3.14,0,0]", # x,y,z,rx,ry,rz
        "p[0.6,0.6,0.6,     1.58,0,0]",  # x,y,z,rx,ry,rz
        "p[0,6,0.6,0.6,     3.14,0,0]",  # x,y,z,rx,ry,rz
        "p[0.6,0.6,0.6,     -1.58,0,0]" # x,y,z,rx,ry,rz

        ]

        for pose in poses:

            _socket.send((f"movej({pose}, a=0.5, v=0.2, t=0, r=0)" + "\n").encode('utf8'))

            time.sleep(5)

        count = count + 1
        data = _socket.recv(1024)
        _socket.close()
        print(f"Data from robot recieved...:{repr(data)}")      ##


if __name__ == '__main__':
    print("starting script")
    main()
