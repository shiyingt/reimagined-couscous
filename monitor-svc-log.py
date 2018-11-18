import numpy as np
import os
import csv
import time
import signal
import sys
import RPi.GPIO as GPIO


t = 0
timed=[]
temperature=[]
cpu=[]
fanspeed=[]
fanPin = 33 # The pin ID, edit here to change it

#DEFINE VARIABLES
def measure_temp():

        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

def measure_cpu():

		CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
		return (CPU_Pct.replace("CPU_Pct=",""))

#FAN VARIABLES
def Shutdown():  
    fanOFF()
    os.system("sudo shutdown -h 1")
    sleep(100) 

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    return temp

def handleFan():
    #fanSpeed = list(map(lambda x: x/66*100, n))
    t=0
    n=0
    while n<66 :
    	
    	myPWM.ChangeDutyCycle(n) #change speed cycle

    	fanSpeed=100-n/66*100 #conversion of range(0,66) to (0,100)
    	fanspeed.append(fanSpeed) #array fanspeed
    	temperature.append(measure_temp()) #array temperature
    	cpu.append(measure_cpu()) #array cpu
    	timed.append(t) #array time


    	time.sleep(10) #for a new fanspeed, keep running for 1 seconds
    	t+=10 #increment of 5 seconds per loop
    	n+=3.3 #increment of 5 for speed	
    	print(n)
    	print(measure_temp())

      
		
def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(fanPin, mode)
    return()

def writeCsv():
	#PUT ARRAYS INTO ROWS
	rows =zip(timed, temperature, cpu, fanspeed)

	#CHANGE TO CSV FILES
	with open('30fps.csv','wb') as csvfile:
		ttcfwriter =csv.writer(csvfile, delimiter=',')
		ttcfwriter.writerows(rows);



#MAIN LOOP   
try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(fanPin, GPIO.OUT)
    myPWM=GPIO.PWM(33,100)
    myPWM.start(100)
    GPIO.setwarnings(False)
    time.sleep(10)
    handleFan()
    writeCsv()

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    fanOFF()
    print('exception')
    myPWM.stop()
    GPIO.cleanup() # resets all GPIO ports used by this program
