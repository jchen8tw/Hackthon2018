'''
    Find Heading by using HMC5883L interface with Raspberry Pi using Python
    http://www.electronicwings.com

'''
from numpy import sign
import smbus        #import SMBus module of I2C
from time import sleep  #import sleep
import math
import acceleration as acc
import math
#some MPU6050 Registers and their Address
Register_A     = 0              #Address of Configuration register A
Register_B     = 0x01           #Address of configuration register B
Register_mode  = 0x02           #Address of mode register

X_axis_H    = 0x03              #Address of X-axis MSB data register
Z_axis_H    = 0x05              #Address of Z-axis MSB data register
Y_axis_H    = 0x07              #Address of Y-axis MSB data register
declination = -0.00669          #define declination angle of location where measurement going to be done
pi          = 3.14159265359     #define pi value


def Magnetometer_Init():
        #write to Configuration Register A
        bus.write_byte_data(Device_Address, Register_A, 0x70)

        #Write to Configuration Register B for gain
        bus.write_byte_data(Device_Address, Register_B, 0xa0)

        #Write to mode Register for selecting mode
        bus.write_byte_data(Device_Address, Register_mode, 0)

def read_raw_data(addr):
        #Read raw 16-bit value
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from module
        if(value > 32768):
            value = value - 65536
        #print('value: ',value)
        return value

def theta():
    z_max=140.
    if abs(z)>z_max:zz=(z_max-0.001)*sign(z)
    else:zz=float(z)
    if y>0 and zz>0:
        #print(zz)
        return abs(90-math.acos(zz/z_max)*180/pi)
    elif y<0 and zz>=0:
        return abs(90+math.acos(zz/z_max)*180/pi)
    elif y>0 and zz<=0:
        return 360-abs(math.acos(zz/z_max)*180/pi-90)
    else:
        return 180+abs(90-math.acos(zz/z_max)*180/pi)
    

bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x1e   # HMC5883L magnetometer device address
#if __name__=='__main__':
#   Magnetometer_Init()     # initialize HMC5883L magnetometer 
#   print (" Reading Heading Angle")
#
#   while True: 
#
#           #Read Accelerometer raw value
#           x = read_raw_data(X_axis_H)
#           z = read_raw_data(Z_axis_H)
#           y = read_raw_data(Y_axis_H)
#           print('y: ',y)
#           print('z: ',z)
#           print('theta: ',theta())
#            sleep(0.5)
def getTheta():
    Magnetometer_Init()
    print("Reading Heading Angle")
    x = read_raw_data(X_axis_H)
    z = read_raw_data(Z_axis_H)
    y = read_raw_data(Y_axis_H)
    return theta()


