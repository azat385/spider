# -*- coding: utf-8 -*-


hexString = lambda byteString : " ".join(x.encode('hex') for x in byteString)


int16 = 'h'
float32 = 'f'
bool0 = '?'

doNotSave = 0
onChange = 1            #3min
percentChange = 2       #3%
onSpecialChange = 3     #otherTagID=value


morgSettings = [
    {
        'settings':
            {
                'request':"\x02\x03\x03\xC0\x00\x10\x44\x4D",
                'unpackStr':'hhffffhhhhhh',
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
            )
        ,
        'virtual':
            [
                {
                    'getFromID': 1,
                    'data':
                        (
                            {'id': 35,	'name': "DIN_пуск"					, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 36,	'name': "DIN_скуд"					, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 37,	'name': "DO_свет"					, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 38,	'name': "DIN_геркон"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 39,	'name': "санкц_доступ"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 40,	'name': "НЕсанкц_доступ"			, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 41,	'name': "DIN_кнопка откр_дверь"		, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 42,	'name': "DO_электр_маг_замок"		, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 43,	'name': "DO_авария"					, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 44,	'name': "DO_работа"					, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 45,	'name': "DO_вент_фильтра"			, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 46,	'name': "DO_вент_охлажд"			, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 47,	'name': "DO_вент_конденс"			, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 48,	'name': "DO_запуск_компр"			, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 49,	'name': "Флаг1_бит14"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 50,	'name': "Флаг1_бит15"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                        )
                }
                ,
                {
                    'getFromID': 2,
                    'data':
                        (
                            {'id': 51,	'name': "Авария бит 1"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 52,	'name': "Авария бит 2"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 53,	'name': "Авария бит 3"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 54,	'name': "Авария бит 4"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 55,	'name': "Авария бит 5"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 56,	'name': "Авария бит 6"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 57,	'name': "Авария бит 7"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                            {'id': 58,	'name': "Авария бит 8"				, 'type': bool0  	, 'saveTrigger': onChange,		},
                        )
                }
            ]
        ,
    },
    {
        'settings':
            {
                'request':"\x02\x03\x03\xD5\x00\x2C\x55\x98",
                'unpackStr':22*'f',
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
            )
    },
]



from crc16 import checkCRC

def simpleCheck(_req, _res):
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



import struct

def rearrangeData(_data,_unpackStr):
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
    else:
        return

def printTuple(dataT, valT, strT):
    import memcache
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    minIndex = min([len(dataT), len(valT)])
    i = 0
    for i in xrange(minIndex):
        print "{} = {}".format(dataT[i]['name'], valT[i])
        mc.set(('морг.'+dataT[i]['name']).replace (" ", "_"),"{};{}".format(valT[i], strT))


def main():
    import socket
    sock = socket.socket()
    sock.connect(('52.29.5.118', 6565))


    from time import sleep
    from datetime import datetime


    for oneSet in morgSettings:
        req = oneSet['settings']['request']

        sock.send(req)
        data = sock.recv(1024)
        strTimeStamp = str(datetime.now())
        #data = "\x02\x03 >\x03\x00\x00\xf3\x88@\x83\xa6\xb9A\x94\xd2\xaaA\xe2.\xbc@\xd6\x00\x00\x00d\x00d\x00d\x00d\x00\x08\xe2\xc2"
        print "request",hexString(data)

        d = simpleCheck(req,data)
        if d == 1:
            continue
        print "Just data", hexString(d)

        #unpackStr = getUnpackStr(response[0])
        unpackStr = oneSet['settings']['unpackStr']
        print "Unpack str", unpackStr

        dNew = rearrangeData(d, unpackStr)
        print "New data", hexString(dNew)

        valueTuple =  struct.unpack('>' + unpackStr, dNew)
        printTuple(oneSet['data'] ,valueTuple, strTimeStamp)

        if oneSet['settings']['virtual']:
            for virtSet in oneSet['virtual']:
                id = virtSet['getFromID'] - 1
                virtTupleVal = valueTuple[id]
                virtTupleLen = len(virtSet['data'])
                virtTuple = tuple([int(bin(virtTupleVal>>i)[-1]) for i in xrange(virtTupleLen)])
                printTuple(virtSet['data'] ,virtTuple, strTimeStamp)

        sleep(5)
    sock.close()

if __name__ == '__main__':
    main()
"""
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set("some_key", "Some value")
value = mc.get("some_key")
mc.set("another_key", 3)
mc.delete("another_key")
mc.set("key", "1")   # note that the key used for incr/decr must be a string.
mc.incr("key")
mc.decr("key")
"""
