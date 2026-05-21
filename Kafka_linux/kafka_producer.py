import time
from kafka import KafkaProducer

# 1. Initialize the Kafka Producer
try:
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: v.encode('utf-8')  # Convert text to bytes
    )
except Exception as e:
    print(f"Error connecting to Kafka: {e}")
    exit(1)

log_file_path = "app.log"

try:
    print(f"Reading from {log_file_path} and sending to Kafka...")
    with open(log_file_path, "r") as file:
        for line in file:
            
            message = line.strip()
            if message:
                producer.send("app-logs", value=message)
                print(f"Sent: {message}")
                time.sleep(0.5)  
                
    producer.flush()  

except FileNotFoundError:
    print(f"Error: The file '{log_file_path}' was not found. Please create it first.")
except KeyboardInterrupt:
    print("\nProducer stopped by user.")