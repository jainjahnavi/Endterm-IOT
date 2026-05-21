import paho.mqtt.client as mqtt
import redis
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/temperature"

r = redis.Redis(host="localhost", port=6379, db=0)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    device_id = data["device_id"]
    key = f"readings:{device_id}"
    
    # Store reading in Redis list
    r.lpush(key, json.dumps(data))
    # Keep only last 100 readings
    r.ltrim(key, 0, 99)
    
    print(f"Stored reading for {device_id}: {data}")

client = mqtt.Client("subscriber") #type:ignore
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("Subscriber running...")
client.loop_forever()