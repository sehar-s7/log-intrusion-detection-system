log_file = "auth.log"

with open(log_file, "r") as file:
    lines = file.readlines()

failed_attempts = {}
successful_logins = []

for line in lines:
    parts = line.split()

    # Detect failed attempts
    if "Failed password" in line:
        ip = parts[-3]

        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

    # Detect successful login
    if "Accepted password" in line:
        ip = parts[-3]
        successful_logins.append(ip)

# Print brute force alerts
print("---- Analysis Report ----")

for ip, count in failed_attempts.items():
    if count > 5:
        print(" ALERT:", ip, "has", count, "failed login attempts (Brute Force)")

# Detect success after failures
for ip in successful_logins:
    if ip in failed_attempts and failed_attempts[ip] > 3:
        print(" WARNING:", ip, "logged in after multiple failed attempts (Possible Compromise)")