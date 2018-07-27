#!/usr/bin/python

import psycopg2
class DataConn:
    def __init__(self):
        try:
            self.conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='test'")
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
	    self.cursor.execute("DROP TABLE rawdata.remittance")
            self.cursor.execute("DROP TABLE rawdata.migration")
        except:
            print ("cant connect")
if __name__ == '__main__':
    dabaconn = DataConn()
