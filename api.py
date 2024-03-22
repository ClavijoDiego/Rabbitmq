from flask import Flask
import pika

app = Flask(__name__)

@app.route('/conrabbit', methods=['GET'])
def get_simple_data():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='example_queue')
    channel.basic_publish(exchange='',
                          routing_key='example_queue',
                          body='Saludando desde la API!')
    connection.close()
    return 'Mensaje enviado a RabbitMQ'
if __name__ == '__main__':
    app.run(debug=True)
