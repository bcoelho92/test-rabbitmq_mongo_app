import pika
import json
import os
from pymongo import MongoClient
import time

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/testdb")

def main():
    time.sleep(10)  # aguarda RabbitMQ e Mongo subirem
    client = MongoClient(MONGO_URI)
    db = client.get_database()
    collection = db["messages"]

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue="messages")

    def callback(ch, method, properties, body):
        data = json.loads(body)
        print(f"[x] Mensagem recebida: {data}")
        collection.insert_one(data)
        print(f"[✓] Salva no MongoDB")

    channel.basic_consume(queue="messages", on_message_callback=callback, auto_ack=True)
    print("🟢 Aguardando mensagens. CTRL+C para sair.")
    channel.start_consuming()

if __name__ == "__main__":
    main()