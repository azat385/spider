#!/usr/bin/python
# -*- coding: utf-8 -*-

db_name = 'test1.db'
import sqlite3
from datetime import datetime

conn = sqlite3.connect(db_name)
conn.text_factory = str

p = ['archive_morg.Давл_нагн', 'archive_morg.Темп_камеры', 'archive_morg.t_всас', 'archive_morg.Темп_охлад']

f = []
for p1 in p:
    c1 = conn.execute("SELECT  VALUE, STIME FROM RAWDATA WHERE NAME=? ORDER BY ID DESC LIMIT 100",(p1,))
    f.append(c1.fetchall())
conn.close()

data = []
for p1,f1 in zip(p,f):
    x1 = []
    y1 = []
    for f2 in f1:
        x1.append(f2[0])
        y1.append(datetime.strptime(f2[1],"%Y-%m-%d %H:%M:%S.%f"))
    #>>> lst=[[1,2,3],[11,12,13],[21,22,23]]
    #>>> zip(*lst)[0]
    #(1, 11, 21)

    trace = dict(name=p1.replace("archive_morg.", ""), y=x1, x=y1)
    data.append(trace)

from plotly.graph_objs import Scatter, Layout
from plotly.offline import plot

plot(data, filename='index.html', auto_open=False)



