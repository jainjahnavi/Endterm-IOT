
import cv2
import socket
import numpy as np

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    
    data, addr = sock.recvfrom(65536)  

    np_data = np.frombuffer(data, dtype=np.uint8)
    
    frame = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #type:ignore
    
     # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Show edges
    cv2.imshow("Canny Edge Stream", edges)
    # Show frame
    cv2.imshow("Grayscale Stream", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
sock.close()