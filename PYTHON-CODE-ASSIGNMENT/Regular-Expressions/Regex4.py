import re
text = "My name is Anshima Sharma and I live in Dewas and currently pursuing Masters degree."
capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
print("Capitalized Words:", capital_words)
