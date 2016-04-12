#!/usr/bin/python
# -*- coding: utf-8 -*-

int16 = 'h'
int32 = 'i'
float32 = 'f'
bool0 = '?'
doNotSave = 0
onChange = 1            #saveAttr:(delta, 3min)
percentChange = 2       #3%
onSpecialChange = 3     #otherTagID=value


morgSettings = [
        {
            'settings':
                {
                    'request':"\x02\x03\x03\xC0\x00\x15\x84\x4E",
                    'unpackStr':'>hhffffhhhhhhffh',
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
                    {'id': 15,     'name': "Флаг2"	        , 'type': int16   	, 'saveTrigger': onChange   , 'saveAttr': (0, 1,),   },
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
                                {'id': 50,	'name': "DO_ТЭН"				, 'type': bool0  	, 'saveTrigger': doNotSave,		},
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
		    ,
                    {
                        'getFromID': 15,
                        'data':
                            (
                                {'id': 59,	'name': "Нужно оттаивать"					, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 60,	'name': "Общее разреш ТЭН"					, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 61,	'name': "Задержка после откл комп"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 62,	'name': "огр 1цикла ТЭНа по врем"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 63,	'name': "огр 1цикла ТЭНа по темп"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 64,	'name': "огр темп ТЭН"						, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 65,	'name': "запуск оттайки по врем"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 66,	'name': "запуск оттайки по низк t охлад"	, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 67,	'name': "ОТКЛ 1цикл ТЭНа по врем"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 68,	'name': "ОТКЛ 1цикл ТЭНа по темп"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 69,	'name': "ОТКЛ темп ТЭН"						, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 70,	'name': "заверш оттайки по числу цикл"		, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 71,	'name': "заверш оттайки по времени"			, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 72,	'name': "Резерв бит 13"						, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 73,	'name': "Резерв бит 14"						, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                                {'id': 74,	'name': "Резерв бит 15"			        	, 'type': bool0  	, 'saveTrigger': doNotSave,		},
                            )
                    }
                ]
            ,
        },
        {
            'settings':
                {
                    'request':"\x02\x03\x03\xD5\x00\x38\x55\x97",
                    'unpackStr':'>'+22*'f'+'hh'+'ffffhh',
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
                    {'id': 37,'name': "Накопл ВКЛ комп"         , 'type': float32  	, 'saveTrigger': onChange            , 'saveAttr': (1, 2,),  },
                    {'id': 38,'name': "Накопл ОТКЛ комп"        , 'type': float32  	, 'saveTrigger': onChange            , 'saveAttr': (1, 2,),  },
                    {'id': 39,'name': "Накопл ВКЛ ТЭН"          , 'type': float32  	, 'saveTrigger': onChange            , 'saveAttr': (1, 2,),  },
                    {'id': 40,'name': "Накопл ОТКЛ ТЭН"         , 'type': float32  	, 'saveTrigger': onChange            , 'saveAttr': (1, 2,),  },
                    {'id': 41,'name': "Тек цикл оттайки"        , 'type': int16  	, 'saveTrigger': onChange            , 'saveAttr': (0, 2,),  },
                    {'id': 42,'name': "Резерв int16"            , 'type': int16  	, 'saveTrigger': doNotSave           , 'saveAttr': (1, 2,),  },
                )
        },
]

mt6050Settings = [
    {
            'settings':
                {
                    'request': "\x04\x03\x00\x00\x00\x0A\xC5\x98",
                    'unpackStr': '>'+10*'h',
                    'timePeriod_sec': 5,
                    'individualTag': False,
                    'virtual': False,
                }
             ,
            'data':
                (
                    {'id': 1 ,'name': "zero"     , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 2 ,'name': "Sec"      , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 3 ,'name': "Min"      , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 4 ,'name': "Hour"     , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 5 ,'name': "Day"      , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 6 ,'name': "Month"    , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 7 ,'name': "Year"     , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 8 ,'name': "Inc100"   , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 9 ,'name': "Var"      , 'type': int16  	, 'saveTrigger': doNotSave,		},
                    {'id': 10,'name': "Tens"    , 'type': int16  	, 'saveTrigger': doNotSave,		},
                )
        },
]

bolgarSettings=[]
common_data_name = {
    'morg': morgSettings,
    'bolgar': bolgarSettings,
    'mt6050': mt6050Settings,
}

common_data_imei = {
    #'351513054631988':'bolgar',
    '351513054570863':'morg',
    '351513054687493':'mt6050',
    }

if __name__ == '__main__':
    pass
