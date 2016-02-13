#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from multiprocessing import Process

import random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))


authReqQuery = '\xC0\x00\x06\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE7\x48\xC2'
authConQuery = '\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2'

outQuery = "\x02\x03 >\x03\x00\x00\xf3\x88@\x83\xa6\xb9A\x94\xd2\xaaA\xe2.\xbc@\xd6\x00\x00\x00d\x00d\x00d\x00d\x00\x08\xe2\xc2"

count = '1'
morgIMEI = '351513054570863'
verPO = '1234567890123456'
verDE = '1234567890'
chType = '1'


"""

Поле 'Данные'
        Смещение    Длинна  Описание
05+01   0x00        0x01    Счетчик авторизаций
06+15   0x01        0x0F    IMEI модема
21+16   0x10        0x10    Версия ПО
37+10   0x20        0x0A    Версия железа
47+01   0x3E        0x01    0 - авторизация по служебному каналу, 1 - авторизация по основному каналу

s.append(ord(data[5]))
s.append(data[5 + 1:5 + 1 + 15])
s.append(data[5 + 16:5 + 16 + 16])
s.append(data[5 + 32:5 + 32 + 10])
s.append(ord(data[47]))
log.msg("handleIMEI:s:{}".format(s))
"""

int_server = '127.0.0.1'

def oneClient(imei):
    a = count+imei+verPO+verDE+chType
    authResQuery = '\xC0\x00\x07\x00\x3f{}\xE9\x85\xC2'.format(a)

    import socket
    sock = socket.socket()
    sock.connect((int_server, 14210))

    data = sock.recv(1024)
    print "get request",data
    sock.send(authResQuery)

    try:
        data = sock.recv(1024)
        print "get confirm",data

        for _ in xrange(100):
            data = sock.recv(1024)
            print "get query",data
            sock.send(outQuery)
    except:
        print "smth is wrong lets exit"
    finally:
        sock.close()



if __name__ == '__main__':
    try:
        clientCount = int(sys.argv[1])
    except:
        clientCount = 100

    rndImeiList = []
    for _ in xrange(clientCount):
        rndImeiList.append(randomword(15))
    imeiList = [morgIMEI, morgIMEI[::-1], 15*"1", 15*"2", 15*"3"]
    imeiList += rndImeiList

    pList = []
    for imei in imeiList:
        pList.append(Process(target=oneClient, args=(imei,)))

    for p in pList:
        p.start()

    for p in pList:
        p.join()
