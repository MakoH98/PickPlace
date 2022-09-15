
from Backend import  JointAngles, mainmenu, freemenu
import time
import rtde_control, rtde_io, rtde_receive
import json

URIP = "192.168.0.15"  # robot adress NB IP ADRESS FOR CLIENT NEEDS TO BE 192.168.0.XX
URPORT = 30002  # robot port for UR comms
PCIP = "192.168.0.14"  # pc adress
PCPORT = 30000  # listing on port
res = {}
seen = set()
PosesFile = 'RobotPos.json'
Poses = dict

def main():

    c = False
    rtde_c = None
    rtde_i = None
    rtde_r = None

    # loop for making connection to robot

    while not c:
        try:
            rtde_c = rtde_control.RTDEControlInterface(URIP)
            rtde_r = rtde_receive.RTDEReceiveInterface(URIP)
            time.sleep(1)
            # rtde_c, rtde_r, rtde_i = setup(URIP) #calling setup function for control recieve and IO conections
            print \
                (f'Connection Estabalished current joint postition =')  # test to see if actual joint position of robot on powerup is passed back might change to actual tcp
            c = True
        except:
            print('nope')
            if input('again y/n') == 'n':
                break

            else:
                pass
    # main menu starts here
    mainmenu()
    option = int(input('enter option: '))

    # loop for main menu

    while option !=0:
        if option == 1:
            freedrive(rtde_c ,rtde_r)

        elif option ==2:
            print(f'moving robot...{JointAngles["safe_start"]}')
            rtde_c.moveJ(JointAngles['safe_start'] ,0.5 ,0.2)
        elif option ==3:

            movetopoint(rtde_c)



        else:
            print('invalid')
        mainmenu()
        option = int(input('enter option: '))

    print('end of program')  # keep at the end


# settign up connections to the robot
def setup(HOST):
    c = rtde_control.RTDEControlInterface(HOST)
    r = rtde_receive.RTDEReceiveInterface(HOST)
    i = rtde_io.RTDEIOInterface(HOST)

    return c


# function to handle the program while robot is in free drive mode
def freedrive(ControlObject, RecieveObject):
    rtde_c = ControlObject
    rtde_r = RecieveObject

    # setting free driveon all axis
    rtde_c.freedriveMode([1, 1, 1, 1, 1, 1])
    # calling option menu
    freemenu()
    # recieving option
    com = int(input('enter option: '))
    # looping trough menu until exit option is selected
    while com !=0:
        if com == 1:
            # ending free drive
            rtde_c.endFreedriveMode()


        elif com == 2:
            # adding robot posiotions to a nested dictionary
            print('getting positions')
            log = rtde_r.getActualTCPPose()
            time.sleep(1)
            print(log)
            global res
            res = add_entry(res, input('name'), log)
            # asking to save current dictionary or add another point
            if input("save to file? y/n") == "y":
                savejson(res, PosesFile)
                print('saved')

        else:
            print('false input')
        # asking for input again
        freemenu()
        com = int(input('enter option: '))
    # making sure free drive exits when loop is broken
    print('exit free')
    rtde_c.endFreedriveMode()


# function add robot pose data to dictionary
def add_entry(res, name, pose):
    cat = 'poses'  # pass it trough function later to use json file for angles aswell
    res['poses'] = {name:{'pose':pose}}

    return res


# function to save dictioary to json file
def savejson(dict, filename):
    cat = 'poses' #pas this inside fucntion when multiple categoriees are avaible is json
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data[cat].update(dict[cat])
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.close()


# function to move robot to waypoints in json file
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
    rtde_c.moveJ_IK(move ,0.5 ,0.2)
    print("moving...")
    json1_file.close()


# covention
if __name__ == '__main__':
    print("starting script")
    main()
