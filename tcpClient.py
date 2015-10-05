from twisted.internet import protocol, reactor
from twisted.protocols import basic
#from twisted.python import log
#from twisted.logger import Logger
from sys import stdout
from random import randint
import gc
import argparse
from datetime import datetime

#log.startLogging(open('statistics.log', 'a'))


parser = argparse.ArgumentParser()
parser.add_argument("-t","--time", nargs="?",type=int, help="elapsed timein seconnds",default=20)
parser.add_argument("-c","--clients", nargs="?",type=int, help="default 3+num clients",default=100)
parser.add_argument("-l","--loops", nargs="?",type=int, help="",default=1)
parser.add_argument("-p","--port", nargs="?", type=int, help="port number",default=1079)
parser.add_argument("-s","--host", type=str, help="server host name",default="127.0.0.1")
args = parser.parse_args()
print "Starting {} clients in {} seconds connecting {}:{}".format(
                        args.clients+3, args.time, args.host, args.port)

#log.msg("Starting {} clients in {} seconds".format(args.clients+3, args.time))

class wrx():
        auth = "\xC0\x00\x06\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE7\x48\xC2"
        authResponse = ""
	authConfirm = "\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2"
        first10words = "\x04\x03\x00\x00\x00\x0A\xC5\x98"
	first10wordsResponse = "\x04\x03\x00\x00\x00\x0A\xC5\x98"
        pass

statistics = {}


class FingerProtocol(protocol.Protocol):
    i = 0
    global statistics

    def connectionMade(self):
	reactor.callLater(args.time, self.closeConnection)
	self.i = 0
	#print "connection is made"
        #self.transport.write("%s\r\n"%(self.factory.user))
        #self.transport.loseConnection()

    def dataReceived(self,data):
	#stdout.write(data)
	#print "incomming request to '{}' data='{}' i={}".format(
	#		self.factory.user, data, self.i)
	if self.i==0:
		self.transport.write(self.factory.user)
		#print "send:{}".format(self.factory.user)
	if self.i==1:
		#print "do nothing"
		pass
	if self.i>1:
		#self.transport.write("{}".format(wrx.first10wordsResponse))
		#print "send last10response"
		if self.factory.user=='ruslan':
			delayTime = 0
		else:
			delayTime = 0 #randint(1,5)
		self.sendDelayedResponse(wrx.first10wordsResponse, delayTime)
	self.i += 1

    def sendDelayedResponse(self, message, delay=1):
	reactor.callLater(delay,self.sendResponse,message) 

    def sendResponse(self, message):
	self.transport.write(message)
	#print "outgoing response from '{}' data='{}' i={}".format(
	#			self.factory.user, message, self.i)

    def closeConnection(self):
	#print "close connection: ", self.factory.user, self.i
	statistics.update({self.factory.user: self.i})
	self.transport.loseConnection()
	#reactor.stop()

class FingerFactory(protocol.ClientFactory):
    protocol = FingerProtocol

    def __init__(self,user):
	self.user = user

    def clientConnectionLost(self, connector, reason):
        #print 'Lost connection.  Reason:', reason
	pass

def stopWithStats():
        print "before stopping the reactor"

        results = {}
        for obj in gc.get_objects():
                if isinstance(obj, FingerProtocol):
                        results.update({obj.factory.user: obj.i})

        #rList = results.values()
        rList = statistics.values()
	rCount = {x:rList.count(x) for x in rList}
        #{17: 1, 4: 85, 5: 17)
        for rKey in sorted(rCount, reverse=1):
                print "RR cycles = {} same for {} clients".format(rKey,rCount[rKey])
	if 0 in rCount:
		zeroClient = rCount[0]
	else:
		zeroClient = 0
	print "*"*60,"\nstatistics\n","-"*60,"\n", "average={}req/sec time={}\n{} zero clients of total {}".format(
			sum(rList)/args.time, args.time, 
			zeroClient, sum(rCount.values()),
			),"\n","*"*60
        reactor.stop()
	#log.msg("Stopping reactor now...")
	print "stopping..."
	f = open('stat.txt', 'a')
	f.write("{}  average= {:6}req/sec time={:4}sec	{:5} zero clients of total {:<5}\n".format(
			datetime.now(),
                        int(sum(rList)/args.time), args.time,
                        zeroClient, sum(rCount.values()),
                        ))
	f.close()

def mainLoop():
	users = ['azat', 'ruslan', 'qwert']
	for n in range(args.clients):
		users.append("client{}".format(n))
	for u in users:
		reactor.connectTCP(args.host, args.port, FingerFactory(u))
	reactor.callLater(args.time+5, stopWithStats)
	reactor.run()
	print "the end loop"

#cant call reactor twice!
mainLoop()
