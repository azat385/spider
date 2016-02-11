# -*- coding: utf-8 -*-
import time
import BaseHTTPServer

from mcStat import getArray

HOST_NAME ='0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8081 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("""
        <html>
            <head><title>Title goes here.</title>
                <meta charset="utf-8">
                <meta http-equiv="refresh" content="60">
                <!-- Latest compiled and minified CSS -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

                <!-- Optional theme -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

                <!-- Latest compiled and minified JavaScript -->
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
        </head>
        """)
        s.wfile.write("<body><p>This is a test.</p>")
        s.wfile.write("<p>You accessed path: {}</p>".format(s.path) )
        #print(str(s.path).decode('cp1251'))
        s.wfile.write("<p>You accessed path: %s</p>" % 'на русском')

        s.wfile.write("""
            <body>
                <div class="table-responsive">
                <table class="table table-striped table-hover">
        """)
        i = 0
        for k,vT in getArray():
            s.wfile.write("<tr>")
            for cell in ((i,k) + vT):
                s.wfile.write("<td>{}</td>".format(cell))
            s.wfile.write("</tr>\n")
            i+=1

        s.wfile.write("""
                </table>
                </div>
            </body>
        </html>""")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
