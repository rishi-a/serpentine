#!/usr/bin/env python
# coding: utf-8

# In[1]:




# In[6]:


import pandas as pd


# In[20]:


import serial
import csv
import signal
import sys

# Replace '/dev/cu.usbmodel1101' with your actual serial port.
ser = serial.Serial('/dev/cu.usbmodem1101', 9600)  # Adjust the baud rate as needed.

# Create a CSV file to write the data.
with open('all.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    def signal_handler(sig, frame):
        # Gracefully close the serial port and CSV file on Ctrl+C.
        ser.close()
        csv_file.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            data = ser.readline()
            decoded_data = data.decode('utf-8')  # Assuming the data is in UTF-8 encoding.
            #print(decoded_data)
            
            # Write the data to the CSV file.
            csv_writer.writerow([decoded_data])
        except KeyboardInterrupt:
            # Handle Ctrl+C to allow for graceful termination.
            ser.close()
            csv_file.close()
            sys.exit(0)

