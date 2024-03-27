import serial
import pandas as pd

arduino = serial.Serial(port='/dev/cu.usbmodem103226201', baudrate=19200)

df = pd.read_csv("/Users/begumcelik/Desktop/Reading_Data_from_Arduino_Due/out1.csv") 

# Remove first row [0,0,0,0,0,0,0,0] - this row was added by the developer for convenience not read from arduino
df = df.iloc[1: , :]

# Remove * character at the end of time values
#df['time_stamp'] = df['time_stamp'].str.rstrip('*')

# Convert all the data / str to int
df = df.apply(pd.to_numeric)

# Subtract the first time stamp from whole column values to define the start action as 0 point.
start_time = df.loc[1].at["time_stamp"]
df['time_stamp'] -= start_time

# drop index column, will be removed in the serial_read later
#df.drop(df.columns[[0,1,2]], axis=1)

# Preview the dataframe
print(df)

df.to_csv('/Users/begumcelik/Desktop/final_out1.csv', index = False)  

'''
print()

for i in range(3):
    arduino.write("hello\n".encode('utf-8'))
#arduino.write(('\n'.encode('utf-8')))

#arduino.close()

#for i in range(len(df)):
    #arduino.write(('hello*'.encode('utf-8')))
    
    #print(df.loc[i+1].at["time_stamp"])
    
    
'''

