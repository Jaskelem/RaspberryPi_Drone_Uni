import Acc_Gyro
import MotorControll
import RadioReceiver

if __name__ == "__main__":
    
    MotorControll.StartUp() # Start motors so they stop beeping
    Acc_Gyro.MPU_Init()     # Initiate Accelerator and Gyroscope