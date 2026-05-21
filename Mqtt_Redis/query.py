import redis
import json

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Key for sensor_01 readings
key = "readings:sensor_01"

# Get the last 10 readings
readings = r.lrange(key, 0, 9)

# Handle empty case
if not readings:
    print("No readings found for sensor_01")
else:
    # Decode JSON and extract temperature values
    temps = [json.loads(entry.decode())["value"] for entry in readings]
    avg_temp = sum(temps) / len(temps)

    print(f"Last 10 readings: {temps}")
    print(f"Average temperature: {avg_temp:.2f}")