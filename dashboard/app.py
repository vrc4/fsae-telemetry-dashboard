# dashboard/streamlit_socket_dashboard.py
import streamlit as st
import socket
import pandas as pd
import plotly.express as px
from io import StringIO

HOST = 'localhost'
PORT = 9999

st.set_page_config(layout="wide")
st.title("🏁 Real-Time Telemetry Dashboard")

st.markdown("Reading live telemetry from TCP socket...")

# TCP socket connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Live chart update
data_buffer = StringIO()
columns = ['Timestamp', 'RPM', 'Speed_km_h', 'Throttle_percent']
df = pd.DataFrame(columns=columns)

placeholder = st.empty()

while True:
    line = client.recv(1024).decode()
    if not line:
        break

    for row in line.strip().split("\n"):
        ts, rpm, speed, throttle = row.split(",")
        df.loc[len(df)] = [ts, int(rpm), float(speed), float(throttle)]

    with placeholder.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.plotly_chart(px.line(df, x='Timestamp', y='RPM', title='RPM'), use_container_width=True)
        with col2:
            st.plotly_chart(px.line(df, x='Timestamp', y='Speed_km_h', title='Speed (km/h)'), use_container_width=True)
        with col3:
            st.plotly_chart(px.line(df, x='Timestamp', y='Throttle_percent', title='Throttle (%)'), use_container_width=True)