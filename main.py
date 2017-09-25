import pika
import time
import json
from zq_calc.calc_mgr import calc_mgr
from zq_gen.str import cmd_str2dic

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='jobs-todo', durable=True)                      # declare the queue
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        SCHEDULE_CMD = 'schedule'
        print(' [x] Received message %r' % body)
        msg = json.loads(body.decode('utf-8'))
        cmd_str = msg['cmd']
        job_id = msg['id']
        print(' [*] cmd_strs is: %r' % cmd_str)

        # Possible command
        # 1. schedule -n JOB_NAME -dsc "JOB_DESC" -t JOB_TYPE -p "JOB_PARAMETERS"

        cmd_dict = cmd_str2dic(cmd_str)
        cmd_name = cmd_dict['cmd_name']
        if  cmd_name == SCHEDULE_CMD:                                           # check the command type and give it to different managers

            def calc_cb(result):
                ''' The callback function when calculation job is done '''
                connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
                channel = connection.channel()
                channel.queue_declare(queue='jobs-done', durable=True)
                msg2send = {
                        'id':       job_id,
                        'status':   'done',
                        'result':   result
                    }
                channel.basic_publish(
                        exchange='',
                        routing_key='jobs-done',
                        body=json.dumps(msg2send),
                        properties=pika.BasicProperties(
                            delivery_mode = 2, # make message persistent
                        ))
                ch.basic_ack(delivery_tag = method.delivery_tag)
                print(' [x] Calculation result has been sent. Task is done.')

            calc_mgr(cmd_dict, calc_cb)
        elif cmd_name == DISPLAY:
            pass                                                                # TODO: display mananger
        else:
            print(' [!] Unknow command %r, skipped' % cmd_name)

    channel.basic_qos(prefetch_count=1)                                         # only accept one message
    channel.basic_consume(callback, queue='jobs-todo')                          # need acknowledge
    channel.start_consuming()

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print('Exception raised when try to connect:', e)
            print('Retry a few seconds later')
            time.sleep(5)
