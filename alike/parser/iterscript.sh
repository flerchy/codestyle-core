#!/bin/bash


IFS=$'\n\b'
files=`find ../repository/django-dynamic-fixture -name '*.py'` 
for f in $files
do 
 python parser.py $f ../stats/stats.out
done
