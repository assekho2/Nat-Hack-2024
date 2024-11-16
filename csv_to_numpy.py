# for each line, get the third number
# normalize each number then convert to array

import numpy as np
import csv

def csv_to_arr(csv_filename):
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    data_arr = np.array(data, dtype=float)
    
    mask = 