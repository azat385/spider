# -*- coding: utf-8 -*-
# start in windows python d:\Python27\Scripts\twistd.py -ny ttcpServer.py
# sudo kill -TERM $(sudo cat gsm.pid)
# sudo python /usr/local/bin/twistd -y ttcpServer.py --pidfile=gsm.pid --uid=0

from twisted.application import internet, service
from twisted.internet import protocol, reactor
from twisted.python import log
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

from datetime import datetime


class myArgs():
    delay = 30
    port = 14210
    delayBeforeDropConnection = 300


class authClass():
    """Authentication and Authorization"""
    authRequestQuery = "\xC0\x00\x06\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE7\x48\xC2"
    authConfirmQuery = "\xC0\x00\x06\x01\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x25\xC2"
    #first10wordsQuery = "\x04\x03\x00\x00\x00\x0A\xC5\x98"
    NotAuth = 0
    WaitAuthResp = 1
    OkAuth = 2
    IMEI = ""
    auth = False

    def __init__(self, ):
        self.status = self.NotAuth
        self.auth = False

    def sendAuthRequestQuery(self):
        self.status = self.WaitAuthResp
        log.msg('send wrx.auth = {}'.format(self.authRequestQuery))
        return self.authRequestQuery

    def sendConfRequestQuery(self):
        self.status = self.OkAuth
        self.auth = True
        return self.authConfirmQuery

    def handleIMEI(self, data):
        s = []
        try:
            #dataArray = [ord(d) for d in data]
            s.append(ord(data[5]))
            s.append(data[5 + 1:5 + 1 + 15])
            s.append(data[5 + 16:5 + 16 + 16])
            s.append(data[5 + 32:5 + 32 + 10])
            s.append(ord(data[47]))
            log.msg("handleIMEI:s:{}".format(s))
        except:
            log.msg("some error in wrx auth response decoding")
            return False
        log.msg('get IMEI from wrxAuth {}'.format(s[1]))
        return s[1] #self.IMEI


    def __call__(self,):
        return self.auth

    def authProgress(self, response):
        if self.status == self.WaitAuthResp:
            self.IMEI = self.handleIMEI(response)
        return self.IMEI



class getServerCommonData():
    #from initData import common_data
    #common_data=common_data
    #for testing
    common_data = {
    ##    '351513054631988':'bolgar',
        '351513054570863':'morg',
    }
    def getName(self, id):
        if self.common_data.has_key(id):
            return self.common_data[id]

int16 = 'h'
float32 = 'f'
bool0 = '?'
doNotSave = 0
onChange = 1            #saveAttr:(delta, 3min)
percentChange = 2       #3%
onSpecialChange = 3     #otherTagID=value



