from collections import defaultdict

abc = 'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
abcu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
test_letters = 'AEIO'

length = len(abc)

cypher1_key = u'STOGAS'

cypher1 = u'''
KTŠRA LETYŽ OĘVGA ZLCĘĮ HŪEKM 
YOGIJ ĘĄCZK SŪYDG NVKĮH ZRTCM 
OVEĮH ZĖTOĘ CODGU ĘCTED PVĮHO 
RNMKT GŠTLF ĖAIŪK MYOĄT HODĮZ 
KCSYO CPSYM ĖĘIĘS DFŪŪY MKOČL 
ŽYKAĄ TVFĮH ŽLSGŽ ĮDOĮT DĮZST 
LRĖŽA ĘSJĮZ TCŪTR GRESN HČDCŪ 
ŠAGUY CNĮRK YĖNEČ SKVŲŪ TIFSD 
AAAIY FORČC SRAŪA CĘNGR EISML 
RRKCI ĖCIĘK TAUAY TNLZŽ CGĮEG 
KSŪKĖ ŲISĮD ĖZRTC MOVEI SKĮZV 
C
'''

cypher2_key_part = u'GAN'

cypher2 = u'''
ĄOČLR RCĄBĮ BGAKA AGZRS ĘZNTV 
BMKGS DHJŲI AITVĖ AGČŽV LĖSKG 
NIUĘA GKTNŪ KKSĄI NUĘIG UDKLĮ 
ALŲEG ŲRUŪZ NOLIŽ DJROU ŪRĘKT 
ĮŲBAY JEHLĖ TYČVŽ ŲYUFŪ EIAHR 
CKJĘŪ FETČV ĘUIIS ATŲOV SEZKG 
PGSFR NŽŪĘA CĘAGD FACĄL NLEAC 
ĄGNSG VHBEĖ RBOKK OFLDA ĘGDŠB 
BGLIŲ MBRIĄ FDMLL PĖGNT ZGSVV 
EVDĘI SCSŽŲ RSKRG ĄBČBŽ IUKTĘ 
ACUOD DRKYR ODDJO ĘRŲĖR RNVCŲ 
ĘŲŠIK ZSPHH AĖROK TĮKVR ČŽDĮI 
ŪMLVŲ RVCCA RLFIM ĄVĄŲR VCŪŲC 
NĘAGY IYĘŪS CĄUCD FTŪĘI TSĮAL 
ŲĖDDH LCVKK LŪNSU IIE
'''

