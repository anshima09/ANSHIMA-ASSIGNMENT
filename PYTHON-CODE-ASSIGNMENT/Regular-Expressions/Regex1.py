import re

text = "Reach out to us at anshima@example.com and anshima@company.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("Emails:", emails)
