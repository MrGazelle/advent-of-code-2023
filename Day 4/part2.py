import pandas as pd
import numpy as np
from collections import defaultdict

df = pd.read_csv('C:/Users/dfale/Desktop/Day 4/input.txt', sep = '\t')
games = np.array(df['games'])

ans = 0
N = defaultdict(int)
for i, game in enumerate(games):
    N[i] += 1
    mine, win = game.split('|')
    id, numb = mine.split(':')
    print()
    mynumb = [int(x) for x in numb.split()]
    winnumb = [int(x) for x in win.split()]
    matches = len(set(mynumb) & set(winnumb))
    for j in range(matches):
        N[i+1+j] += N[i]
    if matches > 0:
        ans += 2**(matches-1)

print(ans)
print(sum(N.values()))
