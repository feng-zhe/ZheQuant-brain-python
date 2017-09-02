import pika
import time
import json

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='jobs-todo', durable=True) # declare the queue
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(' [x] Received message %r' % body)
        msg = json.loads(body.decode('utf-8'))
        cmd_strs = msg["cmd"].split()
        print(' cmd_strs is: %r' % cmd_strs)
        for cmd_str in cmd_strs:
            # todo: parse msg["cmd"]
            # e.g. schedule -n JOB_NAME -dsc "JOB_DESC" -t JOB_TYPE -p "JOB_PARAMETERS"
            pass
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1) # only accept one message
    channel.basic_consume(callback, queue='jobs-todo') # need acknowledge

    channel.start_consuming()

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print('Exception raised when try to connect:', e)
            print('Retry a few seconds later')
            time.sleep(5)
