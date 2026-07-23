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
cases = []

def create_case(ip, attack_type, severity, action_taken):
    case = {
        "case_id": "CASE-" + str(len(cases) + 1),
        "ip": ip,
        "attack_type": attack_type,
        "severity": severity,
        "action_taken": action_taken,
        "timestamp": str(datetime.datetime.now()),
        "status": "resolved"
    }
    cases.append(case)
    print("Case created: " + case["case_id"])
    return case

def show_cases():
    print("CASE MANAGEMENT DASHBOARD")
    print("=========================")
    print("Total Cases: " + str(len(cases)))
    print("=========================")
    for case in cases:
        print("Case ID: " + case["case_id"])
        print("IP: " + case["ip"])
        print("Attack: " + case["attack_type"])
        print("Severity: " + case["severity"])
        print("Action: " + case["action_taken"])
        print("Status: " + case["status"])
        print("Time: " + case["timestamp"])
        print("---")

create_case("192.168.1.100", "brute_force", "critical", "IP Blocked")
create_case("172.16.0.200", "sql_injection", "critical", "Host Isolated")
create_case("10.0.0.55", "malware_detection", "high", "IP Blocked")
create_case("198.51.100.25", "ddos_attack", "high", "IP Monitored")

show_cases()

users = {
    "krish": {"role": "analyst", "password": "analyst123"},
    "admin": {"role": "senior_analyst", "password": "admin123"}
}

def login(username, password):
    if username in users:
        if users[username]["password"] == password:
            role = users[username]["role"]
            print("LOGIN SUCCESS: " + username + " logged in as " + role)
            return role
        else:
            print("LOGIN FAILED: Wrong password!")
            return None
    else:
        print("LOGIN FAILED: User not found!")
        return None

def check_permission(role, action):
    permissions = {
        "analyst": ["view_cases", "view_dashboard"],
        "senior_analyst": ["view_cases", "view_dashboard", "approve_playbook", "delete_case"]
    }
    if action in permissions.get(role, []):
        print("PERMISSION GRANTED: " + role + " can " + action)
        return True
    else:
        print("PERMISSION DENIED: " + role + " cannot " + action)
        return False

print("ROLE BASED ACCESS CONTROL:")
role1 = login("krish", "analyst123")
role2 = login("admin", "admin123")
login("hacker", "wrongpass")

print("PERMISSION CHECKS:")
check_permission(role1, "view_dashboard")
check_permission(role1, "approve_playbook")
check_permission(role2, "approve_playbook")
check_permission(role2, "delete_case")