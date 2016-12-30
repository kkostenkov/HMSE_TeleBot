#!/usr/bin/pyhton3
import config
import json
import serial
import threading
import time

serial_read_frequency = 0.5 # seconds
status_query_frequency = 10 # seconds
status_request_command = "r"
status = {}

def parse_serial_message(message):
    if len(message) == 0:
        return
    try:
        parsed_message = json.loads(message)
    except:
        print("Arduino system message: %s" % message)
        return
    print (parsed_message)
    # Merge into status
    for key, value in parsed_message.items():
        status[key] = value

def serial_listener_loop(ser):
    print("Serial listener loop launched.")
    while True:
        time.sleep(serial_read_frequency)
        serial_message = ser.readline().decode();
        parse_serial_message(serial_message)
        while len(serial_message) != 0:
            serial_message = ser.readline().decode()
            parse_serial_message(serial_message)

def status_query_loop(ser):
    print("Status query loop launched.")
    status_query = status_request_command.encode()
    while True:
        time.sleep(status_query_frequency)
        ser.write(status_query)
            
def start_serial_port(ser):
    ser.baudrate = 9600
    ser.port = config.get_serial_port()
    ser.timeout = 2.0 # Give time to read all init messages.
    print(ser)
    try:
        ser.open()
    except:
        print("Serial port opening failed.")
        config.serial_initialized = False
        return
    print("Serial port opened.")
    config.serial_initialized = True

def execute_command(command):
    ser.write(command.encode())
    response = ser.readline().decode();
    print(response)
    return response;
    
ser = serial.Serial()
start_serial_port(ser)
if config.serial_initialized:    
    # serial_listener_loop
    worker = threading.Thread(target=serial_listener_loop,
                              args=(ser,)
                              )
    worker.setDaemon(True)
    worker.start()
    # status_query_loop
    worker = threading.Thread(target=status_query_loop,
                              args=(ser,)
                              )
    worker.setDaemon(True)
    worker.start()

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
    
