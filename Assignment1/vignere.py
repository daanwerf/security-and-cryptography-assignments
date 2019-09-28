from Assignment1.frequencies import ngram_frequencies
from collections import Counter
import numpy as np


def find_ten_most_common_bigram(plain_text):
    result = []
    l, b, t = ngram_frequencies(plain_text)

    for i in range(10):
        result.append(b[len(b) - i - 1][0])
    return result


def make_bigram_list(plain_text):
    result = []
    for i in range(len(plain_text) - 1):
        if (plain_text[i] in [".", "-", " ", ",", "(", ")", "’"]) or (plain_text[i + 1] in [".", "-", " ", ",", "(", ")", "’"]):
            continue

        result.append(plain_text[i] + plain_text[i + 1])

    return result


def find_distances_between_bigram(target, plain_text):
    distances = []
    found_index = 0

    replace_symbols = [".", "-", " ", ",", "(", ")", "’", ";", "!", ":"]
    for s in replace_symbols:
        plain_text = plain_text.replace(s, "")

    for i in range(len(plain_text) - 2):
        if plain_text[i] + plain_text[i+1] == target:
            if found_index == 0:
                found_index = i
            else:
                distances.append(i - found_index)
                found_index = i

    return distances

# While this method will not always find the correct length of the key, the key can still be found from the final result
def greatest_common_divisor(plain_text):
    result = []
    for bigram in find_ten_most_common_bigram(plain_text):
        distances = find_distances_between_bigram(bigram, plain_text)
        for a in distances:
            for b in distances:
                divisor = greatest_common_divider(a, b)
                if a != b and divisor not in distances and divisor != 1 and divisor != 2:
                    result.append(divisor)

    return most_frequent(result)


def greatest_common_divider(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divider(b, a % b)


def total_variation_distance(a, b):
    return sum(abs(a - b)) / 2


def most_frequent(length_list):
    counter = 0
    num = length_list[0]

    for i in length_list:
        current_frequency = length_list.count(i)
        if current_frequency > counter:
            counter = current_frequency
            num = i

    return num


def find_all_nth_letters(plain_text, pos, word_length):
    result = []

    replace_symbols = [".", "-", " ", ",", "(", ")", "’", ";", "!", ":"]
    for s in replace_symbols:
        plain_text = plain_text.replace(s, "")

    count = 0
    for letter in plain_text:
        if count == pos:
            result.append(letter)
            pos = pos + word_length
            count += 1
        else:
            count += 1

    return Counter(result)


def nth_letters_to_deciphered_letters(counted):
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
        'n': 6.95,
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

    cipher_freq = {}
    counted_dict = dict(counted)

    tot = 0
    for element in counted.most_common():
        tot = tot + element[1]

    for letter in alphabet_freq.keys():
        if letter in counted_dict:
            cipher_freq[letter] = counted_dict[letter]/tot * 100
        else:
            cipher_freq[letter] = 0

    probabilities = []
    for i in range(len(alphabet_freq)):
        probabilities.append(total_variation_distance(np.asarray(list(alphabet_freq.values())), np.asarray(shift(list(cipher_freq.values()), -i))))

    return probabilities.index(min(probabilities))


def shift(seq, n):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]


def find_key_with_plain_text(plain_text):
    word = ""

    for i in range(greatest_common_divisor(plain_text)):
        word += chr(nth_letters_to_deciphered_letters(
            find_all_nth_letters(plain_text, i, greatest_common_divisor(plain_text))) + 97)

    return word


def decipher_with_key(plain_text, key):
    deciphered_string = ""

    count = 0
    for letter in plain_text:
        if letter in [".", "-", " ", ",", "(", ")", "’", ";", "!", ":"]:
            deciphered_string += letter
        else:
            deciphered_string += add_letters(letter, key[count])
            if count == len(key) - 1:
                count = 0
            else:
                count += 1

    return deciphered_string


def add_letters(first, second):
    first_int = ord(first)
    second_int = ord(second)
    return chr(((first_int - second_int) % 26) + 65)


plain_text_book_example = "UTPDHUG NYH USVKCG MVCE FXL KQIB. WX RKU GI TZN, RLS BBHZLXMSNP KDKS; CEB IH HKEW IBA, YYM SBR PFR SBS, JV UPL O UVADGR HRRWXF. JV ZTVOOV YH ZCQU Y UKWGEB, PL UQFB P FOUKCG, TBF RQ VHCF R KPG, OU KFT ZCQU MAW QKKW ZGSY, FP PGM QKFTK UQFB DER EZRN, MCYE, MG UCTFSVA, WP KFT ZCQU MAW KQIJS. LCOV NTHDNV JPNUJVB IH GGV RWX ONKCGTHKFL XG VKD, ZJM VG CCI MVGD JPNUJ, RLS EWVKJT ASGUCS MVGD; DDK VG NYH PWUV CCHIIY RD DBQN RWTH PFRWBBI VTTK VCGNTGSF FL IAWU XJDUS, HFP VHCF, RR LAWEY QDFS RVMEES FZB CHH JRTT MVGZP UBZN FD ATIIYRTK WP KFT HIVJCI; TBF BLDPWPX RWTH ULAW TG VYCHX KQLJS US DCGCW OPPUPR, VG KFDNUJK GI JIKKC PL KGCJ IAOV KFTR GJFSAW KTZLZES WG RWXWT VWTL WP XPXGG, CJ FPOS VYC BTZCUW XG ZGJQ PMHTRAIBJG WMGFG. JZQ DPB JVYGM ZCLEWXR: CEB IAOV NYH JIKKC TGCWXF UHF JZK. WX VCU LD YITKFTK WPKCGVCWIQT PWVY QEBFKKQ, QNH NZTTW IRFL IAS VFRPE ODJRXGSPTC EKWPTGEES, GMCG TTVVPLTFFJ; YCW WV NYH TZYRWH LOKU MU AWO, KFPM VG BLTP VQN RD DSGG AWKWUKKPL KGCJ, XY OPP KPG ONZTT ICUJCHLSF KFT DBQNJTWUG. DYN MVCK ZT MFWCW HTWF FD JL, OPU YAE CH LQ! PGR UF, YH MWPP RXF CDJCGOSF, XMS UZGJQ JL, SXVPN HBG!".lower()
print(find_key_with_plain_text(plain_text_book_example))
print(decipher_with_key(plain_text_book_example, find_key_with_plain_text(plain_text_book_example)))

