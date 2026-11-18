# LoginGuard - Brute Force Detector

Detects brute force login attacks by analyzing failed login attempts per IP address.

## The Problem: Brute Force Attacks

Attackers try thousands of passwords against one account to break in. A SOC analyst can't manually check every failed login — there are too many.

LoginGuard automates this detection.

## How It Works

1.  **Collect Logs:** Reads login attempts (IP + SUCCESS / FAILED)
2.  **Count Failures:** Counts failed logins for each IP
3.  **Detect & Classify:**
    *   `5+ Failed` = **BLOCK** - Brute Force Attack
    *   `3-4 Failed` = **WATCH** - Suspicious
    *   `1-2 Failed` = **OK** - Normal user typo

## Demo Output

```text
LoginGuard - Brute Force Detector

[+] Analyzed 14 login attempts
[+] Found 3 IPs with failed logins

DETECTION RESULTS:

🚨 BLOCK | 192.168.1.50 | Failed: 6 | BRUTE FORCE ATTACK
✅ OK    | 10.0.0.15 | Failed: 1 | Normal
🚨 BLOCK | 172.16.0.9 | Failed: 5 | BRUTE FORCE ATTACK


[+] Total IPs to BLOCK: 2
[+] Recommendation: Block these IPs in firewall immediately.
