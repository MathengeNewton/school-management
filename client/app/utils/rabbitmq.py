import pika
import os


def publish():
    try:
        url = os.getenv('RABBIT_MQ_URL')
        port = os.getenv('RABBIT_MQ_PORT')
        credentials = pika.PlainCredentials('user', 'password')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=8080, credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='my_routing_key', body="hello world")
        print('Connection created successfully')
        connection.close()
        print('message sent')
        return True
    except Exception as e:
        print(e)
        print('message not sent')
        return False