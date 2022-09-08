from Backend import buildsocket
import time

HOST = "192.168.0.15"  # robot adress
PORT = 30002         #robot port for UR comms


def main():
    _socket = buildsocket(HOST, PORT)   #Builidng socket


    time.sleep(1)
    _socket.send(("set_digital_out(0,True)"+"\n").encode('utf8'))
    time.sleep(2)
    _socket.send(("set_digital_out(0,False)" + "\n").encode('utf8'))




if __name__ == '__main__':
    main()
