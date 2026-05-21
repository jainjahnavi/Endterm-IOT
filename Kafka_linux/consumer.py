from kafka import KafkaConsumer

try:
    consumer = KafkaConsumer(
        'app-logs',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',  # Start reading from the beginning if no offset exists
        value_deserializer=lambda x: x.decode('utf-8')  # Convert bytes back to text
    )
except Exception as e:
    print(f"Error connecting to Kafka: {e}")
    exit(1)

output_file_path = "errors_only.log"

print("Consumer is running. Waiting for messages...")

try:
    with open(output_file_path, "a") as error_file:  
        for message in consumer:
            log_line = message.value
            
            #filter error
            if "ERROR" in log_line:
                print(f"Found Error: {log_line}")
                error_file.write(log_line + "\n")
                error_file.flush()  

except KeyboardInterrupt:
    print("\nConsumer stopped by user.")