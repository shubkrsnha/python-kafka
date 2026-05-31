try:
    from kafka import KafkaConsumer
except ImportError as e:
    raise ImportError(
        "kafka library not found. Install with: pip3 install kafka-python"
    ) from e


consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers='localhost:9092'
)

print("Waiting for messages...")


for message in consumer:
    print(
        message.value.decode('utf-8')
    )