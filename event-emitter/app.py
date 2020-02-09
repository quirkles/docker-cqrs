import time
import os

from random import seed, random, choice

from entities import get_online_auction_purchase_event, get_live_auction_purchase_event, get_payment_made_event

seed()

events = [get_online_auction_purchase_event(), get_live_auction_purchase_event()]


def get_event():
    if len(events):
        return events.pop()
    else:
        n = random()
        if n < 0.1:
            return get_online_auction_purchase_event()
        elif n < 0.2:
            return get_live_auction_purchase_event()
        else:
            return get_payment_made_event()


def main():
    # Get the location of the AMQP broker (RabbitMQ server) from
    # an environment variable
    # amqp_url = os.environ['AMQP_URL']
    # print('URL: %s' % (amqp_url,))
    while True:
        event = get_event()
        print(event)
        time.sleep(random())


main()
