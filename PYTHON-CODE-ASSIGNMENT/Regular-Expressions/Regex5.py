import re
text = "It will replace all spaces with -  hyphens"
modified = re.sub(r'\s+', '-', text)
print("Hyphenated Text:", modified)
