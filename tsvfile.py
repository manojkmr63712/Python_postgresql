#!/usr/bin/python
#import psycopg2
import csv
class DataConn:
    def __init__(self):
        with open('/home/manoj/Documents/postresql/remitee.tsv',)as fd:
	    rd = csv.reader(fd,delimiter="\t")
            header_data = next(rd)
            heade_data=1+len(header_data)
	    i = 1
	    #head_data = ', '.join('{0}'.format(w) for w in header_data)
	    try:
                for row in rd:
		    print(row[0])
		    while (i<heade_data):
			print(header_data[i],row[i])
		        i=i+1
            except IndexError:
                print("Data Inserted Success fully but there is an index error")

if __name__ == '__main__':
    dabaconn = DataConn()
