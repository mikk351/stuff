#!/usr/bin/env python
#-*- coding: utf-8 -*-
import string, random, csv, timeit
start = timeit.default_timer()

cols, rows, size = 10, 1000, 3
fileName = 'rand.csv'
fieldNames = ['rand'+str(i) for i in range(1, cols+1)]
fieldNames.insert(0, "id")

with open(fileName, 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
	writer.writeheader()
	for i in range(0, rows):		
		row = {'id': i}
		for j in range(1, cols+1):
			row['rand'+str(j)] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
		writer.writerow(row)

print 'wrote', rows, 'x', cols, 'csv in', round(timeit.default_timer() - start, 5), 'sec'