#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime

db_name = '/home/ubuntu/spider/test1.db'
conn = sqlite3.connect(db_name)
conn.text_factory = str

base_path = "/home/ubuntu/spider/html/"

p = [
    'Давл_нагн',
    'Темп_камеры',
    't_всас',
    'Темп_охлад',
    't_комн_конд'
]

std_pxl_arc = [
    "SCo_t_(наружная)",
    "SCo_t_(канала)",
    "SCo_t_(обр_воды)",
    "SCo_t_(помещения)",
    "SCo_t_(вытяжки)",
    "SCo_Уставка_t",
    "SCo_%ВП",
    "SCo_%ВВ",
]
arc_prefix = "archive_"


def form_dict(name="morg.", prefix=arc_prefix, data_list=std_pxl_arc):
    dir_path = name.replace("_", "/")
    dir_path = dir_path.replace(".", "/")
    d = {"path": dir_path}
    data = []
    tag_prefix = "{}{}".format(prefix, name)
    tag_prefix = tag_prefix.replace("SCo_", "")
    d["tag_prefix"] = tag_prefix
    for l in data_list:
        data.append("{}{}".format(tag_prefix, l))
    d["data"] = data
    return d

settings = [
    form_dict(name="morg.",data_list=p),
    form_dict(name="chuykova."),
    form_dict(name="aktanish.PP2_"),
    form_dict(name="aktanish.PP3_"),
    form_dict(name="aktanish.PP4_")
]

for ss in settings:
    p = ss['data']
    f = []
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

        trace = dict(name=p1.replace(ss['tag_prefix'], ""), y=x1, x=y1)
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






