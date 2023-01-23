import paho.mqtt.client as mqtt

#======= Protocol KIRA DESU Configuration ======#
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

#==== Protocol Configuraion

data = 55
print('Input Data Type : {} '.format(type(data)))

#======

try:
    client.publish(topic = topic, payload = data, qos = 0, retain = True) # Publish the define data into the MQTT Broker
    print('Publish Success')
except:
    print('Publish Fail')    