import AccGyro
import MotorControll
import RadioReceiverV2
import time

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

def xStandartizeNumber(numb):
    #Neutral 510 Min 0 Max 1023
    #number diff 513
    adjustedNumb=(numb-510)/2
    return adjustedNumb
    
def yStandartizeNumber(numb):
    #Neutral 522 Min 0 Max 1023
    #number diff 501
    adjustedNumb=(numb-522)/2
    return adjustedNumb    

def MoveHorizontally(numb):
    numb=yStandartizeNumber(numb)
    reverseNumb=numb*-1
    MotorControll.MotorSpeed(MotorControll.motors[0],reverseNumb)
    MotorControll.MotorSpeed(MotorControll.motors[1],numb)
    MotorControll.MotorSpeed(MotorControll.motors[2],reverseNumb)
    MotorControll.MotorSpeed(MotorControll.motors[3],numb)

def MoveVertically(numb):
    numb=xStandartizeNumber(numb)
    reverseNumb=numb*-1
    MotorControll.MotorSpeed(MotorControll.motors[0],reverseNumb)
    MotorControll.MotorSpeed(MotorControll.motors[1],reverseNumb)
    MotorControll.MotorSpeed(MotorControll.motors[2],numb)
    MotorControll.MotorSpeed(MotorControll.motors[3],numb)

def MoveUp():
    #Increase hight
    for motor in MotorControll.motors:
        MotorControll.MotorSpeed(motor,100)

def MoveDown():
    #Decrease hight
    for motor in MotorControll.motors:
        MotorControll.MotorSpeed(motor,-100)

def TurnOff():
    for motor in MotorControll.motors:
        MotorControll.MotorSpeed(motor,-10)
    Gx,Gy,Gz,Ax,Ay,Az=AccGyro.AverageInfo()
    if(Az<0):
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,-10)
        Gx,Gy,Gz,Ax,Ay,Az=AccGyro.AverageInfo()
    MotorControll.Stop()

def Controll():
    message=RadioReceiverV2.RadioSignal()
    while (True):
        oldMessage=message
        message=RadioReceiverV2.RadioSignal()
        if ((oldMessage==510 and oldMessage==522) and (message==510 and message==522)):
            Hover()
        else:
            if round(message / 10000) == 1:
                logging.info("X: "+ str(message % 10000))
                MoveVertically(message)
            if round(message / 10000) == 2:
                logging.info("Y: "+ str(message % 10000))
                MoveHorizontally(message)
            if round(message / 10000) == 3:
                logging.info("1: "+ str(message % 10000))
                MoveUp()
            if round(message / 10000) == 4:
                logging.info("2: "+ str(message % 10000))
                MoveDown()
            if round(message / 10000) == 5:
                logging.info("3: "+ str(message % 10000))
                TurnOff()
        message=RadioReceiverV2.RadioSignal()    
        time.sleep(0.1)


if __name__ == "__main__":
    
    MotorControll.StartUp() # Start motors so they stop beeping
    AccGyro.MPU_Init()     # Initiate Accelerator and Gyroscope
    Controll()