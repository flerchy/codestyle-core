#!/bin/bash

IFS=$'\n\b'
files=`find ../ml_quality/datasets/fine -name '*.py'`
for f in $files
do 
 echo filename: `basename $f` >> codestyle_stats/fine_codestyle.out
 pycodestyle --max-line-length=81 --statistics -qq $f >> codestyle_stats/fine_codestyle.out
 echo >> codestyle_stats/fine_codestyle.out
done

files=`find ../ml_quality/datasets/shit -name '*.py'`
for f in $files
do 
 echo filename: `basename $f` >> codestyle_stats/shit_codestyle.out
 pycodestyle --max-line-length=81 --statistics -qq $f >> codestyle_stats/shit_codestyle.out
 echo >> codestyle_stats/shit_codestyle.out
done
