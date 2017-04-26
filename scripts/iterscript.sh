#!/usr/bin/bash

files = find ../sources/django -name '*.py' 
for f in $files
do 
 python pythonparse/parser.py $f
done
