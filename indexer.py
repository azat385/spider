#!/usr/bin/python
# -*- coding: utf-8 -*-

#base_path = "html/"
#from plotHTML import base_path
base_path = "/data/spider_html/"
file_name = "index.html"
file_name_sans_ext = file_name.split(".")[0]

from datetime import date
time_str = date.today()
time_str = time_str.isoformat()

import glob2
all_header_files = glob2.glob('{}**/{}'.format(base_path, file_name))
print all_header_files

if not all_header_files:
    exit()
import os
import shutil
for f_old in all_header_files:
    if f_old == base_path + file_name:
	continue
    f_new = f_old.replace(file_name_sans_ext, time_str)
    if os.path.exists(f_new):
        os.remove(f_new)
    shutil.copyfile(f_old, f_new)
