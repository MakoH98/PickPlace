from Backend import buildsocket
import time
import urx

HOST = "192.168.0.15"  # robot adress NB IP ADRESS FOR CLIENT NEEDS TO BE 192.168.0.XX
PORT = 30002         #robot port for UR comms


def main():
    _socket = buildsocket(HOST, PORT)   #Builidng socket


    time.sleep(1)
    _socket.send(("set_digital_out(0,True)"+"\n").encode('utf8'))
    time.sleep(2)
    _socket.send(("set_digital_out(0,False)" + "\n").encode('utf8'))

    # pose1 = "p[200,200,500,0,0,3.14]" # x,y,z,rx,ry,rz
    # _socket.send((f"movej({pose1}, a=1.4, v=1.05, t=0, r=0)").encode('utf8'))

if __name__ == '__main__':
    main()
