import serial


ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.timeout = 2.0 # Give time to read all init messages.
print(ser)
ser.open()
init_message = ser.readline()

while len(init_message) != 0:
    print(len(init_message))
    print(init_message)
    init_message = ser.readline()
print("Serial port opened.")

def execute_command(command):
    ser.write(command.encode())
    response = ser.readline().decode();
    return response;
    

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
    