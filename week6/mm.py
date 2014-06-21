# Madian Maintenace
import sys

arr = []
with open('Median.txt', 'r') as f:
    for line in f.readlines():
        arr.append(int(line))

arr.insert(0, 0)

def MadianMaintenace(arr):

    result = 0
    for i in xrange(1, len(arr)):
        b = sorted(arr[:i+1])
        if (i%2) == 1:
            result+=b[(i+1)/2]
        else:
            result+=b[i/2]
    return result % 10000

print MadianMaintenace(arr)

