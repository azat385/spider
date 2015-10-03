# Read username, output from non-empty factory, drop connections

from twisted.internet import protocol, reactor
from twisted.protocols import basic
from random import randint
from twisted.python import log

class wrx():
	auth = "\xC0\x00\x06\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE7\x48\xC2"
	authConfirm = "\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2"
	first10words = "\x04\x03\x00\x00\x00\x0A\xC5\x98"
	pass

class SpiderProtocol(protocol.Protocol):
    stage = 0
    i = 0
    IMEI = ""
    
    def ___init__(self):
	self.stage = 0
	self.i = 0
	self.IMEI = ""
    
    def connectionMade(self):
	#log.msg('connectionMade from peer %s'% (self.transport.getPeer()))
	print 'connectionMade from peer {}'.format(self.transport.getPeer())
	self.transport.write(wrx.auth)
	print 'send wrx.auth = {}'.format(wrx.auth)
	self.stage = 1
	#reactor.callLater(30, self.closeConnection)

    def dataReceived(self, line):
	#print line, self.stage
	if self.stage == 1:
		self.handleIMEIsimple(line)		
		self.transport.write(wrx.authConfirm)
		self.stage = 2
		self.planRequest(5)
	else:
		self.handleChat(line)

    def handleIMEIsimple(self, message):
	self.IMEI = message
        print 'get IMEI from wrxAuth {}'.format(self.IMEI)
	#return self.IMEI

    def handleIMEI(self, message):
	s = []
	try:
		dataArray = [ord(d) for d in message]
        	s.append(ord(data[5]))
                s.append(data[5+1:5+1+15])
                s.append(data[5+16:5+16+16])
                s.append(data[5+32:5+32+10])
                s.append(ord(data[67]))
	except:
		pass
		return
	self.IMEI = s[1]
	log.msg('get IMEI from wrxAuth {}'.format(self.IMEI))
	return self.IMEI
 
    def handleChat(self, message):
	self.i += 1
	if self.IMEI=='ruslan':
		delay = 0
	else:
		delay = 0
	self.planRequest(delay)
	log.msg('Inc=%s from IMEI %s'%(self.getInc100(message), self.IMEI))
	
    def getInc100(self, message):
	try:
		return ord(message[5])#in fact have to be 5-->18
	except:
		return "raise ERROR here"

    def planRequest(self, delayTime = 1):
	reactor.callLater(delayTime, self.sendRequest, wrx.first10words)

    def sendRequest(self, request):
	self.transport.write(request)

    def connectionLost(self, reason):
	#self.transport.write("Closing connection with IMEI = %s!\r\n"%(user))
	print('lost connection wth IMEI {}'.format(self.IMEI))
	self.transport.loseConnection()


class SpiderFactory(protocol.ServerFactory):
    protocol = SpiderProtocol

    def __init__(self, **kwargs):
        self.users = kwargs

    def getUser(self, user):
        return self.users.get(user, "No such user")

userDict = {'moshes':'Happy' , 'azat':'Very happy', 'ruslan':'2 cildren'}
reactor.listenTCP(1079, SpiderFactory(**userDict))
reactor.run()
