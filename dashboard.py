import datetime

action_log = []

def log_action(ip, action, severity):
    entry = {
        "timestamp": str(datetime.datetime.now()),
        "ip": ip,
        "action": action,
        "severity": severity
    }
    action_log.append(entry)
    print("LOGGED: " + action + " on IP: " + ip)

def show_dashboard():
    print("SOAR INCIDENT DASHBOARD")
    print("=======================")
    print("Total Actions Taken: " + str(len(action_log)))
    print("=======================")
    for entry in action_log:
        print("Time: " + entry["timestamp"])
        print("IP: " + entry["ip"])
        print("Action: " + entry["action"])
        print("Severity: " + entry["severity"])
        print("---")

log_action("192.168.1.100", "IP Blocked", "critical")
log_action("172.16.0.200", "IP Blocked", "high")
log_action("10.0.0.55", "Host Isolated", "critical")
log_action("8.8.8.8", "IP Monitored", "medium")

show_dashboard()