import pika
import sys
import os
import time
from random import seed, random
from logger import LOGGER

seed()

amqp_url = os.environ['AMQP_URL']
connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
while True:
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    LOGGER.info(" [x] Sent %r" % message)
    time.sleep(random())
connection.close()