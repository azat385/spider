# Read username, output from non-empty factory, drop connections

from twisted.application import internet, service
from twisted.internet import protocol, reactor
from twisted.protocols import basic
from random import randint
from twisted.python import log
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile
#log.startLogging(DailyLogFile.fromFullPath("/home/ubuntu/spider/logs/logfile.log"))


"""import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", nargs="?", type=int, help="port number",default=1079)
parser.add_argument("-s","--host", type=str, help="server host name",default="127.0.0.1")
parser.add_argument("-d","--delay", nargs="?",type=int, help="delay between request and reaponse (set 0) or min(set 2..100)",default=0)
args = parser.parse_args()
if args.delay == 1:
        args.delay = 2
log.msg( "Starting server on {} port with delay {}+/-2 sec".format(
	args.port, args.delay)
"""
class args():
	delay=2
	port=14210


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
	log.msg('connectionMade from peer {}'.format(self.transport.getPeer()))
	self.transport.write(wrx.auth)
	log.msg('send wrx.auth = {}'.format(wrx.auth))
	self.stage = 1
	#reactor.callLater(30, self.closeConnection)

    def dataReceived(self, line):
	#log.msg( line, self.stage
	if self.stage == 1:
		log.msg( "dataReceived:line:{}".format(line) )
		self.handleIMEI(line)		
		#self.transport.write(wrx.authConfirm)
		self.stage = 2
		self.planRequest(4, wrx.authConfirm)
		self.planRequest(8, wrx.first10words)
	else:
		log.msg( "self.handleChat:line:{}".format(line))
		self.handleChat(line)

    def handleIMEIsimple(self, message):
	self.IMEI = message
        log.msg( 'get IMEI from wrxAuth {}'.format(self.IMEI) )
	#return self.IMEI

    def handleIMEI(self, data):
	s = []
	try:
		dataArray = [ord(d) for d in data]
        	s.append(ord(data[5]))
                s.append(data[5+1:5+1+15])
                s.append(data[5+16:5+16+16])
                s.append(data[5+32:5+32+10])
                s.append(ord(data[67]))
		log.msg( "handleIMEI:s:{}".format(s) )
	except:
		log.msg( "some error in wrx auth response decoding" )
		return
	self.IMEI = s[1]
	log.msg( 'get IMEI from wrxAuth {}'.format(self.IMEI) )
	return self.IMEI
 
    def handleChat(self, message):
	self.i += 1
        if args.delay==0:
		delayTime = 0
        else:
                delayTime = randint(args.delay-2,args.delay+2)
	log.msg( 'Inc={} from IMEI {}'.format(self.getInc100(message), self.IMEI) )
	self.planRequest(delayTime, wrx.first10words)
	
    def getInc100(self, message):
	try:
		return ord(message[18])#in fact have to be 5-->18
	except:
		return "raise ERROR here"

    def planRequest(self, delayTime = 1, message = wrx.first10words):
	log.msg( "Plan request={} after {} sec IMEI={}".format(message, delayTime, self.IMEI) )
	reactor.callLater(delayTime, self.sendRequest, message)

    def sendRequest(self, request):
	log.msg( "Send request={} IMEI={}".format(request, self.IMEI) )
	self.transport.write(request)

    def connectionLost(self, reason):
	#self.transport.write("Closing connection with IMEI = %s!\r\n"%(user))
	log.msg( 'lost connection wth IMEI {}'.format(self.IMEI) )
	self.transport.loseConnection()


class SpiderFactory(protocol.ServerFactory):
    protocol = SpiderProtocol

    #def __init__(self, service):
    #	self.service = service
    def __init__(self, **kwargs):
        self.users = kwargs

    def getUser(self, user):
        return self.users.get(user, "No such user")


userDict = {'moshes':'Happy' , 'azat':'Very happy', 'ruslan':'2 cildren'}

application = service.Application('spider', uid=1, gid=1)
logfile = DailyLogFile("my.log", "/home/ubuntu/spider/logs/")
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)
factory = SpiderFactory(**userDict)
internet.TCPServer(args.port, factory).setServiceParent(
    service.IServiceCollection(application))

""" for future

class SpiderService(service.Service):
    def __init__(self):
	pass
        #self.poetry_file = poetry_file

    def startService(self):
        service.Service.startService(self)
	log.msg( "Starting service"
        #self.poem = open(self.poetry_file).read()
        #log.msg('loaded a poem from: %s' % (self.poetry_file,))



# configuration parameters
port = 14210
iface = 'localhost'
poetry_file = 'poetry/ecstasy.txt'


topService = service.MultiService()

spider_service = SpiderService()
spider_service.setServiceParent(topService)

factory = SpiderFactory(spider_service)
tcpService = internet.TCPServer(port, factory, interface=iface)
tcpService.setServiceParent(topService)


application = service.Application("spider")

topService.setServiceParent(application)
"""
