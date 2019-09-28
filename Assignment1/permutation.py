from Assignment1.frequencies import show_plain_text_fequency_histogram, show_english_frequency_histogram

plain_text = "VCALIUTOTNOCINISOMTUPUNLNCADUTSRLUACEAFAOCEOXEEWRVTENIESOIAMSNEAMWRCEIHHERTEETCRCOAAAETINESEINEHVWNPALIOLETSDHETTEHDFEOOETAACCERNEVEEYTFALULKOIMARSHNEOSDFEAAHRTOTRYWNTEOINCLNHIGNAGHNTGHRMFOTERRETESUEKTNIHLIWTFIHNEHSTEEATHRTATHORYITYFBUTORSRHWIONMRODLEAPNESADHSDEENBAEMDEDBDEIEAWNSOTUICVSWSHUPPLEIBEHLTHEENTASEMSEVSLTATEIRBTEODERUKTAELHAWLIISODHTEITHNWMEHSTEPEMPLTUEABHVYAEEFNHETLIESERTOMNNCETBSYMDUESHCMNUAOADAPCOSSEHMTEALNECVSIRNNEAGRAAIEWDCNOEFGORLORFOSYMEAEPLOLBOTLWGRRGTIHLETNLEATHOWYEAUDRRPAKCPRERLOTIHSNMOCEAKNSIVNALOASARTGEYRELASMYOLRPSUEPOEOYMLSSTWTIHHNIGEADRPEENYITSOIPDFOUSENQUIATOCCOAASTNHITCTOERHIDLTRNOAEEDTRXUTONSOENAERESCSTIEYELDTRHIEMNNEEIERPASSOTSRHTEOTEFIBNASENXSXDXIE".lower()
key = [1, 5, 3, 6, 4, 0, 2]


def possible_key_lengths(plain_text):
    result = []
    for i in range(1, 20):
        if len(plain_text) % i == 0:
            result.append(i)

    return result


def decipher_with_key(plain_text, key):
    blocks = divide_string_into_n_blocks(len(key), plain_text)

    result = ""
    for block in blocks:
        char_list = list(block)
        for i in range(len(key)):
            result += char_list[key[i]]

    return result.upper()


def divide_string_into_n_blocks(n, string):
    n = max(1, n)
    return list(string[i:i + n] for i in range(0, len(string), n))


show_english_frequency_histogram()
show_plain_text_fequency_histogram(plain_text)

print(possible_key_lengths(plain_text))
print(decipher_with_key(plain_text, key))
