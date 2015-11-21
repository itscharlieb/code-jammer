import sys
import os
import csv
import numpy as np
print(__doc__)
#import matplotlib.pyplot as plt
from sklearn import svm, datasets

cs = {"M":1
     ,"F":0
     ,"YES":1
     ,"NO":0
     ,"Yes":1
     ,"No":0
     ,"NEG":-1
     ,"ND":0
     ,"NotDone":0
     ,"POS":1
     ,"NA":0
     }

#Function that takes a filename as an argument and outputs a tuple
#containing the test data matrix and the survival days matrix.
def parse_matrix_survival_days(fname):
    fs = []
    ls = []
    d = {}
    with open(fname, 'rt') as cf:
        c = csv.reader(cf, delimiter='\t')
        for r in c:
            d[r[0]] = r[1:]

    for row in d:
        ls.append(d[row][267])
        fs.append(d[row][0:265])

    for l in ls:
        i = ls.index(l)
        ls[i] = float(l)

    for f in fs:
        for e in f:
            i = f.index(e)
            #if e in ts:
            if e == 'Anthra-HDAC':
                f[i] = 1
                f.insert(i+1, 0)
                f.insert(i+2, 0)
                f.insert(i+3, 0)
                f.insert(i+4, 0)
            elif e == 'HDAC-Plus':
                f[i] = 0
                f.insert(i+1, 1)
                f.insert(i+2, 0)
                f.insert(i+3, 0)
                f.insert(i+4, 0)
            elif e == 'Flu-HDAC':
                f[i] = 0
                f.insert(i+1, 0)
                f.insert(i+2, 1)
                f.insert(i+3, 0)
                f.insert(i+4, 0)
            elif e == 'StdAraC-Plus':
                f[i] = 0
                f.insert(i+1, 0)
                f.insert(i+2, 0)
                f.insert(i+3, 1)
                f.insert(i+4, 0)
            elif e == 'Anthra-Plus':
                f[i] = 0
                f.insert(i+1, 0)
                f.insert(i+2, 0)
                f.insert(i+3, 0)
                f.insert(i+4, 1)
            elif e in cs:
                e = cs[e]
                f[i] = e
            else:
                if type(e) is int:
                    continue
                e = float(e)
                f[i] = e
    return (fs, ls)
f = sys.argv[1]
a, b = parse_matrix_survival_days(f)
print(a)
print(b)

