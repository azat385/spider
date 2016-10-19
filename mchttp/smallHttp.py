# -*- coding: utf-8 -*-
import time
import BaseHTTPServer

from mcStat import getArray

#import sys
#sys.stderr = open('mchttp.log', 'a')


HOST_NAME ='0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8000 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    log_file = open("mchttp.log", mode="w",)

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
        print txt
        s.wfile.write(txt)


def allText(debug=False, path=''):
    path = path.split("/")[1]

    from urllib import unquote
    path = unquote(path).decode('utf8')

    from mako.template import Template
    name1 = 'Pylons Developer'
    mytemplate = Template(filename='base.html', input_encoding='utf-8')
    text = mytemplate.render(name=name1, path=path, text=getData())
    if debug:
        print text
    return text.encode('utf-8')


def getData():
    import memcache
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)

    almet_list = [
        "T_глик_с_поля",
        "T_глик_на_поле",
        "Tемпература_поля",
        "Давление_всасывания",
        "Давление_нагнетания",
    ]

    arc_prefix = "online_"

    almet_list = ["{}almet.{}".format(arc_prefix, a) for a in almet_list]


    resultDict = mc.get_multi(almet_list)
    resultStr = ""
    for key, value in resultDict.iteritems():
            resultStr += "{} = {}\n".format(key, value)

    return resultStr

if __name__ == '__main__':

    debug = False
    if debug:
        allText(debug=debug)
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
