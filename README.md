# Log-Based Intrusion Detection System

## Overview
This project is a Python-based log analysis tool that detects brute-force attacks and suspicious login activity by analyzing authentication logs.

## Features
- Detects failed login attempts
- Counts attempts per IP address
- Identifies brute-force attacks
- Detects successful login after multiple failures (possible compromise)

## Technologies Used
- Python
- Log Analysis

## How to Run
1. Download the project
2. Open terminal in the project folder
3. Run:
   py log_analyzer.py

## Sample Output
- Flags suspicious IPs
- Detects brute-force attacks
- Identifies potential compromised logins

## Future Scope
- Real-time log monitoring
- SIEM integration
- Alert systems
