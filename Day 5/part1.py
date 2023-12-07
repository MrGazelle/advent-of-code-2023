import sys
import re

D = open("C:/Users/dfale/Desktop/Day 5/input.txt", "r").read()

parts = D.split('\n\n')
seeds, *others = parts
seeds = seeds.split(':')[1].split()

def f(x, o):
    A = []
    for line in o:
        dest, src, sz = [int(x) for x in line.split()]
        if src<=x<=src+sz:
            return dest+(x-src)
    return x

S = []
for seed in seeds:
    seed = int(seed)
    for o in others:
        O = o.split('\n')
        seed = f(seed, O[1:])
    S.append(seed)
print(min(S))