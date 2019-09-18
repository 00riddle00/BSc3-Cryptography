import string
abc=unicode('AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ','utf-8')
n=len(abc)
def prepare(text):
    text=text.upper()
    textn=u''
    for a in text:
        if a in abc:
            textn+=a
    return textn

def Vigenere(text,key): #Vigenere cipher
    textn=prepare(text)
    keyn=prepare(key)
    textc=u""
    keys=[]
    lk=len(keyn)
    for i in range(0,lk):
        keys.append(abc.index(keyn[i]))
    lt=len(textn)
    for i in range(0,lt):
        textc+=abc[(abc.index(textn[i])+keys[i%lk])%n]
    return textc

r=u'KLEVAS'
sifr=u'''
ĘDSFA ĮNŪTC VĄNPJ COUNI ŽSĘAH 
ŠLKĘS VZGHŪ ĮFČBV ŪACCI FYSŪC 
ŽBCĖŪ RDŲCŽ REDMJ ŽHSLD ŽČĖCĖ 
DTPYU ZDNUB ĮŽLFT KMPMZ ŽEBŲH 
'''
sifrn=u''
for a in sifr:
    if a in abc:
        sifrn+=a

rsifr=r+sifrn
N=len(sifrn)
rsifrn=rsifr[0:N]

rdes=u''
for a in rsifrn:
    rdes+=abc[-abc.index(a)%32]

def Vigenere(text,key,abc): #Vigenere cipher
    text = clean_text(text)
    abc_len=len(abc)
    textc=u''
    keys=[]
    lk=len(key)
    for i in range(0,lk):
        keys.append(abc.index(key[i]))
    lt=len(text)
    for i in range(0,lt):
        textc+=abc[(abc.index(text[i])+keys[i%lk])%abc_len]
    return textc


def Vigenere(text,key,abc): #Vigenere cipher
    textn=prepare(text,abc)
    abc_len=len(abc)
    keyn=prepare(key,abc)
    textc=u""
    keys=[]
    lk=len(keyn)
    for i in range(0,lk):
        keys.append(abc.index(keyn[i]))
    lt=len(textn)
    for i in range(0,lt):
        textc+=abc[(abc.index(textn[i])+keys[i%lk])%abc_len]
    return textc
