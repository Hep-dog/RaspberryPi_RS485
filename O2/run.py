import serial
import time
import binascii
import logging

logging.basicConfig( filename='/home/pi/Work/RS485/O2/data/O2.dat', filemode='a', format='%(created)f %(message)s', level=logging.INFO)
ser = serial.Serial("/dev/ttyS0", 9600)

humid, tempt, o2 =  0, 0, 0

TH_input = bytes.fromhex('01 03 00 00 00 02 C4 0B')
O2_input = bytes.fromhex('01 03 00 06 00 01 64 0B')

def read_TH():
    ser.flushInput()
    ser.write(TH_input)
    time.sleep(1)
    s = ser.inWaiting()

    if s != 0:
        data = str(binascii.b2a_hex(ser.read(s)))[2:-1]
        dataInfo = {}
        h = int(data[6:10], 16)/10
        t = int(data[10:14], 16)/10
        return h, t

def read_O2():
    ser.flushInput()
    ser.write(O2_input)
    time.sleep(1)
    s = ser.inWaiting()

    if s != 0:
        data = str(binascii.b2a_hex(ser.read(s)))[2:-1]
        dataInfo = {}
        o = int(data[6:10], 16)/10
        return o


def main():
    ( humid, tempt ) = read_TH()
    o2 = read_O2()
    if humid!=0 and tempt!=0 and o2!=0:
        logging.info('Temp={0:0.1f}C and Humi={1:0.1f}% and O2={2:0.1f}%'.format(tempt, humid, o2))

if __name__ == "__main__":
    main()
