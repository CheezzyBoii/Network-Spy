# 🕵️‍♂️ Network Spy Dashboard

> Real-time network monitoring, port scanning, speed testing, and system stats – all in one powerful Python GUI.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=blue)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## ✨ Features

- 🔍 **Open Ports** → Shows open/listening ports using `netstat`
- 🌐 **Connected IPs** → Lists active external IPs with geolocation via IP-API
- 📶 **WiFi / MAC Info** → Displays adapter configuration using `ipconfig`
- ⚡ **Speed Test** → Measures internet speed with `speedtest-cli`
- 🧠 **System Usage** → Live CPU, RAM, Upload/Download bandwidth monitoring
- 🔎 **Net Processes** → Displays top processes using network resources
- 📝 **Start Logger** → Background logs all stats every 60 seconds
- ℹ️ **Info** → Built-in help guide for all dashboard buttons

---

## 🖥️ Interface Preview

> A simple terminal-style dashboard built using `tkinter`.

---

## 📦 Auto Dependency Installer

> No manual `pip install` needed!  
On launch, the app automatically installs:

required = ['psutil', 'requests', 'speedtest-cli']
🧪 Requirements
Python 3.8+

Windows OS

Internet access (for speed test & IP geolocation)

🚀 Getting Started
bash
Copy
Edit
# 1. Clone the repo
git clone https://github.com/yourusername/network-spy-dashboard.git
cd network-spy-dashboard

# 2. Run the app
'''bash
python network_spy_dashboard.py
'''
📝 Logs are saved in the `/logs` folder with timestamped filenames.

---

> 📂 **logs/**  
> ┣ 📄 **netstat_2025-04-25_14-03-23.txt**  
> ┣ 📄 **connected_ips_2025-04-25_14-04-01.txt**  
> ┣ 📄 **wifi_info_2025-04-25_14-05-16.txt**  
> ┣ 📄 **speedtest_2025-04-25_14-06-00.txt**  
> ┗ 📄 **sys_monitor_2025-04-25_14-06-59.txt**

---

# ⚠️ Disclaimer
This tool is for educational and diagnostic purposes only.
Do not use it for unauthorized network surveillance.

🧀 Author
CheezzyBoii
🐙 GitHub
☕ If this helped you out, star the repo and share it!

