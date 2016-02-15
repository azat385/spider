from twisted.internet import reactor, protocol

#start in windows python d:\Python27\Scripts\twistd.py  multiClient.py

authReqQuery = '\xC0\x00\x06\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE7\x48\xC2'
authConQuery = '\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2'


outDataQuery = "\x02\x03 >\x03\x00\x00\xf3\x88@\x83\xa6\xb9A\x94\xd2\xaaA\xe2.\xbc@\xd6\x00\x00\x00d\x00d\x00d\x00d\x00\x08\xe2\xc2"

count = '1'
morgIMEI = '351513054570863'
verPO = '1234567890123456'
verDE = '1234567890'
chType = '1'

clientsList = []
count_failed = 0
count_lost = 0

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    global clientsList

    def connectionMade(self):
        print "connection is made"
        self.i = 0
        self.imei = self.factory.imei
        clientsList.append(self)

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print "Server said:", data
        if self.i==0:
            a = count+self.imei+verPO+verDE+chType
            authResQuery = '\xC0\x00\x07\x00\x3f{}\xE9\x85\xC2'.format(a)
            self.transport.write(authResQuery)
        if self.i>0:
            self.transport.write(outDataQuery)
        if self.i>=10:
            self.transport.loseConnection()
        self.i+=1

    def connectionLost(self, reason):
        print "connection lost in i={} with imei {}".format(self.i, self.imei)
        #print clientsList
        clientsList.remove(self)
        #print clientsList

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient
    global clientList
    #global count_failed, count_lost

    def __init__(self, imei, number):
        self.imei = imei
        self.number = number

    def clientConnectionFailed(self, connector, reason):
        global count_failed
        print "Connection failed - goodbye! {}".format(self.number)
        count_failed +=1
        self.stop_reactor_safe()

    def clientConnectionLost(self, connector, reason):
        global count_lost
        print "Connection lost - goodbye! {}".format(self.number)
        count_lost += 1
        self.stop_reactor_safe()

    def stop_reactor_safe(self):
        if not clientsList:
            print "All clients are done....Stop reactor...."
            print clientsList
            #reactor.stop()
            print count_failed, count_lost


# this connects the protocol to a server running on port 8000
def main():
    import sys
    import random, string
    def randomword(length):
       return ''.join(random.choice(string.lowercase) for i in range(length))

    try:
        clientCount = int(sys.argv[1])
    except:
        clientCount = 200


    imeiList = [morgIMEI, 5*'123', morgIMEI, 5*'321', morgIMEI]
    rndImeiList = []
    for _ in xrange(clientCount):
        rndImeiList.append(randomword(15))
    imeiList += rndImeiList

    from initData import common_data
    imeiList+=common_data.keys()[:clientCount]

    from random import shuffle
    shuffle(imeiList)

    print "prepared imeiList len = {}".format(len(imeiList))
    fList = []
    i=1
    for imei in imeiList:
        fList.append(EchoFactory(imei, i))
        i +=1

    for f in fList:
        reactor.connectTCP("127.0.0.1", 14210, f)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
