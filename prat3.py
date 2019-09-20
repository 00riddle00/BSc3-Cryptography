import string
from collections import defaultdict

abc=unicode('AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ','utf-8')
abcu='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
test=unicode('AEIO','utf-8')

length=len(abc)


sifr1_raktas = u'STOGAS'
  
sifr1 = u'''
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

sifr2_rakto_dalis = u'GAN'

sifr2 = u'''
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

sifr3 = u'''
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

sifr4_raktas = u'KLEVAS'

sifr4=u'''
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

def sifr_to_desifr(sifr_raktas):
    desifr_raktas = u''
    for let in sifr_raktas:
        ind = abc.index(let)
        new_ind = (-1 * ind) % length
        desifr_raktas += abc[new_ind]
    return desifr_raktas

def friedmann_test(sifr_rakto_dalis):
    if sifr_rakto_dalis == u'GAN':
        # do some googling:
        # https://cryptii.com/pipes/vigenere-cipher
        # http://www.lkz.lt
        sifro_raktas = u'GANDRAS'
    return sifro_raktas

def Vigenere(text,key): #Vigenere cipher
    text = clean_text(text)
    abc_len=len(abc)
    textc=u''
    keys=[]
    lk=len(key)
    for i in range(0,lk):
        keys.append(abc.index(key[i]))
    lt=len(text)
    for i in range(0,lt):
        textc+=abc[(abc.index(text[i])+keys[i%lk])%length]
    return textc

def auto_vigenere(text, key):
    text = clean_text(text)
    fin_res = u''
    ilgis = len(key)
    viso_text_ilgis = len(text)
    teksto_dalis = u''
    for i in range(ilgis,viso_text_ilgis,ilgis):
        teksto_dalis = text[i-ilgis:i]
        desifr_key = sifr_to_desifr(key)
        res = Vigenere(teksto_dalis, desifr_key)
        key = teksto_dalis
        fin_res +=res
    return fin_res

# Dažniai
#def freq(text):
#    d = defaultdict(int)
#    s=""
#    for w in text:
#        if w in abc:
#            d[w] += 1                   
#    for w in sorted(d, key=d.get, reverse=True):
#        s+=w
#    return s

# Dažniai (mano f-ja)
def freq2(text):
    d = defaultdict(int)
    s=""
    for w in text:
        if w in abc:
            d[w] += 1
    return d

# Friedmano testas
def friedm(text,k):
    textn=unicode("",'utf-8')
    for r in text:
        if r in abc:
            textn+=r
    l=len(textn)
    s=0
    for i in range(k,l):
        if textn[i]==textn[i-k] :
            s+=1
    return  1.*s/(l-k)  

# Skaidymas
def split(text,d):
    tspl=['']*d
    n=len(text)
    for i in range(0,n):
        tspl[i%d]+=text[i]
    return tspl   

# Raktui spėti
# def guess(test, k, sifr): #test - dažniausių raidžių eilutė, k - spėjamas šifro raktas
#     tst=unicode('','utf-8')
#     for r in test:
#         if r in abc:
#             tst+=r    
#     tstk=unicode('','utf-8')
#     for r in tst:
#         tstk+=abc[(abc.index(r)+k)%length]
#     d = defaultdict(int)
#     sifrn=unicode('','utf-8')
#     for r in sifr:
#         if r in abc: sifrn+=r
#     for r in sifrn:
#         if r in tstk: d[r]+=1
#     kiek=len(sifrn)
#     s=0
#     for a in d.keys(): s+=d[a]
#     return s/kiek

# Raktui spėti (mano f-ja)
def guess2(test, c_x): #test - dažniausių raidžių eilutė, c_x -> pvz c1 = 'ABCD' -> perrikiuotas tekstas pagal rakto ilgi
    for i in range(0, length):
        if i == 0:
            test_list = [char for char in test]
        else:
            test_list = [abc[  (abc.index(char) + 1) % length ] for char in test_list]  
        counts = 0
        dazniai = freq2(c_x)
        for char in test_list:
            counts += dazniai[char]
        print(u"i={}, raktas={}, dazniai={}, raides={}".format(i, abc[i], counts, ''.join(map(unicode, test_list))))

# PVZ
#print Vigenere(u'KALNAS', u'ŽEMĖ')

# UZD1
#print Vigenere(sifr1,sifr_to_desifr(sifr1_raktas))

# UZD2
#print Vigenere(sifr2,sifr_to_desifr((friedmann_test(sifr2_rakto_dalis))))

# UZD3
sifr3 = clean_text(sifr3)

# ieskome rakto ilgio
for i in range(1,20):
    print("i={}, friedm={}".format(i, friedm(sifr3,i)))
    
# radome, ilgis yra 7
ilgis = 7

# padaliname sifra i 7 dalis, perrikiuodami pagal rakto ilgi
#c1='FVY...
#c2='ĮFŽ...
#c3='LBC...
#c4='PPF...
#c5='IFĘ...
#c6='ŽOE...
#c7='HHS...

c_x = []
for i in range(0,ilgis):
    x = ''.join(map(unicode, split(sifr3[i:],ilgis)[0]))
    c_x.append(x)

for i in range(0, ilgis):
    print("spejame C{}".format(i+1))
    guess2(test, c_x[i])

# pagal daznius ir intuicija mazdaug nustateme, kad raktas yra 'STIPRUS'
print(Vigenere(sifr3,sifr_to_desifr(u'STIPRUS')))


# UZD4
#print auto_vigenere(sifr4, sifr4_raktas)




