import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import tornado
import tornado.websocket
import time
import datetime
from datetime import timedelta
import json
import ast
import Queue

qmsg = Queue.Queue()
clients = []

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
            data = {}
            try:
                text = qmsg.get()
                print("DATA FROM MQTT TO WEBSOCKET: ")
                print(text)
                data = text
                data["timestamp"] = time.time()
            except Exception as e:
                raise
                print("EXCEPTION IN TEST READ FROM MQTT TO WS: ")
                print(e)
                #print(info)
                data = {
                    "luz"  : float("0.0"),
                    "humedad"  : float("0.0"),
                    "temperatura"   : float("0.0"),
                    "tierra" : float("0.0"),
                    "estado"    : -1,
                    "timestamp" : time.time()
                }
                #raise(e)
            print(data)
            self.write_message(data)
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

def msg_ws(msg):
   resp = publish.single("data_to_web", msg, hostname="localhost")
   return resp


def on_connect(client, userdata, flags, rc):
   print("MQTT Connected with result code "+str(rc))

   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   #client.subscribe("sensors/new_sensor")
   client.subscribe("sensors/new_data")

data_list = []

def on_message(client, userdata, msg):
    #mosquitto_pub -t "sensors/new_data" -m '{"data":1}'
    print("msg.topic: " + msg.topic+" msg.payload "+str(msg.payload))
    try:
        list = json.loads(msg.payload)
        data_json = {}
        for key,value in list.iteritems():
            data_json[key] = value
            qmsg.put(data_json)
    except Exception as e:
        print "Exception in on_message: " + str(e)

def on_subscribe(client, userdata,mid, granted_qos):
   print "userdata : " +str(userdata)

def on_publish(mosq, obj, mid):
   print("mid: " + str(mid))

class MqttClient(object):
    """docstring for MqttClient."""
    def __init__(self, client=mqtt.Client()):
        super(MqttClient, self).__init__()
        self.client = client
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect("localhost", 1883, 60)
        actions = Queue.Queue()

    def get_actions_queue(self):
        return self.actions

    def get_client(self):
        return self.client

    def set_on_connect(self, func):
        self.on_connect = func

    def publish(message, topic):
         print("Sending %s " % (message))
         publish.single(str(topic), message, hostname="localhost")
         return "Sending msg: %d " % (message)

socket = tornado.web.Application([(r"/websocket", WebSocketHandler),])
if __name__ == "__main__":
    print "Starting MQTT"
    mqtt = MqttClient()
    mqtt.client.loop_start()
    print("Opening port 8888")
    socket.listen(8888)

tornado.ioloop.IOLoop.instance().start()
