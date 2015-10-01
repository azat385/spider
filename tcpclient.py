from twisted.internet import protocol, reactor
from twisted.protocols import basic
from sys import stdout
from random import randint

class wrx():
        auth = "\xC0\x00\x06\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE7\x48\xC2"
        authResponse = ""
	authConfirm = "\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2"
        first10words = "\x04\x03\x00\x00\x00\x0A\xC5\x98"
	first10wordsResponse = "\x04\x03\x00\x00\x00\x0A\xC5\x98"
        pass



class FingerProtocol(protocol.Protocol):
    i = 0
    def connectionMade(self):
	reactor.callLater(60, self.closeConnection)
	self.i = 0
	print "connection is made"
        #self.transport.write("%s\r\n"%(self.factory.user))
        #self.transport.loseConnection()

    def dataReceived(self,data):
	#stdout.write(data)
	print "incomming request to '{}' data='{}' i={}".format(
			self.factory.user, data, self.i)
	if self.i==0:
		self.transport.write(self.factory.user)
		print "send:{}".format(self.factory.user)
	if self.i==1:
		print "do nothing"
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
	print "outgoing response from '{}' data='{}' i={}".format(
				self.factory.user, message, self.i)

    def closeConnection(self):
	print "close connection: ", self.factory.user, self.i
	self.transport.loseConnection()
	#reactor.stop()

class FingerFactory(protocol.ClientFactory):
    protocol = FingerProtocol

    def __init__(self,user):
	self.user = user

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason


users = ['azat', 'ruslan', 'qwert']
for n in range(1000):
	users.append("client{}".format(n))
for u in users:
	reactor.connectTCP("127.0.0.1",1079, FingerFactory(u))
reactor.run()
