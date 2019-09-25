abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lg = len(abc)

# uzd2
L1=[20, 3, 24, 18, 8, 5, 15, 4, 7, 11, 0, 13, 9, 22, 12, 23, 10, 1, 19, 21, 17, 16, 2, 25, 6, 14]
L2=[8, 13, 24, 18, 9, 0, 7, 14, 10, 11, 19, 25, 4, 17, 12, 21, 15, 3, 22, 2, 20, 16, 23, 1, 6, 5]

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


def clean_text(text):
    return text.replace('\n', ' ').replace('\r', '').replace(' ', '')

def deenigma(text, k1, k2, L1, L2):
    res = []
    
    text = clean_text(text)
    lt = len(text)

    mapL1 = dict()

    for i in range(0, lg):
        mapL1[L1[i]] = i

    mapL2 = dict()

    for i in range(0, lg):
        mapL2[L2[i]] = i

    for i in range(0, lt):
        k = i
        m1 = k%26
        m2 = ((k-m1)//26) % 26
        
        m1 = m1+k1
        m2 = m2+k2

        a = abc.index(text[i])

        a = (a+m2) % lg
        a = mapL2[a]
        a = (a-m2) % lg
        a = (a+m1) % lg
        a = mapL1[a]
        a = (a-m1) % lg
        res.append(a)
        
    for i in range(0, lt):
        res[i] = abc[res[i]]
        
    return ''.join(res)
    

    
# uzd1
#print deenigma(s1, k1, k2, L1, L2)

# uzd2
for i in range(0,lg):
    res = deenigma(s2, 15, i, L1, L2)
    if res[0] == 'S':
        print res

    
    
    
    
