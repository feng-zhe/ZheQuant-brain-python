import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='job-todo', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received message %r" % body)
    msg = json.loads(body)
    # todo: parse msg["cmd"]
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1) # only accept one message
channel.basic_consume(callback, queue='task_queue') # need acknowledge

channel.start_consuming()
