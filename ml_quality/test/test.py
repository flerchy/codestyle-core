import argparse
import numpy as np
from sklearn.externals import joblib

bad_array = np.load('../train/bad.all.npy')
good_array = np.load('../train/good.all.npy')

clf = joblib.load('../model.pkl') 


parser = argparse.ArgumentParser(description="Test file on this path")
parser.add_argument('filename', metavar='f', help="Path to file")

args = parser.parse_args()

print(args)

file = open(args.filename)
X_test = []
i = 0
j = 0
X_test.append([])
for line in file:
    #print line
    if line.strip().isdigit() and (j % 6) == 0:
        X_test[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 1:
        num1 = int(line)
        X_test[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 3:
        num1 = int(line)
        X_test[i].append(float(line))
    if line.strip().isdigit() and (j % 6) == 4:
        X_test[i].append(float(line))
        X_test[i].append(190)
        i += 1
        X_test.append([])
    j += 1
X_test.pop()
print(X_test)
X_t = np.asarray(X_test)
if (clf.predict(X_t.reshape(1, -1))):
    print("{\"answer\": \"fine code\"}")
else:
    print("{\"answer\": \"shitcode\"}")
