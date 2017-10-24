import tornado
import tornado.websocket
from datetime import timedelta
import datetime, sys, time
from pprint import pprint
import json
import serial.tools.list_ports
import serial

clients = []
arduino_name = "SNR=95333353037351D071B0"

ports = serial.tools.list_ports.comports()
print(ports)
arduino_port = ""
for p in ports:
    print (p)
    if p[0] != "":
        print ("This is an Arduino!")
        print (p)
        arduino_port = p[0]

if arduino_port == "":
    print ("Arduino not found")
    sys.exit("where is it?")

# Establish the connection on a specific port
ser = serial.Serial(arduino_port, 115200) #9600)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    tt = datetime.datetime.now()
    def check_origin(self, origin):
        #print "origin: " + origin
        return True
    # the client connected
    def open(self):
        print ("New client connected")
        self.write_message("You are connected")
        clients.append(self)
        tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=1), self.test)

    def test(self):
        try:
            info = {}
            try:
                text = ser.readline() # Read the newest output from the Arduino
                print("TEXT: ")
                print(text)
                values = str(text).split(".")
                """
		info = {
                    "luz"      : float(values[1]),
                    "humedad"  : float(values[2]),
                    "temperatura"   : float(values[3]),
                    "tierra" : float(values[0]),
                    "estado"    : int(values[3]),
                    "timestamp" : time.time()
		}
		"""
                info = {
                    "luz"      : float(values[0]), 
                    "humedad"  : float(values[1]), 
                    "temperatura"   : float(values[2]), 
                    #"tierra" : float(values[0]), 
                    "estado"    : int(values[3]),
                    "timestamp" : time.time()
                }
                print info
            except Exception as e:
                print("EXCEPTION IN TEST READ FROM READ SERIAL: ")
                print(e)
                #print(info)
                info = {
                    "humedad"  : float("0.0"),
                    "temperatura"   : float("0.0"),
                    "tierra" : float("0.0"),
                    "estado"    : -1,
                    "timestamp" : time.time()
                }
                #raise(e)
            print(info)
            self.write_message(info)
        except Exception as e:
            print ("restartplease")
            self.write_message("restartplease")
            print e
            #raise(e)
        else:
            tornado.ioloop.IOLoop.instance().add_timeout(timedelta(seconds=0.1), self.test)

    # the client sent the message
    def on_message(self, message):
        print ("message: " + message)
        try:
            message = json.loads(message)
            #pprint(message)

        except Exception as e:
            print ("cant send value to arduino")
            #raise(e)
        #self.write_message(message)

    # client disconnected
    def on_close(self):
        print ("Client disconnected")
        clients.remove(self)

socket = tornado.web.Application([(r"/websocket", WebSocketHandler),])
if __name__ == "__main__":
    print("Trying to read data from serial: ")
    text = ser.readline() 
    print("Data from serial: ")
    print(text)
    values = str(text).split(".")
    print values
    print("Opening port 8888")
    socket.listen(8888)

tornado.ioloop.IOLoop.instance().start()
