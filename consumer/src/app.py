#!/usr/bin/env python
import pika
import os
from logger import LOGGER

amqp_url = os.environ['AMQP_URL']
connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

LOGGER.info(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    LOGGER.info(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()