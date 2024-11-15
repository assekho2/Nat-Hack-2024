"""
Main file for Nathacks 2024
EXG PILL signal recognition
15/11/2024

Khushdeep Brar
"""
import serial 
import time
import csv 
import numpy as np
from scipy.signal import butter, sosfilt
import matplotlib.pyplot as plt 

PORT = 'COM3' # our device COM number replace 
BAUD_RATE = 9600 # its a typical rate for BiOAMP
DURATION = 60 # time of measuirng our data
OUTPUT_FILE = 'eeg_data.csv'

def acquire_eeg_data(port, baud_rate, duration, output_file):
    try: # just getting the data from the device 
        ser = serial.Serial(port, baud_rate, timeout= 1)
        print(f"Connected to {port} at {baud_rate} baud.")


        with open(output_file, mode = 'w', newline = ' ') as file:
            writer  = csv.writer(file)
            writer.writerow(["Timestamp", "EEG Signal"])

            start_time = time.time()
            while time.time() - start_time < duration:
                if ser.in_waiting >0 :
                    line = ser.readline().decode ("utf-8").strip()
                    if line.isdigit():
                        timestamp = time.time()
                        writer.writerow([timestamp, float(line)])
                        print(f"Recorded: {timestamp}, {line}")
        print(f"Data collection complete. Saved to {output_file}.")
        ser.close()
    except Exception as e: 
        print(f"Error: {e}")

acquire_eeg_data(PORT, BAUD_RATE, DURATION, OUTPUT_FILE)




