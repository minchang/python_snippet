# -*- coding=utf8 -*-
import socket
import MySQLdb as db

timeout = 10
socket.setdefaulttimeout( timeout )

DB_HOST = 'xx.mydb.com'
DB_PORT = 3306
DB_USER = 'username'
DB_PASSWORD = 'password'
DB_NAME  = 'mydb'

def testDbConnectError():
        con = db.connect( host=DB_HOST, port =DB_PORT, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME );

        try:
                cur = con.cursor()
                cur.execute( "SELECT a FROM table");
                jobid = cur.fetchone()[0]

        except db.Error, e:
                print e;
        finally:
                if con:
                        con.close()


if __name__ == '__main__':

        try:
                testDbConnectError();

        except db.Error, e:
                print "catch error!"
                print e

