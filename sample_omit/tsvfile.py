#!/usr/bin/python

import csv
class DataConn:
    def __init__(self):
        with open('/home/manoj/Documents/postresql/sample_omit/data.tsv',)as raw_data:           # input path to the file
            file_data = csv.reader(raw_data,delimiter="\t")			# reading as csv and set delimiter by default its csv
            n=0
            colnum=0
            heade = ''
            for row in file_data:	# convert the raw data in to rows
                if n == 0:		# split the header row
                    header = row
                else:
                    colnum = 0
                for col in row:		# split the rows into column
                    if colnum == 0:
                        heade=col	# assining the column value to the variable
                    else:
			if (col == 'N/A') or (col == '0*'):
			    col = 0
		 	    print(heade,header[colnum],col)		# insert the data into table already created with schema
#			else:
#			    print(heade,header[colnum],col)
                    colnum +=1
                n+=1
            raw_data.close()
if __name__ == '__main__':
    dabaconn = DataConn()
