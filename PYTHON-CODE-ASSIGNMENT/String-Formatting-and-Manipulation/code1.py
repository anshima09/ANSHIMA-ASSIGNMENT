def capitalize_words(text):
    words = text.split()
    capitalized = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized)

s = "hello world from python"
print("Original String: ",s)
print("Capitalized String: ",capitalize_words(s)) 