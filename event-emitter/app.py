import time
import os

from random import seed, random
from flask import Flask

seed()

app = Flask(__name__)

events = ['live_auction_event', 'online_auction_event', 'user_made_payment']

def get_event():


def main():
    # Get the location of the AMQP broker (RabbitMQ server) from
    # an environment variable
    amqp_url = os.environ['AMQP_URL']
    print('URL: %s' % (amqp_url,))
    while True:
        event = get_random_event()
        time.sleep(random() * 10)


