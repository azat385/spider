#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import numpy as np
#from datetime import datetime

days = 2
DEBUG = False

if DEBUG:
    base_path = "/html/"
    db_name = 'test1.db.20170130'
else:
    base_path = "/data/spider_html/"
    db_name = '/home/ubuntu/spider/test1.db'

conn = sqlite3.connect(db_name)
conn.text_factory = str


p = [
    'Давл_нагн',
    'Темп_камеры',
    't_всас',
    'Темп_охлад',
    't_комн_конд'
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
    "SCo_t_(наружная)",
    "SCo_t_(канала)",
    "SCo_t_(обр_воды)",
    "SCo_t_(помещения)",
    "SCo_t_(вытяжки)",
    "SCo_Уставка_t",
    "SCo_%ВП",
    "SCo_%ВВ",
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

almet_list = [
    "T_глик_с_поля",
    "T_глик_на_поле",
    "Tемпература_поля",
    "Давление_всасывания",
    "Давление_нагнетания",
    "Tемпература_всас_компрес_1",
    "Tемпература_нагн_комп_1",
    "Т_улица",
    "Т_масла",
    "Вентиляторы_итого",
    "Компрессоры_итого",
    "Компрессор1",
    "Компрессор2",
    "Компрессор3",
    "MinTуст",
    "MaxTуст",
    "MinTдатч",
    "MaxTдатч",
    "MinРнагн",
    "MaxРнагн",
    "MinРвсас",
    "MaxРвсас",
    "MinТнагн",
    "MaxTнагн",
    "EKD_u20_S2_Temp",
    "EKD_u21_Superheat",
    "EKD_u22_SuperheatRef",
    "EKD_u24_Opening_OD",
    "EKD_u25_EvapPres_Pe",
    "EKD_u26_EvapTemp_Te",
    "ВентОбщ",
    "СтупеньРегул",
    "ТемпВагон",
    "ТемпШкаф",

]
arc_prefix = "archive_"


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
   #form_dict(name="fedos.", data_list=f),
   #form_dict(name="test.PV1_"),
   #form_dict(name="test.PV2_"),
   form_dict(name="mavl.PV11_"),
   form_dict(name="almet.", data_list=almet_list),
   form_dict(name="mavl.PV11_"),
]

p_all = []
for ss in settings:
    p_all += ss['data']

f = []
print p_all
f = conn.execute("""SELECT  NAME, VALUE, STIME
    FROM RAWDATA
    WHERE NAME in ({}) AND (STIME>= datetime('now','-{} day'))
    ORDER BY NAME DESC""".format(",".join(["?"]*len(p_all)),days),(p_all))
rows = f.fetchall()
np_rows = np.array(rows)
conn.close()

for ss in settings:
    p = ss['data']
    data = []
    for p1 in p:
        # get only needed p1 from np_rows
        f1 = np_rows[np_rows[:, 0] == p1][:, 1:]
        x1 = f1[:,0]
        y1 = f1[:,1]
        #for f2 in f1:
            #x1.append(f2[0])
            #y1.append(datetime.strptime(f2[1],"%Y-%m-%d %H:%M:%S.%f"))
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


if __name__ == '__main__':
    pass




