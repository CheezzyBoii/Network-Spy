import subprocess
import sys
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading, time, os, requests
import psutil

# 🔧 Auto-install required libraries
required = ['psutil', 'requests', 'speedtest-cli']
for package in required:
    try:
        __import__(package.replace('-', '_'))
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, encoding='utf-8', stderr=subprocess.STDOUT)
    except Exception as e:
        return f"Error: {str(e)}"

def get_netstat():
    return run_command("netstat -an")

def get_connections():
    connections = psutil.net_connections()
    result = []
    for c in connections:
        if c.raddr:
            ip = c.raddr.ip
            result.append(ip)
    return list(set(result))

def geo_ip(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=2)
        data = res.json()
        return f"{ip} - {data.get('country', '?')} / {data.get('city', '?')}"
    except:
        return f"{ip} - Location Unknown"

def get_wifi_info():
    return run_command("ipconfig /all")

def get_speedtest():
    return run_command("speedtest-cli --simple")

def log_to_file(name, data):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"{LOG_DIR}/{name}_{timestamp}.txt", "w", encoding='utf-8') as f:
        f.write(data)

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "Unknown"

def get_bandwidth():
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()
    upload_speed = (net2.bytes_sent - net1.bytes_sent) / 1024
    download_speed = (net2.bytes_recv - net1.bytes_recv) / 1024
    return round(upload_speed, 2), round(download_speed, 2)

def get_network_processes():
    results = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr and conn.pid:
            try:
                proc = psutil.Process(conn.pid)
                results.append(f"{proc.name()} (PID {conn.pid}) -> {conn.raddr.ip}:{conn.raddr.port}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    return results[:20]

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    upload, download = get_bandwidth()
    return cpu, mem, upload, download

class NetworkSpyApp:
    def __init__(self, root):
        self.root = root
        root.title("🕵️ Network Spy Dashboard")
        root.geometry("980x720")
        root.configure(bg="#0f0f0f")

        self.public_ip = get_public_ip()

        self.title = tk.Label(root, text=f"🕵️ NETWORK SPY DASHBOARD | Public IP: {self.public_ip}", fg="lime", bg="#0f0f0f",
                              font=("Consolas", 14, "bold"))
        self.title.pack(pady=10)

        self.tabs = tk.Frame(root, bg="#0f0f0f")
        self.tabs.pack(fill=tk.X, padx=10)

        self.output = scrolledtext.ScrolledText(root, bg="#111", fg="#00FF00", font=("Courier", 10),
                                                insertbackground="white", borderwidth=0)
        self.output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.bandwidth_label = tk.Label(root, text="", fg="cyan", bg="#0f0f0f", font=("Consolas", 10, "bold"))
        self.bandwidth_label.pack(pady=5)

        buttons = [
            ("🔍 Open Ports", self.show_netstat),
            ("🌐 Connected IPs", self.show_ips),
            ("📶 WiFi / MAC Info", self.show_wifi),
            ("⚡ Speed Test", self.show_speed),
            ("🧠 System Usage", self.show_sys_stats),
            ("🔎 Net Processes", self.show_net_procs),
            ("📝 Start Logger", self.toggle_logger),
            ("ℹ️ Info", self.show_info)
        ]

        for (label, func) in buttons:
            b = tk.Button(self.tabs, text=label, command=func,
                          bg="#222", fg="lime", font=("Consolas", 10, "bold"),
                          activebackground="#333", width=16, relief="flat", padx=5, pady=5)
            b.pack(side=tk.LEFT, padx=4)

        self.logging = False
        self.update_bandwidth()

    def update_bandwidth(self):
        upload, download = get_bandwidth()
        self.bandwidth_label.config(text=f"📡 Upload: {upload} KB/s | ⬇️ Download: {download} KB/s")
        self.root.after(2000, self.update_bandwidth)

    def show_netstat(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "[*] Fetching open ports...\n\n")
        data = get_netstat()
        self.output.insert(tk.END, data)
        log_to_file("netstat", data)

    def show_ips(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "[*] Gathering active connections and geolocation...\n\n")
        ips = get_connections()
        geo_results = [geo_ip(ip) for ip in ips]
        data = "\n".join(geo_results)
        self.output.insert(tk.END, data)
        log_to_file("connected_ips", data)

    def show_wifi(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "[*] Getting WiFi / MAC / DHCP info...\n\n")
        data = get_wifi_info()
        self.output.insert(tk.END, data)
        log_to_file("wifi_info", data)

    def show_speed(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "[*] Running speed test...\n\n")
        self.root.update()
        result = get_speedtest()
        self.output.insert(tk.END, result)
        log_to_file("speedtest", result)

    def show_sys_stats(self):
        self.output.delete("1.0", tk.END)
        cpu, mem, upload, download = get_system_stats()
        data = f"🧠 CPU Usage: {cpu}%\n💾 RAM Usage: {mem}%\n📡 Upload Speed: {upload} KB/s\n⬇️ Download Speed: {download} KB/s"
        self.output.insert(tk.END, data)
        log_to_file("system_stats", data)

    def show_net_procs(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "[*] Active processes using network:\n\n")
        procs = get_network_processes()
        self.output.insert(tk.END, "\n".join(procs))
        log_to_file("net_processes", "\n".join(procs))

    def toggle_logger(self):
        if not self.logging:
            self.logging = True
            threading.Thread(target=self.background_logger, daemon=True).start()
            messagebox.showinfo("Logger", "📝 Background logging started.")
        else:
            self.logging = False
            messagebox.showinfo("Logger", "❌ Background logging stopped.")

    def background_logger(self):
        while self.logging:
            try:
                log_to_file("netstat", get_netstat())
                log_to_file("connected_ips", "\n".join([geo_ip(ip) for ip in get_connections()]))
                log_to_file("wifi_info", get_wifi_info())
                cpu, mem, up, down = get_system_stats()
                log_to_file("sys_monitor", f"CPU: {cpu}% | RAM: {mem}% | Up: {up} KB/s | Down: {down} KB/s")
            except:
                pass
            time.sleep(60)

    def show_info(self):
        info = """
🕵️ DASHBOARD FUNCTION GUIDE:

🔍 Open Ports
• Shows all current open and listening ports via 'netstat -an'.

🌐 Connected IPs
• Lists active outbound connections and shows basic location (country/city) for each IP.

📶 WiFi / MAC Info
• Dumps all IP config details including MAC, DHCP, DNS, and adapter status.

⚡ Speed Test
• Runs an internet speed test using speedtest-cli.
• Includes download & upload speeds.

🧠 System Usage
• Shows CPU, RAM usage, and bandwidth snapshot.

🔎 Net Processes
• Displays active processes using the network and their connections.

📝 Start Logger
• Starts background logging of all above stats every 60 seconds.

ℹ️ Info
• Displays this help guide.
"""
        messagebox.showinfo("🕵️ Network Spy - Help", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSpyApp(root)
    root.mainloop()
