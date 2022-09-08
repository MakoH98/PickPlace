from Backend import buildsocket
import time


HOST = "192.168.0.15"  # robot adress NB IP ADRESS FOR CLIENT NEEDS TO BE 192.168.0.XX
PORT = 30002         #robot port for UR comms

# x, y, z, rx, ry , rz = 200, 300 , 500 ,0 ,0 ,3.14

def main():
    _socket = buildsocket(HOST, PORT)   #Builidng socket

    #
    # time.sleep(1)
    # _socket.send(("set_digital_out(0,True)" + "\n").encode('utf8'))
    # time.sleep(2)
    # _socket.send(("set_digital_out(0,False)" + "\n").encode('utf8'))
    while True:
        poses = [
        "p[0.8,0.4,0.1,     3.14,0,0]", # x,y,z,rx,ry,rz
        "p[0.8,0.4,0.8,     3.14,0,0]",  # x,y,z,rx,ry,rz
        "p[0,1,0.8,     3.14,0,0]",  # x,y,z,rx,ry,rz
        "p[0,1,0.1,     3.14,0,0]",  # x,y,z,rx,ry,rz
        "p[0,1,0.8,     3.14,0,0]",  # x,y,z,rx,ry,rz
        "p[0.8,0.4,0.8,     3.14,0,0]"  # x,y,z,rx,ry,rz
        ]
        for pose in poses:

            _socket.send((f"movel({pose}, a=0.5, v=1.3, t=0, r=0)" + "\n").encode('utf8'))

            time.sleep(3)


if __name__ == '__main__':
    main()
