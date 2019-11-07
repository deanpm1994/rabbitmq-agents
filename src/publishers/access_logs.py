import socket
import pika

def upd_server(host='localhost', port=5050):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((host,port))
    while True:
        (data, _) = s.recvfrom(128*1024)
        yield data

params = pika.ConnectionParameters(host='rabbitmq')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='squid-logs')
channel.exchange_declare(exchange='logs', exchange_type='fanout')

for data in upd_server():
    for logs in data.split('\n')[:-1]:
        channel.basic_publish(exchange='', routing_key='', body=logs)