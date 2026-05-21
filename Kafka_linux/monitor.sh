#!/bin/bash

# Define filenames and paths
CONSUMER_SCRIPT="consumer.py"
LOG_FILE="monitor.log"

echo "Starting Kafka Consumer Monitor..."

while true
 de
    # (i) Check if the consumer script is running
    # pgrep -f looks for the process by its full command line name
    if pgrep -f "$CONSUMER_SCRIPT" > /dev/null
    then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - Consumer is running fine."
    else
        # (ii) Restart it if not found and log the event with a timestamp
        echo "$(date '+%Y-%m-%d %H:%M:%S') - WARNING: Consumer stopped! Restarting..." >> "$LOG_FILE"
        
        # Start the consumer in the background (&) so the script can keep looping
        python3 "$CONSUMER_SCRIPT" &
    fi

    # (iii) Repeat the check every 30 seconds
    sleep 30
done