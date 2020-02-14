'''import warnings
import serial
import serial.tools.list_ports
from time import sleep


try:
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description
    ]
    if not arduino_ports:
        raise IOError("No Arduino found")
    if len(arduino_ports) < 4:
        warnings.warn('Maybe some arduino didn\'t got a port')
    sleep(3)
except OSError:
    print("No Arduino found")
    ser = None
ser = serial.Serial('COM3', 9600, timeout=0.2)

def call_serial(char_name):
    ser.open()
    ser.write(char_name.encode('ascii'))
    ser.close()'''


import warnings
import serial
import serial.tools.list_ports


def arduino_port():
    try:
        arduino_ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'Arduino' in p.description
        ]
        if not arduino_ports:
            raise IOError("No Arduino found")
        if len(arduino_ports) > 1:
            warnings.warn('Multiple Arduinos found - using the first')
        ser = serial.Serial(arduino_ports[0])
    except OSError:
        print("No Arduino found")
        ser = None
    return ser