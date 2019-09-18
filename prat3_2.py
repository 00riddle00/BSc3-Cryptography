## Dazniai
from collections import defaultdict
abc=unicode('AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ','utf-8')
def freq(text):
    d = defaultdict(int)
    s=""
    for w in text:
        if w in abc:
            d[w] += 1                   
    for w in sorted(d, key=d.get, reverse=True):
        s+=w
    return s

t='TRRyyyIIU'
print(freq(t))

'AEIO'

## Friedmann test
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
t=unicode('PIGĄU KCLĘR ŽSOPĘ CKCIŲ ĖGACY ','utf-8')
print(friedm(t,2))

from collections import defaultdict
abc=unicode('AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ','utf-8')
n=len(abc)

## Raktui speti
def guess(test, k, sifr): #test - dažniausių raidžių eilutė, k - spėjamas šifro raktas
    tst=unicode('','utf-8')
    for r in test:
        if r in abc:
            tst+=r    
    tstk=unicode('','utf-8')
    for r in tst:
        tstk+=abc[(abc.index(r)+k)%n]
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
test=unicode('ABC','utf-8')
sifr=unicode('ABABABASSDDHHDKKKCCCCCLKLDKSJJSJSJLL','utf-8')

guess(test,2,sifr)

## SKAIDYMAS
abcu='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=len(abcu)
def prepare2(text): #remove non-ascii
    textn=''
    for a in text:
        if a in abcu:
            textn+=a
    return textn.upper()


def split(text,d):
    textn=prepare2(text)
    tspl=['']*d
    n=len(textn)
    for i in range(0,n):
        tspl[i%d]+=textn[i]
    return tspl    
    
f=split('ABABABABABAB',2)
f[0],f[1]
