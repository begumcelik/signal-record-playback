import serial
import pandas as pd

# Do not forget to change the port and baudrate for serial connection with Arduino in your setup
arduino = serial.Serial(port='/dev/cu.usbmodem103226201', baudrate=28800)

output = "00000000"
initial =  {'time_stamp': 0, 'input1': output[0], 'input2': output[1], 'input3': output[2], 'input4': output[3], 'input5': output[4], 'input6': output[5], 'input7': output[6], 'input8': output[7]}
cols = ['time_stamp', 'input1', 'input2', 'input3', 'input4', 'input5', 'input6', 'input7', 'input8']
df = pd.DataFrame(data = initial, columns = cols, index = [0])

# The last pin open and closes the pipe blower in the current setup. If it turns 1 it means the execution is over.
# Depends on the configuration of the pins it can be either first or the last pin, you can change the index accordingly.
while (output[7] == "0" ):
    data = arduino.read_until(b'*')
    print(data)

    data = data.rstrip()
    data = data.decode("utf-8", errors='ignore')

    data_arr = data.split(';')
    output = data_arr[0]
    output = output.strip('\x00')
    time_stamp = data_arr[1]
    time_stamp = time_stamp.strip('\x00')
    time_stamp = time_stamp.rstrip('*')

    print(output)

    new_row = {'time_stamp': time_stamp, 'input1': output[0], 'input2': output[1], 'input3': output[2], 'input4': output[3], 'input5': output[4], 'input6': output[5], 'input7': output[6], 'input8': output[7]}
    #df = df.append(new_row, ignore_index=True) #append function will be removed in the future python version, so that concat func used instead
    df = pd.concat([df, pd.DataFrame(new_row, columns = cols, index = [0])], ignore_index=True)

    data = ""
    data_arr = []
   
    # If the sequence is over, write the data into csv file and end the execution
    if(output[7] == "1" ):
        #drop first column
        #df = df.iloc[: , 1:]
        df.to_csv('/Users/begumcelik/Desktop/Reading_Data_from_Arduino/out.csv', header=None)
        

arduino.close()


