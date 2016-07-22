#!/usr/bin/python
# -*- coding: utf-8 -*-
from mcStat import getKeys
mcKeyLimit = 1000

import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
#mc.flush_all()

def get_data_array(val):
    try:
        valT = val.split(";;;")
        arr = []
        for val in valT:
            arr.append(val.split(";"))
        return arr
    except:
        return None

def write_data_to_db(_key,arr):
    #import sqlite3
    conn = sqlite3.connect(db_name)
    #print "Opened database successfully";
    if check_table_exist():
        pass
    else:
        create_table()
    key = _key.decode('utf8')
    for a in arr:
        if len(a)<2:
            continue
        #print "data to add {} {} {}".format(key, a[0], a[1])
        conn.execute("INSERT INTO RAWDATA (NAME,VALUE,STIME)\
                VALUES (?, ?, ?)", (key, a[0], a[1]))
    conn.commit()
    print "Records for {} key created successfully".format(_key)
    conn.close()




def create_table():
    #import sqlite3
    conn = sqlite3.connect(db_name)
    conn.execute('''CREATE TABLE RAWDATA(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   NAME           TEXT      NOT NULL,
   VALUE          REAL      NOT NULL,
   STIME          CHAR(50));''')
    conn.close()
    print "create db {}".format(db_name)

def check_table_exist():
    #import sqlite3
    conn = sqlite3.connect(db_name)
    c1 = conn.execute("SELECT * FROM sqlite_master WHERE name ='RAWDATA' and type='table';")
    f1 = c1.fetchall()
    if f1:
        return True
    else:
        return False

if __name__ == '__main__':
    #create_table()
    #write_data_to_db()
    #exit()
    db_name = 'test1.db'
    import sqlite3
    #conn = sqlite3.connect(db_name)
    from time import sleep

    while 1:
        top100keys = getKeys(limit=mcKeyLimit)
        for key in top100keys:
            if "archive" in key:
                for _ in xrange(5):
                    #try:
                        val = mc.get(key)
                        if mc.cas(key, ''):
                            arr = get_data_array(val)
                            if arr is not None:
                                try:
                                    write_data_to_db(key,arr)
                                except:
                                    print "smthing wrong with db!"
        for i in xrange(180):
            if not i%10:
                print i
            sleep(1)
