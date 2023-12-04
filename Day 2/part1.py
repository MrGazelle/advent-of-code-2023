# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:52:21 2023

@author: dfale
"""

import re
import pandas as pd
import numpy as np

aux = 0

def check_game(game_str):
    # Extract the number of cubes of each color
    global aux
    pattern = r"(\d+) (\w+)"
    matches = re.findall(pattern, game_str)
    cubes = {
        'green': 0,
        'red': 0,
        'blue': 0}
    for match in matches:
        count, color = match
        if color == 'red':
            if cubes[color] > 12:
                break
            else: 
                cubes[color] = int(count)
        if color == 'green':
            if cubes[color] > 13:
                break
            else: 
                cubes[color] = int(count)
        if color == 'blue':
            if cubes[color] > 14:
                break
            else: 
                cubes[color] = int(count)

    # Check if the number of cubes of each color is valid
    if cubes["red"] > 12 or cubes["green"] > 13 or cubes["blue"] > 14:
        return False
    else:
        ints = []
        splot = game_str.split(": ")
        splut = splot[0].split(" ")
        ints = splut[1]
        print(ints)
        print(len(ints))
        if len(ints) == 2: 
            ints = ints[0]+ints[1]
            aux = int(ints)
        elif len(ints) == 1:
            aux = int(ints[0])
        elif len(ints) == 3:
            ints = ints[0] + ints[1] + ints[2]
            aux = int(ints)
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
        print(aux)
        summ = summ + aux;
        print(summ)

# Print the possible games
print("Possible games:")
for game in possible_games:
    print(game)
print("Sum of the IDs: ", summ)