#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

#ll = ['aktanish', 'morg', 'asvasdvasd']
#mc.set("name_busy_list",cPickle.dumps(ll))

data = mc.get("name_busy_list")
name_busy_list = cPickle.loads(data)

print "{} active connections:".format(len(name_busy_list))

if len(name_busy_list)>0:
    i = 1
    for l in name_busy_list:
        print "{}. {}".format(i, l)
        i += 1
