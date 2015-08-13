#!/usr/bin/env python
#-*- coding: utf-8 -*-
import string
import random
import csv
import timeit

start = timeit.default_timer()

cols = 10 
rows = 1000
size = 3
fileName = 'rand.csv'

fieldNames = ['rand'+str(i) for i in range(1, cols+1)]
fieldNames.insert(0, "id")

chars=string.ascii_uppercase + string.digits
with open(fileName, 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
	writer.writeheader()
	for i in range(0, rows):		
		row = {'id': i}
		for j in range(1, cols+1):
			row['rand'+str(j)] = ''.join(random.choice(chars) for _ in range(size))
		writer.writerow(row)	

print 'wrote', size, 'characters in', rows, 'rows\nin', cols, 'columns in',\
round(timeit.default_timer() - start, 5), 'seconds',