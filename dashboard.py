#!/usr/bin/env python3
"""
Terminal Dashboard
Displays current time, weather, and system info.
"""

import subprocess
import sys
from datetime import datetime
import urllib.request
import urllib.error

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_weather():
    try:
        # Using wttr.in with format=3 for a compact one-line report
        url = "http://wttr.in/?format=3"
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read().decode('utf-8').strip()
    except Exception as e:
        return f"Weather unavailable: {e}"

def get_system_info():
    try:
        # Get load average (Linux/macOS)
        load_avg = subprocess.check_output(['uptime']).decode('utf-8').strip()
        # Extract the load average part
        if 'load average:' in load_avg:
            load_avg = load_avg.split('load average:')[1].strip()
        else:
            load_avg = "Load avg: N/A"
        return load_avg
    except Exception:
        return "Load avg: N/A"

def main():
    print("=" * 50)
    print("Terminal Dashboard")
    print("=" * 50)
    print(f"Time: {get_time()}")
    print(f"Weather: {get_weather()}")
    print(f"System Load: {get_system_info()}")
    print("=" * 50)

if __name__ == "__main__":
    main()
