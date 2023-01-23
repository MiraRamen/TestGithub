import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

#======= Protocol WATASHI NO NAMAE HA KIRA YOSHIKAGE Configuration ======#
host = 'test.mosquitto.org' # Define the URL  or IP toware the MQTT Broker
port = 1883                 # Define the specific port toward the MQTT Broker
group = 'Calculus2'
yourname = 'Sora'
topic = group + '/' + yourname # Define the topic to store the data
username = ''                  # Define the authentication username
password = ''                  # Define the authentication password

#====== protocol Configuration =====#

client = mqtt.Client()                   # Initialize the connecting gateway to the MQTT server
client.username_pw_set(username, password)  #Initialize the authentication for the MQTT Broker
client.connect(host, port)                  # Initialize the MQTT Broker



#======

try:
    msg = subscribe.simple(topic, hostname = host, port = port)
    print('subscribe Success')
    get_topic = msg.topic
    data = msg.payload
    print('{} : {}'.format(get_topic, data))
    print('Data Type : {}'.format(type(data)))
   
except:
    print('Publish Fail')   