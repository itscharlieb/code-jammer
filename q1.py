import sys
import os
import csv
print(__doc__)
import pickle
import numpy as np
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
#containing the test data matrix and the labels matrix.
def parse_matrix_labels(fname):
    fs = []
    ls = []
    d = {}
    with open(fname, 'rt') as cf:
        c = csv.reader(cf, delimiter='\t')
        for r in c:
            d[r[0]] = r[1:]

    for row in d:
        ls.append(d[row][265])
        fs.append(d[row][0:265])

    ls = [int('C' in l) for l in ls]

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
a, b = parse_matrix_labels(f)
#print(a)
c = []
for row in a:
    c.append(row[:14])
print(b)
svc = svm.SVC(kernel='linear', C=1).fit(c,b)
print "finished one"

#svc = svm.SVC(kernel='linear', C=0.01).fit(a,b)
print "finished the other"
spickle = pickle.dumps(svc)
print spickle
print svc

