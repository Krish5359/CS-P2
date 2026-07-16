import json
import datetime

def parse_alert(alert):
    ip = alert.get("ip_address", "unknown")
    attack_type = alert.get("attack_type", "unknown")
    timestamp = alert.get("timestamp", str(datetime.datetime.now()))
    severity = alert.get("severity", "low")
    return {
        "ip": ip,
        "attack_type": attack_type,
        "timestamp": timestamp,
        "severity": severity
    }

alert1 = {
    "ip_address": "192.168.1.100",
    "attack_type": "brute_force",
    "timestamp": "2026-07-16 10:30:00",
    "severity": "high"
}

alert2 = {
    "ip_address": "10.0.0.55",
    "attack_type": "malware_detection",
    "timestamp": "2026-07-16 11:00:00",
    "severity": "critical"
}

print("ALERT 1:")
print(parse_alert(alert1))

print("ALERT 2:")
print(parse_alert(alert2))

alert3 = {
    "ip_address": "172.16.0.200",
    "attack_type": "sql_injection",
    "timestamp": "2026-07-16 12:00:00",
    "severity": "critical"
}

alert4 = {
    "ip_address": "192.168.1.105",
    "attack_type": "ddos_attack",
    "timestamp": "2026-07-16 13:00:00",
    "severity": "high"
}

alert5 = {
    "ip_address": "10.0.0.99",
    "attack_type": "phishing",
    "timestamp": "2026-07-16 14:00:00",
    "severity": "medium"
}

print("ALERT 3:")
print(parse_alert(alert3))

print("ALERT 4:")
print(parse_alert(alert4))

print("ALERT 5:")
print(parse_alert(alert5))