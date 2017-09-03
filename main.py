import pika
import time
import json
from zq_calc.calc_mgr import calc_mgr

def cmd_str2dic(cmd_str):
    for cmd_str in cmd_strs:
        # e.g. schedule -n JOB_NAME -dsc "JOB_DESC" -t JOB_TYPE -p "JOB_PARAMETERS"
        pass

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='jobs-todo', durable=True) # declare the queue
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        SCHEDULE_CMD_NAME = 'schedule'
        print(' [x] Received message %r' % body)
        msg = json.loads(body.decode('utf-8'))
        cmd_strs = msg["cmd"].split()
        print(' cmd_strs is: %r' % cmd_strs)
        cmd_dict = cmd_str2dic(cmd_str)
        cmd_name = cmd_dict['cmd_name']
        # check the command type and give it to different managers
        if  cmd_name == SCHEDULE:
            calc_mgr(cmd_dict)
        elif cmd_name == DISPLAY:
            pass # TODO: display mananger
        else:
            print(' [!] Unknow command %r, skipped' % cmd_name)
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
