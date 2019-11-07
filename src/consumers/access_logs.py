import pika
import json
from ..utils import *


queue = "access_logs"
parameters = (
    pika.ConnectionParameters(host=RABBITMQ_HOST, connection_attemps=10, retry_delay=5)
)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue=queue)
channel.basic_consume(consumer_callback, queue=queue, no_ack=True)