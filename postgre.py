#!/usr/bin/python

import psycopg2
try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='test'")
except:
    print ("cant connect")
cur = conn.cursor()
try:
    cur.execute("INSERT INTO playground values('slide','blue','south','2014-04-28')")
except:
    print ("cant print")
#rows = cur.fetchall()
#print("\nRows: \n")
#for row in rows:
#    print(row[0],row[1],row[2],row[3],row[4])
