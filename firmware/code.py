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
    if data['Temp1']:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC1 Temp: %2.3fC" % (float(data['Temp1'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.5,0.0),
            anchored_position = (int(display.display.width / 2),line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if data['Temp2']:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC2 Temp: %2.3fC" % (float(data['Temp2'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.5,0.0),
            anchored_position = (int(display.display.width / 2),line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if data['ADC0']:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC0: %1.6fV" % (float(data['ADC0'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.5,0.0),
            anchored_position = (int(display.display.width / 2),line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if data['ADC1']:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC1: %1.6fV" % (float(data['ADC1'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.5,0.0),
            anchored_position = (int(display.display.width / 2),line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if data['ADC2']:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC2: %1.6fV" % (float(data['ADC2'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.5,0.0),
            anchored_position = (int(display.display.width / 2),line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if data['ADC3']:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC3: %1.6fV" % (float(data['ADC3'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.5,0.0),
            anchored_position = (int(display.display.width / 2),line),
            scale = 3,
        )
        line += lineStep
        rootWindow.append(ChLabel)
    if data['ADC4']:
        ChLabel = label.Label (
            font=terminalio.FONT,
            text = "ADC4: %1.6fV" % (float(data['ADC4'])),
            color = 0xFFFFFF,
            background_color= 0x654321,
            background_tight=True,
            anchor_point = (0.5,0.0),
            anchored_position = (int(display.display.width / 2),line),
            scale = 3,
        )
        line += lineStep
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

import board
import busio
from supervisor import reload
import digitalio
import scpi
from ads122 import ads122c04
from ad569x import ad5696

#import displayio
import adafruit_qualia.graphics as graphics

display = graphics.Graphics(graphics.Displays.BAR320X820, default_bg=0x222222,auto_refresh=False)

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

pinA0 = True   # TMOD
pinA1 = True  # LD Driver Enable




dac1.setDAC([4],[int((1.024 / 2.5) * 2**16)]) # Default to mid range 0V out on TMOD

dac1.calMin = -3.0155     # Measured value at MinLimit
dac1.calMax = +2.986      # Measured value at MaxLimit
dac1.calMinLimit = 0.0    # Minimum allowed Value RAW DAC
dac1.calMaxLimit = 2.048  # Maximum allowed value RAW DAC

commands = scpi.console()
done = False
data = {}
while not done:
    data['Temp1'] = adc1.getTemp()
    data['Temp2'] = adc2.getTemp()
    data['ADC0'] = adc1.getVolt(8)
    data['ADC1'] = adc1.getVolt(9)
    data['ADC2'] = adc1.getVolt(10)
    data['ADC3'] = adc1.getVolt(11)
    data['ADC4'] = adc2.getVolt(8)
    data['ADC5'] = adc2.getVolt(9)
    data['ADC6'] = adc2.getVolt(10)
    data['ADC7'] = adc2.getVolt(11)
    root(display,data)
    commands.checkStream()
    command = commands.nextCommand().upper()
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

            if ecommand[0][:3] == "DAC":
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
                            if len(argv) == 2:
                                if argv[0].isdigit and is_number(argv[1]):
                                    dac1.setDAC(int(argv[0]),int(argv[1])) 
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
