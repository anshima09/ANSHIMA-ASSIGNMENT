import re
# Extracting valid phone numbers from a string
text = "Valid: 123-456-7890, Invalid: 1234567890"
phones = re.findall(r'\b\d{3}-\d{3}-\d{4}\b', text)
print("Valid Phone Numbers:", phones)
