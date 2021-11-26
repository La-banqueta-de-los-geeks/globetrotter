import redis
publisher = redis.Redis(host='iot_redis', port=6379,
                         db=0, password="vurokrazia")
message = ""
channel = "device_port_1"
while(message != "exit"):
    message = input("")
    send_message = "Python : " + message
    publisher.publish(channel, send_message)
