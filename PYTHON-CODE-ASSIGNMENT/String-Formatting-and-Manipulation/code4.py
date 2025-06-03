def count_text_stats(text):
    lines = text.splitlines()
    words = text.split()
    characters = len(text)
    return {
        'lines': len(lines),
        'words': len(words),
        'characters': characters
    }

text = "Hello world\nThis is Python\nMy name is Anshima\nI love coding"
print("This is out string: \n",text)
print("Count: ",count_text_stats(text))