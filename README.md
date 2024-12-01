# HealthCheckCLI

HealthCheckCLI is a lightweight command-line tool for automating health checks of web servers. It checks the availability and performance of web services by monitoring HTTP response codes, measuring latency, and logging results. This tool is particularly useful for developers and SREs to ensure reliable uptime and track service performance.

## Features

- **Server Uptime Monitoring**: Periodically checks the status of specified URLs and reports response codes and latency.
- **Custom Configuration**: Allows users to specify URLs, check intervals, and thresholds via a configuration file.
- **Logging**: Logs results to a local file for analysis and tracking over time.
- **Simple Command-Line Interface**: Easy to set up and use with intuitive commands.
- **Extensible**: Built for flexibility, enabling future additions like alerts and visualizations.

## Tech Stack

- **Programming Language**: Python
- **Libraries**:
  - `requests` for HTTP checks
  - `click` for CLI functionality
  - `json` for configuration and logging

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HealthCheckCLI.git
   cd HealthCheckCLI
2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

