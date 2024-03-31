"""
This module contains tools such as IP Locator, IP Finder,
Pinging and Port Scanner.
DISCLAIMER: Please consider using Port Scanner in educational purposes only.


## TOOLS DESCRIPTION
### IP Locater
Takes the IP address and with the help of an [API](https://ip-api.com/), extracts data about the IP address.
Then writes the extracted data in two different files with the same name "ip_data". One of the files is a JSON file. The other one is 
a text file. These files will be saved on the system's desktop.

### IP Finder
Takes the domain name and extracts the IPs that are relevant with the domain name.
It uses windows `nslookup` command to get IPs.

### Pinging
Takes the domain name or IP address and then pings it.
It uses `ping` command to ping the domain name or IP address.

### Port Scanner
Takes the domain name or IP address. After that, it gets the range of the ports to scan.
Then it starts scanning to look for open ports. The Port Scanner will only look for open ports.
So if a port is not open, it will not show it on the screen.
"""


# Import necessary modules
import subprocess
import platform
import requests
import pyfiglet
import datetime
import socket
import json
import os
import re


# Make the foreground color of the terminal green.
subprocess.call("color A", shell=True)

# A pattern to validate an IP address.
ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"


# Tools
def locate_ip():
    """
    Locate an IP address using an API.
    """
    # Clear up the terminal.
    subprocess.call("cls", shell=True)
    # Banner of the tool.
    banner = pyfiglet.figlet_format("IP LOCATER")
    print(banner)
    # Get the IP address. Check the input whether it is a valid IP address.
    # This while loop will run until it gets a valid IP address that matches the IP pattern.
    while True:
        IP_address = input("\nEnter a valid IP address: ")
        # Check if the given input whether it is 'q'.
        # If it is, then it will abort operation and quit program.
        if IP_address.lower() == 'q':
            quit()
        # Validating the given IP address.
        if not re.match(ip_pattern, IP_address):
            print("Invalid IP address")
            continue
        else:
            break
    # Change current working directory to system's desktop
    os.chdir(rf"C:\Users\{os.getlogin()}\Desktop")
    # File names containing data of the IP address.
    file_name_json = "ip_data.json"
    file_name_text = "ip_data.txt"
    # The files containing IP data will have these fields.
    fields = "status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,mobile,proxy,hosting,query"
    # Sending a request to extract data.
    url = f"http://ip-api.com/json/{IP_address}?fields={fields}"
    response = requests.get(url)
    # Write the extracted data in the files.
    # Write on both JSON file and text file.
    with open(file_name_json, 'w') as ip_data_file_json:
        json.dump(response.json(), ip_data_file_json, indent=4)
    with open(file_name_text, 'w') as ip_data_file_text:
        ip_data_file_text.write(response.text)
    # Let the user know that files created on the system's desktop.
    print("You got the files containing data about the given IP address.")
    print("Please check your system desktop.")
    input("\nPress any key to continue...")


def get_ip():
    """
    Get the IP address of a certain domain name.
    """
    subprocess.call("cls", shell=True)
    # Banner of the tool.
    banner = pyfiglet.figlet_format("IP FINDER")
    print(banner)
    # Get the domain name.
    # Check if the given input whether it is 'q'.
    # If it is, then it will abort operation and quit program.
    domain_name = input("\nEnter a valid domain name: ")
    if domain_name.lower() == 'q':
        quit()
    # Get the IP of the domain name.
    command = f"nslookup {domain_name}"
    subprocess.call(command) == 0
    input("\nPress any key to continue...")


def ping():
    """
    Ping a domain or website or IP address.
    """
    subprocess.call("cls", shell=True)
    # Banner of the tool.
    banner = pyfiglet.figlet_format("PING")
    print(banner)
    # Get the host to ping.
    # Host can be a domain name or an IP address.
    # Check the given input whether it is 'q'.
    # If it is, then abort operation and quit program.
    host = input("Enter a valid domain name or IP address: ")
    if host.lower() == 'q':
        quit()
    # If the os is Windows, then the parameter is "-n".
    # If not, the parameter is "-c"
    if platform.system().lower() == "windows":
        parameter = "-n"
    else:
        parameter = "-c"
    # It will send 5 packages to ping the host.
    command = f"ping {parameter} 5 {host}"
    subprocess.call(command) == 0
    input("\nPress any key to continue...")


def port_scanner():
    """
    Scan ports on a certain host.
    """
    subprocess.call("cls", shell=True)
    # Banner of the tool.
    banner = pyfiglet.figlet_format("PORT SCANNER")
    print(banner)
    print("For scanning using a domain, enter <domain>.\nFor scanning using an IP, enter <ip>")
    # All this terrifying while loop does is to check the given input at "scan_type".
    # If it is "q", then it will abort operation and quit program.
    # If it is "ip", then it will validate the IP address. If it is valid, then it will break the loop.
    # If it is "domain", then it will get the domain name and break the loop.
    # If it is none of the above, it will let the user know that the input is not valid.
    while True:
        scan_type = input(">>> ")
        if scan_type.lower() == 'q':
            quit()
        if scan_type.lower() == 'ip':
            while True:
                host = input("Enter IP for scanning:\n>>> ")
                if host.lower() == 'q':
                    quit()
                if not re.match(ip_pattern, host):
                    print("Invalid IP address.\n")
                    continue
                else:
                    break
            break
        elif scan_type.lower() == 'domain':
            host = input("Enter domain for scanning:\n>>> ")
            if host.lower() == 'q':
                quit()
            break
        else:
            print("Invalid input.\n")
            continue
    # Get the IP address of the domain name if a domain name is given.
    hostIP = socket.gethostbyname(host)
    # Get the port range.
    port_range = input("Enter port range in format <start>-<end> (ex: 20-80):\n>>> ")
    # Split the starting port and the ending port.
    port_range = port_range.split("-")
    # Make a neat banner again containing IP address and the time that scanning started.
    print("_"*60)
    print("Scanning ports on host: ", hostIP)
    start_time = datetime.datetime.now()
    print("Scan started at ", start_time)
    print("_"*60)
    print("\nPort\t\t\tStatus\n")
    # Start scanning ports
    for port in range(int(port_range[0]), int(port_range[1])+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Timeout time for scanning each port is half a second.
        s.settimeout(0.5)
        connection = s.connect_ex((hostIP, port))
        # Check whether the port is open or not.
        # If it is open, print it.
        # If it is not open, pass the closed port.
        if connection == 0:
            print(f"{port}\t----------\tOpen")
        else:
            pass
        s.close()
    # Scan ending time.
    end_time = datetime.datetime.now()
    # Time taken to scan.
    time_taken = end_time - start_time
    # Make a neat banner again containing the time that scanning ended and the time taken to scan.
    print("_"*60)
    print("Scan ended at ", end_time)
    print("Time taken: ", time_taken)
    print("_"*60)
    input("\nPress any key to continue...")
