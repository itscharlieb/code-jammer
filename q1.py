import sys
import os
import csv
import fileinput
import re

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
     ,"":0
     }

def parse_testing_matrix(lname):
    fs = []
    d = {}

    for r in lname:
        a = r.split("\t")
        d[a[0]] = a[:]

    for row in d:
        fs.append(d[row][0:265])
    for f in fs:
        for e in f:
            i = f.index(e)
            # if e == 'Anthra-HDAC':
            #     f[i] = 1
            #     f.insert(i+1, 0)
            #     f.insert(i+2, 0)
            #     f.insert(i+3, 0)
            #     f.insert(i+4, 0)
            # elif e == 'HDAC-Plus':
            #     f[i] = 0
            #     f.insert(i+1, 1)
            #     f.insert(i+2, 0)
            #     f.insert(i+3, 0)
            #     f.insert(i+4, 0)
            # elif e == 'Flu-HDAC':
            #     f[i] = 0
            #     f.insert(i+1, 0)
            #     f.insert(i+2, 1)
            #     f.insert(i+3, 0)
            #     f.insert(i+4, 0)
            # elif e == 'StdAraC-Plus':
            #     f[i] = 0
            #     f.insert(i+1, 0)
            #     f.insert(i+2, 0)
            #     f.insert(i+3, 1)
            #     f.insert(i+4, 0)
            # elif e == 'Anthra-Plus':
            #     f[i] = 0
            #     f.insert(i+1, 0)
            #     f.insert(i+2, 0)
            #     f.insert(i+3, 0)
            #     f.insert(i+4, 1)
            if e in cs:
                e = cs[e]
                f[i] = e
            else:
                if not re.search('[a-zA-Z]', e):                    
                    e = float(e)
                f[i] = e
    return fs
print("This is a test")
f = sys.stdin
a = parse_testing_matrix(f)
print(a)
print(b)
#print(a)
#print(b)
# c = []
# for row in a:
#     c.append(row[:10])
# c_1 = c[:100]
# c_2 = c[100:]
# b_1 = b[:100]
# b_2 = b[100:]
#svc = svm.SVC(kernel='linear', C=0.01).fit(a,b)
#print svc.score(c_2, b_2)

