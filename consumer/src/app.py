import os
from Consumer import ReconnectingExampleConsumer
from logger import LOGGER

def main():
    amqp_url = os.environ['AMQP_URL']
    LOGGER.info('URL: %s' % (amqp_url,))
    consumer = ReconnectingExampleConsumer(amqp_url)
    consumer.run()


if __name__ == '__main__':
    main()