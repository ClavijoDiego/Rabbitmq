
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='example_queue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='example_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Esperando mensajes. Si desea salir, presione CTRL+C')
channel.start_consuming()
