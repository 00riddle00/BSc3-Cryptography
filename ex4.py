abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lg = len(abc)

s1 = '''
GJPRD TPQDW ZCMOL IDZWD TQGSF 
OLMDV EAPWN BLJTK HJFBH QXXLC 
HDZPG BSMET JABWY KDYMB KJYWR 
CBTTV XIIVG LVAIM LPOQD AVOBO 
OZOOW HUSNM IAFCA EAHMA ZUITB 
YEXUJ CMSCI VUSQA FUZNK BJEOH 
FCVJS TPVPN PSQZA NTBIG KTXCW 
TRDNC ICGBE FHIIX GETHZ ZEZDW 
CSOGJ LTYQP AQXZX PWPUB HKHZR 
NPZMU JSJUP LAZZB AEOAJ UWCRR 
VTPBN ETZZD VWBIY TCATW SWTVA 
VMAEF STQLW PWPGG HOHCY APFFH 
HPGUS LOPSU ZLHFB LEYTK CYXTT 
DVFDT NARMJ EFJCQ XVIRY CIUWL 
HMZZN BJDOS HTLLO JEKFU SNCJA 
PDZVR GQKTW RWCDA ARCKS MGRMG 
FNKKH DOKBX HXBYH LBHRR NGXPF 
QBJFO DKFKO OKOPA WZLCD DLZYN 
AMR
'''

s2 = '''
DMWKK QVXIJ GSMWX MENAL PCOMX 
FVBXO RSRDS OBJGM HBAVF GRUMB 
XTEGS BMRHL PPKEK YZILE MHDQC 
WYUGK MWONR ALPMC MGFQQ NWTLS 
YYMSK TGBUY QKJLA DPKKA AKPKR 
LRCDT UXSVH FFVKH QLLOI GPSJV 
RUYRU VIADR HYHXF YEQUW NYRIC 
HHRJM OCTZO XQLBI DMFUZ KQEGI 
QEXUT JBEIZ NDELJ QDUYU IAZUW 
NQGDA DHRQV CSUQT KNQPI TGBRD 
VDHKK LZBHW GTQIF XMOLG TSNRI 
TCBRW EPTGA ZAUEW WQGKF VGVWQ 
QBZHR ATCNC MZTOQ LMSSY YMBFO 
RTDSP 
'''

s3 = '''
BAARE ZUYKK GNWYW WNYIR IYWGF 
IGNGJ CDDTC CKRDN MGZCU FRSRQ 
OGVME NJPEK AZPMH CZKYL QTWPG 
XKASP GZAZH EATDP AQBRC AOFRK 
LJYJK FBIRF VDHPQ BQJGS GZWYV 
LBQAB AULCK DXKMW TAWHH XLWPP 
ITBJQ HRNCG BIORV ZCYOM FEUVJ 
ZXYTH LPLSE RGRST SHZRX PTYTC 
LMZBP VFDIA AYIKE TRQSC TTIRL 
PPHNP ZTPUE TLQEZ FYBBZ PHTHI 
CTYEK FJFPN VEFSY XAYPI MBHII 
HHUNC EAOCV FNXGT ERLCV OSYEI 
CMSNC WTNCM XTACX NBQJV JICBP 
WOFXN EYWTW PYWJF GFTKE PEKPK 
RKOWY DONBJ NFPGY MQPAV PWSJW 
CVGSZ WKHDJ NFEKL KMZWF VOMFX 
WHLFP KWSKV MDBPM YDZEC DNMYO 
JNUTG VOZIK NQGHZ JOOLF CHRYJ 
IMU
'''


def clean_text(text):
    return text.replace('\n', ' ').replace('\r', '').replace(' ', '')


def deenigma(text, k1, k2, l1, l2):
    res = []

    text = clean_text(text)
    lt = len(text)

    map_l1 = dict()

    # create inverse substitute
    for i in range(0, lg):
        map_l1[l1[i]] = i

    map_l2 = dict()

    # create inverse substitute
    for i in range(0, lg):
        map_l2[l2[i]] = i

    # rotors
    for i in range(0, lt):
        k = i
        m1 = k % 26
        m2 = ((k - m1) // 26) % 26

        m1 = m1 + k1
        m2 = m2 + k2

        a = abc.index(text[i])

        a = (a + m2) % lg
        a = map_l2[a]
        a = (a - m2) % lg
        a = (a + m1) % lg
        a = map_l1[a]
        a = (a - m1) % lg
        res.append(a)

    for i in range(0, lt):
        res[i] = abc[res[i]]

    return ''.join(res)


def enigma(text, k1, k2, l1, l2):
    res = []

    text = clean_text(text)
    lt = len(text)

    map_l1 = dict()

    # create substitute
    for i in range(0, lg):
        map_l1[i] = l1[i]

    map_l2 = dict()

    # create substitute
    for i in range(0, lg):
        map_l2[i] = l2[i]

    # rotors
    for i in range(0, lt):
        k = i
        m1 = k % 26
        m2 = ((k - m1) // 26) % 26

        m1 = m1 + k1
        m2 = m2 + k2

        a = abc.index(text[i])

        a = (a + m1) % lg
        a = map_l1[a]
        a = (a - m1) % lg
        a = (a + m2) % lg
        a = map_l2[a]
        a = (a - m2) % lg

        res.append(a)

    return res


# T1
k1, k2 = 1, 2

l1 = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
l2 = [10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]

print(deenigma(s1, k1, k2, l1, l2))

# T2
k1 = 15
k2 = -1  # is not known

l1 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
l2 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]

for i in range(0, lg):
    k2 = i
    res = deenigma(s2, k1, k2, l1, l2)
    if res[0] == 'S':
        print(res)

# T3

# Enigma cyper's (with reflection) key=[25,18]
k1, k2 = 25, 18

l1 = [20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
l2 = [8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]

# Reflection's substitute
s = [2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]

tmp = enigma(s3, k1, k2, l1, l2)

for i in range(0, len(tmp)):
    tmp[i] = abc[s[tmp[i]]]

tmp_text = ''.join(tmp)

print(deenigma(tmp_text, k1, k2, l1, l2))
