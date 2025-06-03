import re
text = "Hello, world! Let's code in : Python"
tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
print("Tokens:", tokens)
