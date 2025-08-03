# 🏎️ Racing Telemetry Dashboard

A real-time racing telemetry dashboard built using **Python**, **Streamlit**, and **Plotly** to simulate and visualize CAN-based vehicle data such as RPM, speed, throttle, brake pressure, and GPS track location — inspired by professional tools used in GT and endurance racing.

---

## 📸 Demo

![Dashboard Screenshot](assets/demo.gif)  
*Real-time telemetry with simulated racing data*

---

## 🚀 Features

- 📊 **Live updating graphs**: RPM, Speed, Throttle, Brake Pressure
- 🗺️ **GPS-based track map** with moving vehicle dot
- ⏱️ **Lap & sector timers** (simulated)
- ⚙️ **Data simulation** using Python (no hardware required)
- 📦 Modular structure for future integration with real CAN data

---

## 🛠️ Tech Stack

| Component        | Tech Used          |
|------------------|--------------------|
| Frontend         | [Streamlit](https://streamlit.io) + [Plotly](https://plotly.com/python/) |
| Backend          | Python (data simulation & logic) |
| Visualization    | Line charts, scatter plots, layout grid |
| Deployment-ready | Yes (Streamlit sharing, local server, or Docker) |

---

## 🧪 Prerequisites

- Python 3.8+
- pip or virtualenv (recommended)
- Git

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/telemetry-dashboard.git
cd telemetry-dashboard
