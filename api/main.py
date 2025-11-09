from fastapi import FastAPI
import pika
import json
import os

app = FastAPI()
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")

@app.post("/send/")
def send_message(data: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue="messages")
    channel.basic_publish(
        exchange="",
        routing_key="messages",
        body=json.dumps(data)
    )
    connection.close()
    return {"status": "Message sent", "data": data}
