suspicious_ips = [
    "192.168.1.100",
    "172.16.0.200",
    "10.0.0.55",
    "203.0.113.50",
    "198.51.100.25"
]

def check_ip_reputation(ip):
    if ip in suspicious_ips:
        print("DANGEROUS IP FOUND: " + ip + " - Risk Score: HIGH")
        return "high"
    else:
        print("CLEAN IP: " + ip + " - Risk Score: LOW")
        return "low"

print("IP REPUTATION CHECK:")
check_ip_reputation("192.168.1.100")
check_ip_reputation("10.0.0.55")
check_ip_reputation("172.16.0.200")
check_ip_reputation("8.8.8.8")
check_ip_reputation("1.1.1.1")
ip_geolocation = {
    "192.168.1.100": "Russia",
    "172.16.0.200": "China",
    "10.0.0.55": "North Korea",
    "203.0.113.50": "Iran",
    "198.51.100.25": "Unknown",
    "8.8.8.8": "United States",
    "1.1.1.1": "Australia"
}

def get_geolocation(ip):
    location = ip_geolocation.get(ip, "Unknown")
    print("IP: " + ip + " is located in: " + location)
    return location

print("GEOLOCATION CHECK:")
get_geolocation("192.168.1.100")
get_geolocation("172.16.0.200")
get_geolocation("10.0.0.55")
get_geolocation("8.8.8.8")
get_geolocation("1.1.1.1")