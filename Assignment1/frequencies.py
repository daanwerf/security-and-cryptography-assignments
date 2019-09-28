import operator
import matplotlib.pyplot as plt


def ngram_frequencies(plainText):
    letter_freq = {}
    bigram_freq = {}
    trigram_freq = {}

    for i in plainText:
        if i in letter_freq:
            letter_freq[i] += 1
        else:
            letter_freq[i] = 1

    sorted_letter_freq = sorted(letter_freq.items(), key=operator.itemgetter(1))

    for i in range(len(plainText) - 1):
        if plainText[i] == " " or plainText[i + 1] == " ":
            continue

        bigram = plainText[i] + plainText[i + 1]
        if bigram in bigram_freq:
            bigram_freq[bigram] += 1
        else:
            bigram_freq[bigram] = 1

    sorted_bigram_freq = sorted(bigram_freq.items(), key=operator.itemgetter(1))

    for i in range(len(plainText) - 2):
        if plainText[i] == " " or plainText[i + 1] == " " or plainText[i + 2] == " ":
            continue

        trigram = plainText[i] + plainText[i + 1] + plainText[i + 2]
        if trigram in trigram_freq:
            trigram_freq[trigram] += 1
        else:
            trigram_freq[trigram] = 1

    sorted_trigram_freq = sorted(trigram_freq.items(), key=operator.itemgetter(1))

    return sorted_letter_freq, sorted_bigram_freq, sorted_trigram_freq


def show_english_frequency_histogram():
    alphabet_freq = {
        'a': 8.12,
        'b': 1.49,
        'c': 2.71,
        'd': 4.31,
        'e': 12.02,
        'f': 2.30,
        'g': 2.03,
        'h': 5.92,
        'i': 7.31,
        'j': 0.10,
        'k': 0.69,
        'l': 3.98,
        'm': 2.61,
        'n': 0,
        'o': 7.68,
        'p': 1.82,
        'q': 0.11,
        'r': 6.02,
        's': 6.28,
        't': 9.10,
        'u': 2.88,
        'v': 1.11,
        'w': 2.09,
        'x': 0.17,
        'y': 2.11,
        'z': 0.07
    }

    plt.bar(list(alphabet_freq.keys()), alphabet_freq.values(), color='g')
    plt.show()


def show_plain_text_fequency_histogram(plainText):
    plaintext_freq = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    replace_symbols = [".", "-", " ", ",", "(", ")", "’", ";", "!", ":"]
    for s in replace_symbols:
        plainText = plainText.replace(s, "")

    for letter in plainText:
        plaintext_freq[letter] += 1

    for key in plaintext_freq.keys():
        plaintext_freq[key] = plaintext_freq[key] / len(plainText)

    plt.bar(list(plaintext_freq.keys()), plaintext_freq.values(), color='g')
    plt.show()
