import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/dfale/Desktop/Day 4/input.txt', sep = '\t')
games = np.array(df['games'])

ans = 0
for game in games:
    mine, win = game.split('|')
    id, numb = mine.split(':')
    print()
    mynumb = [int(x) for x in numb.split()]
    winnumb = [int(x) for x in win.split()]
    matches = len(set(mynumb) & set(winnumb))
    if matches > 0:
        ans += 2**(matches-1)

print(ans)
