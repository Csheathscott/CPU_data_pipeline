# CPU_data_pipeline
First project related to building pipelines as a data engineer

## Overview
This project monitors CPU usage data from your laptop every second and saves it to a CSV file for analysis.

## Features
- Collects CPU usage percentage every second
- Monitors per-core CPU usage
- Tracks CPU frequency (current, min, max)
- Saves data to CSV file with timestamps
- Displays real-time monitoring in console

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Csheathscott/CPU_data_pipeline.git
cd CPU_data_pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run continuous monitoring (Press Ctrl+C to stop):
```bash
python cpu_monitor.py
```

### Run monitoring for a specific duration (e.g., 60 seconds):
```bash
python cpu_monitor.py -d 60
```

### Save to a custom output file:
```bash
python cpu_monitor.py -o my_cpu_data.csv
```

### Help:
```bash
python cpu_monitor.py --help
```

## Output

The script generates a CSV file (`cpu_data.csv` by default) with the following columns:
- `timestamp`: Date and time of measurement
- `cpu_percent`: Overall CPU usage percentage
- `cpu_count`: Number of CPU cores
- `cpu_freq_current`: Current CPU frequency (MHz)
- `cpu_freq_min`: Minimum CPU frequency (MHz)
- `cpu_freq_max`: Maximum CPU frequency (MHz)
- `cpu_core_X_percent`: CPU usage per core

## Example Console Output
```
Starting CPU monitoring... (Press Ctrl+C to stop)
Data will be saved to: cpu_data.csv
[1] 2025-10-28 05:53:45 - CPU: 15.2%
[2] 2025-10-28 05:53:46 - CPU: 18.7%
[3] 2025-10-28 05:53:47 - CPU: 12.3%
...
```
