

from Backend import Hostsocket, JointAngles, mainmenu, TCPPoses, freemenu, waypointmenu
import time
import rtde_control, rtde_io, rtde_receive
import json

URIP = "192.168.0.15"  # robot adress NB IP ADRESS FOR CLIENT NEEDS TO BE 192.168.0.XX
URPORT = 30002         #robot port for UR comms
PCIP = "192.168.0.14" #pc adress
PCPORT = 30000          #listing on port
res = {}
seen = set()
PosesFile = 'RobotPos.json'
Poses = dict

def main():

    c = False
    rtde_c = None
    rtde_i = None
    rtde_r = None

    while not c:
        try:
            rtde_c = rtde_control.RTDEControlInterface(URIP)
            rtde_r = rtde_receive.RTDEReceiveInterface(URIP)
            time.sleep(1)
            # rtde_c, rtde_r, rtde_i = setup(URIP) #calling setup function for control recieve and IO conections
            print(f'Connection Estabalished current joint postition =') #test to see if actual joint position of robot on powerup is passed back might change to actual tcp
            c = True
        except:
            print('nope')
            if input('again y/n') == 'n':
                break

            else:
                pass
    mainmenu()
    option = int(input('enter option: '))

    while option !=0:
        if option == 1:
            freedrive(rtde_c,rtde_r)

        elif option ==2:
            print(f'moving robot...{JointAngles["safe_start"]}')
            rtde_c.moveJ(JointAngles['safe_start'],0.5,0.2)
        elif option ==3:

            movetopoint(rtde_c)



        else:
            print('invalid')
        mainmenu()
        option = int(input('enter option: '))

    print('end of program') #keep at the end


def setup(HOST): #setting up all the conections
    c = rtde_control.RTDEControlInterface(HOST)
    r = rtde_receive.RTDEReceiveInterface(HOST)
    i = rtde_io.RTDEIOInterface(HOST)

    return c


def freedrive(ControlObject, RecieveObject):
    rtde_c = ControlObject
    rtde_r = RecieveObject

    rtde_c.freedriveMode([1, 1, 1, 1, 1, 1]) #set free drive on all axis
    freemenu()
    com = int(input('enter option: '))

    while com !=0:
        if com == 1:
            rtde_c.endFreedriveMode()


        elif com == 2:
            print('getting positions')
            log = rtde_r.getActualTCPPose()
            time.sleep(1)
            print(log)
            global res
            res = add_entry(res, input('name'), log)
            if input("save to file? y/n") == "y":
                savejson(res, PosesFile)
                print('saved')

        else:
            print('false input')
        freemenu()
        com = int(input('enter option: '))

    print('exit free')
    rtde_c.endFreedriveMode()

def add_entry(name, pose):
    cat = 'poses' #pass it trough function later to use json file for angles aswell
    res[cat][name] = {'pose':pose}




    return res


def savejson(list, filename):

    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["poses_robot"].append(list)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.close()


def movetopoint(ControlObject):
    rtde_c = ControlObject
    # aquire options
    json1_file = open('RobotPos.json')
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)

    json1_data = json1_data['poses']
    print(json1_data)

    option = str(input('enter name'))

    move = json1_data[option]['pose']
    rtde_c.moveJ_IK(move,0.5,0.2)
    print("moving...")
    json1_file.close()





if __name__ == '__main__':
    print("starting script")
    main()
