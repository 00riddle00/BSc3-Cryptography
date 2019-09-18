import string

abc_lt=unicode('AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ','utf-8')
abc_en=unicode('ABCDEFGHIJKLMNOPQRSTUVWXYZ','utf-8')

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

sifr4_lt_raktas = u'KLEVAS'

sifr4_lt=u'''
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

sifr4_en_raktas = u'DECEPTIVE'
sifr4_en=u'ZICVTWQNGKZEIIGASXSTSLVVWLA'

#def prepare(text):
#    text=text.upper()
#    textn=u''
#    for a in text:
#        if a in abc:
#            textn+=a
#    return textn

def clean_text(text):
    return text.replace('\n', ' ').replace('\r', '').replace(' ', '')

def sifr_to_desifr(sifr_raktas,abc):
    abc_len = len(abc)
    desifr_raktas = u''
    for let in sifr_raktas:
        ind = abc.index(let)
        new_ind = (-1 * ind) % abc_len
        desifr_raktas += abc[new_ind]
    return desifr_raktas

def friedmann_test(sifr_rakto_dalis):
    if sifr_rakto_dalis == u'GAN':
        # do some googling:
        # https://cryptii.com/pipes/vigenere-cipher
        # http://www.lkz.lt
        sifro_raktas = u'GANDRAS'
    return sifro_raktas

def Vigenere(text,key,abc): #Vigenere cipher
    text = clean_text(text)
    textc=u''
    keys=[]
    lk=len(key)
    abc_len=len(abc)
    for i in range(0,lk):
        keys.append(abc.index(key[i]))
    lt=len(text)
    for i in range(0,lt):
        textc+=abc[(abc.index(text[i])+keys[i%lk])%abc_len]
    return textc

def auto_vigenere(text, key, abc):
    text = clean_text(text)
    fin_res = u''
    ilgis = len(key)
    viso_text_ilgis = len(text)
    for i in range(ilgis,viso_text_ilgis,ilgis):
        print("i=", i)
        print("Textas=" + text[i-ilgis:i])

        desifr_key = sifr_to_desifr(key,abc)
        print("Desifr_key=" + desifr_key)

        res = Vigenere(text[i-ilgis:i], desifr_key, abc)
        print(res)
        key = res
        print("res="+res)
        fin_res +=res
    return fin_res

# PVZ
#print Vigenere(u'KALNAS', u'ŽEMĖ', abc_lt)

# UZD1
#print Vigenere(sifr1,sifr_to_desifr(sifr1_raktas,abc_lt),abc_lt)

# UZD2
#print Vigenere(sifr2,sifr_to_desifr((friedmann_test(sifr2_rakto_dalis)), abc_lt),abc_lt)

# UZD3

# UZD4
#print(auto_vigenere(sifr4_en, sifr4_en_raktas, abc_en))
#print(10 * '--------------------------------\n')
print(auto_vigenere(sifr4_lt, sifr4_lt_raktas, abc_lt))



