import csv
import time
import random
from datetime import datetime

def generate_mock_can_data():
    """
    Simulates CAN data for RPM, speed (km/h), and throttle (%).
    """
    rpm = random.randint(1000, 8000)          # Engine RPM
    speed = random.uniform(0, 200)             # Speed in km/h
    throttle = random.uniform(0, 100)          # Throttle position (%)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return [timestamp, rpm, round(speed, 2), round(throttle, 2)]

def log_can_data(file_path='data/sample_log.csv', duration=30):
    """
    Logs simulated CAN data to a CSV file for a specified duration (seconds).
    """
    with open(file_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write CSV header
        writer.writerow(['Timestamp', 'RPM', 'Speed_km_h', 'Throttle_percent'])
        
        start_time = time.time()
        while time.time() - start_time < duration:
            data = generate_mock_can_data()
            writer.writerow(data)
            print(f"Logged: {data}")
            time.sleep(0.1)  # 100 ms interval

if __name__ == '__main__':
    log_can_data()