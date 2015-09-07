#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)==1:
    logger.error("Usage {} portNum".format(sys.argv[0]))
    sys.exit("No port")
try:
    port = int(sys.argv[1])
#if not isinstance(port, int):
except:
    logger.error("{} is not a number".format(sys.argv[1]))
    sys.exit("Not a number")


import logging
from logging.handlers import TimedRotatingFileHandler

logHandler = TimedRotatingFileHandler("logs/logfile", when="midnight") #when = "M")
logHandler.suffix = "%Y-%m-%d.html"
logFormatter = logging.Formatter('%(levelname)-10.10s %(asctime)s [%(funcName)-12.12s] [%(threadName)-15.15s] [port:{:>6}] %(message)s </br>\r'.format(port))
logHandler.setFormatter( logFormatter )
logger = logging.getLogger( 'MyLogger' )
logger.addHandler( logHandler )
logger.setLevel( logging.INFO ) # CHANGE to INFO after start up!!!
#for console logging
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler( consoleHandler )

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

logger.info('PROGRAMM IS STARTING...\n\n')


import socket
from time import sleep as sleep

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', port))
sock.listen(1)
logger.info("waiting for connection on {} port...".format(port))
conn, addr = sock.accept()
print 'connected:', addr

def wrxAuth():
	global conn,data
	s = []
	conn.send("\xC0\x00\x06\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE7\x48\xC2")
	#print "Wait for reply..."
	data = conn.recv(1024)
	#print "Reply:",data
	dataArray = [ord(d) for d in data]
	#print dataArray
	sleep(3)
	#print "Send Auth confirmation..."
	conn.send("\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2")
	s.append(ord(data[5]))
	s.append(data[5+1:5+1+15])
	s.append(data[5+16:5+16+16])
	s.append(data[5+32:5+32+10])
	s.append(ord(data[67]))
	logger.warn("WRX Auth {}".format(s))
	return s
	#sleep(3)
	
	


def makeConnection():
	global sock, conn
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('', port))
	sock.listen(1)
	conn, addr = sock.accept()
	#print 'connected:', addr
	logger.warn("Client connected {}".format(addr))


def requestLoop():
    global sock, conn
    while True:
	#conn.send("\x04\x03\x00\x07\x00\x01\x35\x9E")
	conn.send("\x04\x03\x00\x00\x00\x0A\xC5\x98")
	data = conn.recv(1024)
	#print [hex(ord(d)) for d in data], ord(data[18])
	dataArray = [ord(d) for d in data]
	logger.debug("Recieved msg in dec = {}".format(dataArray))
	try:
		inc100 = ord(data[18])
		logger.info("Inc100 = {:03}".format(inc100))
	except:
		logger.error("Some error in recieved query in dec = {}".format(dataArray))
	sleep(10)

#makeConnection()
wrxAuth()
while True:
    try:
	requestLoop()
    except socket.error:
	conn.close()
	sleep(15)
	makeConnection()
	wrxAuth()

conn.close()
