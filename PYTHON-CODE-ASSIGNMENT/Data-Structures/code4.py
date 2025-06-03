def count_words(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print("Frequencies:", count_words(word_list))