from twisted.internet import protocol, reactor
from twisted.protocols import basic
from sys import stdout
from random import randint
import gc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t","--time", nargs="?",type=int, help="elapsed timein seconnds",default=20)
parser.add_argument("-c","--clients", nargs="?",type=int, help="default 3+num clients",default=100)
args = parser.parse_args()
print "Starting {} clients in {} seconds".format(args.clients+3, args.time)

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
			delayTime = randint(1,5)
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
        reactor.stop()
	print "stopping..."	

users = ['azat', 'ruslan', 'qwert']
for n in range(args.clients):
	users.append("client{}".format(n))
for u in users:
	reactor.connectTCP("127.0.0.1",1079, FingerFactory(u))
reactor.callLater(args.time+5, stopWithStats)
reactor.run()

print "the end"
