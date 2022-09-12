from Backend import Hostsocket, JointAngles
import socket
import time
import rtde_control, rtde_io, rtde_receive

URIP = "192.168.0.15"  # robot adress NB IP ADRESS FOR CLIENT NEEDS TO BE 192.168.0.XX
URPORT = 30002         #robot port for UR comms
PCIP = "192.168.0.14" #pc adress
PCPORT = 30000          #listing on port

def main():
    s = True
    while s == True:
        try:
            rtde_c, rtde_r, rtde_i = setup(URIP)
            print(f'Connection Estabalished current joint postition = {rtde_c.getActualJointPositionsHistory()}')
            if input("Go to safe joint pos? y/n") == 'y':
                rtde_c.moveJ(JointAngles['safe_start'])
                print('moving to safe start angles')
        except:
            print('connecting failed')
            if input('retry = y/n') == 'n':
                s = False

    print('end of program') #keep at the end

def setup(HOST):
    c = rtde_control.RTDEControlInterface(HOST)
    r = rtde_receive.RTDEReceiveInterface(HOST)
    i = rtde_io.RTDEIOInterface(HOST)

    return c, r, i


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



def UR_host(HOST, PORT):
    count = 0
    while count < 1000:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        c, addr = s.accept()

        try:
            msg = c.recv(1024)
            print(msg)

            if msg == "Ask_Data":
                count = count + 1
                print("trying to send data..")
                time.sleep(0.5)
                command = "(0.2,0.05,45)"
                c.send(command)

        except socket.error as socketerror:
            print(count)

    c.close()
    s.close()


if __name__ == '__main__':
    print("starting script")
    main()
