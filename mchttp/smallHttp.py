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
        if DEBUG:
            s.wfile.write("<p>You accessed path: {}</p>".format(s.path) )
            #print(str(s.path).decode('cp1251'))
            #s.wfile.write("<p>You accessed path: %s</p>" % 'на русском')
        txt = allText(path=s.path)
        if DEBUG:
            print txt
        s.wfile.write(txt)


def allText(path='/almet'):
    path = path.split("/")[1]

    from urllib import unquote
    path = unquote(path).decode('utf8')

    from mako.template import Template
    name1 = "Юбилейный".decode('utf-8')
    mytemplate = Template(filename='base.html', input_encoding='utf-8')
    commonData1, listDictExpanded, listDictCollapsed = getData(objName=path)
    text = mytemplate.render(commonData=commonData1, ldExpanded=listDictExpanded, ldCollapsed=listDictCollapsed)
    if DEBUG:
        print text
    return text.encode('utf-8')


def getData(objName='almet'):
    import memcache
    
    if DEBUG:
        host = '52.29.5.118:14212'
    else:
        host = '127.0.0.1:11211'

    mc = memcache.Client([host], debug=0)
    
    import yaml

    with open("data.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    if not cfg.has_key(objName):
        objName = 'almet'

    almet_common = cfg[objName]['common']

    def getMCdata(almet_list):
        arc_prefix = "online_"
        almet_col = [row[0] for row in almet_list]
        almet_col = ["{}{}.{}".format(arc_prefix, objName, a.encode('utf-8')) for a in almet_col]

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
                    v_float = round(float(v_float)*koef, 2) #val = float("{0:.2f}".format(float(v[0])))
                    v_time_full = v_time
                    v_time = datetime.strptime(v_time,"%Y-%m-%d %H:%M:%S.%f")
                    v_time_str = humanize.naturaltime(datetime.now() - v_time)
                    resultList.append([almet_list[pos][1], "{} {}".format(v_float, almet_list[pos][2].encode('utf-8')).decode('utf-8'), v_time_str.decode('utf-8'), v_time_full])
                    #resultStr += "{} = {}{} {}<br>\n".format(almet_list[pos][1], v_float, almet_list[pos][2], v_time_str)

        humanize.i18n.deactivate()
        resultList.sort()
        if DEBUG:
            print resultList
        return resultList
        
    resultExpandTableList = []
    resultCollapsedTableList = []
    for table in cfg[objName]['tables']:
        if not table.has_key('koef'):
            koef = 1.0
        else:
            koef = table['koef']
        resDict = {'caption':table['caption'], 'data':getMCdata(almet_list=table['data'])}
        if table['expand']:
            resultExpandTableList.append(resDict)
        else:
            resultCollapsedTableList.append(resDict)

    return almet_common, resultExpandTableList, resultCollapsedTableList

if __name__ == '__main__':

    if DEBUG:
        print getData(objName="mavl")
        print allText("/mavl")
        #exit()

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)


