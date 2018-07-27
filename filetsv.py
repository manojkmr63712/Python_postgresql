#!/usr/bin/python

import csv
with open('/home/manoj/Documents/postresql/remiteesample.tsv',)as fd:
    rd = csv.reader(fd,delimiter="\t")
    n=0
    colnum=0
    heade = ''
    for row in rd:
	if n == 0:
	    header = row
	else:
	    colnum = 0
	for col in row:
	    if colnum == 0:
		heade=col
		#print(heade)
	    else:
		print(heade,header[colnum],col)
	    print(colnum)
	    print(n)
	    colnum +=1
	n+=1
    fd.close()
