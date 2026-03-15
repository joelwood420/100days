def word_frequency(text) -> dict:
    string = text.lower()
    word_freq = {}
    words = string.split()
    for word in words:
        clean_word = ''.join(char for char in word if char.isalpha())
        if clean_word:
            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
    return word_freq


if __name__ == "__main__":
    print(word_frequency(input()))


