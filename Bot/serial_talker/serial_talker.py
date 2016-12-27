#!/usr/bin/pyhton3
import config
import serial


def start_serial_port():
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM3'
    ser.timeout = 2.0 # Give time to read all init messages.
    print(ser)
    try:
        ser.open()
    except:
        print("Serial port opening failed.")
        config.serial_initialized = False
        return
    init_message = ser.readline()

    while len(init_message) != 0:
        print(len(init_message))
        print(init_message)
        init_message = ser.readline()
    print("Serial port opened.")
    config.serial_initialized = True

def execute_command(command):
    ser.write(command.encode())
    response = ser.readline().decode();
    return response;
    

start_serial_port()

if __name__ == "__main__":
    
    ser.write(b'4')
    reads = 4
    while reads > 0:
        reads -= 1
        s = ser.readline()
        print("{} {}".format(reads, s))
    
    #
    ser.write(b's')
    reads = 5
    while reads > 0:
        reads -= 1
        s = ser.readline()
        print("{} {}".format(reads, s))
    
