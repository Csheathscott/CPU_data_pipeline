#!/usr/bin/env python3
"""
CPU Data Monitor
Collects CPU usage data from the laptop every second.
"""

import psutil
import time
import csv
from datetime import datetime
import os


def get_cpu_data():
    """
    Collect CPU usage data.
    
    Returns:
        dict: Dictionary containing CPU metrics
    """
    cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
    cpu_percent_per_core = psutil.cpu_percent(interval=0, percpu=True)
    cpu_freq = psutil.cpu_freq()
    cpu_count = psutil.cpu_count()
    
    data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cpu_percent': cpu_percent,
        'cpu_count': cpu_count,
        'cpu_freq_current': cpu_freq.current if cpu_freq else None,
        'cpu_freq_min': cpu_freq.min if cpu_freq else None,
        'cpu_freq_max': cpu_freq.max if cpu_freq else None,
    }
    
    # Add per-core CPU percentages
    for i, percent in enumerate(cpu_percent_per_core):
        data[f'cpu_core_{i}_percent'] = percent
    
    return data


def save_to_csv(data, filename='cpu_data.csv'):
    """
    Save CPU data to a CSV file.
    
    Args:
        data (dict): CPU data dictionary
        filename (str): Output CSV filename
    """
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)


def monitor_cpu(duration=None, output_file='cpu_data.csv'):
    """
    Monitor CPU usage continuously every second.
    
    Args:
        duration (int, optional): Duration in seconds to monitor. If None, runs indefinitely.
        output_file (str): Output CSV filename
    """
    print(f"Starting CPU monitoring... (Press Ctrl+C to stop)")
    print(f"Data will be saved to: {output_file}")
    
    start_time = time.time()
    iteration = 0
    
    try:
        while True:
            # Collect CPU data
            cpu_data = get_cpu_data()
            
            # Save to CSV
            save_to_csv(cpu_data, output_file)
            
            # Print to console
            iteration += 1
            print(f"[{iteration}] {cpu_data['timestamp']} - CPU: {cpu_data['cpu_percent']}%")
            
            # Check if duration limit reached
            if duration and (time.time() - start_time) >= duration:
                print(f"\nMonitoring completed after {duration} seconds.")
                break
            
            # Wait for the next second (accounting for processing time)
            # Note: get_cpu_data() already waits 1 second internally
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user.")
        print(f"Total samples collected: {iteration}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Monitor CPU usage every second')
    parser.add_argument('-d', '--duration', type=int, default=None,
                        help='Duration in seconds to monitor (default: indefinite)')
    parser.add_argument('-o', '--output', type=str, default='cpu_data.csv',
                        help='Output CSV filename (default: cpu_data.csv)')
    
    args = parser.parse_args()
    
    monitor_cpu(duration=args.duration, output_file=args.output)
