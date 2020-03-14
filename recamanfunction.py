#! usr/bin/env python3

"""
Created on Fri Mar 13 14:44:22 2020

@author: LD
"""

def recaman(n):
    seq = [0]
    x = 0
    i = 0
    while i < n:
        for i in range(0, n + 1):
            if (i == 0):
                seq[0] = 0
                print(i, seq[0])
            else:
                x = seq[i - 1] - i
                if (x >= 0 and x not in seq):
                    seq.append(x)
                    print(i, x)
                else:
                    x = seq[i - 1] + i
                    seq.append(x)
                    print(i, x)
        return seq

n = (int(input('How many terms do you want? ')))
print(recaman(n))