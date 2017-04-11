#!/usr/bin/python
# -*- coding: utf-8 -*-

import struct

int16 = 'h'
int32 = 'i'
float32 = 'f'
flt32 = 'f'
bool0 = '?'
doNotSave = 0
onChange = 1            #saveAttr:(delta, 3min)
percentChange = 2       #3%
onSpecialChange = 3     #otherTagID=value

#(40960, 41065)
pixel_std_map = (
    (
        {'id': 1 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCADA",	},
        {'id': 2 , 'type': int32,	'saveTrigger': doNotSave,	'name':"Version",	},
        {'id': 3 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (SCADA)",	},
        {'id': 4 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (CPU)",	},
        {'id': 5 , 'type': int32,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Код (Аварии)",	},
        {'id': 6 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (SENS)",	},
        {'id': 7 , 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Код (Состояние)",	},
        {'id': 8 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (Отключение)",	},
        {'id': 9 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (Расположение)",	},
        {'id': 10, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (Программа)",	},
        {'id': 11, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (MV)",	},
        {'id': 12, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R2)",	},
        {'id': 13, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R3)",	},
        {'id': 14, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R4)",	},
        {'id': 15, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R5)",	},
        {'id': 16, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R6)",	},
        {'id': 17, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R7)",	},
        {'id': 18, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(наружная)",	},
        {'id': 19, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(канала)",	},
        {'id': 20, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(обр_воды)",	},
        {'id': 21, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(помещения)",	},
        {'id': 22, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(вытяжки)",	},
        {'id': 23, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Влажность",	},
        {'id': 24, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Расход_Приток",	},
        {'id': 25, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Расход_Вытяжка",	},
        {'id': 26, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_CO2",	},
        {'id': 27, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_PDS_Рекуперат",	},
        {'id': 28, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_t_(обр_воды2)",	},
        {'id': 29, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_ДR1",	},
        {'id': 30, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_ДR2",	},
        {'id': 31, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_ДR3",	},
        {'id': 32, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_ДR4",	},
        {'id': 33, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.1, 60,),	'name':"SCo_Уставка_t",	},
        {'id': 34, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_h",	},
        {'id': 35, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_CO2",	},
        {'id': 36, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_tзл",	},
        {'id': 37, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_ВГ",	},
        {'id': 38, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_поправка(t)",	},
        {'id': 39, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_итог(t)",	},
        {'id': 40, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_РЗВ",	},
        {'id': 41, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_ВКЛ",	},
        {'id': 42, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_Задатчик",	},
        {'id': 43, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R2",	},
        {'id': 44, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R3",	},
        {'id': 45, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R4",	},
        {'id': 46, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R5",	},
        {'id': 47, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_t)",	},
        {'id': 48, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_t)",	},
        {'id': 49, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_h)",	},
        {'id': 50, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_h)",	},
        {'id': 51, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_CO2)",	},
        {'id': 52, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_CO2)",	},
        {'id': 53, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_tзл)",	},
        {'id': 54, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_tзл)",	},
        {'id': 55, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Задатчик)",	},
        {'id': 56, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Задатчик)",	},
    ),
    (
        {'id': 57, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R2)",	},
        {'id': 58, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R2)",	},
        {'id': 59, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R3)",	},
        {'id': 60, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R3)",	},
        {'id': 61, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R4)",	},
        {'id': 62, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R4)",	},
        {'id': 63, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R5)",	},
        {'id': 64, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R5)",	},
        {'id': 65, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Status_ЖП",	},
        {'id': 66, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ЖВ",	},
        {'id': 67, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ВП",	},
        {'id': 68, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ВВ",	},
        {'id': 69, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Status_ВоКал",	},
        {'id': 70, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Насос",	},
        {'id': 71, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ЭКал",	},
        {'id': 72, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Рекуп",	},
        {'id': 73, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_СмЗасл",	},
        {'id': 74, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Увлаж",	},
        {'id': 75, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Охлад",	},
        {'id': 76, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R1",	},
        {'id': 77, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R2",	},
        {'id': 78, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R3",	},
        {'id': 79, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R4",	},
        {'id': 80, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R5",	},
        {'id': 81, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R6",	},
        {'id': 82, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R7",	},
        {'id': 83, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%ВоКал",	},
        {'id': 84, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%ЭКал",	},
        {'id': 85, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_СтЭКал",	},
        {'id': 86, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%Рекуп",	},
        {'id': 87, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%СмЗасл",	},
        {'id': 88, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%Охл",	},
        {'id': 89, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%Увл",	},
        {'id': 90, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%ВП",	},
        {'id': 91, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%ВВ",	},
        {'id': 92, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R1",	},
        {'id': 93, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R2",	},
        {'id': 94, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R3",	},
        {'id': 95, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R4",	},
        {'id': 96, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R5",	},
        {'id': 97, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R6",	},
        {'id': 98, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R7",	},
    )
)


def form_std_settings(dic, modbus_set=(1, 3, 40960), prepend_name=""):
    data_dic = dic
    std_dict = \
        {
            'settings':
                {
                    'request': "\x04\x03\x00\x00\x00\x0A\xC5\x98",
                    'unpackStr': ">"+10*'h',
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
                    {'id': 10,'name': "Tens"     , 'type': int16  	, 'saveTrigger': doNotSave,		},
                )
        }

    unpackStr = '>'
    new_data_dic = ()
    for elem in data_dic:
        unpackStr += elem['type']
        elem1 = elem.copy()
        elem1['name']= "{}{}".format(prepend_name, elem1['name'])
        new_data_dic += (elem1,)

    std_dict['data'] = new_data_dic
    std_dict['settings']['unpackStr'] = unpackStr

    len_req = struct.calcsize(unpackStr)/2
    modbus_set += (len_req, )
    std_dict['settings']['request'] = form_modbus_request(req=modbus_set)

    return std_dict


def form_modbus_request(req=(1, 3, 40960, 105)):
    req_str = struct.pack(">bbHH", *req)
    from crc16 import addCRC
    req_str = addCRC(req_str)
    return str(req_str)


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

aktanishSettings = [
    {
            'settings':
                {
                    'request': "\x04\x03\x00\x00\x00\x0A\xC5\x98",
                    'unpackStr': ">"+10*'h',
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
                    {'id': 10,'name': "Tens"     , 'type': int16  	, 'saveTrigger': doNotSave,		},
                )
        },
]

aktanishSettings.append(form_std_settings(pixel_std_map[0], modbus_set=(4, 3, 960), prepend_name="PP2_"))
aktanishSettings.append(form_std_settings(pixel_std_map[1], modbus_set=(4, 3, 1065), prepend_name="PP2_"))
aktanishSettings.append(form_std_settings(pixel_std_map[0], modbus_set=(4, 3, 1960), prepend_name="PP3_"))
aktanishSettings.append(form_std_settings(pixel_std_map[1], modbus_set=(4, 3, 2065), prepend_name="PP3_"))
aktanishSettings.append(form_std_settings(pixel_std_map[0], modbus_set=(4, 3, 2960), prepend_name="PP4_"))
aktanishSettings.append(form_std_settings(pixel_std_map[1], modbus_set=(4, 3, 3065), prepend_name="PP4_"))
aktanishSettings.append(form_std_settings(pixel_std_map[0], modbus_set=(4, 3, 3960), prepend_name="PP1_"))
aktanishSettings.append(form_std_settings(pixel_std_map[1], modbus_set=(4, 3, 4065), prepend_name="PP1_"))
#41115
aktanish_PP1_additional = (
{'id': 99 , 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "ТЕ1 приток ГВС1",	},
{'id': 100, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "ТЕ2 обр ГВС1",	},
{'id': 101, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "ТЕ3 приток ГВС2",	},
{'id': 102, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "ТЕ4 обр ГВС2",	},
{'id': 103, 'type': flt32,	'saveTrigger': doNotSave,	'name': "Резерв AI4",	},
{'id': 104, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (3.0, 5,),	'name': "FT1 ppm",	},
{'id': 105, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name': "DI slave pixel",	},
{'id': 106, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name': "DO обр связь",	},
{'id': 107, 'type': int32,	'saveTrigger': doNotSave,	'name': "Флаг32",	},
{'id': 108, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "ГВС1 %%АО1",	},
{'id': 109, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "ГВС2 %%АО2",	},
{'id': 110, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 h",	},
{'id': 111, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 t",	},
{'id': 112, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 h",	},
{'id': 113, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 t",	},
{'id': 114, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 h",	},
{'id': 115, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 t",	},
{'id': 116, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 h",	},
{'id': 117, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 t",	},
{'id': 118, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 h",	},
{'id': 119, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 t",	},
{'id': 120, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "PE2 нагн",	},
{'id': 121, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "РЕ3 всас",	},
{'id': 122, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 H",	},
{'id': 123, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 H",	},
{'id': 124, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 H",	},
{'id': 125, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 H",	},
{'id': 126, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 H",	},
{'id': 127, 'type': int16,	'saveTrigger': doNotSave,	'name': "KVS",	},
{'id': 128, 'type': int16,	'saveTrigger': doNotSave,	'name': "RV4 переосуш",	},
{'id': 129, 'type': int16,	'saveTrigger': doNotSave,	'name': "RV7 рециркуляция",	},
{'id': 130, 'type': int16,	'saveTrigger': doNotSave,	'name': "ЖП",	},
{'id': 131, 'type': int16,	'saveTrigger': doNotSave,	'name': "ЖВ",	},
)
aktanishSettings.append(form_std_settings(aktanish_PP1_additional, modbus_set=(4, 3, 4115), prepend_name="PP1_"))


chuykovaSettings = [form_std_settings(pixel_std_map[0], modbus_set=(17, 3, 40960), ),
                    form_std_settings(pixel_std_map[1], modbus_set=(17, 3, 41065), )
                    ]

fedoseevskaya_data = (
    {'id': 1 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Счетчик",},
    {'id': 2 , 'type': int16,	'saveTrigger': doNotSave,	'saveAttr': (0.3, 5,),		'name': "plain1",},
    {'id': 3 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Counter",},
    {'id': 4 , 'type': int16,	'saveTrigger': doNotSave,	'saveAttr': (0.3, 5,),		'name': "plain2",},
    {'id': 5 , 'type': int32,	'saveTrigger': doNotSave,	'saveAttr': (0.3, 5,),		'name': "plain3",},
    {'id': 6 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Уставка_копия",},
    {'id': 7 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "TE9_подача",},
    {'id': 8 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "TE8_обратка",},
    {'id': 9 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "TE1_нагн_1",},
    {'id': 10, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "TE2_всас_1",},
    {'id': 11, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "TE3_нагн_2",},
    {'id': 12, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "TE4_всас_2",},
    {'id': 13, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "TE5_конденсат",},
    {'id': 14, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "PE11_нагн_1",},
    {'id': 15, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "PE22_нагн_2",},
    {'id': 16, 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Вент_3%",},
    {'id': 17, 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Вент_6%",},
    {'id': 18, 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Флаги",},
    {'id': 19, 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Аварии_1",},
    {'id': 20, 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Аварии_2",},
    {'id': 21, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Pвсас_1",},
    {'id': 22, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "Pвсас_2",},
    {'id': 23, 'type': int32,	'saveTrigger': doNotSave,	'saveAttr': (0.3, 5,),		'name': "plain4",},
    {'id': 24, 'type': int32,	'saveTrigger': doNotSave,	'saveAttr': (0.3, 5,),		'name': "plain5",},
    {'id': 25, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_00",},
    {'id': 26, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_01",},
    {'id': 27, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_02",},
    {'id': 28, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_03",},
    {'id': 29, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_04",},
    {'id': 30, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_05",},
    {'id': 31, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_06",},
    {'id': 32, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_07",},
    {'id': 33, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_08",},
    {'id': 34, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_09",},
    {'id': 35, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_10",},
    {'id': 36, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_11",},
    {'id': 37, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_12",},
    {'id': 38, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_13",},
    {'id': 39, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_14",},
    {'id': 40, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_15",},
    {'id': 41, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "min_16",},
    {'id': 42, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_00",},
    {'id': 43, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_01",},
    {'id': 44, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_02",},
    {'id': 45, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_03",},
    {'id': 46, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_04",},
    {'id': 47, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_05",},
    {'id': 48, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_06",},
    {'id': 49, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_07",},
    {'id': 50, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_08",},
    {'id': 51, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_09",},
    {'id': 52, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_10",},
    {'id': 53, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_11",},
    {'id': 54, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_12",},
    {'id': 55, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_13",},
    {'id': 56, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_14",},
    {'id': 57, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_15",},
    {'id': 58, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "max_16",},
    {'id': 59, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "flg_00",},
    {'id': 60, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "flg_01",},
    {'id': 61, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "flg_02",},
    {'id': 62, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "flg_03",},
    {'id': 63, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "flg_04",},
    {'id': 64, 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.3, 5,),		'name': "flg_05",},
)
fedoseevskayaSettings = [form_std_settings(fedoseevskaya_data, modbus_set=(4, 3, 94), )]
testSettings = [
    form_std_settings(pixel_std_map[0], modbus_set=(4, 3, 40960), prepend_name="PV1_"),
    form_std_settings(pixel_std_map[1], modbus_set=(4, 3, 41065), prepend_name="PV1_"),
    form_std_settings(pixel_std_map[0], modbus_set=(7, 3, 40960), prepend_name="PV2_"),
    form_std_settings(pixel_std_map[1], modbus_set=(7, 3, 41065), prepend_name="PV2_"),
]

sterlitamakSettings = []
sterlitamakStep = 400
sterlitamakInit = 200
for n in range(1, 22):
    sterlitamakSettings.append(form_std_settings(pixel_std_map[0], modbus_set=(4, 3, sterlitamakInit + (n - 1) * sterlitamakStep), prepend_name="RT{}_".format(n)))
    sterlitamakSettings.append(form_std_settings(pixel_std_map[1], modbus_set=(4, 3, sterlitamakInit + (n - 1) * sterlitamakStep + 105), prepend_name="RT{}_".format(n)))

#41122
mavl_additional = (
    (
        {'id':  99, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 h",	},
        {'id': 100, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 t",	},
        {'id': 101, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 h",	},
        {'id': 102, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 t",	},
        {'id': 103, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 h",	},
        {'id': 104, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 t",	},
        {'id': 105, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 h",	},
        {'id': 106, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 t",	},
        {'id': 107, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 h",	},
        {'id': 108, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 t",	},
        {'id': 109, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 H",	},
        {'id': 110, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 H",	},
        {'id': 111, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 H",	},
        {'id': 112, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 H",	},
        {'id': 113, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 H",	},
    ),
)
mavlSettings = [form_std_settings(pixel_std_map[0], modbus_set=(11, 3, 960), prepend_name="PV11_"),
                form_std_settings(pixel_std_map[1], modbus_set=(11, 3, 1065), prepend_name="PV11_"),
				form_std_settings(mavl_additional[0], modbus_set=(11, 3, 1122), prepend_name="PV11_"),
                ]

almet_data = (
    (
        {'id': 1  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MinTуст",},
        {'id': 2  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MaxTуст",},
        {'id': 3  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MinTдатч",},
        {'id': 4  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MaxTдатч",},
        {'id': 5  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MinРнагн",},
        {'id': 6  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MaxРнагн",},
        {'id': 7  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MinРвсас",},
        {'id': 8  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MaxРвсас",},
        {'id': 9  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MinТнагн",},
        {'id': 10 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "MaxTнагн",},
        {'id': 11 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "EKD_u20_S2_Temp",},
        {'id': 12 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "EKD_u21_Superheat",},
        {'id': 13 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "EKD_u22_SuperheatRef",},
        {'id': 14 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "EKD_u24_Opening_OD",},
        {'id': 15 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "EKD_u25_EvapPres_Pe",},
        {'id': 16 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "EKD_u26_EvapTemp_Te",},
        {'id': 17 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "EKD_u27_Temp_S3",},
        {'id': 18 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "t_вверх",},
        {'id': 19 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "t_вниз",},
        {'id': 20 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "K1_hr",},
        {'id': 21 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "K2_hr",},
        {'id': 22 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.05, 2,),		'name': "K3_hr",},
        {'id': 23 , 'type': int32,  'saveTrigger': onChange,    'saveAttr': (0.05, 2,),     'name': "ГМ_hr", },
        {'id': 24 , 'type': int32,  'saveTrigger': onChange,    'saveAttr': (0.05, 2,),     'name': "B1_hr", },
        {'id': 25 , 'type': int32,  'saveTrigger': onChange,    'saveAttr': (0.05, 2,),     'name': "B2_hr", },
        {'id': 26 , 'type': int32,  'saveTrigger': onChange,    'saveAttr': (0.05, 2,),     'name': "B3_hr", },
        {'id': 27 , 'type': int32,  'saveTrigger': onChange,    'saveAttr': (0.05, 2,),     'name': "B4_hr", },
        {'id': 28 , 'type': int32,  'saveTrigger': onChange,    'saveAttr': (0.05, 2,),     'name': "B5_hr", },
        )
    ,(
        {'id': 1  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Т Уставки Копия",},
        {'id': 2  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "T глик с поля",},
        {'id': 3  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "T глик на поле",},
        {'id': 4  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Tемпература поля",},
        {'id': 5  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Давление всасывания",},
        {'id': 6  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Давление нагнетания",},
        {'id': 7  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Tемпература всас компрес 1",},
        {'id': 8  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Tемпература нагн комп 1",},
        {'id': 9  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Tемператураh всас комп 2",},
        {'id': 10 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Tемпература нагн комп 2",},
        {'id': 11 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Т улица",},
        {'id': 12 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "T фреона из испарителя",},
        {'id': 13 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Т масла",},
        {'id': 14 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Флаги 1",},
        {'id': 15 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Флаги 2",},
        {'id': 16 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Аварии",},
        {'id': 17 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ФлагВент",},
        {'id': 18 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ПЧ_проценты",},
        {'id': 19 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Флаг4",},
        {'id': 20 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Флаг5",},
        {'id': 21 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ВентОбщ",},
        {'id': 22 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "СтупеньРегул",},
        {'id': 23 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ТемпВагон",},
        {'id': 24 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ТемпШкаф",},
        {'id': 25 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "СтатусОвен",},
        {'id': 26 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "СтупеньРегулОС",},
        {'id': 27 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "СтупеньРегулMAX",},
        {'id': 28 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "СтупеньРегулPID",},
        {'id': 29 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Вентиляторы итого",},
        {'id': 30 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Компрессоры итого",},
        {'id': 31 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Маслоохладитель итого",},
        {'id': 32 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Вент1",},
        {'id': 33 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Вент2",},
        {'id': 34 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Вент3",},
        {'id': 35 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Вент4",},
        {'id': 36 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Компрессор1",},
        {'id': 37 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Компрессор2",},
        {'id': 38 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Насос1",},
        {'id': 39 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Насос2",},
        {'id': 40 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Компрессор1Вкл",},
        {'id': 41 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Компрессор2Вкл",},
        {'id': 42 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "НасосЛюбойВкл",},
        {'id': 43 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ЛюбойКомпрессорВкл",},
        {'id': 44 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ВентМасла1",},
        {'id': 45 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ВентМасла2",},
        {'id': 46 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ВентМасла3",},
        {'id': 47 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "Компрессор3",},

        )
    ,(
        {'id': 1  , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_sci_cmd",},
        {'id': 2  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_sci_val",},
        {'id': 3  , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_sci_r1",},
        {'id': 4  , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_sci_r2",},
        {'id': 5  , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_sci_r3",},
        {'id': 6  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_AO",},
        {'id': 7  , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_режимУстанов",},
        {'id': 8  , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_аварии",},
        {'id': 9  , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_флаги",},
        {'id': 10 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_var1",},
        {'id': 11 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "ГМ_var2",},
    ),
    (
        {'id': 1  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_ГВС_приток",},
        {'id': 2  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_ГВС_обратка",},
        {'id': 3  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_заправки",},
        {'id': 4  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_Бака",},
        {'id': 5  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_Бак_обр",},
        {'id': 6  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_Яма",},
        {'id': 7  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_Яма_обр",},
        {'id': 8  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_Поля_обр",},
        {'id': 9  , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_Поля",},
        {'id': 10 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Темп_воздух_над_полем",},
        {'id': 11 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Флаг1",},
        {'id': 12 , 'type': int32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_Флаг2",},
        {'id': 13 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_АО1%%_3х_ходов",},
        {'id': 14 , 'type': flt32,	'saveTrigger': onChange,	'saveAttr': (0.1, 5,),		'name': "УТ_АО2%%_RV3",},

    )

)
almetSettings = [form_std_settings(almet_data[0], modbus_set=(5, 3, 110), ),
                 form_std_settings(almet_data[1], modbus_set=(5, 3, 1), ),
                 form_std_settings(almet_data[2], modbus_set=(5, 3, 200), ),
                 form_std_settings(almet_data[3], modbus_set=(5, 3, 300), ),
                 ]

#(40960, 41065)
grenada_map = (
    (
        {'id': 1 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCADA",	},
        {'id': 2 , 'type': int32,	'saveTrigger': doNotSave,	'name':"Version",	},
        {'id': 3 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (SCADA)",	},
        {'id': 4 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (CPU)",	},
        {'id': 5 , 'type': int32,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Код (Аварии)",	},
        {'id': 6 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (SENS)",	},
        {'id': 7 , 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Код (Состояние)",	},
        {'id': 8 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (Отключение)",	},
        {'id': 9 , 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (Расположение)",	},
        {'id': 10, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (Программа)",	},
        {'id': 11, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (MV)",	},
        {'id': 12, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R2)",	},
        {'id': 13, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R3)",	},
        {'id': 14, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R4)",	},
        {'id': 15, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R5)",	},
        {'id': 16, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R6)",	},
        {'id': 17, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Код (R7)",	},
        {'id': 18, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(наружная)",	},
        {'id': 19, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(канала)",	},
        {'id': 20, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(обр_воды)",	},
        {'id': 21, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(помещения)",	},
        {'id': 22, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(вытяжки)",	},
        {'id': 23, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_Влажность",	},
        {'id': 24, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Расход_Приток",	},
        {'id': 25, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Расход_Вытяжка",	},
        {'id': 26, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_CO2",	},
        {'id': 27, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_FT_Pa",	},
        {'id': 28, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_(обр_KVS)",	},
        {'id': 29, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_t_смешения",	},
        {'id': 30, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_ДR2",	},
        {'id': 31, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_ДR3",	},
        {'id': 32, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name':"SCo_FT_м3ч",	},
        {'id': 33, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.1, 60,),	'name':"SCo_Уставка_t",	},
        {'id': 34, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.1, 60,),	'name':"SCo_Уставка_h",	},
        {'id': 35, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_CO2",	},
        {'id': 36, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_tзл",	},
        {'id': 37, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_ВГ",	},
        {'id': 38, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_поправка(t)",	},
        {'id': 39, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_итог(t)",	},
        {'id': 40, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_РЗВ",	},
        {'id': 41, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_ВКЛ",	},
        {'id': 42, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_Задатчик",	},
        {'id': 43, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R2",	},
        {'id': 44, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R3",	},
        {'id': 45, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R4",	},
        {'id': 46, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_Уставка_R5",	},
        {'id': 47, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_t)",	},
        {'id': 48, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_t)",	},
        {'id': 49, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_h)",	},
        {'id': 50, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_h)",	},
        {'id': 51, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_CO2)",	},
        {'id': 52, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_CO2)",	},
        {'id': 53, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_max_(Уст_tзл)",	},
        {'id': 54, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_min_(Уст_tзл)",	},
        {'id': 55, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_max_(Задатчик)",	},
        {'id': 56, 'type': flt32,	'saveTrigger': doNotSave,	'name':"SCo_min_(Задатчик)",	},
    ),
    (
        {'id': 57, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R2)",	},
        {'id': 58, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R2)",	},
        {'id': 59, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R3)",	},
        {'id': 60, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R3)",	},
        {'id': 61, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R4)",	},
        {'id': 62, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R4)",	},
        {'id': 63, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_max_(R5)",	},
        {'id': 64, 'type': int32,	'saveTrigger': doNotSave,	'name':"SCo_min_(R5)",	},
        {'id': 65, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Status_ЖП",	},
        {'id': 66, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ЖВ",	},
        {'id': 67, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ВП",	},
        {'id': 68, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ВВ",	},
        {'id': 69, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Status_ВоКал",	},
        {'id': 70, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Насос",	},
        {'id': 71, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_ЭКал",	},
        {'id': 72, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Рекуп",	},
        {'id': 73, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_Status_СмЗасл",	},
        {'id': 74, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Увлаж",	},
        {'id': 75, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_Охлад",	},
        {'id': 76, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R1",	},
        {'id': 77, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R2",	},
        {'id': 78, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%KVS",	},
        {'id': 79, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R4",	},
        {'id': 80, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R5",	},
        {'id': 81, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%ЖП",	},
        {'id': 82, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_Status_R7",	},
        {'id': 83, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%ВоКал",	},
        {'id': 84, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%ЭКал",	},
        {'id': 85, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_СтЭКал",	},
        {'id': 86, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%Рекуп",	},
        {'id': 87, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%СмЗасл",	},
        {'id': 88, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%Охл",	},
        {'id': 89, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%Увл",	},
        {'id': 90, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%ВП",	},
        {'id': 91, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_%ВВ",	},
        {'id': 92, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R1",	},
        {'id': 93, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R2",	},
        {'id': 94, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R3",	},
        {'id': 95, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R4",	},
        {'id': 96, 'type': int16,	'saveTrigger': doNotSave,	'name':"SCo_%R5",	},
        {'id': 97, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_РециркУт_нагрев",	},
        {'id': 98, 'type': int16,	'saveTrigger': onChange, 'saveAttr': (0.9, 60,),	'name':"SCo_РециркУт_охлажд",	},
    )
)

#41135
grenada_additional = (
    (
        {'id':  99, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 h",	},
        {'id': 100, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 t",	},
        {'id': 101, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 h",	},
        {'id': 102, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 t",	},
        {'id': 103, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 h",	},
        {'id': 104, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 t",	},
        {'id': 105, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 h",	},
        {'id': 106, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 t",	},
        {'id': 107, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 h",	},
        {'id': 108, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 t",	},
        {'id': 109, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT1 H",	},
        {'id': 110, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT2 H",	},
        {'id': 111, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT3 H",	},
        {'id': 112, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT4 H",	},
        {'id': 113, 'type': flt32,	'saveTrigger': onChange, 'saveAttr': (0.3, 5,),	'name': "UT5 H",	},
    ),
)

grenada_map = grenada_map + grenada_additional
#print grenada_map[2]

grenadaSettings = [ form_std_settings(grenada_map[0], modbus_set=(5, 3,  960), prepend_name="PV1_"),
                    form_std_settings(grenada_map[1], modbus_set=(5, 3, 1065), prepend_name="PV1_"),
                    form_std_settings(grenada_map[2], modbus_set=(5, 3, 1135), prepend_name="PV1_"),
                    form_std_settings(grenada_map[0], modbus_set=(5, 3, 1960), prepend_name="PV2_"),
                    form_std_settings(grenada_map[1], modbus_set=(5, 3, 2065), prepend_name="PV2_"),
                    form_std_settings(grenada_map[2], modbus_set=(5, 3, 2135), prepend_name="PV2_"),
                ]

gorka_data = (
    {'id': 1 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Temp",},
    {'id': 2 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Temp_4s",},
    {'id': 3 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Humid",},
    {'id': 4 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Humid_4s",},
    {'id': 5 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Dew_point",},
    {'id': 6 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Abs_humid",},
    {'id': 7 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Mix_ratio",},
    {'id': 8 , 'type': int16,	'saveTrigger': onChange,	'saveAttr': (3, 5,),		'name': "Enthalpy",},
)
gorkaSettings = [form_std_settings(gorka_data, modbus_set=(2, 4, 0), ), ]


bolgarSettings = []
common_data_name = {
    'morg': morgSettings,
    'bolgar': bolgarSettings,
    'aktanish': aktanishSettings,
    'chuykova': chuykovaSettings,
    'fedos': fedoseevskayaSettings,
    'test': testSettings,
    'sterlitamak': sterlitamakSettings,
    'mavl': mavlSettings,
    'almet': almetSettings,
    'grenada': grenadaSettings,
    'gorka': gorkaSettings,
}

common_data_imei = {
    #'351513054631988':'bolgar',
    '353173067390771': 'test', #fake for test --> ЦПК
    '353173062414303': 'fedos',
    '351513054570863': 'morg',
    '351513054687493': 'aktanish',
    '353173063444515': 'chuykova',
    '353173067393130': 'sterlitamak',
    '351513052870364': 'mavl',
    '351513054389629': 'almet',
    '353173063486193': 'grenada',
    '355234054969205': 'gorka',
}

if __name__ == '__main__':
    hexString = lambda byteString : " ".join(x.encode('hex') for x in byteString)
    decString = lambda byteString : " ".join(str(int(x.encode('hex'), 16)) for x in byteString)
    print "hex:", hexString(fedoseevskayaSettings[0]['settings']['request'])
    print "dec:", decString(fedoseevskayaSettings[0]['settings']['request'])
    pass
