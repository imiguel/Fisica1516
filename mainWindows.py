from tkinter import *
from serial import *



def readSerialPort():
    serialPort = serial.Serial('COM3', 9600)

#ser = serial.Serial('COM3', 9600) #serial.Serial('porta', 9600)
#s = ser.read(1000)
#print(s)


