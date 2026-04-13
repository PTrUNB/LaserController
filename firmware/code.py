import displayio
import terminalio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label as label
import sys
import supervisor
supervisor.runtime.autoreload = False

font = bitmap_font.load_font('fonts/Helvetica-Bold-16.bdf')

## Create a display class here
def setupDisplay():    
    display = Graphics(Displays.BAR320X820, default_bg=0x222222,auto_refresh=False)
    return display

def input(display):
   if display.touch.touched:
        coord = []
        try:  # Adafruit Library bug
            for touch in display.touch.touches:
                x = touch['x']
                y = touch['y']
                coord.append([x,y])
        except RuntimeError: # Adafruit Library bug
            pass
        return coord

def inputLast(display):
    coord = input(display)
    if coord and (type(coord) != type(None)): 
        return coord[-1]
    else:
        return []

def inputFirst(display):
    coord = input(display)
    if coord: 
        return coord[0]
    else:
        return []

def root(display,data):
    touchZones = {} 
    rootWindow = displayio.Group(scale=1,x=0,y=0)
    # Text area definition
    line = 0
    lineStep = 32
    col = 270
    if 'Temp1' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC1 Temp: %+7.3fC" % (float(data['Temp1'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'Temp2' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC2 Temp: %+7.3fC" % (float(data['Temp2'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'ADC0' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC0: %+7.4fV" % (float(data['ADC0'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'ADC1' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC1: %+7.4fV" % (float(data['ADC1'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'ADC2' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC2: %+7.4fV" % (float(data['ADC2'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'ADC3' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC3: %+7.4fV" % (float(data['ADC3'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'ADC4' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC4: %+7.4fV" % (float(data['ADC4'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'VIN0' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "VIN0: %+6.3fV" % (float(data['VIN0'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'VIN1' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "VIN1: %+6.3fV" % (float(data['VIN1'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'VIN2' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "VIN2: %+6.3fV" % (float(data['VIN2'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'VIN3' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "VIN3: %+6.3fV" % (float(data['VIN3'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'VOUT' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "VOUT: %+6.3fV" % (float(data['VOUT'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (col,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    # Formated user data
    line = 0
    col = 0
    if 'TMODE' in data:
        if data['TMODE']:
            bgcolor = 0x551111
            txt = "    Control    "
        else:
            bgcolor = 0x115511
            txt = "    Mid Val    "
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = txt,
            color = 0xFFFFFF,
            background_color= bgcolor,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (0,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'TSET' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = " TSET:%+7.3f°C " % (float(data['TSET'])),
            color = 0xFFFFFF,
            background_color= bgcolor,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (0,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'TMOD' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = f" TMOD:{float(data['TMOD']):+7.3f}°C ",
            color = 0xFFFFFF,
            background_color= bgcolor,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (0,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'TACT' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = " TACT:%+7.3f°C " % (float(data['TACT'])),
            color = 0xFFFFFF,
            background_color= bgcolor,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (0,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    line = 160
    if 'LDE' in data:
        if data['LDE']:
            bgcolor = 0x551111
            txt = "    Enabled    "
        else:
            bgcolor = 0x115511
            txt = "    Offline    "
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = txt,
            color = 0xFFFFFF,
            background_color= bgcolor,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (0,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'ILD' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = f" I LD:{float(data['ILD']): 6.1f}mA ",
            color = 0xFFFFFF,
            background_color= bgcolor,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (0,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if 'IPD' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = f" I PD:{float(data['IPD']): 6.1f}mA ",
            color = 0xFFFFFF,
            background_color= bgcolor,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (0,line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    ### TMOD interface
    if 'Cursor' in data:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "TMOD SET",
            color = 0xFFFFFF,
            background_color= 0x000000,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (410,0),
            scale = 3,
        )
        rootWindow.append(ChLabel)
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = " <      > ",
            color = 0xFFFFFF,
            background_color= 0x000000,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (410,240),
            scale = 7,
        )
        rootWindow.append(ChLabel)
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "<   >",
            color = 0xFFFFFF,
            background_color= 0x000000,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (740,0),
            scale = 7,
            label_direction="UPR"
        )
        rootWindow.append(ChLabel)
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = ">  <",
            color = 0xFFFFFF,
            background_color= 0x000000,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (637-data['Cursor']*24,44),
            scale = 5,
            label_direction="UPR"
        )
        rootWindow.append(ChLabel)
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = f"{float(data['TMODSET']):+5.3f}°C ",
            color = 0xFFFFFF,
            background_color= 0x000000,
            background_tight=True,
            anchor_point = (0.0,0.0),
            anchored_position = (540,80),
            scale = 4,
        )
        rootWindow.append(ChLabel)
    display.splash.append(rootWindow)
    display.display.refresh()
    display.splash.remove(rootWindow)

def is_number(s):
    try:
        float(s)  # Try converting to a float
        return True
    except ValueError:
        return False

from math import log
# Simplified from Thorlabs
def V2T(volt):
    # linear fit T = volt * 6.14202 + 9.92712
    Rth = (10.0 - volt) / (5.0 + volt)
    return  1/(3.3540170E-3 + 2.5617244E-4 * log(Rth) + 2.1400943E-6 * (log(Rth))**2 + -7.2405219E-9 * (log(Rth))**3) - 273.15

def V2A(volt):
    return (volt-1)*0.1

import board
import busio
from supervisor import reload
import digitalio
import scpi
from ads122 import ads122c04
from ad569x import ad5696

#import displayio
import adafruit_qualia.graphics as graphics

display = graphics.Graphics(graphics.Displays.BAR320X820, rotation=90 , default_bg=0x000000,auto_refresh=False)

i2c = display.i2c_bus
#i2c = busio.I2C(board.SCL,board.SDA)

adc1 = ads122c04(i2c,68)
adc2 = ads122c04(i2c,69)
dac1 = ad5696(i2c,14)
dac2 = ad5696(i2c,15)

pinA0 = digitalio.DigitalInOut(board.A0)
pinA0 = digitalio.Direction.OUTPUT

pinA1 = digitalio.DigitalInOut(board.A1)
pinA1 = digitalio.Direction.OUTPUT


dac1.setDAC([4],[int((1.024 / 2.5) * 2**16)]) # Default to mid range 0V out on TMOD

dac1.cal[0] = [-2.738 , 0.1 ]  # [measured,set] Cal lower limit
dac1.cal[1] = [-0.0362, 1.024    ]  # [measured,set] Cal lower limit
dac1.cal[2] = [+2.539 , 1.90  ]  # [measured,set] Cal upper limit
dac1.calMinLimit = 0.0    # Minimum allowed Value RAW DAC
dac1.calMaxLimit = 2.048  # Maximum allowed value RAW DAC

adc0Cal = [[ 0.0241, 0.0512 ],[ 1.8761 , 3.7990  ]]  # [measured low ,set low ] [measured high,set high ]
adc1Cal = [[ 0.0246, 0.0512 ],[ 1.9661 , 3.7990  ]]  
adc2Cal = [[ 0.2320, 1.10005],[+1.9253 , 1.9495  ]] 
adc3Cal = [[ 0.2989, 1.10005],[+1.9965 , 1.9495  ]]
adc4Cal = [[-2.7370, 0.1005 ],[+2.5400  , 1.90  ]]

adc0Calm  = (adc0Cal[0][1] - adc0Cal[1][1]) / (adc0Cal[0][0] - adc0Cal[1][0])
adc0Calb0 = adc0Cal[0][0] 
adc0Calb1 = adc0Cal[0][1] 

adc1Calm  = (adc1Cal[0][1] - adc1Cal[1][1]) / (adc1Cal[0][0] - adc1Cal[1][0])
adc1Calb0 = adc1Cal[0][0] 
adc1Calb1 = adc1Cal[0][1] 

adc2Calm  = (adc2Cal[0][1] - adc2Cal[1][1]) / (adc2Cal[0][0] - adc2Cal[1][0])
adc2Calb0 = adc2Cal[0][0] 
adc2Calb1 = adc2Cal[0][1] 

adc3Calm  = (adc3Cal[0][1] - adc3Cal[1][1]) / (adc3Cal[0][0] - adc3Cal[1][0])
adc3Calb0 = adc3Cal[0][0] 
adc3Calb1 = adc3Cal[0][1] 

adc4Calm  = (adc4Cal[0][1] - adc4Cal[1][1]) / (adc4Cal[0][0] - adc4Cal[1][0])
adc4Calb0 = adc4Cal[0][0] 
adc4Calb1 = adc4Cal[0][1] 

commands = scpi.console()
done = False

#Initial state
pinA0 = False  # TMOD
pinA1 = False  # LD Driver Enable
data = {}
data['Cursor'] = 0 
data['TMODSET'] = 0.0
dac1dVdV = (dac1.cal[0][0] - dac1.cal[-1][0]) / (dac1.cal[0][1] - dac1.cal[-1][1])
vout = (data['TMODSET'] - dac1.cal[0][0]) /  dac1dVdV + dac1.cal[0][1]
dac1.setDAC([4],int((vout / dac1.reference)*2**16))
while not done:
    Vadc0 = adc1.getVolt(8)
    Vadc1 = adc1.getVolt(9)
    Vadc2 = adc1.getVolt(10)
    Vadc3 = adc1.getVolt(11)
    Vadc4 = adc2.getVolt(8)
    #data['Temp1'] = adc1.getTemp()
    #data['Temp2'] = adc2.getTemp()
    #data['ADC0'] = Vadc0
    #data['ADC1'] = Vadc1
    #data['ADC2'] = Vadc2
    #data['ADC3'] = Vadc3
    #data['ADC4'] = Vadc4
    #data['ADC5'] = adc2.getVolt(9)
    #data['ADC6'] = adc2.getVolt(10)
    #data['ADC7'] = adc2.getVolt(11)
    #data['VIN0']  = (Vadc0 - adc0Calb0) * adc0Calm + adc0Calb1
    #data['VIN1']  = (Vadc1 - adc1Calb0) * adc1Calm + adc1Calb1 
    #data['VIN2']  = (Vadc2 - adc2Calb0) * adc2Calm + adc2Calb1 
    #data['VIN3']  = (Vadc3 - adc3Calb0) * adc3Calm + adc3Calb1 
    #data['VOUT']  = (Vadc4 - adc4Calb1) / adc4Calm + adc4Calb0
    data['TSET']  = V2T((Vadc0 - adc0Calb0) * adc0Calm + adc0Calb1)
    data['TACT']  = V2T((Vadc1 - adc1Calb0) * adc1Calm + adc1Calb1)
    data['ILD']   = V2A((Vadc2 - adc2Calb0) * adc2Calm + adc2Calb1)*1000
    data['IPD']   = V2A((Vadc3 - adc3Calb0) * adc3Calm + adc3Calb1)*1000 
    data['TMOD']  = ((Vadc4 - adc4Calb1) / adc4Calm + adc4Calb0 ) * 0.1
    data['TMODE'] = pinA0
    data['LDE']   = pinA1
    root(display,data)
    commands.checkStream()
    command = commands.nextCommand().upper()
    touchInput = inputFirst(display)
    if touchInput :
        # Enable or disable laser and TMOD
        if (touchInput[1] >= 0 ) & (touchInput[1] <= 270):
            if(touchInput[0] >= 0   ) & (touchInput[0] < 160):
                pinA1 = not(pinA1)
            if(touchInput[0] >= 160 ) & (touchInput[0] < 320):
                pinA0 = not(pinA0)
        # Digit TMODSET select
        if(touchInput[0] >= 0) & (touchInput[0] < 120):
            if (touchInput[1] > 615) & (touchInput[1] <=820):
                data['Cursor'] -= 1 
            if (touchInput[1] > 410) & (touchInput[1] <615):
                data['Cursor'] += 1 
            if data['Cursor'] < 0:
                data['Cursor'] = 0
            if data['Cursor'] > 2:
                data['Cursor'] = 2
        # Increase and decrease TMODSET DIGIT
        if (touchInput[1] >= 740) & (touchInput[1] <=820):
            if(touchInput[0] >= 120 ) & (touchInput[0] < 220):
                data['TMODSET'] -= 10**(data['Cursor']-3)
            if(touchInput[0] >= 220 ) & (touchInput[0] < 320):
                data['TMODSET'] += 10**(data['Cursor']-3)
            if data['TMODSET'] < -0.3:
                data['TMODSET'] = -0.3
            if data['TMODSET'] > 0.3:
                data['TMODSET'] = 0.3
            vout = (data['TMODSET']*10 - dac1.cal[0][0]) /  dac1dVdV + dac1.cal[0][1]
            dac1.setDAC([4],int((vout / dac1.reference)*2**16))
    if command != '':
        # Standard SCPI commands
        if command[0] == '*':
            if command == '*IDN?':
                print("Laser Monitor V0.1")
            if command == '*OPT?':
                i2c.try_lock()
                i2cbus = i2c.scan()
                print("Option ",i2cbus)
                i2c.unlock()
                for dev in i2cbus:
                    unknown = True
                    if dev >= 12 and dev<=15:
                        print(dev,"AD5659x DAC 16bits")
                        unknown = False
                    if dev >= 64 and dev<=79:
                        print(dev,"ADS1xx ADC 24bits")
                        unknown = False
                    if unknown:
                        print(dev,"Unknown device")
            if command == '*RST':
                done = True
        # Equipment specific commands
        ecommand = command.split(':')
        argv = []
        if len(ecommand[len(ecommand)-1].split(' ')) > 1:
            argv = ecommand[len(ecommand)-1].split(' ')[1:]
        if len(ecommand[0])>2:
            ### GENERIC Hardware commands
            if ecommand[0][:4] == "TEM":
                temp1 = adc1.getTemp()
                temp2 = adc2.getTemp()
                print(" %3.2fC %3.2fC" % (temp1,temp2))
            if ecommand[0][:4] == "VOL":
                if len(command) == 1:
                    print("%1.6fV " % adc1.getVolt(8),end="")
                    print("%1.6fV " % adc1.getVolt(9),end="")
                    print("%1.6fV " % adc1.getVolt(10),end="")
                    print("%1.6fV " % adc1.getVolt(11),end="")
                    print("%1.6fV " % adc2.getVolt(8),end="")
                    print("%1.6fV " % adc2.getVolt(9),end="")
                    print("%1.6fV " % adc2.getVolt(10),end="")
                    print("%1.6fV " % adc2.getVolt(11),end="")
            if ecommand[0][:4] == "ADC": #ADC Raw
                if len(command) == 1:
                    print("%06X " % adc1.getADC(8),end="")
                    print("%06X " % adc1.getADC(9),end="")
                    print("%06X " % adc1.getADC(10),end="")
                    print("%06X " % adc1.getADC(11),end="")
                    print("%06X " % adc2.getADC(8),end="")
                    print("%06X " % adc2.getADC(9),end="")
                    print("%06X " % adc2.getADC(10),end="")
                    print("%06X " % adc2.getADC(11),end="")
            ## ADC commands
            # :GET       Channel(0-15) raw value
            # :GET:VOLt  Channel(0-15) volt
            if ecommand[0][:3] == "ADC":
                if len(ecommand) >=2:
                    if len(ecommand) >=3:
                        if ecommand[2][:3] == "VOL":
                            if len(argv) >= 1:
                                print("TODO ADC:GET:VOLT")
                    else:
                        if ecommand[1][:3] == "GET":
                            if len(argv) >= 1:
                                print("TODO ADC:GET") 
            ## DAC commands
            # :SET      CHANNEL(1-4) int(0-65535)  raw value
            # :SET:VOLt CHANNEL(1-4) float(0-2.5)  Volts
            # :GET                                 Channel4 raw value
            # :GET:VOLt                            Channel4 volt
            if ecommand[0][:3] == "DAC":
                print("DAC")
                if len(ecommand) >=2:
                    if ecommand[1][:3] == "GET":
                        print("----DAC:GET",ecommand)
                        if len(ecommand) >=3:
                            if ecommand[2][:3] == "VOL":
                                print("VOLT")
                                if len(argv) == 1:
                                    if argv[0].isdigit():
                                        print(adc2.getVolt(8+int(argv[0])))
                        else:
                            if len(argv) == 1:
                                if argv[0].isdigit():
                                    print(adc2.getADC(8+int(argv[0])))
                    if ecommand[1][:3] == "SET":
                        print("DAC SET")
                        if len(ecommand) >= 3:
                            if ecommand[2][:3] == "VOL":
                                if len(argv) == 2:
                                    if argv[0].isdigit and is_number(argv[1]):
                                        print("Set DAC voltage",argv[0],argv[1])
                                        dac1.setDAC(int(argv[0]), int((float(argv[1])/dac1.reference)*2**16) ) 
                        else:    
                            if len(argv) == 2:
                                print("Set DAC raw value")
                                if argv[0].isdigit and is_number(argv[1]):
                                    print(argv[0],argv[1])
                                    dac1.setDAC(int(argv[0]),int(argv[1])) 
            ### APPLICATION COMMANDS
            # Scaled VOUt channel 4
            # dac1.cal[0] = [-1.5720, 0.5   ]  # [measured,set] Cal lower point
            # dac1.cal[1] = [-0.0362, 1.024 ]  # [measured,set] Cal mid point
            # dac1.cal[2] = [+1.3590, 1.5 ]    # [measured,set] Cal upper point
            # dac1.calMinLimit = 0.0    # Minimum allowed Value RAW DAC
            # dac1.calMaxLimit = 2.048  # Maximum allowed value RAW DAC
            if ecommand[0][:3] == "VOU":
                if len(ecommand) == 1:
                    if len(argv) == 1:
                        vout = (float(argv[0]) - dac1.cal[0][0]) /  dac1dVdV + dac1.cal[0][1]
                        if vout > dac1.calMaxLimit:
                            vout = dac1.calMaxLimit
                        if vout < dac1.calMinLimit:
                            vout = dac1.calMinLimit
                        dac1.setDAC([4],int((vout / dac1.reference)*2**16) )
                    else:
                        if 'VOUT' in data:
                            print("VOUT %+1.3f" % (data['VOUT']))
            if ecommand[0][:3] == "VIN":
                if len(ecommand) == 1:
                    if len(argv) == 1:
                        if is_number(argv[0]):
                            channel = int(argv[0])  
                            if 'VIN%1d' % channel in data:
                                print("VIN%1d %+1.3f" % (channel,data['VIN%1d' % channel]))
            if ecommand[0][:4] == "TMO": 
                dVdV = (dac1.calMaxLimit - dac1.calMinLimit)  / (dac1.calMax-dac1.calMin)
                if len(ecommand) >= 2:
                    if ecommand[1][:3] == "GET":
                        print(adc2.getADC(8) )
                    if ecommand[1][:3] == "SET":
                        if len(argv) == 1:
                            if is_number(argv[0]):
                                value = (dac1.calMaxLimit - dac1.calMinLimit)  / (dac1.calMax-dac1.calMin) * (float(argv[0]) - dac1.calMin)
                                if value >dac1.calMaxLimit:
                                    value = dac1.calMaxLimit
                                    print(value)
                                if value <dac1.calMinLimit:
                                    value = dac1.calMinLimit
                                    print(value)
                                dac1.setDAC([4],[int((value / dac1.reference) * 2**16)]) # Default to mid range 0V out on TMOD
                            else:
                                print("Usage: TMOD VALUE, Value was not numeric")
                        else:
                            print("Usage: TMOD VALUE")
print("Done")
reload()
