from Backend import Hostsocket
import socket
import time


URIP = "192.168.0.15"  # robot adress NB IP ADRESS FOR CLIENT NEEDS TO BE 192.168.0.XX
URPORT = 30002         #robot port for UR comms
PCIP = "192.168.0.14"
PCPORT = 30000

def main():
    # pc_host(URIP, URPORT) sends commands via socket
    UR_host(PCIP, PCPORT)

def pc_host(HOST, PORT):
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
        print(f"Data from robot recieved...:{repr(data)}")



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
                command = "(200,50,45)"
                c.send(command)

        except socket.error as socketerror:
            print(count)

    c.close()
    s.close()


if __name__ == '__main__':
    main()
