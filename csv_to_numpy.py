# for each line, get the third number
# normalize each number then convert to array

import numpy as np
import csv

def csv_to_arr(csv_filename):
    data = []

    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            if len(row) >= 3:
                try:
                    data.append(float(row[2]))
                except:
                    pass
    
    return np.array(data)