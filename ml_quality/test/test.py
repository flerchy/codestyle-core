import argparse
import subprocess
import numpy as np
from sklearn.externals import joblib
import pythonparse 
import re
import json
bad_array = np.load('../train/bad.all.npy')
good_array = np.load('../train/good.all.npy')

clf = joblib.load('../model.pkl') 


parser = argparse.ArgumentParser(description="Test file on this path")
parser.add_argument('filename', metavar='f', help="Path to file")
parser.add_argument('cscheck', metavar='c', help="Set if you want to see codestyle checker output")

args = parser.parse_args()

print args.cscheck

if (args.cscheck == "1"):
    
    subprocess.check_call('touch cscheck.out', shell=True)
    cscheck = subprocess.check_output('pycodestyle ' + str(args.filename) + ' | cat > cscheck.out', shell=True)
    cs_file = open("cscheck.out")
    num_lines = []
    err = []
    for line in cs_file:
        num_lines.append(re.search(r'\d+', line).group())
        err.append(line.rsplit(':', 1)[-1][:-1])
    cs_res = open("cscheck.json", 'w+')
    res_dict = dict(zip(num_lines, err))
    cs_res.write(json.dumps(res_dict))
    cs_res.close()
    
pythonparse.run(args.filename)


subprocess.check_call('touch lint.out', shell=True)
subprocess.check_call('pycodestyle ' + str(args.filename) + ' | wc -l > lint.out', shell=True)
file = open("res.out")

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
#print X_test
X_t = np.asarray(X_test)
if (clf.predict(X_t.reshape(1, -1))):
    print "{\"answer\": \"fine code\"}"
else:
    print "{\"answer\": \"shitcode\"}"
