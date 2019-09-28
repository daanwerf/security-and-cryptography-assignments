from Assignment1.frequencies import ngram_frequencies

o_alphabet = "abcdefghijklmnopqrstuvwxyz"
c_alphabet = "n-pg--d-irclb-e-y-hamostfu"

cipher = "XSO MJIWXVL JODIVA STW VAO VY OZJVCO’W LTJDOWX KVAKOAXJTXIVAW VY SIDS XOKSAVLVDQ IAGZWXJQ. KVUCZXOJW, KVUUZAIKTXIVAW TAG UIKJVOLOKXJVAIKW TJO HOLL JOCJOWOAXOG, TLVADWIGO GIDIXTL UOGIT, KVUCZXOJ DTUOW TAG OLOKXJVAIK KVUUOJKO.".lower()
decipher = ""

for c in cipher:
    if c in [".", "-", " ", ",", "(", ")", "’"]:
        decipher += c
    else:
        decipher += c_alphabet[o_alphabet.index(c)]


plainText = "XSO MJIWXVL JODIVA STW VAO VY OZJVCO’W LTJDOWX KVAKOAXJTXIVAW VY SIDS XOKSAVLVDQ IAGZWXJQ. KVUCZXOJW, KVUUZAIKTXIVAW TAG UIKJVOLOKXJVAIKW TJO HOLL JOCJOWOAXOG, TLVADWIGO GIDIXTL UOGIT, KVUCZXOJ DTUOW TAG OLOKXJVAIK KVUUOJKO.".lower()
ngram_frequencies(plainText)

print()
print(cipher)
print(decipher)
