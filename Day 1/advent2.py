import pandas as pd
import numpy as np

df = pd.read_csv('input2.txt', sep = '\t')
codes = np.array(df['codes'])
numbers = []

thisdict = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

for i in range(len(df)):
    ints = []
    for index, char in enumerate(codes[i]):
        if char.isdigit():
            ints.append(char)
        else:
            str2 = ''
            for index1, char1 in enumerate(codes[i][index:len(codes[i])]):
                str2 = str2 + char1
                if str2 in thisdict.keys():
                    ints.append(thisdict[str2])
                    break
    ints = ints[0]+ints[len(ints)-1]
    aux = int(ints)
    numbers.append(aux)
    
summm = sum(numbers)