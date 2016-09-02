#!/usr/bin/python
# -*- coding: utf-8 -*-

import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

mc.delete("common_data_imei")
mc.delete("common_data_name")

print mc.get("common_data_imei")
print mc.get("common_data_name")