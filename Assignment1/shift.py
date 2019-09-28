from Assignment1.frequencies import show_plain_text_fequency_histogram, show_english_frequency_histogram

plain_text = "JOVJVSHAL DHZ PUCLUALK MVBY AOVBZHUK FLHYZ HNV PU H ZTHSS CPSSHNL PU OVUKBYHZ HUK OHZ AOYPCLK LCLY ZPUJL".lower()
shift_amount = 7
deciphered = ""

for c in plain_text:
    if c == " ":
        deciphered += c
    else:
        pos = (ord(c) - 97) - shift_amount

        if pos < 0:
            deciphered += chr(26 + pos + 97)
        else:
            deciphered += chr(pos + 97)


show_plain_text_fequency_histogram(plain_text)
print(deciphered.upper())