class getDeviceData():
    """write usage here"""

    morgSettings = [
        {
            'settings':
                {
                    'request':"\x02\x03\x03\xC0\x00\x15\x84\x4E",
                    'unpackStr':'hhffffhhhhhhffh',
                    'timePeriod_sec': 5,
                    'individualTag': True,
                    'virtual': True,
                }
            ,
            'data':
                (
                    {'id': 1,     'name': "Флаг1"        	, 'type': int16		, 'saveTrigger': onChange   , 'saveAttr': (0, 3,),   },
                    {'id': 2,     'name': "Авария"       	, 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (0, 3,),   },
                    {'id': 3,     'name': "Темп камеры"  	, 'type': float32	, 'saveTrigger': onChange   , 'saveAttr': (0.2, 3,),   },
                    {'id': 4,     'name': "Давл нагн"    	, 'type': float32 	, 'saveTrigger': onChange   , 'saveAttr': (0.2, 3,),   },
                    {'id': 5,     'name': "t комн конд"  	, 'type': float32 	, 'saveTrigger': onChange   , 'saveAttr': (0.2, 3,),   },
                    {'id': 6,     'name': "t всас"       	, 'type': float32 	, 'saveTrigger': onChange   , 'saveAttr': (0.2, 3,),   },
                    {'id': 7,     'name': "тек авария"   	, 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (0, 3,),   },
                    {'id': 8,     'name': "АО охл"       	, 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (5, 3,),   },
                    {'id': 9,     'name': "АО конд"      	, 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (5, 3,),   },
                    {'id': 10,     'name': "ПИД конд"     	, 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (5, 3,),   },
                    {'id': 11,     'name': "ПИД охлад"    	, 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (5, 3,),   },
                    {'id': 12,     'name': "текущий цикл"	, 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (0, 3,),   },
                    {'id': 13,     'name': "P всас расчет"	, 'type': float32   	, 'saveTrigger': doNotSave   , 'saveAttr': (0, 3,),   },
                    {'id': 14,     'name': "Темп охлад"	    	, 'type': float32   	, 'saveTrigger': onChange   , 'saveAttr': (0.2, 3,),   },
                    {'id': 15,     'name': "Флаг2"	        , 'type': int16   	, 'saveTrigger': doNotSave   , 'saveAttr': (0, 3,),   },
                )
            ,
            'virtual':
                [
                    {
                        'getFromID': 1,
                        'data':
                            (
                                {'id': 35,	'name': "DIN_пуск"					, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 36,	'name': "DIN_скуд"					, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 37,	'name': "DO_свет"					, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 38,	'name': "DIN_геркон"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 39,	'name': "санкц_доступ"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 40,	'name': "НЕсанкц_доступ"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 41,	'name': "DIN_кнопка откр_дверь"		, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 42,	'name': "DO_электр_маг_замок"		, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 43,	'name': "DO_авария"					, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 44,	'name': "DO_работа"					, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 45,	'name': "DO_вент_фильтра"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 46,	'name': "DO_вент_охлажд"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 47,	'name': "DO_вент_конденс"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 48,	'name': "DO_запуск_компр"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 49,	'name': "ОС_работа_компр"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 50,	'name': "Флаг1_бит15"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                            )
                    }
                    ,
                    {
                        'getFromID': 2,
                        'data':
                            (
                                {'id': 51,	'name': "Авария бит 1"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 52,	'name': "Авария бит 2"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 53,	'name': "Авария бит 3"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 54,	'name': "Авария бит 4"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 55,	'name': "Авария бит 5"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 56,	'name': "Авария бит 6"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 57,	'name': "Авария бит 7"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 58,	'name': "Авария бит 8"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
			    )
                    }
                ]
            ,
        },
        {
            'settings':
                {
                    'request':"\x02\x03\x03\xD5\x00\x2E\xD4\x59",
                    'unpackStr':22*'f'+'hh',
                    'timePeriod_sec': 25,
                    'individualTag': False,
                    'virtual': False,
                }
             ,
            'data':
                (
                    {'id': 13,'name': "время цикла ВКЛ  0"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 14,'name': "время цикла ОТКЛ 0"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 15,'name': "время цикла ВКЛ  1"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 16,'name': "время цикла ОТКЛ 1"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 17,'name': "время цикла ВКЛ  2"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 18,'name': "время цикла ОТКЛ 2"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 19,'name': "время цикла ВКЛ  3"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 20,'name': "время цикла ОТКЛ 3"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 21,'name': "время цикла ВКЛ  4"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 22,'name': "время цикла ОТКЛ 4"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 23,'name': "время цикла ВКЛ  5"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 24,'name': "время цикла ОТКЛ 5"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 25,'name': "время цикла ВКЛ  6"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 26,'name': "время цикла ОТКЛ 6"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 27,'name': "время цикла ВКЛ  7"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 28,'name': "время цикла ОТКЛ 7"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 29,'name': "время цикла ВКЛ  8"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 30,'name': "время цикла ОТКЛ 8"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 31,'name': "время цикла ВКЛ  9"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 32,'name': "время цикла ОТКЛ 9"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 33,'name': "время цикла ВКЛ  А"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 34,'name': "время цикла ОТКЛ А"      , 'type': float32  	, 'saveTrigger': onSpecialChange     ,'saveAttr': (12, 9,),    },
                    {'id': 35,'name': "Все пуски"	        , 'type': int16   	, 'saveTrigger': onSpecialChange     ,'saveAttr': (0, 3,),   },
                    {'id': 36,'name': "Удачные пуски"	        , 'type': int16   	, 'saveTrigger': onSpecialChange     ,'saveAttr': (0, 3,),   },
                )
        },
    ]
    bolgarSettings=[]
    common_data = {
        'morg': morgSettings,
        'bolgar': bolgarSettings,
    }

    def __init__(self, name):
        self.morgSet = self.getOneDeviceData(name=name)
        self.i = 0
        self.i_max = len(self.morgSet)-1
        self.name = name
        self.try_current_req = 0
        self.try_current_req_max = 3


    def getOneDeviceData(self, name):
        #return self.common_data['morg']
        #for testing
        if self.common_data.has_key(name):
            return self.common_data[name]

    def currentRequest(self):
        last_msg = self.morgSet[self.i]['settings']['request']
        return last_msg

    def handleResponse(self, data, strTimeStamp,):
        d = simpleCheck(_req=self.currentRequest(), _res=data)
        if d == 1:
            print "error in check"
            self.errorOccuredDuringResponseCheck()
            return self.currentRequest()
        unpackStr = self.morgSet[self.i]['settings']['unpackStr']
        dNew = rearrangeData(d, unpackStr)
        if dNew == False:
            print "error in dNew"
            self.errorOccuredDuringResponseCheck()
            return self.currentRequest()

        import struct
        valueTuple = struct.unpack('>' + unpackStr, dNew)
        printTuple(self.morgSet[self.i]['data'] ,valueTuple, strTimeStamp, prependStr=self.name)
        if self.morgSet[self.i]['settings']['virtual']:
            for virtSet in self.morgSet[self.i]['virtual']:
                id = virtSet['getFromID'] - 1
                virtTupleVal = valueTuple[id]
                virtTupleLen = len(virtSet['data'])
                virtTuple = tuple([int(bin(virtTupleVal>>i)[-1]) for i in xrange(virtTupleLen)])
                printTuple(virtSet['data'] ,virtTuple, strTimeStamp, prependStr=self.name)
        self.incr_i_safely()
        self.try_current_req = 0
        return self.currentRequest()

    def errorOccuredDuringResponseCheck(self):
        self.try_current_req += 1
        log.msg( "error occured  try ones more" )
        if self.try_current_req >= self.try_current_req_max:
            self.try_current_req = 0
            self.incr_i_safely()
            print "end up trying lets send another one"

    def incr_i_safely(self):
        self.i += 1
        if self.i>self.i_max:
            self.i = 0

def simpleCheck(_req, _res):
    from crc16 import checkCRC
    if checkCRC(_res):
        print "Error in CRC"
        return 1
    if _req[0]<>_res[0]:
        print "Error in address id"
        return 1
    if _req[1]<>_res[1]:
        print "Error in function"
        return 1
    if ord(_req[5])*2 <> ord(_res[2]):
        print "Error in len field"
        return 1
    if ord(_req[5])*2 <> len(_res)-5: # addr, code, len , data in bytes, lrc, crc
        print "Error in response lenght"
        return 1
    return _res[3:-2] #maybe return bytearray


def getUnpackStr(_reqArr):
    _unpackStr = ''
    for _req in _reqArr:
        _unpackStr += _req['type']
    return _unpackStr



def rearrangeData(_data,_unpackStr):
    import struct
    if len(_data) == struct.calcsize(_unpackStr):
        iBegin = 0
        iEnd = 0
        dataNew = ''
        for s in _unpackStr:
            iEnd = iBegin + struct.calcsize(s)
            if s == 'f':
                addData = _data[iBegin:iEnd][2:] + _data[iBegin:iEnd][:2]
            else:
                addData = _data[iBegin:iEnd]
            dataNew += addData
            iBegin = iEnd
        return dataNew


def printTuple(dataT, valT, strT, prependStr='', key_str_separater='.', val_str_separater=';'):
    import memcache
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    #mc.flush_all()

    onlineStr = "online"
    lastSavedStr = "lastSaved"
    archiveStr = "archive"

    def form_key_str(base_str, adding_str):
        return "{}_{}".format(adding_str, base_str)


    minIndex = min([len(dataT), len(valT)])
    i = 0
    for i in xrange(minIndex):
        value = valT[i]
        #online values
        formKeyStr = "{}{}{}".format(prependStr, key_str_separater, dataT[i]['name'])
        formKeyStr = formKeyStr.replace(" ", "_")   #no blanks in key
        formValStr = "{}{}{}".format(value,val_str_separater, strT)
        print "{}={}".format(formKeyStr, formValStr)
        mc.set(form_key_str(formKeyStr,onlineStr), formValStr)
        #last saved values and append archiving
        if dataT[i]['saveTrigger']==onChange:
            #get last saved value
            keyLastSaved = form_key_str(formKeyStr,lastSavedStr)
            #print "key: {}".format(keyLastSaved)
            lastSavedValue = mc.get(keyLastSaved)
            #print "value: {}".format(lastSavedValue)
            if lastSavedValue is None:
                mc.set(keyLastSaved,formValStr)
                #print "Set {}={}".format(keyLastSaved,formValStr)
                continue
            else:
                vT = tuple(lastSavedValue.split(";"))
                lastSaved_value,lastSaved_time = vT[:2]
                lastSaved_value = float(lastSaved_value)
                if not dataT[i].has_key('saveAttr'):
                    continue
                delta_value, delta_time = dataT[i]['saveAttr']
                if (abs(lastSaved_value-value)>delta_value) \
                    or (check_time_passed(t1=lastSaved_time, t2=strT, deltaSec=delta_time*60)):
                    mc.set(keyLastSaved,formValStr)
                    appendKey = form_key_str(formKeyStr,archiveStr)
                    if mc.append(appendKey,';;;'+formValStr) is False:
                        mc.set(appendKey,formValStr)



def check_time_passed(t1,t2,deltaSec=180):
    t1 = datetime.strptime(t1,"%Y-%m-%d %H:%M:%S.%f")
    t2 = datetime.strptime(t2,"%Y-%m-%d %H:%M:%S.%f")
    dif = t2-t1
    dif_sec = abs(dif.total_seconds())
    return dif_sec >= deltaSec
    #print "dif time= {} delta= {}".format(dif_sec,deltaSec)



class SpiderProtocol(protocol.Protocol):
    stage = 0
    i = 0
    IMEI = ""
    auth = ""
    name = ""
    name_busy_list = []

    def ___init__(self):
        self.stage = 0
        self.i = 0
        self.IMEI = ""

    def connectionMade(self):
        self.auth = authClass()
        log.msg('connectionMade from peer {}'.format(self.transport.getPeer()))
        msg = self.auth.sendAuthRequestQuery()
        self.transport.write(msg)
        self.timeout = reactor.callLater(myArgs.delayBeforeDropConnection, self.dropConnection)

    def dataReceived(self, line):
        if self.auth.auth:
            if self.name:
                if self.getDD:
                    self.timeout.reset(myArgs.delayBeforeDropConnection)
                    strTimeStamp = str(datetime.now())
                    nextMsg = self.getDD.handleResponse(data=line, strTimeStamp=strTimeStamp)
                    self.planRequest(delayTime=myArgs.delay, message=nextMsg)
                else:
                    self.dropConnection(reason='no data for that name in server!!!')
            else:
                self.dropConnection(reason='no name!!!')
        else:
            self.IMEI = self.auth.authProgress(line)
            if self.IMEI:
                getSCD = getServerCommonData()
                self.name = getSCD.getName(self.IMEI)
                if self.name:
                    if not self.check_name_in_list():
                        log.msg("Add name {} to name list".format(self.name))
                        self.name_busy_list.append(self.name)
                        self.allow_to_remove = True
                    else:
                        #reject connection
                        log.msg("ERROR!!! name {} is already in name list".format(self.name))
                        self.dropConnection(reason='name is already active')
                        return
                    msg = self.auth.sendConfRequestQuery()
                    self.transport.write(msg)
                    # now time to plan to send first real request
                    self.getDD = getDeviceData(self.name)
                    if self.getDD:
                        msg = self.getDD.currentRequest()
                        self.planRequest(myArgs.delay, message=msg)
                    else:
                        self.dropConnection(reason='no data for that name in server!!!')
                else:
                    self.dropConnection(reason='IMEI not found in set')
            else:
                self.dropConnection(reason='not auth')

    def planRequest(self, delayTime=1, message=""):
        log.msg("Plan request={} after {} sec IMEI={}".format(message, delayTime, self.IMEI))
        self.nextRequest = reactor.callLater(delayTime, self.sendRequest, message)

    def sendRequest(self, request):
        log.msg("Send request={} IMEI={}".format(request, self.IMEI))
        self.transport.write(request)

    def connectionLost(self, reason):
        log.msg('lost connection with IMEI {} reason: {}'.format(self.IMEI, reason))
        if hasattr(self, 'allow_to_remove'):
            if self.allow_to_remove:
                if self.check_name_in_list():
                    log.msg("Remove name {} from name list".format(self.name))
                    self.name_busy_list.remove(self.name)
        self.cancel_planned_request()
        self.cancel_timeout_drop()

    def dropConnection(self, reason='silence'):
        log.msg("Drop connection from server to client {} due to {}".format(self.transport.getPeer(), reason) )
        self.cancel_planned_request()
        self.cancel_timeout_drop()
        self.transport.loseConnection()

    def check_name_in_list(self):
        return self.name in self.name_busy_list

    def cancel_planned_request(self):
        if hasattr(self, 'nextRequest'):
            if self.nextRequest.active():
                log.msg("Cancel planned request IMEI={}".format(self.IMEI))
                self.nextRequest.cancel()

    def cancel_timeout_drop(self):
        if hasattr(self, 'timeout'):
            if self.timeout.active():
                log.msg("Cancel planned timeout drop client={}".format(self.transport.getPeer()))
                self.timeout.cancel()

class SpiderFactory(protocol.ServerFactory):
    protocol = SpiderProtocol

    # def __init__(self, service):
    #	self.service = service
    def __init__(self, **kwargs):
        self.users = kwargs

    def getUser(self, user):
        return self.users.get(user, "No such user")


userDict = {'moshes': 'Happy', 'azat': 'Very happy', 'ruslan': '2 cildren'}

application = service.Application('spider', uid=0, gid=0,)
logfile = DailyLogFile("my.log", "logs/")
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)
factory = SpiderFactory(**userDict)
internet.TCPServer(myArgs.port, factory).setServiceParent(
    service.IServiceCollection(application))

