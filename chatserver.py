"""The most basic chat protocol possible.

run me with twistd -y chatserver.py, and then connect with multiple
telnet clients to port 1025
"""
port = 6565
delayBeforeDropConnection = 120


#from twisted.protocols import basic
from twisted.internet import protocol, reactor
from twisted.application import service, internet



class MyChat(protocol.Protocol):
    def connectionMade(self):
        print "Got new client: {}".format(self.transport.getPeer())
        self.factory.clients.append(self)
	self.timeout = reactor.callLater(delayBeforeDropConnection, self.dropConnection)

    def connectionLost(self, reason):
        print "Lost a client! reason: {}".format(reason)
        self.factory.clients.remove(self)

    def dataReceived(self, line):
        print "received", repr(line)
	self.timeout.reset(delayBeforeDropConnection)
        for c in self.factory.clients:
            if c != self:
		c.message(line)

    def message(self, message):
        self.transport.write(message)

    def dropConnection(self):
	self.transport.loseConnection()



factory = protocol.ServerFactory()
factory.protocol = MyChat
factory.clients = []

application = service.Application("chatserver")
internet.TCPServer(port, factory).setServiceParent(application)
