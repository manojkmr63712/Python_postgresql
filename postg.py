#!/usr/bin/python

import psycopg2
class DataConn:
    def __init__(self):
        try:
	    self.conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='test'")
	    self.conn.autocommit = True
	    self.cursor = self.conn.cursor()
	except:
            print ("cant connect")
    def insert_rec(self):
	new_record = ("3","slide1","blueberry","south","2014-03-29")
	insert_comm = "INSERT INTO playground values('"+new_record[0]+"','"+new_record[1] + "','" + new_record[2] + "','" +new_record[3] +"','"+new_record[4]+"')"
	print (insert_comm)
	self.cursor.execute(insert_comm)
if __name__ == '__main__':
    dabaconn = DataConn()
    dabaconn.insert_rec()
