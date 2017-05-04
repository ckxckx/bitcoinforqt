# -*- coding: utf-8 -*-

import sqlite3



def insert_one_ckx(param):


    conn=sqlite3.connect("accounts.db")
   # print param
    c=conn.cursor()
    sql_insert="insert into {tablename}(id, private, public, address, wif) values {ourvalue}".format(tablename="account",ourvalue=param)
    try:
        c.execute(sql_insert)
    except:
        'sql_insert is not correct!!'
    #print sql_insert

    conn.commit()
    conn.close()



def add_account_table():
    conn=sqlite3.connect("test.db")
    c=conn.cursor()
    sql="create table account(id int primary key,\
                              privatekey varchar (64),\
                              publickey varchar(65),\
                              addresss varchar(34))"
    #actually, don't forget the real len is 64 33 34 towards these 3
    c.execute(sql)
    conn.commit()

    conn.close()







#########
#########This is examples of sqlite use!#########
#########
def add_table_test():
    # test.db is a file in the working directory
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    # create tables
    sql = '''create table student (id int primary key, name varchar(20), score int, sex varchar(10), age int)'''
    c.execute(sql)
        # save the changes
    conn.commit()
    conn.close()



def add_data_test():

    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    students = [(2, 'mark', 80, 'male', 18),
                (3, 'tom', 78, 'male', 17),
                (4, 'lucy', 98, 'female', 18),
                (5, 'jimi', 60, 'male', 16)]

    # 第一种：execute "INSERT"
    c.execute("insert into student(id, name, score, sex, age) values (1,'jack',80,'male',18)")

    # 第二种：execute multiple commands
    c.executemany('insert into student values (?,?,?,?,?)', students)

    # 第三种：using the placeholder
    c.execute("insert into student values (?,?,?,?,?)", (6, 'kim', 69, 'male', 16))

    conn.commit()
    conn.close()




def query_data_test():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    # 第一种：retrieve one record
    c.execute('select * from student order by score desc')
    print(c.fetchone())  #第1条记录
    print(c.fetchone())  #第2条记录

    # 第二种：retrieve all records as a list
    c.execute('select * from student order by score desc')
    print(c.fetchall())

    # 第三种：terate through the records
    rs = c.execute('select * from student order by score desc')
    for row in rs:
        print(row)
    conn.commit()
    conn.close()



def update_data_test():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    sql = "update student set name='jerry' where id = 2"
    c.execute(sql)

    conn.commit()
    conn.close()


def delete_data_test():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    c.execute('delete from student where id=2')

    conn.commit()
    conn.close()

    #c.execute('drop table tableName')




############examples ends##############
##################################
################################