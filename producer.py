from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

message = "Hello Kafka"

producer.send(
    "test-topic",
    message.encode('utf-8')
)

producer.flush()

print("Message Sent")