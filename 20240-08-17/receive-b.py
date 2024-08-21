import sys
import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv
import os

sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

redis_conn = redis.Redis(host='localhost', port=6379,password='1234')
#render_redis_conn = redis.Redis.from_url(os.environ['RENDER_REDIS'])
print(redis_conn.ping())

def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    redis_conn.rpush(topic,message)
    #render_redis_conn.rpush(topic,message)
    print(f"topic={topic},message:{message}")

if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect('127.0.0.1')
    client.subscribe('501教室/監視器-1',qos=2)
    client.loop_forever()