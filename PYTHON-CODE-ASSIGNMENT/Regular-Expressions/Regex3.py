import re
text = "Example String #Python #Devlopment #Anshima #NuleusTeq"
hashtags = re.findall(r'#\w+', text)
print("Hashtags:", hashtags)
