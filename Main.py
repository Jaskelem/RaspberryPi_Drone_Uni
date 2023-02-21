import AccGyro
import MotorControll
import RadioReceiver

#makes the drone stay in one place
def Hover():
    Gx,Gy,Gz,Ax,Ay,Az=AccGyro.AverageInfo()

    if (Az>0):
        #Reduce hight
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,-5)
    elif(Az<0):
        #Increase hight
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,5)

    if (Gy<0):
        #Tilt Back
        MotorControll.MotorSpeed(MotorControll.motors[0],5)
        MotorControll.MotorSpeed(MotorControll.motors[1],5)
        MotorControll.MotorSpeed(MotorControll.motors[2],-5)
        MotorControll.MotorSpeed(MotorControll.motors[3],-5)
    elif (Gy>0):
        #Tilt Forward
        MotorControll.MotorSpeed(MotorControll.motors[0],-5)
        MotorControll.MotorSpeed(MotorControll.motors[1],-5)
        MotorControll.MotorSpeed(MotorControll.motors[2],5)
        MotorControll.MotorSpeed(MotorControll.motors[3],5)
    
    if (Gx>0):
        #Tilt Right
        MotorControll.MotorSpeed(MotorControll.motors[0],5)
        MotorControll.MotorSpeed(MotorControll.motors[1],-5)
        MotorControll.MotorSpeed(MotorControll.motors[2],5)
        MotorControll.MotorSpeed(MotorControll.motors[3],-5)
    elif (Gx>0):
        #Tilt Left
        MotorControll.MotorSpeed(MotorControll.motors[0],-5)
        MotorControll.MotorSpeed(MotorControll.motors[1],5)
        MotorControll.MotorSpeed(MotorControll.motors[2],-5)
        MotorControll.MotorSpeed(MotorControll.motors[3],5)



if __name__ == "__main__":
    
    MotorControll.StartUp() # Start motors so they stop beeping
    AccGyro.MPU_Init()     # Initiate Accelerator and Gyroscope
    