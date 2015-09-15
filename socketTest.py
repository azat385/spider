#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv)==1:
    logger.error("Usage: {} portNum 0/1(wrxAuth)".format(sys.argv[0]))
    sys.exit("No port")
try:
    port = int(sys.argv[1])
#if not isinstance(port, int):
except:
    logger.error("{} is not a number".format(sys.argv[1]))
    sys.exit("Not a number")
try:
    doWrxAuth = int(sys.argv[2])
except:
    print "by default wrxAuh is OFF"
    doWrxAuth = 0
print "doWrxAuth={}".format(doWrxAuth )

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
	try:
		data = conn.recv(1024)
	except socket.error as err:
		logger.error("Error: Socket error: {}".format(err))
		return s		
	#print "Reply:",data
	try:
		dataArray = [ord(d) for d in data]
		s.append(ord(data[5]))
		s.append(data[5+1:5+1+15])
		s.append(data[5+16:5+16+16])
		s.append(data[5+32:5+32+10])
		s.append(ord(data[67]))
	except:
		logger.error("Error: in response calcualations")
		return s
	#print dataArray
	sleep(3)
	#print "Send Auth confirmation..."
	conn.send("\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2")
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
    i=0
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
	if i==2:
		raise ValueError("Raise exception to close the connection")
	i += 1
	sleep(10)

def printFloat(byteArray,startByte):
	return struct.unpack(">f",data[startByte:startByte+4][2:4]+data[startByte:startByte+4][0:2])[0]
#data range(5,100,4)===1...24 floats

def printWord(byteArray,startByte):
	return struct.unpack(">h",data[startByte:startByte+2])[0]
#range(101,120,2)===25...34 shorts

#makeConnection()
if doWrxAuth:
	wrxAuth()
while True:
    try:
	requestLoop()
    except (socket.error,ValueError) as err:
        print err
	conn.close()
	sleep(15)
	makeConnection()
	if doWrxAuth:
		wrxAuth()

conn.close()