cypher3 = u'''
FĮLPI ŽHVFB PFOHY ŽCFĘE SĮDCČ 
ROKCF BĄROY CTŠSK LYLHI OZFZY 
GŠŽBG CTDBD YNCVK LCŲTC HDBĖB 
AĘLĮŽ ŲĮEYĘ DBĄRĮ LHŠFP BČRŪŠ 
ŠKŠAK ĘURĄĖ UGĄTV ĄIRIŽ MŠGIY 
FVMOČ RLSJN HIBIV ĮFŠPK ŪLOĮD 
CĘOKD GEYBG OCŽŽF ŲUCYG IĄEYK 
SJĄPB LKĮTČ DZFHO TZNŲT CSDFF 
FEHYF IĘŠUĮ DĖMYČ HCSDV PYĮHE 
ĮFPFŽ LHŪID ĮBŪSH IICGH ĘGŠJĮ 
LLYDG ŽIETZ KŪFEE VTŽĄH RLFCL 
ŪĄYEK CŽCMR KYKĘZ PBUKY DCYGF 
SLDBV ĖESLR IĄEMŲ CĮDĄH YĘSHY 
PIĘIS KĄĄIŽ SFTCD GFSGŽ DMRKĘ 
CIRPB EJFĄD CJUYĘ IUŽRL ĘSŠŪF 
EĘFSŠ ĮYKMŲ CUVPK GHĘJM GYĘIS 
KŠEŪĮ ĘCTEĄ IJSĘĄ VĄROE ČŲEMG 
ĮVKNČ TBUYO DLJDA ĮSZIJ JUFYT 
EIĮNC ĘGASK NVĖED FEĘĖV IRMSN 
SĮKŠĄ YJHID MHBUL YDČGM LKŠYI 
ONAĖĄ DIJHA ĮEEĄH GHSGC ĮBFEN 
ĮDIĄI ULŪĮŽ JGFSG VŠRĖO ĮPDŽJ 
MGLSY DHROĘ KUCPK HŽĖĘL OBYJO 
DMISG SYHIĖ ŲUĮHK ŠDGŽŽ ĖZAĘB 
OHYDF ĄĮYĘC TŠIFE VĘTŠI ŠAKĘĮ 
ŪĄRĘĮ SIŪPĮ JSĘGŠ JNOYC UCĘKH 
ĘFŽŽP ĮYĖCT BĄĮŪL OĮIYI UYKTC 
DGĮVJ DZYRL FVMĘG IEVJH IĖKTĄ 
CHCYR ĮKIGI ĖŪNSY NŪPĮE SIGŠĖ 
EŽOCK IJĘAY ĮTEUG ĮŠCJH CŲKŠI 
ŽBDŪN LĮDII ŲAJCH DIKSC ĮLEĘĖ 
AKMYB ĄŪFHY IMSKS HIJŠP INŽEA 
CČGGY ĘĮCĘB ĮCYGI ĄNUYS IIĄĮH 
SCFIĄ ĮČSFĮ FFYAI ĖDAYŪ YĮCĖI 
DRŽŪO DRJŠP ROTŠŽ PŽRCO ĄERĮV 
KĮCŲF AĄSGŠ PJLCĮ TCYBČ DOĘYV 
ŠOOHG IĄEYF STŪIB YFSMA DBPIĖ 
TŽŲJP HĮŲŠY GLTVY IEBYO HKŪŲB 
ZCSKŠ UZHĄĮ TFĄJU UCIŠK ĮSDĮT 
FĄĖPĘ DGIĖU EMTŽC ĄĮOĘS IDUNE 
VFKIJ ĘBFSY VĄFGO CŽŽPE EKŠ  
'''

cypher4_key = u'KLEVAS'

cypher4 = u'''
ĘDSFA ĮNŪTC VĄNPJ COUNI ŽSĘAH 
ŠLKĘS VZGHŪ ĮFČBV ŪACCI FYSŪC 
ŽBCĖŪ RDŲCŽ REDMJ ŽHSLD ŽČĖCĖ 
DTPYU ZDNUB ĮŽLFT KMPMZ ŽEBŲH 
ŠPMBM KZĮZO HĘŠGG GCĄGŪ KCZRA 
ĖRMMĮ NYŠIJ ĄĖČČI DUKNH COYAG 
ŲSHAI VĘYŪA ŠUĘDŪ NŠEZR ŪŽĖEG 
ĮEŽUU ĘĄZDJ HNPSH CĄŽČS ŲCEČĄ 
CDVĖŽ AADFM ZDŽLČ ĘJDMS VŲEHD 
VĘŲSS DRZĘĮ SŪJGL ŲOGLM NPLZB 
MŽDDK BMJŪL ČOMĖK ĄKJĘT KORĖB 
ĮERBĄ RČĖŪS ĄĘKŪT HŠSRĖ VSŠYB 
ĮDĖBČ BGLĄB ĘYVVŪ TČŪNV TDRSC 
HGDFŲ JEIHA ĘEAŪH NAHVĖ LDSHS 
TTSSA ĖDIĘO IYŠIS ADJ
'''


def clean_text(text):
    return text.replace('\n', ' ').replace('\r', '').replace(' ', '')


def cypher_to_decipher(cypher_key):
    decipher_key = u''
    for let in cypher_key:
        ind = abc.index(let)
        new_ind = (-1 * ind) % length
        decipher_key += abc[new_ind]
    return decipher_key


