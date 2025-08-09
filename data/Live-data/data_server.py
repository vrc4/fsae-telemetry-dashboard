import socket
import time
import random
from datetime import datetime

HOST = 'localhost'
PORT = 9999

def generate_mock_data():
    timestamp = datetime.now().strftime('%H:%M:%S')
    rpm = random.randint(1000, 9000)
    speed = round(random.uniform(0, 200), 2)
    throttle = round(random.uniform(0, 100), 2)
    return f"{timestamp},{rpm},{speed},{throttle}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER] Waiting for connections on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"[SERVER] Connected by {addr}")

        with conn:
            while True:
                try:
                    data = generate_mock_data()
                    conn.sendall((data + "\n").encode())
                    time.sleep(1)
                except (BrokenPipeError, ConnectionResetError):
                    print(f"[SERVER] Connection to {addr} lost. Waiting for new connection...")
                    break  # go back to s.accept()