import re
query = "name=Anshima & age=21 & city=Dewas & country=India"
kv_pairs = dict(re.findall(r'(\w+)=([\w%]+)', query))
print("Key-Value Pairs:", kv_pairs)
