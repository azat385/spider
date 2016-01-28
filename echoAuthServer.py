"""The most basic chat protocol possible.

run me with twistd -y chatserver.py, and then connect with multiple
telnet clients to port 1025

sudo kill -TERM $(sudo cat chat.pid)
sudo twistd  --python=chatserver.py --pidfile=chat.pid --logfile=chatlog/chat.log

"""
port = 6567
delayBeforeDropConnection = 300


#from twisted.protocols import basic
from twisted.internet import protocol, reactor, error
from twisted.application import service, internet
from twisted.python import log

class auth():
    Request = "WhoAreYou?"
    Clients = [ "ImYourClient001\n", "ImYourClient001" ]
    Confirm = "OKletsSwitchToTrasparentMode"
    Failed  = "NOT_AUTH"
    pass

class MyChat(protocol.Protocol):
    stage = 0

    def connectionMade(self):
        log.msg( "Got new client: {}".format(self.transport.getPeer()) )
        self.factory.clients.append(self)
	self.timeout = reactor.callLater(delayBeforeDropConnection, self.dropConnection)
	self.stage = 1
	self.message(auth.Request)

    def connectionLost(self, reason):
        log.msg( "Lost a client! reason: {}".format(reason) )
        self.factory.clients.remove(self)

    def dataReceived(self, line):
        log.msg( "received {}".format( repr(line) ) )
	if self.stage == 1:
	    if line in auth.Clients:
		self.stage = 2
		self.message(auth.Confirm)
	    else:
		self.message(auth.Failed)
		#self.stage = 3
		self.dropConnection()
	else:
	    self.timeout.reset(delayBeforeDropConnection)
            for c in self.factory.clients:
            	#if c != self:
	    	# send to all active clients
	    	c.message(line)

    def message(self, message):
        self.transport.write(message)

    def dropConnection(self):
	log.msg( "Drop connection from server due to silence{}".format(self.transport.getPeer()) )
	self.transport.loseConnection()

factory = protocol.ServerFactory()
factory.protocol = MyChat
factory.clients = []

application = service.Application("echoServer", uid=0, gid=0, )
internet.TCPServer(port, factory).setServiceParent(application)
