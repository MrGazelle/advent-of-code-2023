import sys
import re

D = open("C:/Users/dfale/Desktop/Day 5/input.txt", "r").read().strip()

parts = D.split('\n\n')
seeds, *others = parts
#seeds = seeds.split(':')[1].split()
seeds = [int(x) for x in seeds.split(':')[1].split()]

def f(R, o):
    A = []
    for line in o:
        dest, src, sz = [int(x) for x in line.split()]
        src_end = src+sz
        NR = []
        while R:
            (st, ed) = R.pop()
            before = (st, min(ed, src))
            intermediate = (max(st, src), min(src_end, ed))
            after = (max(src_end, st), ed)
            if before[1]>before[0]:
                NR.append(before)
            if intermediate[1]>intermediate[0]:
                A.append((intermediate[0]-src+dest, intermediate[1]-src+dest))
            if after[1]>after[0]:
                NR.append(after)
        R = NR
    return A+R

S = []
si = 0
while si < len(seeds):
    st, sz = seeds[si], seeds[si+1]
    si += 2
    R = [(st, st+sz)]
    for o in others:
        O = o.split('\n')
        R = f(R, O[1:])
    S.append(min(R)[0])
print(min(S))