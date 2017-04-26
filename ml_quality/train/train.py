import numpy
import sklearn
import math

import pickle

from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier as knn

X1 = []
f = open("../../scripts/pythonparse/bad_1.out")
i = 0
j = 0
X1.append([])
for line in f:
    #print line
#    print line.strip().isdigit()
    if line.strip().isdigit() and (j % 6) == 0:
        num1 = int(line)
        X1[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 2:
        X1[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 3:
        X1[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 4:
        X1[i].append(float(line))
        i += 1
        X1.append([])
    j += 1
X1.pop()
f.close()
print X1[:10]
print len(X1)

f = open("../../scripts/bad_lint_1.out")
i = 0
j = 0
for line in f:
    #print line
#    print line.strip().isdigit()
    #print i
    X1[i].append(int(line))
    i += 1
    if i >= len(X1):
        break
f.close()
while (i < len(X1)):
    X1[i].append(2)
    i += 1
print X1[:10]
X1 = numpy.array(X1)
print len(X1)

for i in range(1, len(X1)):
   if (len(X1[i]) < 5):
    print len(X1[i]), i

X2 = []
f = open("../../scripts/pythonparse/good_1.out")
j = 0
i = 0
X2.append([])
for line in f:
    #print line
    params = 0
    if line.strip().isdigit() and (j % 6) == 0:
        num1 = int(line)
        X2[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 2:
        X2[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 3:
        num1 = int(line)
        X2[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 4:
        X2[i].append(float(line))
        i += 1
        X2.append([])
    j += 1
    if (j > 900):
        break
X2.pop(i)

print len(X2)

f = open("../../scripts/good_lint_1.out")
i = 0
j = 0
for line in f:
    #print line
#    print line.strip().isdigit()
    #print i
    X2[i].append(int(line))
    i += 1
    if i >= len(X2):
        break
f.close()
#print X2[:10]
X2 = numpy.array(X2)
#for i in range(1, len(X2)):
  #  print len(X2[i])
print len(X2)

y1 = []
y2 = []
y1 = [[0]]*len(X1)
y2 = [[1]]*len(X2)

Xn = []
yn = []
numpy.append(X1, X2)
yn = y1 + y2
print len(X1)
print len(X2)
Xn = numpy.append(X1, X2, axis = 0)
print len(yn)
print len(Xn)
print X1
print X2
print yn

clf = svm.SVC(kernel="rbf")
clf.fit(Xn, yn)

from sklearn.externals import joblib

joblib.dump(clf, '../model_new.pkl')
print "done"