plain_text_assignment = "FFX ZSGST UALWLFD CL RTC PVFWR UP FFX ZSGST UALWLFD CL RTC TUQTSTR IMKSR TG G JUQM VT CSSYDITIZP QULERKBQEWULE MY JZLGYGOYE HBEWWSURR NWGST ZK TTYWZIY YGRAVFD WT EGGWLPZCQQ AP IVSXG VMBSEHF LAULS YGJWPBZ FQJELBTQ ZMGPBZHD. ORRTMNNV EVK JUQM, PB THY AGPKLBE TUPY, BBK BZH YRMZBSWDS ALFGE AVP FKLMGLZOYQK, RTC YPFDH YSOF EPGEG UD ECOLB HCTBQPL KOES LPAK MOS DSIMZB VLBEIXW NA. MOS ZFOEULTS ZTGZ GZQIPFPR OLZSFLFLPRC HCKZWZBY RTPHBUS HNC MEXZ, CQHKL XGLAWYU YCHCG LBEFOCE. MY AVP CXGSGGHZ DSBCZ UHURPFY, MZJR VBP HNC SPXHH AMXYYGW VT RWFY (MJLV QLZRCP RAL DJFGKUB HM YSILS, MDMLF EVK NTYKHCS KNM NSBSH TH), ZFQ MEKSDH UD FFX HBNWKLF UHURPFY PQKTPBD FKJMRBCSWM OLFYVA. HSS IMXMLZID CL PTMWLG, EVK JUEAAVZIYC AD TSSIOTBDGT, AVP AGSEMELIX OZ FMJBJOCBGQESL, AVP HKKBJX VT LFZCYGL HBO HNC ERTAIP CL XQSL DSCS GJX BXZHCCECP. RAL ZZQGRUMG HBO IRRUKTAS QOZC AD MOS SOTEULZ NOCRKLE YKL IYYTMIL, TUR EVKPQ GL ZDPQAJMRBVB EVGR FFXF ALM TMF FTCS PLOQFCW HH LZR. RTC EPGE QUTQPXK CYZE RTC LJIWDZSDYE HBO OXATGMLQEIXYX KHUIXSTRE MY AVP AKBURXYFLBKYZ YGK ATRJJQ CTZHPFT PQEBVBD, KNGOF MOSY QUKBPBZSO HNC WLHDB HCXJP DHY HSS MPQCDZ. VPBIC, QVMHBE GORQQ ULMZBJ RTGL YSLZS UQPX UCE QULEGWLFPR GQ BYKA CQ QULFCFWCCOXW MAVVIYHY. RTC IYWXOXW MAVVIYHY, AAKBUU QFUK TCESSYWYRUA PYWESXQ, MJLV VPOBGXW BUTWIKLOCW AVP DRYOCL PBNZABQB BU HSS CMZBXYG WWYR. RGOL CQ HNC ECOLB PBZPUCL HFP O ICXCUYOEWUL AD ZYSPY GAOMFWZTGNKQLMZ WY HNC MPMZ OYR GPOFBASNHAPQ (RAL SIQKNFGHUG MSOLS RAL DJFGKUBL VT RWFY MLW AVP VGLSGGN ULFJCZQ HM PLPEJAL). MOS DSBCZ UHURPFY MZ YGAWAOZCD’Q EPGE KUL BPTPGPG LMD RALWC BURMZEL TPOZSDCL, YOYUOLS DKVA DIVCDJTAWGSY MR RAL VTUNCER HY ZLFMCER HM HSSOP FWILG, EC ZFQ YKAWDHXW IGMO KSWIF FFXF KPFK CJCVBHPR. ZFQGK HFNVORQAMBFLZ GLP YKAWDHOA RCTAICSY UQPX PATHGRQB MOFZIMFASM AVP VKJXCGPGEWI UAPEK OYR HCKMGK. HSS MPQCD PBQZACZAX PB CCSYZ ANSHFFK, YZB MOS CSBGHYE VT RFKAA-PHTOY OXRUQMPQ DHEJQQ WBFTBM RTC KLBLWYQMLVL QLIMFF RAL WXOMGZYMPCY CL CGPHWSLB GPFGLAG LBJ RDYOLZWSXQ. BYBUHTBMQ MLW ZQFZVRGPXZ OWZABULZ AC LBZGBYMLF’D ZOQF UXYS XOJC, IFBSS LRBCZRNYSCG LJAADLR EC ZFQ YVAILZ YGFCL AC ASXQALTSZJ KORZCLZ HSS CMZBXYG. WSMCZBL JWCQAJMRXK HZ TAPFFXY QZAVJQKXUH EVK QGNXYZLHOTQQ HM HSS CMZBXYG.".lower()
print(find_key_with_plain_text(plain_text_assignment))
print(decipher_with_key(plain_text_assignment, find_key_with_plain_text(plain_text_assignment)))
