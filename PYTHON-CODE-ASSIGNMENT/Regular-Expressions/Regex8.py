import re
text = "Valid: 192.168.1.1, 8.8.8.8 | Invalid: 256.300.8.1"
ip_matches = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
valid_ips = [ip for ip in ip_matches if all(0 <= int(part) <= 255 for part in ip.split('.'))]
print("Valid IPv4 Addresses:", valid_ips)
