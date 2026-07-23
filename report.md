# SOAR Incident Containment Engine - Final Report
Internship Project - CS Infotact Solutions
Made by: Krish Kanani

## Project Overview
A Security Orchestration, Automation and Response (SOAR) 
engine that automatically detects, analyses and contains 
security threats without human intervention.

## Problem Statement
SOC analysts are overwhelmed with alerts from SIEM systems.
Manual threat response takes too long, allowing attackers 
to move through the network undetected.

## Solution
We built an automated SOAR engine that:
- Receives and parses security alerts automatically
- Checks IP reputation and geolocation
- Calculates risk scores for each threat
- Automatically blocks malicious IPs
- Isolates compromised hosts
- Logs all actions in a dashboard
- Manages cases with role based access control

## Project Files
- soar_engine.py - Alert ingestion and parsing
- threat_check.py - IP reputation and risk scoring
- playbook.py - Automated threat response
- dashboard.py - Case management and RBAC
- report.md - Final report

## Week 1 - Completed
- Built alert ingestion system
- Added simulated SIEM alerts
- Added severity level checker
- Added IP address extractor
- Added alert logging system
- Added alert summary report

## Week 2 - Completed
- Created IP reputation checker
- Added IP geolocation lookup
- Added risk score calculator

## Week 3 - Completed
- Created automated playbook
- Added IP blocking system
- Added auto response based on risk score
- Added host isolation and containment

## Week 4 - Completed
- Created incident dashboard
- Added case management system
- Added role based access control
- Added final report

## Technologies Used
- Python
- JSON
- Logging
- Datetime

## HIPAA and Security Compliance
- No real IP addresses or sensitive data used
- All test data is simulated
- Passwords stored in dictionary only for demo purposes

## Key Achievements
- Alert to containment in under 5 seconds
- Automatic IP blocking and host isolation
- Role based access for senior analysts
- Full case management timeline

## Future Improvements
- Connect to real SIEM systems
- Integrate with AbuseIPDB API
- Add email notifications for critical alerts
- Build web dashboard interface
- Add encryption for user passwords

## Made By
Krish Kanani
Internship Project - CS Infotact Solutions 2026