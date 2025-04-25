# 🕵️‍♂️ Network Spy Dashboard

> Real-time network monitoring, port scanning, speed testing, and system stats – all in one powerful Python GUI.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=blue)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## ✨ Features


&nbsp;🔍 Open Ports       → Shows open/listening ports using netstat
&nbsp;🌐 Connected IPs    → Lists active external IPs with geolocation (IP-API)
&nbsp;📶 WiFi / MAC Info  → Displays adapter configuration via ipconfig
&nbsp;⚡ Speed Test        → Measures internet speed using speedtest-cli
&nbsp;🧠 System Usage      → Live CPU, RAM, Upload/Download bandwidth
&nbsp;🔎 Net Processes     → Shows top processes using network resources
&nbsp;📝 Start Logger      → Background logger for all features every 60 seconds
&nbsp;ℹ️ Info              → Built-in help guide for all buttons
&nbsp;📸 Interface Preview
&nbsp;Simple, terminal-style dashboard built with tkinter.


Dashboard	Geolocated IPs
📦 Auto Dependency Installer
No manual pip installing needed! On launch, the app will auto-install:

python
Copy
Edit
required = ['psutil', 'requests', 'speedtest-cli']
🧪 Requirements
Python 3.8+

Windows OS

Internet access (for speed test + IP geolocation)

🚀 Getting Started
bash
Copy
Edit
# 1. Clone the repo
git clone https://github.com/yourusername/network-spy-dashboard.git
cd network-spy-dashboard

# 2. Run the app
python network_spy_dashboard.py
📝 Logs are saved in the /logs folder with timestamped filenames.

📁 Log Samples
Copy
Edit
📂 logs/
 ┣ 📄 netstat_2025-04-25_14-03-23.txt
 ┣ 📄 connected_ips_2025-04-25_14-04-01.txt
 ┣ 📄 wifi_info_2025-04-25_14-05-16.txt
 ┣ 📄 speedtest_2025-04-25_14-06-00.txt
 ┗ 📄 sys_monitor_2025-04-25_14-06-59.txt
⚠️ Disclaimer
This tool is for educational and diagnostic use only. Do not use it for unauthorized network surveillance.

🧀 Author
CheezzyBoii
🐙 GitHub
☕ If this helped you out, star the repo and share it!
