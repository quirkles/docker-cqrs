import os
import time
from random import seed, random

from entities import get_online_auction_purchase_event, get_live_auction_purchase_event, get_payment_made_event
from Publisher import Publisher
from logger import LOGGER

seed()

events = [get_online_auction_purchase_event(), get_live_auction_purchase_event()]

channel = None


def main():
    """Main entry point to the program."""

    # Get the location of the AMQP broker (RabbitMQ server) from
    # an environment variable
    amqp_url = os.environ['AMQP_URL']
    LOGGER.info('URL: %s' % (amqp_url,))

    # Connect to localhost:5672 as guest with the password guest and virtual host "/" (%2F)
    Publisher(amqp_url, on_connection_complete=publish_events)


def publish_events(publisher):
    while True:
        event = get_event()
        publisher.publish_message(event)
        time.sleep(random())


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


if __name__ == '__main__':
    main()
