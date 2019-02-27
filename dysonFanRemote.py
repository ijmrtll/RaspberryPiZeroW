import os
import argparse
from time import sleep

cmds_init = "irsend SEND_ONCE dyson KEY_"
cmds_keys = ["POWER", "DIRECTION", "UP", "DOWN", "SLEEP", "AWAKE"]
    
def dyson_fan_po_cmd():
    #Send one power on/off command to the fan
    os.system(cmds_init + cmds_keys[0])
    if is_verbose:
        print("Fan power ON/OFF command sent")
    
def dyson_fan_os_cmd():
    #Send one oscillate command to the fan
    os.system(cmds_init + cmds_keys[1])
    if is_verbose:
        print("Fan oscillating ON/OFF command sent")

def dyson_fan_set_cmd(intensity):
    #Send "intensity" number of times the increase air intensity command to the fan
    if intensity < 10:
        dyson_fan_return_cmd()
        sleep(1)
        for i in range(intensity - 1):
            os.system(cmds_init + cmds_keys[2])
            if intensity > 1:
                sleep(2)
        if is_verbose:
            print("Fan air intensity command sent {} time(s)".format(intensity))
    elif intensity >=10:
        for i in range(10):
            os.system(cmds_init + cmds_keys[2])
            if intensity > 1:
                sleep(0.5)
        if is_verbose:
            print("Fan air intensity command sent {} time(s)".format(intensity))

def dyson_fan_de_cmd(intensity):
    #Send "intensity" number of times the decrease air intensity command to the fan
    for i in range(intensity):
        os.system(cmds_init + cmds_keys[3])
        if intensity > 1:
            sleep(2)
    if is_verbose:
        print("Fan air intensity command sent {} time(s)".format(intensity))

def dyson_fan_return_cmd():
    #Helping function that return the air intensity to the lowest value
    for i in range (10):
        os.system(cmds_init + cmds_keys[3])
        sleep(0.5)
    
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description="Control the fan by sending IR commands")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-se", "--set", type=int, default=0, help="Set the inensity of the air to the specified value")
    group.add_argument("-de", "--decre", type=int, default=0, help="Decrease the intensity of the air by the specified amount")
    parser.add_argument("-po", "--power", action="store_true", help="Send a power on/off command to the fan")
    parser.add_argument("-os", "--oscillate", action="store_true", help="Send a ocillating on/off command to the fan")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    is_verbose = args.verbose
    
    if args.power:
        dyson_fan_po_cmd()
        sleep(1)
    if args.oscillate:
        dyson_fan_os_cmd()
        sleep(1)
    if args.set >= 1:
        dyson_fan_in_cmd(args.set)
        sleep(1)
    if args.decre >= 1:
        dyson_fan_de_cmd(args.decre)
        sleep(1)