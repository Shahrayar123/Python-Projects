import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import requests
import json
import socket
import os
import re
import datetime

# Regular expression to validate IP address
ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

class NetworkingTools:
    def __init__(self, master):
        self.master = master
        self.master.title("Basic Networking Tools")

        # Create UI elements
        self.label = tk.Label(master, text="Enter IP address or Domain:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=30)
        self.entry.pack(pady=10)

        self.ip_button = tk.Button(master, text="Locate IP", command=self.locate_ip)
        self.ip_button.pack(pady=5)

        self.domain_button = tk.Button(master, text="Get IP from Domain", command=self.get_ip)
        self.domain_button.pack(pady=5)

        self.ping_button = tk.Button(master, text="Ping", command=self.ping)
        self.ping_button.pack(pady=5)

        self.port_button = tk.Button(master, text="Scan Ports", command=self.port_scanner)
        self.port_button.pack(pady=5)

        self.history_button = tk.Button(master, text="View History", command=self.view_history)
        self.history_button.pack(pady=5)

        self.output_area = scrolledtext.ScrolledText(master, width=50, height=10)
        self.output_area.pack(pady=10)

        self.history = []

        # Ensure the log file exists
        self.log_file = "networking_tools_log.txt"
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("Log of Networking Tools\n")
                f.write("="*30 + "\n")

    def log_action(self, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write(f"{timestamp} - {action}\n")

    def locate_ip(self):
        ip_address = self.entry.get()
        if not re.match(ip_pattern, ip_address):
            messagebox.showerror("Error", "Invalid IP address")
            return

        fields = "status,message,continent,country,region,city,zip,lat,lon,isp"
        url = f"http://ip-api.com/json/{ip_address}?fields={fields}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.output_area.insert(tk.END, json.dumps(data, indent=4) + "\n")
            self.history.append(f"Locate IP: {ip_address} - {data}")
            self.log_action(f"Locate IP: {ip_address} - {data}")
        else:
            messagebox.showerror("Error", "Failed to get data")

    def get_ip(self):
        domain_name = self.entry.get()
        if not domain_name:
            messagebox.showerror("Error", "Domain name cannot be empty")
            return

        command = f"nslookup {domain_name}"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        self.output_area.insert(tk.END, result.stdout + "\n")
        self.history.append(f"Get IP: {domain_name} - {result.stdout}")
        self.log_action(f"Get IP: {domain_name} - {result.stdout}")

    def ping(self):
        host = self.entry.get()
        if not host:
            messagebox.showerror("Error", "IP address or domain cannot be empty")
            return

        parameter = "-n" if os.name == "nt" else "-c"
        command = f"ping {parameter} 5 {host}"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        self.output_area.insert(tk.END, result.stdout + "\n")
        self.history.append(f"Ping: {host} - {result.stdout}")
        self.log_action(f"Ping: {host} - {result.stdout}")

    def port_scanner(self):
        host = self.entry.get()
        if not host or not re.match(ip_pattern, host):
            messagebox.showerror("Error", "Invalid IP address")
            return

        port_range = tk.simpledialog.askstring("Port Range", "Enter port range (e.g., 20-80):")
        if not port_range:
            return

        start_port, end_port = map(int, port_range.split('-'))
        host_ip = socket.gethostbyname(host)

        self.output_area.insert(tk.END, f"Scanning ports on {host_ip} from {start_port} to {end_port}\n")
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host_ip, port))
                if result == 0:
                    self.output_area.insert(tk.END, f"Port {port} is open\n")
                    self.history.append(f"Port Scanner: {host_ip}:{port} - Open")
                    self.log_action(f"Port Scanner: {host_ip}:{port} - Open")

    def view_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("History")
        history_area = scrolledtext.ScrolledText(history_window, width=60, height=20)
        history_area.pack(pady=10)

        for entry in self.history:
            history_area.insert(tk.END, entry + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    tools = NetworkingTools(root)
    root.mainloop()
