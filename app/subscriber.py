import redis
subscriber = redis.Redis(host='iot_redis', port=6379,
                         db=0, password="vurokrazia")
channel = 'device_port_1'
p = subscriber.pubsub()
p.subscribe(channel)
print("RUN")
while True:
    message = p.get_message()
    if message and not message['data'] == 1:
        message = message['data'].decode('utf-8')
        print(message)
