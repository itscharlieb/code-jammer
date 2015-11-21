import csv
from sklearn import svm
import numpy as np
print(__doc__)
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

import matplotlib.pyplot as plt
from sklearn import svm, datasets

d = {}
with open('data.txt', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        d[row[0]] = row[1:]
features = []
labels = []
for row in d:
	#print d[row][10]
	labels.append(d[row][265])
	features.append(d[row][0:3])
labels = [int('C' in label) for label in labels]
for feature in features:
	feature[0] = int('F' in feature[0])
	feature[1] = float(feature[1])/10
    feature[2] = float(feature[2])*1

print features

X = features
y = labels
h = .02  # step size in the mesh
X_1 = [feature[0] for feature in features]
X_2 = [feature[1] for feature in features]
# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
lin_svc = svm.LinearSVC(C=C).fit(X, y)