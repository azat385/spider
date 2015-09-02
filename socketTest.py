#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging.handlers import TimedRotatingFileHandler

logHandler = TimedRotatingFileHandler("logs/logfile", when="midnight") #when = "M")
logHandler.suffix = "%Y-%m-%d.html"
logFormatter = logging.Formatter('%(levelname)-10.10s %(asctime)s [%(funcName)-12.12s] [%(threadName)-15.15s] %(message)s </br>\r')
logHandler.setFormatter( logFormatter )
logger = logging.getLogger( 'MyLogger' )
logger.addHandler( logHandler )
logger.setLevel( logging.DEBUG ) # CHANGE to INFO after start up!!!
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
sock.bind(('', 14210))
sock.listen(1)
conn, addr = sock.accept()
print 'connected:', addr

def makeConnection():
	global sock, conn
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('', 14210))
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
	#print [hex(ord(d)) for d in data], ord(data[4])
	dataArray = [ord(d) for d in data]
	logger.debug("Recieved msg in dec = {}".format(dataArray))
	logger.info("Inc100 = {:03}".format( ord(data[18]) ))
	sleep(10)

#makeConnection()
while True:
    try:
	requestLoop()
    except socket.error:
	conn.close()
	sleep(15)
	makeConnection()
	#requestLoop()

conn.close()