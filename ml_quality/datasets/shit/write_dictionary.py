#!/usr/bin/python

import os,csv, json, cStringIO

package_root = os.path.abspath('../')
data_dir = os.path.join(package_root, 'pyweather/data/')
dictionary = {}

with open(os.path.join(data_dir, 'data.csv'), 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for rows in reader:
        dictionary[rows[1]] = rows[2]
	

with open(os.path.join(data_dir, 'city_dictionary.json'), 'w') as output:
    output.write(json.dumps(dictionary, ensure_ascii=False, encoding="utf-8"))
