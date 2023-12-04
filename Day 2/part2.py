# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:52:21 2023

@author: dfale
"""

import re
import pandas as pd
import numpy as np

mult = 0

def check_game(game_str):
    # Extract the number of cubes of each color
    global mult
    pattern = r"(\d+) (\w+)"
    matches = re.findall(pattern, game_str)
    cubes = {
        'green': 0,
        'red': 0,
        'blue': 0}
    for match in matches:
        count, color = match
        if cubes[color] > int(count):
            continue
        else: 
            cubes[color] = int(count)

    # Check if the number of cubes of each color is valid
    mult = cubes['red']*cubes['blue']*cubes['green']

    return True

# Read the input string
df = pd.read_csv('input1.txt', sep = '\t')
codes = np.array(df['games'])

# Split the input string into games
# games = codes.split("\n")

# Check which games would have been possible
possible_games = []
summ = 0;
for game in codes:
    if check_game(game):
        possible_games.append(game)
        print(mult)
        summ = summ + mult;
        print(summ)

# Print the possible games
print("Possible games:")
for game in possible_games:
    print(game)
print("Sum of the IDs: ", summ)