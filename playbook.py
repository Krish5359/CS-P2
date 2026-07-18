blocked_ips = []

def block_ip(ip):
    if ip not in blocked_ips:
        blocked_ips.append(ip)
        print("ACTION: IP " + ip + " has been BLOCKED successfully!")
    else:
        print("INFO: IP " + ip + " is already blocked!")

def unblock_ip(ip):
    if ip in blocked_ips:
        blocked_ips.remove(ip)
        print("ACTION: IP " + ip + " has been UNBLOCKED!")
    else:
        print("INFO: IP " + ip + " was not in blocked list!")

def show_blocked_ips():
    print("CURRENTLY BLOCKED IPS:")
    if len(blocked_ips) == 0:
        print("No IPs blocked yet!")
    else:
        for ip in blocked_ips:
            print("- " + ip)

print("PLAYBOOK ACTIONS:")
block_ip("192.168.1.100")
block_ip("172.16.0.200")
block_ip("10.0.0.55")
block_ip("192.168.1.100")
show_blocked_ips()

contained_hosts = []

def isolate_host(host):
    if host not in contained_hosts:
        contained_hosts.append(host)
        print("ACTION: Host " + host + " has been ISOLATED from network!")
    else:
        print("INFO: Host " + host + " is already isolated!")

def run_containment_playbook(ip, host, risk_score):
    print("RUNNING CONTAINMENT PLAYBOOK...")
    print("Threat IP: " + ip)
    print("Affected Host: " + host)
    print("Risk Score: " + str(risk_score))
    print("---")
    block_ip(ip)
    isolate_host(host)
    print("CONTAINMENT COMPLETE!")
    print("Time to contain: under 5 seconds!")

print("CONTAINMENT PLAYBOOK:")
run_containment_playbook("192.168.1.100", "HOST-001", 90)
run_containment_playbook("172.16.0.200", "HOST-002", 70)
run_containment_playbook("10.0.0.55", "HOST-003", 40)