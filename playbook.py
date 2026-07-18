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