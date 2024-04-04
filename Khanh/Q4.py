
def word_statistics(filename):
    words = {}
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
    return words


def find_max_frequency(words):
    max_frequency = 0
    max_word = ''
    for word, frequency in words.items():
        if frequency > max_frequency:
            max_frequency = frequency
            max_word = word
    return max_word, max_frequency


filename = 'twitter_user_preprocessed.txt'
words = word_statistics(filename)
max_word, max_frequency = find_max_frequency(words)
print(f'Most repeated word: "{max_word}" \nFrequency: {max_frequency}'.replace(',', ''))
