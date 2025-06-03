import re
text = "Today's date is 03-06-2025 and tomorrow is 04-06-2025"
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Dates:", dates)
