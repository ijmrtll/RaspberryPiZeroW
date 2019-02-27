# Reading temperature from agilent sensor pmod tmp3
import smbus
from time import sleep

pmod_tmp3_address = 0x48

pmod_tmp_reg = 0x00    #Temperature T_a register
pmod_config_reg = 0x01 #Configuration register
pmod_Thyst_reg = 0x02  #Temperature hysteresis register
pmod_Tset_reg = 0x03   #Temperature limit-set register

bus = smbus.SMBus(1)

LOW_RES = 0x20
MID_RES = 0x40 
HIGH_RES = 0x60   #12 bit resolution
SHUTDOWN_ENABLE = 0X1
SHUTDOWN_DISABLE = 0X0
ONE_SHOT_READING = 0x80

#initinial configuration Pmod
PMOD_CONFIG = bus.read_byte_data(pmod_tmp3_address, pmod_config_reg) #Getting current configuration
PMOD_CONFIG = PMOD_CONFIG | HIGH_RES | SHUTDOWN_ENABLE #High resolution and enable shutdown everything else the defauls
bus.write_byte_data(pmod_tmp3_address, pmod_config_reg, PMOD_CONFIG) #Wite configuration

#read temperature function
def readTemp_C():
    bus.write_byte_data(pmod_tmp3_address, pmod_config_reg, PMOD_CONFIG | ONE_SHOT_READING) # One shot reading
    sleep(0.250) # wait 250ms to refresh register for high resolution
    data = bus.read_word_data(pmod_tmp3_address, pmod_tmp_reg)
    upper_byte = data & 0x00FF
    lower_byte = data >> 8
    tempC = upper_byte + (lower_byte >> 4)/16.0
    return tempC
 
if __name__ == '__main__': 
    tempC = readTemp_C()
    tempF = 1.8*tempC+32 # Change temperature from C to F.
    print("Temperature: %0.4f degC (%0.4f degF)" % (tempC,tempF))