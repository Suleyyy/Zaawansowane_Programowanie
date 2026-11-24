import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=8081)
)
channel = connection.channel()

channel.queue_declare(queue="demo_tasks")

for i in range(1, 101):
    message = f"Task {i}"
    channel.basic_publish(exchange="", routing_key="demo_tasks", body=message)
    print(f"Sent: {message}")

connection.close()
