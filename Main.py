import AccGyro
import MotorControll
import RadioReceiverV2
import time

#makes the drone stay in one place
def Hover():

    Gx,Gy,Gz,Ax,Ay,Az=AccGyro.AverageInfo()
    if (Az>0.2):
        #Reduce hight
        print("Reduce hight")
        #for speed in range(0,5,1):
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,-1)
    elif(Az<-0.2):
        #Increase hight
        print("Increase hight")
        #for speed in range(0,5,1):
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,1)

    if (Gy>0.2):
        #Tilt Back
        print("Tilt back")
        #for speed in range(0,5,1):
        MotorControll.MotorSpeed(MotorControll.motors[0],1)
        MotorControll.MotorSpeed(MotorControll.motors[1],1)
        MotorControll.MotorSpeed(MotorControll.motors[2],-1)
        MotorControll.MotorSpeed(MotorControll.motors[3],-1)
    elif (Gy<-0.2):
        #Tilt Forward
        print("Tilt forward")
        #for speed in range(0,5,1):
        MotorControll.MotorSpeed(MotorControll.motors[0],-1)
        MotorControll.MotorSpeed(MotorControll.motors[1],-1)
        MotorControll.MotorSpeed(MotorControll.motors[2],1)
        MotorControll.MotorSpeed(MotorControll.motors[3],1)
    
    if (Gx<-0.2):
        #Tilt Right
        print("Tilt right")
        #for speed in range(0,5,1):
        MotorControll.MotorSpeed(MotorControll.motors[0],1)
        MotorControll.MotorSpeed(MotorControll.motors[1],-1)
        MotorControll.MotorSpeed(MotorControll.motors[2],1)
        MotorControll.MotorSpeed(MotorControll.motors[3],-1)
    elif (Gx>0.2):
        #Tilt Left
        print("Tilt left")
        #for speed in range(0,5,1):
        MotorControll.MotorSpeed(MotorControll.motors[0],-1)
        MotorControll.MotorSpeed(MotorControll.motors[1],1)
        MotorControll.MotorSpeed(MotorControll.motors[2],-1)
        MotorControll.MotorSpeed(MotorControll.motors[3],1)

def xStandartizeNumber(numb):
    #Neutral 510 Min 0 Max 1023
    #number diff 513
    print(numb)
    adjustedNumb=round((numb-510)/300)
    print("adjustedNumb: "+str(adjustedNumb))
    return adjustedNumb
    
def yStandartizeNumber(numb):
    #Neutral 522 Min 0 Max 1023
    #number diff 501
    adjustedNumb=round((numb-522)/300)
    print(adjustedNumb)
    return adjustedNumb    

def MoveHorizontally(numb):
    numb=yStandartizeNumber(numb)
    for speed in range(0,1,1):
        MotorControll.MotorSpeed(MotorControll.motors[0],numb)
        MotorControll.MotorSpeed(MotorControll.motors[1],-numb)
        MotorControll.MotorSpeed(MotorControll.motors[2],numb)
        MotorControll.MotorSpeed(MotorControll.motors[3],-numb)

def MoveVertically(numb):
    numb=xStandartizeNumber(numb)
    print("numb: "+str(numb))
    print("reverseNumb: "+str(numb*-1))
    for speed in range(0,1,1):
        MotorControll.MotorSpeed(MotorControll.motors[0],-numb)
        MotorControll.MotorSpeed(MotorControll.motors[1],-numb)
        MotorControll.MotorSpeed(MotorControll.motors[2],numb)
        MotorControll.MotorSpeed(MotorControll.motors[3],numb)

def MoveUp():
    #Increase hight
    for speed in range(0,10,1):
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,1)

def MoveDown():
    #Decrease hight
    for speed in range(0,10,1):
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,-1)

def TurnOff():
    for speed in range(0,10,1):
        for motor in MotorControll.motors:
            MotorControll.MotorSpeed(motor,-1)
    Gx,Gy,Gz,Ax,Ay,Az=AccGyro.AverageInfo()
    
    while(Az<0):
        for speed in range(0,10,1):
            for motor in MotorControll.motors:
                MotorControll.MotorSpeed(motor,-1)
        Gx,Gy,Gz,Ax,Ay,Az=AccGyro.AverageInfo()
        time.sleep(0.1)
    MotorControll.Stop()

def Controll():
    message=RadioReceiverV2.RadioSignal()
    noneCount=0
    while(True):
        #print(message)
        if (message==None):
            noneCount=noneCount+1
            if (noneCount>100):
                TurnOff()
                return "OFF"
        else:
            
            oldMessage=message % 10000
            messgeModified=message % 10000
            noneCount=0
            if (((oldMessage>500 and oldMessage<520) or (oldMessage>512 and oldMessage<530)) and ((messgeModified>500 and messgeModified<520) or (messgeModified>512 and messgeModified<530))):
                Hover()
            else:
                print("message: "+str(message))
                modifiedMessage=message % 10000
                if round(round(message / 10000)) == 1:
                    print("X: "+ str(message % 10000))
                    MoveVertically(modifiedMessage)
                if round(round(message / 10000)) == 2:
                    print("Y: "+ str(message % 10000))
                    MoveHorizontally(modifiedMessage)
                if round(round(message / 10000)) == 3:
                    print("1: "+ str(message % 10000))
                    MoveUp()
                if round(round(message / 10000)) == 4:
                    print("2: "+ str(message % 10000))
                    MoveDown()
                if round(round(message / 10000)) == 5:
                    print("3: "+ str(message % 10000))
                    TurnOff()
                    return "OFF"
        message=RadioReceiverV2.RadioSignal()    
        time.sleep(0.005)


if __name__ == "__main__":
    
    MotorControll.StartUp() # Start motors so they stop beeping
    print("Motor Start Up complete")
    AccGyro.MPU_Init()     # Initiate Accelerator and Gyroscope
    print("AccGyro Set Up complete")
    print(Controll())