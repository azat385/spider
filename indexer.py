#!/usr/bin/python
# -*- coding: utf-8 -*-

#base_path = "html/"
#from plotHTML import base_path
base_path = "/home/ubuntu/spider/html/"
file_name = "index.html"
file_name_sans_ext = file_name.split(".")[0]

from datetime import date
time_str = date.today()
time_str = time_str.isoformat()

import glob2
all_header_files = glob2.glob('{}**/*.html'.format(base_path))
print all_header_files

import shutil
for f_old in all_header_files:
    f_new = f_old.replace(file_name_sans_ext, time_str)
    shutil.copyfile(f_old, f_new)
