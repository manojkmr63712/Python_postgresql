#!/usr/bin/python

import psycopg2
import csv
class Sample_Data_Conn:
    def __init__(self):
        try:
	    self.conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='test'")   # connection string to connect postgresql
	    self.conn.autocommit = True		# to enable connection
	    self.cursor = self.conn.cursor()	# allow to execute the commands
	except:
            print ("cant connect")		# print error in connection

    def insert_remi_rec(self):
	with open('/home/manoj/Documents/postresql/remitee.tsv',)as raw_data:		# input path to the file
    	    file_data = csv.reader(raw_data,delimiter="\t")				# reading as csv and set delimiter by default its csv
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
			if(col == 'N/A') or (col == '0*'):	# some rows contains non of integer value to omit this loop helps
			    col = 0
			    self.cursor.execute("INSERT INTO rawdata.remittance values('"+ heade +"','"+ header[colnum] +"','"+ col +"')")		# insert the data into table already created with schema
			else:
			    self.cursor.execute("INSERT INTO rawdata.remittance values('"+ heade +"','"+ header[colnum] +"','"+ col +"')")
		    colnum +=1
		n+=1
	    #self.cursor.execute("DELETE FROM rawdata.remittance where country = ''")	# delete the row with empty value
    	    raw_data.close()

    def insert_migr_rec(self):
        with open('/home/manoj/Documents/postresql/migration.tsv',)as raw_data:           # input path to the file
            file_data = csv.reader(raw_data,delimiter="\t")				# reading as csv and set delimiter by default its csv
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
			self.cursor.execute("INSERT INTO rawdata.migration values('"+ heade +"','"+ header[colnum] +"','"+ col +"')")		# insert the data into table already created with schema
                    colnum +=1
                n+=1
	    #self.cursor.execute("DELETE FROM rawdata.migration where country = ''")	# delete the row with empty value
            raw_data.close()

if __name__ == '__main__':
    dabaconn = Sample_Data_Conn()	# creating object to the class
    dabaconn.insert_remi_rec()		# calling the method over object
    dabaconn.insert_migr_rec()		# calling the method over object
