#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import BaseHTTPServer

DEBUG = False

HOST_NAME ='0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8000 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    log_file = open("mchttp.log", mode="a",)

    def log_message(self, format, *args):
        self.log_file = open("mchttp.log", mode="a",)
        self.log_file.write("%s - - [%s] %s\n" %
                            (self.client_address[0],
                             self.log_date_time_string(),
                             format%args))
        self.log_file.close()

    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        #s.wfile.write("<p>You accessed path: {}</p>".format(s.path) )
        #print(str(s.path).decode('cp1251'))
        #s.wfile.write("<p>You accessed path: %s</p>" % 'на русском')
        txt = allText(path=s.path)
        if DEBUG:
            print txt
        s.wfile.write(txt)


def allText( path='/almet'):
    path = path.split("/")[1]

    from urllib import unquote
    path = unquote(path).decode('utf8')

    from mako.template import Template
    name1 = "Юбилейный".decode('utf-8')
    mytemplate = Template(filename='base.html', input_encoding='utf-8')
    text1 = getData()
    text = mytemplate.render(name1=name1, path=path, text="dvvd", rows=text1)
    if DEBUG:
        print text
    return text.encode('utf-8')


def getData():
    import memcache
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)

    almet_list = [
        ["T_глик_с_поля",           "Т гликоля с поля",     "°C",],
        ["T_глик_на_поле",          "Т гликоля на поле",     "°C",],
        ["Tемпература_поля",        "Т льда",     "°C",],
        ["Давление_всасывания",     "Р фреона всасывания ",     "Бар",],
        ["Давление_нагнетания",     "Р фреона нагнетания",     "Бар",],
    ]

    arc_prefix = "online_"

    almet_col = [row[0] for row in almet_list]

    almet_col = ["{}almet.{}".format(arc_prefix, a) for a in almet_col]


    resultDict = mc.get_multi(almet_col)
    resultList = []

    import humanize
    _t = humanize.i18n.activate('ru_RU')
    from datetime import datetime

    for key, value in resultDict.iteritems():
            if key in almet_col:
                pos = almet_col.index(key)
                v = value.split(";")
                v_float, v_time = v
                v_float = round(float(v_float), 2) #val = float("{0:.2f}".format(float(v[0])))
                v_time_full = v_time
                v_time = datetime.strptime(v_time,"%Y-%m-%d %H:%M:%S.%f")
                v_time_str = humanize.naturaltime(datetime.now() - v_time)
                resultList.append([almet_list[pos][1].decode('utf-8'), "{} {}".format(v_float, almet_list[pos][2]).decode('utf-8'), v_time_str.decode('utf-8'), v_time_full])
                #resultStr += "{} = {}{} {}<br>\n".format(almet_list[pos][1], v_float, almet_list[pos][2], v_time_str)

    humanize.i18n.deactivate()
    print resultList
    return resultList

if __name__ == '__main__':

    if DEBUG:
        allText()
        exit()

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)


