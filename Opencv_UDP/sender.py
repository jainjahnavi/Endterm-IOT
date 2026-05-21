import cv2
import socket

# UDP socket setup
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    _, buffer = cv2.imencode('.jpg', frame)

   
    sock.sendto(buffer.tobytes(), (UDP_IP, UDP_PORT))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
sock.close()