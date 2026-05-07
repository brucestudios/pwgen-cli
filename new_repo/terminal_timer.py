#!/usr/bin/env python3
"""
terminal_timer.py - A simple cross-terminal timer with popup notification.

Usage:
    python3 terminal_timer.py 10s
    python3 terminal_timer.py 5m
    python3 terminal_timer.py 1h
    python3 terminal_timer.py 1h30m10s

The timer waits for the specified duration and then shows a popup notification.
"""

import sys
import time
import re
import tkinter as tk
from tkinter import messagebox

def parse_time_string(time_str):
    """Parse a time string like '10s', '5m', '1h', '1h30m10s' into seconds."""
    # Regular expression to match numbers followed by unit (s, m, h)
    pattern = r'(\d+)(s|m|h)'
    matches = re.findall(pattern, time_str.lower())
    if not matches:
        raise ValueError("Invalid time format. Use format like 10s, 5m, 1h, or combine: 1h30m10s")
    
    total_seconds = 0
    for value, unit in matches:
        value = int(value)
        if unit == 's':
            total_seconds += value
        elif unit == 'm':
            total_seconds += value * 60
        elif unit == 'h':
            total_seconds += value * 3600
    return total_seconds

def show_popup(message):
    """Show a popup notification using tkinter."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Timer Finished", message)
    root.destroy()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    time_str = sys.argv[1]
    try:
        seconds = parse_time_string(time_str)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    print(f"Timer set for {time_str} ({seconds} seconds).")
    time.sleep(seconds)
    
    # Show popup when time is up
    show_popup(f"Time's up! {time_str} has elapsed.")

if __name__ == "__main__":
    main()