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
    from datetime import datetime, date, timedelta
    ts = str(datetime.now())
    db_name = 'test2.db'
    from peewee import *

    db = SqliteDatabase(db_name)

    class RAWDATA(Model):
        NAME = TextField()
        VALUE = FloatField()
        STIME = CharField(max_length=50)

        class Meta:
            database = db # This model uses the "people.db" database.

    #RAWDATA.create_table(fail_silently=True)

    #RAWDATA.create(NAME="tag01", VALUE=330.33, STIME=ts)
    #RAWDATA.create(NAME="tag02", VALUE=331.30, STIME=ts)
    #RAWDATA.create(NAME="tag03", VALUE=332.30, STIME=ts)

    key = "archive_sterlitamak.RT22_SCo_t_(обр_воды)"
    arr = (
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.7532024384, "2016-06-28 12:10:25.587980"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.7156429291, "2016-06-28 12:15:38.381105"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.7156429291, "2016-06-28 12:20:41.424295"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.7156429291, "2016-06-28 12:25:43.121070"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.6405220032, "2016-06-28 12:30:53.396369"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.6655635834, "2016-06-28 12:36:14.181619"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.5528831482, "2016-06-28 12:41:39.534234"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.4902820587, "2016-06-28 12:47:22.491720"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.5278434753, "2016-06-28 12:52:30.615641"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.5153217316, "2016-06-28 12:57:39.587488"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.5153217316, "2016-06-28 13:02:44.328145"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.4902820587, "2016-06-28 13:07:49.428175"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.5153217316, "2016-06-28 13:12:56.932940"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.4527225494, "2016-06-28 13:18:07.808674"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.4276828766, "2016-06-28 13:23:11.533018"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.6405220032, "2016-06-28 13:28:11.801325"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.6530437469, "2016-06-28 13:33:12.968851"),
             ("archive_sterlitamak.RT22_SCo_t_(обр_воды)", 20.6906032562, "2016-06-28 13:38:13.768756"),
    )

    #RAWDATA.insert_many().execute()

    r1 = RAWDATA\
        .select()\
        .where((RAWDATA.NAME ** "archive_morg.Темп%") & (RAWDATA.STIME >= datetime.now()-timedelta(hours=3)))\
        .order_by(RAWDATA.NAME)\
        .limit(500)

    print r1

    for r in r1:
        print r.id, r.NAME, r.VALUE, r.STIME
    #create_table()
    #write_data_to_db()
    exit()

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
                                write_data_to_db(key,arr)
                            break
        for i in xrange(180):
            if not i%10:
		print i
            sleep(1)


