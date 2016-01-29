import sys
import socket
import serial
import serial.threaded

import threading

class SerialToNet(serial.threaded.Protocol):
    """serial->socket"""
    dataToSend = ''

    def __init__(self):
        self.socket = None

    def __call__(self):
        return self

    def data_received(self, data):
        logger.debug("serial received data: {}".format(data))
        self.dataToSend = self.dataToSend + data
        logger.debug("dataToSend: {}".format(self.dataToSend))
        try:
            if self.t.isAlive():
                self.t.cancel()
        except:
            pass
        self.t = threading.Timer( 0.05, self.sendData, [self.dataToSend,] )
        logger.debug("Plan the timer with data {}".format(self.dataToSend))
        self.t.start()

    def sendData(self, data):
        if self.socket is not None:
            self.socket.send(data)##sendall(data)
            logger.info("Received from serial-->TCP: {}".format(data))
            self.dataToSend = ''


from time import sleep
import logging
from logging.handlers import TimedRotatingFileHandler

logHandler = TimedRotatingFileHandler("logfile", when="midnight") #when = "M")
logHandler.suffix = "%Y-%m-%d.html"
logFormatter = logging.Formatter('%(levelname)-10.10s %(asctime)s [%(funcName)-12.12s] [%(threadName)-15.15s] %(message)s </br>')
logHandler.setFormatter( logFormatter )
logger = logging.getLogger( 'MyLogger' )
logger.addHandler( logHandler )
logger.setLevel( logging.INFO ) # CHANGE to INFO after start up!!!
#for console logging
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler( consoleHandler )

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
logger.info('PROGRAMM IS STARTING...\n\n')

if __name__ == '__main__':

    # connect to serial port
    ser = serial.serial_for_url("COM8", do_not_open=True)
    ser.baudrate = 9600
    ser.bytesize = 8
    ser.stopbits = 1
    ser.parity = 'N'
    ser.rtscts = 0
    ser.xonxoff = 0
    ser.timeout = 1

    try:
        ser.open()
        logger.info("Port {} is opened".format(ser.name))
    except serial.SerialException as e:
        logger.error("Could not open serial port {}: {}".format(ser.name, e))
        sys.exit(1)

    ser_to_net = SerialToNet()
    serial_worker = serial.threaded.ReaderThread(ser, ser_to_net)
    serial_worker.start()


    try:
        while 1:
            # make a new connection here!
            #start opening connection
            sock = socket.socket()
            sock.connect(('52.29.5.118', 6567))
            data = sock.recv(1024)
            logger.info(data)

            #send Auth key
            sock.send('ImYourClient001')

            #receive confirmation
            data = sock.recv(1024)
            if data == "OKletsSwitchToTrasparentMode":
                logger.info("connection is OK")
            else:
                logger.warning("Auth is failed!")
                sys.exit(1)
            try:
                ser_to_net.socket = sock

                # enter network <-> serial loop
                while 1:
                    try:
                        data = sock.recv(1024)
                        logger.info("Received from TCP-->serial: {}".format(data))
                        if not data:
                            break
                        ser.write(data)                 # get a bunch of bytes and send them
                    except socket.error as msg:
                        logger.error( str(msg) )
                        # probably got disconnected
                        break
            except socket.error as msg:
                logger.error( str(msg) )
            finally:
                ser_to_net.socket = None
                logger.info('Disconnected')
                sock.close()
    except KeyboardInterrupt:
        pass

    logger.info('\n--- exit ---\n')
    serial_worker.stop()
