# Python DevOps Automation Scripts 

![Python](https://img.shields.io/badge/Python-3.x-blue)
![DevOps](https://img.shields.io/badge/DevOps-Automation-green)
![AWS](https://img.shields.io/badge/AWS-boto3-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

This repository contains **Python scripts used for DevOps automation tasks** such as monitoring servers, analyzing logs, checking disk usage, and interacting with cloud infrastructure.

The goal of this project is to demonstrate **practical DevOps automation using Python**.

---

# Project Structure

```id="pc3xhy"
python-devops-scripts
│
├── server-health-check
│   └── health_check.py
│
├── log-analyzer
│   └── log_analyzer.py
│
├── disk-monitor
│   └── disk_check.py
│
├── docker-check
│   └── docker_status.py
│
└── aws-automation
    └── ec2_list.py
```

---

# Features

* Server health monitoring
* Log file analysis
* Disk usage monitoring
* Docker container checks
* AWS EC2 automation

These scripts simulate **real DevOps tasks used in production environments**.

---

# Scripts Overview

## Server Health Check

This script checks whether servers are reachable using the **ping command**.

Run the script:

```id="mxnvtg"
python3 health_check.py
```

Example output:

```id="yhtup7"
[OK] google.com is reachable
[OK] github.com is reachable
[ERROR] server is unreachable
```

---

## Log File Analyzer

Reads log files and detects **ERROR messages**.

Run:

```id="4mo39q"
python3 log_analyzer.py
```

Example output:

```id="g3w6ci"
[ERROR DETECTED] Database connection failed
[ERROR DETECTED] Timeout occurred

Total Errors Found: 2
```

---

## Disk Usage Monitor

Checks system disk usage and prints a warning when usage exceeds safe limits.

Run:

```id="1tnffo"
python3 disk_check.py
```

---

## Docker Container Status

Runs Docker commands from Python to check container status.

Run:

```id="ehd06k"
python3 docker_status.py
```

---

## AWS EC2 Automation

Uses **AWS boto3 SDK** to interact with EC2 instances.

Install dependency:

```id="z61r4s"
pip3 install boto3
```

Run:

```id="2l04nt"
python3 ec2_list.py
```

---

# Technologies Used

* Python 3
* Linux Commands
* AWS boto3
* Docker
* DevOps Automation

---

# Getting Started

Clone the repository:

```id="o3fwq4"
git clone https://github.com/sebastiantnalu-crypto/python-devops-scripts.git
```

Navigate into the project:

```id="q85j2n"
cd python-devops-scripts
```

Run any script:

```id="nftu9j"
python3 script_name.py
```

---

# Learning Objectives

This project demonstrates:

* Python automation for DevOps
* Infrastructure monitoring scripts
* Log analysis automation
* Cloud automation basics

---

# Future Improvements

* Add Kubernetes monitoring scripts
* Implement Slack alert notifications
* Automate infrastructure deployment
* Integrate CI/CD pipeline automation

---

# Author

**Sebastian Tomichan Naluthengumgal**

Aspiring DevOps / Cloud Engineer

LinkedIn:
https://www.linkedin.com/in/sebastiantomichan/

GitHub:
https://github.com/sebastiantnalu-crypto
