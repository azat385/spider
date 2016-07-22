#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        database = db


arc_prefix = "archive_"

import sqlite3
from datetime import datetime

base_path = "/home/ubuntu/spider/html/"
db_name = '/home/ubuntu/spider/test1.db'

conn = sqlite3.connect(db_name)
conn.text_factory = str


p = [
    {'key': 'Давл_нагн',    'name': 'Р нагнетания'},
    {'key': 'Темп_камеры',  'name': 'Т камеры'},
    {'key': 't_всас',       'name': 'Т всас фреон'},
    {'key': 'Темп_охлад',   'name': 'Т охладителя'},
    {'key': 't_комн_конд',  'name': 'Т комн конденс'},
]

f = [
    "Уставка_копия",
    "TE9_подача",
    "TE8_обратка",
    "TE1_нагн_1",
    "TE2_всас_1",
    "TE3_нагн_2",
    "TE4_всас_2",
    "TE5_конденсат",
    "PE11_нагн_1",
    "PE22_нагн_2",
    "Вент_3%",
    "Вент_6%",
    "Pвсас_1",
    "Pвсас_2",
]
std_pxl_arc = [
    {'key': "SCo_t_(наружная)",     'name': 'T наружняя'},
    {'key': "SCo_t_(канала)",       'name': 'T притока'},
    {'key': "SCo_t_(обр_воды)",     'name': 'T обр воды'},
    {'key': "SCo_t_(помещения)",    'name': 'T вытяжки'},
    {'key': "SCo_t_(вытяжки)",      'name': 'T выброса'},
    {'key': "SCo_Уставка_t",        'name': 'T уставка'},
    {'key': "SCo_%ВП",              'name': '%% ВП'},
    {'key': "SCo_%ВВ",              'name': '%% ВВ'},
]

add_aktanish_PP1_arc = [
    "FT1_ppm",
    "UT1_h",
    "UT1_t",
    "UT2_h",
    "UT2_t",
    "UT3_h",
    "UT3_t",
    "UT4_h",
    "UT4_t",
    "UT5_h",
    "UT5_t",
    "PE2_нагн",
    "РЕ3_всас",
    "UT1_H",
    "UT2_H",
    "UT3_H",
    "UT4_H",
    "UT5_H",
]
add_aktanish_PP1_arc = std_pxl_arc + add_aktanish_PP1_arc



def form_dict(name="morg.", prefix=arc_prefix, data_list=std_pxl_arc):
    dir_path = name.replace("_", "/")
    dir_path = dir_path.replace(".", "/")
    d = {"path": dir_path}
    data = []
    tag_prefix = "{}{}".format(prefix, name)
    d["tag_prefix"] = tag_prefix
    for l in data_list:
        data.append("{}{}".format(tag_prefix, l))
    d["data"] = data
    return d

settings = [
    form_dict(name="morg.", data_list=p),
    form_dict(name="chuykova."),
    form_dict(name="aktanish.PP1_", data_list=add_aktanish_PP1_arc),
    form_dict(name="aktanish.PP2_"),
    form_dict(name="aktanish.PP3_"),
    form_dict(name="aktanish.PP4_"),
    form_dict(name="fedos.", data_list=f),
    form_dict(name="test.PV1_"),
    form_dict(name="test.PV2_"),
]


def form_one_graph(common_name="morg.", prefix=arc_prefix, data_dict=std_pxl_arc):
    return


if __name__ == '__main__':
    exit()
    #previous
    for ss in settings:
        p = ss['data']
        f = []
        # SELECT "t1"."id", "t1"."NAME", "t1"."VALUE", "t1"."STIME"
        # FROM "rawdata" AS t1
        # WHERE (("t1"."NAME" LIKE ?) AND ("t1"."STIME" >= ?))
        # ORDER BY "t1"."NAME"
        # LIMIT 500 [u'archive_morg.%', u'2016-06-27 12:55:12.130000']
        for p1 in p:
            c1 = conn.execute("SELECT  VALUE, STIME FROM RAWDATA WHERE NAME=? AND (STIME>= datetime('now','-1 day')) ORDER BY ID DESC",(p1,))
            f.append(c1.fetchall())

        if not f:
            continue
        data = []
        for p1, f1 in zip(p, f):
            x1 = []
            y1 = []
            for f2 in f1:
                x1.append(f2[0])
                y1.append(datetime.strptime(f2[1],"%Y-%m-%d %H:%M:%S.%f"))
            #>>> lst=[[1,2,3],[11,12,13],[21,22,23]]
            #>>> zip(*lst)[0]
            #(1, 11, 21)
            cool_str_in_graph = p1.replace(ss['tag_prefix'], "")
            cool_str_in_graph = cool_str_in_graph.replace("SCo_", "")
            trace = dict(name=cool_str_in_graph, y=x1, x=y1)
            data.append(trace)

        from plotly.graph_objs import Scatter, Layout
        from plotly.offline import plot
        add_path = ss['path']
        full_path = "{}{}".format(base_path,add_path)
        import os
        if not os.path.isdir(full_path):
            os.makedirs(full_path)
        plot(data, filename='{}index.html'.format(full_path), auto_open=False, show_link=False)

    conn.close()




