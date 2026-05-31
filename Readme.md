Python Kafka Project
Overview

This project demonstrates a simple implementation of Apache Kafka using Python with Producer and Consumer applications.

The application flow:

Producer → Kafka Broker → Topic → Consumer

The producer sends messages to Kafka and the consumer continuously listens for and receives messages from the Kafka topic.

Project Structure
python-kafka/
│
├── producer.py
├── consumer.py
├── docker-compose.yml
├── .gitignore
├── README.md
Technologies Used
Python 3
Apache Kafka
Zookeeper
Docker
Docker Compose
kafka-python library
Kafka Architecture
Producer.py
      ↓
Kafka Broker
      ↓
test-topic
      ↓
Consumer.py
Setup Instructions
Step 1: Clone Repository
git clone https://github.com/shubkrsnha/python-kafka.git

cd python-kafka
Step 2: Start Kafka and Zookeeper
docker compose up -d

Check running containers:

docker ps

Expected:

zookeeper
kafka
Step 3: Create Kafka Topic
docker exec -it python-kafkaprojects-kafka-1 kafka-topics \
--create \
--topic test-topic \
--bootstrap-server localhost:9092

Verify topic:

docker exec -it python-kafkaprojects-kafka-1 kafka-topics \
--list \
--bootstrap-server localhost:9092
Step 4: Install Dependencies
pip3 install kafka-python
Step 5: Run Consumer

Open terminal 1:

python3 consumer.py

Expected:

Waiting for messages...
Step 6: Run Producer

Open terminal 2:

python3 producer.py

Expected:

Message Sent

Consumer output:

Waiting for messages...

Hello Kafka
