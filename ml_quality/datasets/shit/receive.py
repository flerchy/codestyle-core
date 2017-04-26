import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.basic_qos(prefetch_count = 1)

channel.queue_declare(queue='hello', durable = True)

print('[*] Waiting for messages. To exit press Ctrl-C')

def callback(ch, method, properties, body):
    print('[x] Received %r' % (body,))
    time.sleep(body.count('.'))
    print('[x] Done')
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback, queue='hello')

channel.start_consuming()
