import serial


if __name__ == "__main__":
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM3'
    print(ser)
    ser.open()
    ser.write(b'4')
    reads = 10
    while reads > 0:
        reads -= 1
        s = ser.readline()
        print("{} {}".format(reads, s))