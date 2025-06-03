import re
text = "Password@123, simplepass, Helloanshima!, Admin123#"
passwords = re.findall(r'\b(?=.*\d)(?=.*[!@#$%^&*])(?=\S{8,})\S+\b', text)
print("Valid Passwords:", passwords)
