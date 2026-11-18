# LoginGuard - Brute Force Detector
# Detects IPs trying to brute force logins

print("LoginGuard - Brute Force Detector")
print("=" * 40)

# Simulated login logs: (ip, status)
# In real SOC, this would come from a log file
logs = [
    ("192.168.1.50", "FAILED"),
    ("192.168.1.50", "FAILED"),
    ("192.168.1.50", "FAILED"),
    ("192.168.1.50", "FAILED"),
    ("192.168.1.50", "FAILED"),
    ("192.168.1.50", "FAILED"),
    ("10.0.0.15", "FAILED"),
    ("10.0.0.15", "SUCCESS"),
    ("172.16.0.9", "FAILED"),
    ("172.16.0.9", "FAILED"),
    ("172.16.0.9", "FAILED"),
    ("172.16.0.9", "FAILED"),
    ("172.16.0.9", "FAILED"),
    ("8.8.8.8", "SUCCESS"),
]

# Count failed logins per IP
failed_counts = {}
for ip, status in logs:
    if status == "FAILED":
        if ip in failed_counts:
            failed_counts[ip] += 1
        else:
            failed_counts[ip] = 1

print(f"\n[+] Analyzed {len(logs)} login attempts")
print(f"[+] Found {len(failed_counts)} IPs with failed logins\n")

print("DETECTION RESULTS:")
print("-" * 40)

blocked = 0
for ip, count in failed_counts.items():
    if count >= 5:
        print(f"🚨 BLOCK | {ip} | Failed: {count} | BRUTE FORCE ATTACK")
        blocked += 1
    elif count >= 3:
        print(f"⚠️  WATCH | {ip} | Failed: {count} | Suspicious")
    else:
        print(f"✅ OK    | {ip} | Failed: {count} | Normal")

print("-" * 40)
print(f"\n[+] Total IPs to BLOCK: {blocked}")
print("[+] Recommendation: Block these IPs in firewall immediately.")
