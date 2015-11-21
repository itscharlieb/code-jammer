import sys
import os
import csv
print(__doc__)
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
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
print(a)
print(b)

# import some data to play with
#iris = datasets.load_iris()
#X = iris.data[:, :2]  # we only take the first two features. We could
#                      # avoid this ugly slicing by using a two-dim dataset
#y = iris.target
#X = features
#y = labels
#h = .02  # step size in the mesh
#X_1 = [feature[0] for feature in features]
#X_2 = [feature[1] for feature in features]
## we create an instance of SVM and fit out data. We do not scale our
## data since we want to plot the support vectors
#C = 1.0  # SVM regularization parameter
#svc = svm.SVC(kernel='linear', C=C).fit(X, y)
#rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
#poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
#lin_svc = svm.LinearSVC(C=C).fit(X, y)
#
## create a mesh to plot in
#x_min, x_max = -1, 2
#y_min, y_max = 0, 10
#xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                     np.arange(y_min, y_max, h))
#
## title for the plots
#titles = ['SVC with linear kernel',
#          'LinearSVC (linear kernel)',
#          'SVC with RBF kernel',
#          'SVC with polynomial (degree 3) kernel']
#for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
#    # Plot the decision boundary. For that, we will assign a color to each
#    # point in the mesh [x_min, m_max]x[y_min, y_max].
#    plt.subplot(2, 2, i + 1)
#    plt.subplots_adjust(wspace=0.4, hspace=0.4)
#
#    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#
#    # Put the result into a color plot
#    Z = Z.reshape(xx.shape)
#    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
#
#    # Plot also the training points
#    plt.scatter(X_1, X_2, c=y, cmap=plt.cm.Paired)
#    plt.xlabel('Sepal length')
#    plt.ylabel('Sepal width')
#    plt.xlim(xx.min(), xx.max())
#    plt.ylim(yy.min(), yy.max())
#    plt.xticks(())
#    plt.yticks(())
#    plt.title(titles[i])
#
#plt.show()

