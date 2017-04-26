import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable = True)

message = ' '.join(sys.argv[1:]) or 'Hello World'

channel.basic_publish(exchange='', 
		routing_key='hello', 
		body=message,
		properties=pika.BasicProperties(
			delivery_mode = 2,))

print('[x] Send %r' % message)

connection.close()