# ex. vigenere(u'KALNAS', u'ŽEMĖ')
def vigenere(text, key):  # vigenere cipher
    text = clean_text(text)
    abc_len = len(abc)
    textc = u''
    keys = []
    lk = len(key)
    for i in range(0, lk):
        keys.append(abc.index(key[i]))
    lt = len(text)
    for i in range(0, lt):
        textc += abc[(abc.index(text[i]) + keys[i % lk]) % length]
    return textc


def auto_vigenere(text, key):
    text = clean_text(text)
    fin_res = u''
    lg = len(key)
    whole_text_len = len(text)
    text_part = u''
    for i in range(lg, whole_text_len, lg):
        text_part = text[i - lg:i]
        decipher_key = cypher_to_decipher(key)
        res = vigenere(text_part, decipher_key)
        key = text_part
        fin_res += res
    return fin_res


# Frequencies
def freq(text):
    d = defaultdict(int)
    s = ""
    for w in text:
        if w in abc:
            d[w] += 1
    return d


# Friedman test
def friedm(text, k):
    l = len(text)
    s = 0
    for i in range(k, l):
        if text[i] == text[i - k]:
            s += 1
    return 1. * s / (l - k)


# Splitting Vigenere into Caesar cyphers
def split(text, d):
    tspl = [''] * d
    n = len(text)
    for i in range(0, n):
        tspl[i % d] += text[i]
    return tspl


# For guessing the key
# prints the sum of test letters (ex. 'AEIO') in a text
# ::params:: test - test letters (most frequent letters)
# ::params:: c_x - Caesar cypher, made according to the Vigenere key length
def guess(test, c_x):
    for i in range(0, length):
        if i == 0:
            test_list = [char for char in test]
        else:
            test_list = [abc[(abc.index(char) + 1) % length] for char in test_list]
        counts = 0
        freqs = freq(c_x)
        for char in test_list:
            counts += freqs[char]
        print(u"i={}, key={}, freqs={}, letters={}".format(i, abc[i], counts, ''.join(map(str, test_list))))


# T1
print(vigenere(cypher1, cypher_to_decipher(cypher1_key)))

# T2
# ============= cool way =============

# key_start = 'GAN'
# do some googling:
# https://cryptii.com/pipes/vigenere-cipher
# http://www.lkz.lt
cypher2_key = 'GANDRAS'
print(vigenere(cypher2, cypher_to_decipher('GANDRAS')))

# ============= lame way =============

cypher2 = clean_text(cypher2)

# searching for key length
for i in range(1, 20):
    print("i={}, friedm={}".format(i, friedm(cypher2, i)))

# found the key length
key_len = 7

# split cypher in 7 parts (Caesar cyphers) by key length
c_x = split(cypher2, key_len)

for i in range(0, key_len):
    print("guessing C{}".format(i + 1))
    guess(test_letters, c_x[i])

# according to frequencies and intuition we deduce that the key is 'GANDRAS'
print(vigenere(cypher2, cypher_to_decipher('GANDRAS')))

# T3
cypher3 = clean_text(cypher3)

# searching for key length
for i in range(1, 20):
    print("i={}, friedm={}".format(i, friedm(cypher3, i)))

# found the key length
key_len = 7

# split cypher in 7 parts (Caesar cyphers) by key length
# c1='FVY...
# c2='ĮFŽ...
# c3='LBC...
# c4='PPF...
# c5='IFĘ...
# c6='ŽOE...
# c7='HHS...
c_x = split(cypher3, key_len)

for i in range(0, key_len):
    print("guessing C{}".format(i + 1))
    guess(test_letters, c_x[i])

# according to frequencies we deduce easily that the key is 'STIPRUS'
print(vigenere(cypher3, cypher_to_decipher('STIPRUS')))

# T4
print(auto_vigenere(cypher4, cypher4_key))
