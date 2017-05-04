# -*- coding: utf-8 -*-
####here are works for initiation
#####
#####
sqlitedbname='accounts.db'
import sqlite3
from os.path import exists
import os
def setupsql():
    try:
        if not exists(sqlitedbname):
            fp = open(sqlitedbname,'w')
            fp.close()
        conn=sqlite3.connect(sqlitedbname)
        c=conn.cursor()
        sql="create table account(id int primary key,\
                                  private varchar (64),\
                                  public varchar(65),\
                                  address varchar(34),\
                                  wif varchar(60))"
        #actually, don't forget the real len is 64 33 34 towards these 3
        c.execute(sql)
        conn.commit()
        conn.close()
    except:
        print "table exists already!"


def delete_sql_table():
    try:
        conn = sqlite3.connect(sqlitedbname)
        c = conn.cursor()

        c.execute('drop table account')
        conn.commit()
        conn.close()
    except:
        print "no table exists!"
    #c.execute('drop table tableName')
#delete_sql_table()
setupsql()
#delete_sql_table()

