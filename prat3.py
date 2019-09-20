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
def freq(text):
    d = defaultdict(int)
    s=""
    for w in text:
        if w in abc:
            d[w] += 1                   
    for w in sorted(d, key=d.get, reverse=True):
        s+=w
    return s

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

#Raktui spėti
def guess(test, k, sifr): #test - dažniausių raidžių eilutė, k - spėjamas šifro raktas
    tst=unicode('','utf-8')
    for r in test:
        if r in abc:
            tst+=r    
    tstk=unicode('','utf-8')
    for r in tst:
        tstk+=abc[(abc.index(r)+k)%length]
    d = defaultdict(int)
    sifrn=unicode('','utf-8')
    for r in sifr:
        if r in abc: sifrn+=r
    for r in sifrn:
        if r in tstk: d[r]+=1
    kiek=len(sifrn)
    s=0
    for a in d.keys(): s+=d[a]
    return s/kiek



# Skaidymas
def prepare(text): #remove non-ascii
    textn=''
    for a in text:
        if a in abcu:
            textn+=a
    return textn.upper()


def split(text,d):
    #textn=prepare(text)
    tspl=['']*d
    n=len(text)
    for i in range(0,n):
        tspl[i%d]+=text[i]
    return tspl    
    






# PVZ
#print Vigenere(u'KALNAS', u'ŽEMĖ')

# UZD1
#print Vigenere(sifr1,sifr_to_desifr(sifr1_raktas))

# UZD2
#print Vigenere(sifr2,sifr_to_desifr((friedmann_test(sifr2_rakto_dalis))))

# UZD3

### dazniai
#t='TRRyyyIIU'
#print(freq(t))

### skaidymas
#f=split('ABABABABABAB',2)
#print(f)
#print f[0]
#print f[1]

sifr3 = clean_text(sifr3)

for i in range(1,20):
    print("i={}, friedm={}".format(i, friedm(sifr3,i)))
    
# ilgis = 7

c_x = []
for i in range(0,7):
    x = ''.join(map(unicode, split(sifr3[i:],7)[0]))
    c_x.append(x)

c1 = c_x[0]
c2 = c_x[1]
c3 = c_x[2]
c4 = c_x[3]
c5 = c_x[4]
c6 = c_x[5]
c7 = c_x[6]

print(u"c1={}".format(c1))
print(u"c2={}".format(c2))
print(u"c3={}".format(c3))
print(u"c4={}".format(c4))
print(u"c5={}".format(c5))
print(u"c6={}".format(c6))
print(u"c7={}".format(c7))



#c1='FVY...
#c2='ĮFŽ...
#c3='LBC...
#c4='PPF...
#c5='IFĘ...
#c6='ŽOE...
#c7='HHS...

#for i in range(0,32):
#    print("i = ", i)
#    print float(guess(test,i,c1))
   
def freq2(text):
    d = defaultdict(int)
    s=""
    for w in text:
        if w in abc:
            d[w] += 1
    return d

fre = freq2(c7)
for key, val in fre.items():
    print u'{}={}'.format(key, val),

print('\n')





for i in range(0, 32):
    if i == 0:
        test_x = [char for char in test]
    else:
        test_x = [abc[  (abc.index(char) + 1) % length ] for char in test_x]  
    counts = 0
    for char in test_x:
        counts += fre[char]
    print(u"i={}, {}, counts={}, raides={}".format(i, abc[i], counts, ''.join(map(unicode, test_x))))
    print float(guess(u'AEIO', i, x))
    print float(guess(''.join(map(unicode, test_x)), i, x))
    
    
    
print(Vigenere(sifr3,sifr_to_desifr(u'STIPRUS')))





# UZD4
#print auto_vigenere(sifr4, sifr4_raktas)




