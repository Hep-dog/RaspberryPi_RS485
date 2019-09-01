import serial
import time
import binascii

ser = serial.Serial("/dev/ttyS0", 9600)
myinput = bytes.fromhex('01 03 00 00 00 02 C4 0B')
ser.write(myinput)

time.sleep(2)
s = ser.inWaiting()

if s != 0:
    data = str(binascii.b2a_hex(ser.read(s)))[2:-1]
    dataInfo = {}
    w = int(data[6:10], 16)/10
    s = int(data[10:14], 16)/10
    print( w, s )

ser.flushInput()
