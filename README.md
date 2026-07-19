# Project 3 - SOAR Incident Containment Engine
Internship Project - CS Infotact Solutions

## Project Overview
A Security Orchestration, Automation and Response (SOAR) engine
that automatically detects, analyses and contains security threats
without any human intervention.

## Problem Statement
Security Operations Center (SOC) analysts are overwhelmed with
alerts from SIEM systems. Manual threat response takes too long,
allowing attackers to move through the network undetected.

## Solution
We built an automated SOAR engine that:
- Receives and parses security alerts automatically
- Checks IP reputation and geolocation
- Calculates risk scores for each threat
- Automatically blocks malicious IPs
- Isolates compromised hosts
- Logs all actions in a dashboard

## Project Files
- soar_engine.py - Main alert ingestion and parsing system
- threat_check.py - IP reputation and risk score checker
- playbook.py - Automated threat response and containment
- dashboard.py - Incident timeline and action logger
- README.md - Project documentation

## Week 1 - Completed
- Built alert ingestion system
- Added simulated SIEM alerts
- Added severity level checker
- Added IP address extractor
- Added alert logging system
- Added alert summary report

## Week 2 - Completed
- Created threat intelligence checker
- Added IP reputation system
- Added IP geolocation lookup
- Added risk score calculator

## Week 3 - Completed
- Created automated playbook system
- Added IP blocking and unblocking
- Added auto response based on risk score
- Added host isolation and containment

## Week 4 - In Progress
- Created incident dashboard
- Adding case management system
- Adding final report

## Technologies Used
- Python
- JSON
- Logging
- Datetime

## Made By
Krish Kanani
Internship Project - CS Infotact Solutions