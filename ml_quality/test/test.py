import lasagne
import numpy as np
import theano.tensor as T
import theano
import parser
import argparse
import subprocess
import numpy as np
from sklearn.externals import joblib
import re
import json

def build_network(input_var=None):
    l_in = lasagne.layers.InputLayer(shape=(None, 82),
                                     input_var=input_var)
    l_hid = lasagne.layers.DenseLayer(l_in, num_units=82, 
                                       nonlinearity=lasagne.nonlinearities.rectify,
                                       W=lasagne.init.GlorotUniform())
    l_hid2 = lasagne.layers.DenseLayer(l_hid, num_units=41, 
                                       nonlinearity=lasagne.nonlinearities.rectify,
                                       W=lasagne.init.GlorotUniform())
    l_hid3 = lasagne.layers.DenseLayer(l_hid2, num_units=20, 
                                       nonlinearity=lasagne.nonlinearities.softmax,
                                       W=lasagne.init.GlorotUniform())
    l_out = lasagne.layers.DenseLayer(l_hid3, num_units=2, 
                                      nonlinearity=lasagne.nonlinearities.softmax)
    return l_out



def iterate_minibatches_2(inputs, batchsize):
    for start_idx in range(0, len(inputs) - batchsize + 1, batchsize):
        excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt]
        


ps = argparse.ArgumentParser(description="Test file on this path")
ps.add_argument('filename', metavar='f', help="Path to file")
ps.add_argument('cscheck', metavar='c', help="Set if you want to see codestyle checker output")

args = ps.parse_args()

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
    
parser.run(args.filename)




X_test = []
X_test.append([])
subprocess.check_call("touch test_codestyle.out", shell=True)
print str(args.filename)
subprocess.check_call("echo filename: " + str(args.filename) + "| cat > test_codestyle.out", shell=True)
subprocess.check_call("pycodestyle --max-line-length=81 --statistics -qq " + str(args.filename) + "| cat >> test_codestyle.out", shell=True)



f = open("test_codestyle.out", "r")
res = open("test_codestyle.json", "w+")
begin_coord = 0
lines_count = []
file_info = []

i = 0 
for line in f:
    errors = {"E101": 0, "E191": 0,"E122": 0,"E305": 0,"E302": 0,"E111": 0, "E112": 0,
            "E113": 0,"E114": 0,"E116": 0,"E115": 0,"E121": 0,"E123": 0,"E124": 0, 
            "E129": 0,"E126": 0,"E127": 0,"E128": 0,"E131": 0,"W291": 0,"E125": 0,
            "W503": 0,"E701": 0,"E203": 0,"E201": 0,"E202": 0,"E702": 0,"E211": 0,
            "E221": 0,"E222": 0,"E223": 0,"E224": 0,"E225": 0,"E226": 0,"E227": 0,
            "E228": 0,"E231": 0,"E241": 0,"E242": 0,"E251": 0,"E272": 0,"E261": 0,
            "E262": 0, "E265": 0, "E266": 0, "E271": 0, "E273": 0, "E274": 0, "E743": 0, 
            "E741": 0, "E402": 0, "E275": 0, "E301": 0, "E303": 0, "E304": 0, "E306": 0, "E401": 0,
             "E501": 0, "E502": 0, "E703": 0, "E704": 0, "E711": 0, "E712": 0, "E713": 0, "E714": 0, "E721": 0,
            "E722": 0, "E731": 0, "E901": 0,"W293": 0,"W601": 0,"W602":0,"W603":0,"W604":0, "W191":0, "W292":0, "W391":0} 
    if (line[0] == "f"):
        info = {}
        filename = line[10:-1]
        info["filename"] = filename
        i += 1
        continue
    if (line[0]) == "\n":
        file_info.append(info)
        i += 1
        continue
    amount = line.split("   ")
#   print "123"
    print amount[0]
    errno = amount[-1].lstrip()[:4]
    info["errors"] = errors
    if (errno not in errors):
        print errno
    errors[errno] += int(amount[0])
    i += 1
else:
    file_info.append(info)
mid = 0
print len(file_info)
res.write(json.dumps(file_info, indent=4))
print "OK\n"
f.close()
res.close()

with open("test_codestyle.json", "r") as cs_bad_stats:
    cs_bad_data = cs_bad_stats.read().replace('\n', ' ')
    parsed_cs_bad = json.loads(cs_bad_data)
    print parsed_cs_bad[:10]
with open("test_custom.json", "r") as custom_bad_stats:
    custom_bad_data = custom_bad_stats.read().replace('\n', ' ')
    parsed_custom_bad = json.loads(custom_bad_data)
    print parsed_custom_bad[:10]
res = open("test_res.json", "w+")
merged_bad = []
for i in range(0, len(parsed_custom_bad)):
    if (parsed_custom_bad[i]["filename"] == parsed_cs_bad[i]["filename"]):
        print parsed_custom_bad[i]["filename"]
        if "errors" in parsed_cs_bad[i]:
            parsed_custom_bad[i]["errors"] = parsed_cs_bad[i]["errors"]
res.write(json.dumps(parsed_custom_bad, indent=4))
res.close()
f.close()

testf = open("test_res.json", "r")

test_data = testf.read().replace('\n', ' ')
test_dict = json.loads(test_data)
X_test = []
for i in range(0, len(test_dict)):
    s = []
    if ('errors' in test_dict[i]):
        #print bad_dict[i]['errors']
        s.extend(test_dict[i]['errors'].values())
        #print s
    else:
        s.extend([0]*(len(test_dict[0]['errors'])))
    #print s
    #print s
    for key, value in test_dict[i].items():
         if key not in ('errors', 'filename'):
            s.append(int(value))
    print s
    s = np.array(s) 
    X_test.append(s)

X_test = np.array(X_test)



input_var = T.matrix('inputs')
target_var = T.ivector('targets')

network = build_network(input_var)

print X_test.shape
        
# use trained network for predictions
test_prediction = lasagne.layers.get_output(network, deterministic=True)
predict_fn = theano.function([input_var], T.argmax(test_prediction, axis=1))

sum = 0
for batch in iterate_minibatches_2(inputs=X_test,batchsize=1):
        inputs = batch
        result=predict_fn(inputs)
        if (result[0] == 1):
            print '{"answer": "fine code"}'
        else:
            print '{"answer": "shitcode"}'
