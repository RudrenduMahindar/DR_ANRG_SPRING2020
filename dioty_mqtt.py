import paho.mqtt.client as mqtt
import time
# Define event callbacks

def on_connect(client, userdata, rc):
    if rc == 0:
        print("Connected successfully.")
    else:
        print("Connection failed. rc= "+str(rc))

def on_publish(client, userdata, mid):
    print("Message "+str(mid)+" published.")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid "+str(mid)+" received.")

def on_message(client, userdata, msg):
    print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)

mqttclient = mqtt.Client()

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish
mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

root_topic= "/useremail@email.com/"   #root topic in your dioty account    
#send_string_message= "Hello World Message!"
send_number_message= 24  #send this number to dioty server
broker_host= "mqtt.dioty.co"
broker_port= 1883
user_id= "useremail@email.com"    #type your user email here linked with dioty mqtt
password= "password"    #type your dioty password here 
keep_alive_time=60

# Connect
mqttclient.username_pw_set(user_id, password)
mqttclient.connect(broker_host, broker_port,keep_alive_time)  #keep_alive_time is optional here

# Start subscription
mqttclient.subscribe(root_topic)            #(yourRootTopic)

# Publish a message
#mqttclient.publish(root_topic, send_number_message)

rc = mqttclient.loop()
# Loop; exit on error rc = 0
while rc == 0: #rc=0 for successful connection 
    rc = mqttclient.loop()
    mqttclient.publish(root_topic, send_number_message)
    time.sleep(5) #publish after every 5 seconds 

print("Disconected with rc: " + str(rc))