'''
        Read Gyro and Accelerometer by Interfacing Raspberry Pi with MPU6050 using Python
    http://www.electronicwings.com
'''
import smbus         #import SMBus module of I2C
from time import sleep          #import

def MPU_Init():

    #some MPU6050 Registers and their Address
    PWR_MGMT_1   = 0x6B
    SMPLRT_DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_ENABLE   = 0x38
    ACCEL_XOUT_H = 0x3B
    ACCEL_YOUT_H = 0x3D
    ACCEL_ZOUT_H = 0x3F
    GYRO_XOUT_H  = 0x43
    GYRO_YOUT_H  = 0x45
    GYRO_ZOUT_H  = 0x47
    
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
    Device_Address = 0x68   # MPU6050 device address

def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

def GyroscopeInfo():
    #Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)

    Gx = round(gyro_x/131.0,1)
    Gy = round(gyro_y/131.0,1)
    Gz = round(gyro_z/131.0,1)

    Gx=Gx+0.1
    Gy=Gy-0.3
    Gz=Gz+0.005

    return Gx,Gy,Gz

def AccelerometerInfo():
    #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)

    Ax = round(acc_x/16384.0,2)
    Ay = round(acc_y/16384.0,2)
    Az = round(acc_z/16384.0,2)

    Ay=Ay+0.052
    Az=Az-1

    return Ax,Ay,Az

def AverageInfo():
    
    TGx=0
    TGy=0
    TGz=0
    TAx=0
    TAy=0
    TAz=0
    for i in range(0,5,1):
        Gx,Gy,Gz=GyroscopeInfo()
        Ax,Ay,Az=AccelerometerInfo()
        TGx=+Gx
        TGy=+Gy
        TGz=+Gz
        TAx=+Ax
        TAy=+Ay
        TAz=+Az
        sleep(0.1)
    
    return TGx,TGy,TGz,TAx,TAy,TAz
      

if __name__ == "__main__":
    
    MPU_Init()
    print (" Reading Data of Gyroscope and Accelerometer")  
    while True:
        Gx,Gy,Gz,Ax,Ay,Az=AverageInfo()
        print ("Gx=%.1f" %Gx, u'\u00b0'+ "/s", "\tGy=%.1f" %Gy, u'\u00b0'+ "/s", "\tGz=%.1f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
        sleep(0.1)
