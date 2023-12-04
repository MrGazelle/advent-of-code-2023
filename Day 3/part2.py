# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 17:38:04 2023

@author: dfale
"""

import re

def calculate_part_numbers(grid):
    part_numbers = []
    part_number = []
    currRow = 0
    hasAdjacent = False
    # Iterate through each row of the grid
    for row in range(0, len(grid)):
        # Iterate through each character in the row
        for i, char in enumerate(grid[currRow]):
            # Check if the character is a digit
            if char.isdigit():
                # Check for adjacent symbols
                part_number.append(char)
                for j in range(-1, 2):
                    rowIn = currRow + j
                    if(rowIn > 139):
                        break
                    for k in range(-1, 2):
                        column = i + k
                        if column > 139:
                            break
                        adjacent_char = grid[rowIn][column]
                        if adjacent_char in "*":
                            hasAdjacent = True
                            astIndex = (rowIn, column)
            else:
                if hasAdjacent == True:
                    if len(part_number) == 1:
                        part_number = part_number[0]
                    elif len(part_number) == 2:
                        part_number = part_number[0] + part_number[1]
                    elif len(part_number) == 3:
                        part_number = part_number[0] + part_number[1] + part_number[2]
                    part_numbers.append([part_number, astIndex])
                    hasAdjacent = False
                part_number = []           
        currRow += 1
    return part_numbers


import pandas as pd
import numpy as np

df = pd.read_csv('input.txt', sep = '\t')
codes = np.array(df['grid'])

# Calculate the sum of part numbers
part_numbers = calculate_part_numbers(codes)
part_numbers = part_numbers
sum_of_part_numbers = 0
multAfterSum = 0
for k in range(0, len(part_numbers)):
    for i in range(k+1, len(part_numbers)):
        if(part_numbers[k][1] == part_numbers[i][1]):  
            sum_of_part_numbers += int(part_numbers[k][0])*int(part_numbers[i][0])

print(sum_of_part_numbers)