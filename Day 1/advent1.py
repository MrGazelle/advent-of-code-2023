# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:32:19 2023

@author: dfale
"""

import pandas as pd
import numpy as np

df = pd.read_csv('input1.txt', sep = '\t')
codes = np.array(df['codes'])
numbers = []

for i in range(len(df)):
    ints = []
    for index, char in enumerate(codes[i]):
        if char.isdigit():
            ints.append(char)
    ints = ints[0]+ints[len(ints)-1]
    aux = int(ints)
    numbers.append(aux)
    
summm = sum(numbers)
