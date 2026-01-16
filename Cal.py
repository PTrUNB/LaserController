#!/usr/bin/python
import sys
from time import sleep
import numpy as np
from gpib import eth as gpibeth
from gpib import usb as gpibusb 
from instruments import E3631A

GPIB1HOST = "172.20.0.50"
GPIB1PORT = "1234"

GPIB2HOST = "172.20.0.51"
GPIB2PORT = "1234"

GPIB3HOST = "/dev/ttyACM0"
GPIB3BAUD = 38400

voltMin       = 0.0  # Start Voltage
voltMax       = 5.0  # Stop Voltage
voltPointsMin = 20   # Minumum point between
voltMinStep   = 0.005  # Volts
dVdVLimit     = 0.2 # Change in linearity to request more points 
voltList      = np.linspace(voltMin,voltMax,voltPointsMin)
#voltList = [ 0,0.1,0.2,0.25,0.5,0.9,0.95,0.975,1.0,1.025,1.05,1.1,1.25,1.5,1.75,1.9,2,2.1,2.5,3,3.5,3.8,3.9,3.975,4,4.025,4.05,4.1,4.2,4.5,5.0 ]
gpib1 = gpibeth(GPIB1HOST,GPIB1PORT,verbose=False) 
gpib2 = gpibeth(GPIB2HOST,GPIB2PORT,verbose=False) 
gpib3 = gpibusb(GPIB3HOST,GPIB3BAUD,verbose=False)

# Power Supply setup
PSU = E3631A(gpib2,addr=1)
PSU.send("OUTPUT 0")
PSU.setVolts([1,2,3],[0.0,15.0,-15.0])
PSU.setCurrents([1,2],[0.010,0.2,0.2])
PSU.send("OUTPUT 1")
for index,volt,current in zip(range(1,4),PSU.measVolts([1,2,3]),PSU.measCurrents([1,2,3])):
    print("Volt %d: %2.3fV %1.3fA" % (index,float(volt),float(current)))

# Flush Input buffer
print('Device  :',gpib3.getvalue("*IDN?"))
print('Options :',gpib3.getvalue("*OPT?"))
print('Temp    :',gpib3.getvalue("TEMP"))


results = {}
newMeasurements = True
while newMeasurements:
    newMeasurements = False
    voltList = sorted(voltList)
    for volt in voltList:
        volt = round(volt,3)
        if volt not in results:
            print("New point ",volt)
            PSU.setVolts(1,volt)
            data = gpib3.getvalue("VOLT").replace('\r','').replace('V','').split('\n')[1].split(' ')[0:4]
            results[volt] = {0 : {'vin':float(data[0])},1 :{'vin':float(data[1])},2:{'vin':float(data[2])},3:{'vin':float(data[3])}}
    resultKeys = list(enumerate(sorted(results)))
    for i,volt in resultKeys[1:-1]:
        for channel in results[volt]:
            v1 = results[resultKeys[i-1][1]][channel]['vin']
            v2 = results[resultKeys[i+1][1]][channel]['vin']
            results[resultKeys[i][1]][channel]['dVdV'] = (v2-v1)/(resultKeys[i+1][1]-resultKeys[i-1][1])
    for i,volt in resultKeys[2:-2]:
        for channel in results[volt]:
            v1  = resultKeys[i-1][1]
            v2  = resultKeys[i+1][1]
            dV1 = results[resultKeys[i-1][1]][channel]['dVdV']
            dV2 = results[resultKeys[i+1][1]][channel]['dVdV']
            if (round(abs(dV2-dV1),3) > dVdVLimit):
                newpoints = []
                if (round(abs((v1-volt)/2),3) > voltMinStep):
                    newpoints = np.append(newpoints,volt-(volt-v1)/2)
                if (round(abs((v2-volt)/2),3) > voltMinStep):
                    newpoints = np.append(newpoints,volt+(v2-volt)/2)
                if len(newpoints)>0:
                    voltList = sorted(np.append(voltList,newpoints))
                    newMeasurements = True
                    print("----    Adding points between : current:%0.3fV dV: %0.3f dVdV:%0.3f" % (volt,(v2-v1),(dV2-dV1)),newpoints )
    print("====================")
    print("Interim results")
    for volt in sorted(results):
        print(volt, ',', results[volt][0]['vin'], ',', results[volt][1]['vin'], ',', results[volt][2]['vin'], ',', results[volt][3]['vin']) 
    print("====================")

gpib1.close()
gpib2.close()
gpib3.close()

