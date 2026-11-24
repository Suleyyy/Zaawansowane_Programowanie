import time
import pika


def callback(ch, method, properties, body):
    task_name = body.decode()
    print(f"Start: {task_name}")
    time.sleep(5)
    print(f"Done:  {task_name}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=8081)
)
channel = connection.channel()

channel.queue_declare(queue="demo_tasks")
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="demo_tasks", on_message_callback=callback)

print("Consumer started. Waiting for tasks...")
channel.start_consuming()
