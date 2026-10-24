# CYBERSEBTINEL-AI
# Basic Cybersecurity Threat Detection

def detect_threat(ip_address, failed_attempts):
    print("\n--- Security Analysis ---")
    print("IP Address:", ip_address)
    print("Failed Login Attempts:", failed_attempts)

    if failed_attempts >= 5:
        print("ALERT: Suspicious activity detected!")
        print("Risk Level: HIGH")
    else:
        print("Status: Normal activity")
        print("Risk Level: LOW")


print("CYBER SENTINEL - AI SECURITY SYSTEM")

detect_threat("192.168.1.10", 2)
detect_threat("192.168.1.25", 7)
