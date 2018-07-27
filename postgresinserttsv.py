#!/usr/bin/python

import psycopg2
import csv
class DataConn:
    def __init__(self):
        try:
	    self.conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='test'")
	    self.conn.autocommit = True
	    self.cursor = self.conn.cursor()
	except:
            print ("cant connect")
    def insert_remi_rec(self):
	with open('/home/manoj/Documents/postresql/remitee.tsv',)as fd:
	    rd = csv.reader(fd,delimiter="\t")
            header_data = next(rd)
            da_data = []
            heade_data=1+len(header_data)
	    head_data = ', '.join('{0}'.format(w) for w in header_data)
	    try:
                for row in rd:
		    da_data = [row[i] for i in range(1, heade_data - 1)]
		    da1_data = ', '.join('{0}'.format(w) for w in da_data)
		    self.cursor.execute("INSERT INTO rawdata.remittance values('"+ row[0] +"','{"+ head_data + "}','{" + da1_data + "}')")
	            del da_data[:]
	    except IndexError:
                print("Data Inserted Success fully but there is an index error")

    def insert_migr_rec(self):
	with open('/home/manoj/Documents/postresql/migration.tsv',)as fd:
	    rd = csv.reader(fd,delimiter="\t")
            header_data = next(rd)
            ca_data = []
            heade_len=1+len(header_data)
	    i = 2
	    head_data = ', '.join('{0}'.format(w) for w in header_data)
	    try:
                for row in rd:
  		    ca_data = [row[i] for i in range(1,heade_len - 1)]
		    ca1_data = ', '.join('{0}'.format(w) for w in ca_data)
		    self.cursor.execute("INSERT INTO rawdata.migration values('"+ row[0] +"','{"+ head_data + "}','{" + ca1_data + "}')")
	            del ca_data[:]
	    except IndexError:
		print("Data Inserted Success fully but there is an index error")

if __name__ == '__main__':
    dabaconn = DataConn()
    dabaconn.insert_remi_rec()
    dabaconn.insert_migr_rec()
