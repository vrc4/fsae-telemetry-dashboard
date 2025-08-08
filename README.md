# 🏎️ Racing Telemetry Dashboard

A real-time racing telemetry dashboard built with **Python**, **Streamlit**, and **Plotly**. This project simulates and visualizes CAN-based vehicle data (RPM, speed, throttle, brake pressure, GPS, etc.), inspired by professional GT/endurance racing tools. It supports both live data streaming and CSV log playback.

---

## 📸 Demo

![Dashboard Screenshot](assets/output.gif)  
_Real-time telemetry with simulated racing data_

---

## 🚀 Features

- 📊 **Live updating graphs**: RPM, Speed, Throttle, Brake Pressure
- 🗺️ **GPS-based track map** with moving vehicle dot
- ⏱️ **Lap & sector timers** (simulated)
- ⚙️ **Data simulation** (no hardware required)
- 🗄️ **CSV log playback** and logging utilities
- 🧩 **Modular structure** for future CAN hardware integration

---

## 🛠️ Tech Stack

| Component        | Tech Used                                                                |
| ---------------- | ------------------------------------------------------------------------ |
| Frontend         | [Streamlit](https://streamlit.io) + [Plotly](https://plotly.com/python/) |
| Backend          | Python (data simulation & logic)                                         |
| Data Logging     | CSV, Python scripts                                                      |
| Deployment-ready | Yes (Streamlit sharing, local server, or Docker)                         |

---

## 🧪 Prerequisites

- Python 3.8+
- pip or virtualenv (recommended)
- Git

---

## ⚙️ Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/fsae-telemetry-dashboard.git
cd fsae-telemetry-dashboard
```

### 2. Create & activate a virtual environment

**POSIX:**

```sh
python3 -m venv fsae-dashboard-env
source fsae-dashboard-env/bin/activate
```

**Windows (PowerShell):**

```sh
python -m venv fsae-dashboard-env
.\fsae-dashboard-env\Scripts\Activate.ps1
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

Or run the helper script:

```sh
bash install_prerequisites.sh
```

---

## ▶️ Usage

### Simulate and log CAN data

Generate a sample log:

```sh
python logger/can_logger.py
```

This writes simulated CAN data to `data/sample_log.csv`.

### Start the live data server

In a terminal:

```sh
python data/Live-data/data_server.py
```

This starts a TCP server streaming mock telemetry.

### Run the dashboard

In another terminal (with the virtual environment activated):

```sh
streamlit run dashboard/app.py
```

The dashboard will connect to the live data server and display real-time telemetry.

---

## 📂 Project Structure

```
├── assets/                # Images, demo GIFs, etc.
├── dashboard/             # Streamlit dashboard app
│   └── app.py
├── data/
│   ├── can_telemetry.csv  # Example CAN data
│   ├── sample_log.csv     # Simulated log output
│   ├── track_map.json     # Track map data
│   └── Live-data/
│       └── data_server.py # Live data TCP server
│   └── Logged-data/       # Example logged data
├── logger/
│   ├── can_logger.py      # CAN data logger (simulated)
│   └── mock_data.py       # Mock data utilities
├── utils/                 # Configs and parsers
│   ├── config.py
│   └── parser.py
├── tests/                 # Unit tests
│   └── test_logger.py
├── requirements.txt
├── install_prerequisites.sh
├── run.sh
├── README.md
```

---

## 🧩 Extending

- Add real CAN hardware support by replacing the mock data generator in [`data/Live-data/data_server.py`](data/Live-data/data_server.py).
- Add new data channels or visualizations by editing [`dashboard/app.py`](dashboard/app.py).
- Use [`utils/parser.py`](utils/parser.py) for custom CSV or CAN log parsing.

---

## 🧪 Testing

Run unit tests:

```sh
python -m unittest discover tests
```

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- Inspired by professional motorsport telemetry tools.
- Built with [Streamlit](https://streamlit.io), [Plotly](https://plotly.com/python/), and [python-can](https://python-can.readthedocs.io/)
