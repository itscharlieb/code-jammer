import csv
from sklearn import svm
d = {}
with open('data.txt', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        d[row[0]] = row[1:]

#for row in d:
	#print d[row]

features = []
labels = []

for row in d:
	#print d[row][10]
	labels.append(d[row][265])
	features.append(d[row][100:105])
#print labels
labels = [int('C' in label) for label in labels]
#print labels
# for row in d:
# 	features = d[row]
#print vals[0]
print len(labels)
print len(features)
clf = svm.SVC()
clf.fit(features, labels)
